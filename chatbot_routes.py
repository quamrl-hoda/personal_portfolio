"""
chatbot_routes.py
Flask blueprint exposing a /api/chat endpoint that answers visitor questions
grounded in Quamrul Hoda's resume, using the OpenAI API.

Register in app.py with:
    from chatbot_routes import chatbot_bp
    app.register_blueprint(chatbot_bp)
"""

import os
import time
from collections import defaultdict, deque
import openai
from dotenv import load_dotenv
from flask import Blueprint, request, jsonify, session
from resume_data import SYSTEM_PROMPT

load_dotenv()
chatbot_bp = Blueprint("chatbot", __name__)

MODEL = "gpt-4o-mini"          # fast & cost-effective for grounded Q&A
MAX_TOKENS = 400
MAX_HISTORY_TURNS = 6          # keep last N user/assistant pairs per session
MAX_MESSAGE_CHARS = 800        # guard against huge pasted input

# --- simple in-memory rate limiter (per IP) ---------------------------
_rate_limit_window = 60          # seconds
_rate_limit_max_requests = 15    # requests per window per IP
_request_log = defaultdict(deque)


def _is_rate_limited(ip: str) -> bool:
    now = time.time()
    q = _request_log[ip]
    while q and now - q[0] > _rate_limit_window:
        q.popleft()
    if len(q) >= _rate_limit_max_requests:
        return True
    q.append(now)
    return False


def _get_openai_client():
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        return None
    return openai.OpenAI(api_key=api_key)


@chatbot_bp.route("/api/chat", methods=["POST"])
def chat():
    ip = request.headers.get("X-Forwarded-For", request.remote_addr)
    if _is_rate_limited(ip):
        return jsonify({"error": "Too many messages — please wait a moment and try again."}), 429

    data = request.get_json(silent=True) or {}
    user_message = (data.get("message") or "").strip()

    if not user_message:
        return jsonify({"error": "Message is empty."}), 400
    if len(user_message) > MAX_MESSAGE_CHARS:
        return jsonify({"error": "Message is too long."}), 400

    client = _get_openai_client()
    if not client:
        return jsonify({"error": "Chatbot service API key is not configured on the server."}), 500

    # Keep short conversation history in the Flask session (cookie-based).
    history = session.get("chat_history", [])
    history.append({"role": "user", "content": user_message})

    # Prepare OpenAI messages format with system prompt
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    for msg in history[-(MAX_HISTORY_TURNS * 2):]:
        messages.append({"role": msg["role"], "content": msg["content"]})

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=messages,
            max_tokens=MAX_TOKENS,
            temperature=0.7,
        )
        reply_text = response.choices[0].message.content.strip()
    except openai.OpenAIError as e:
        print(f"OpenAI API Error: {e}")
        return jsonify({"error": "The assistant is temporarily unavailable. Please try again shortly."}), 502
    except Exception as e:
        print(f"Chatbot Unexpected Error: {e}")
        return jsonify({"error": "An unexpected error occurred. Please try again."}), 500

    history.append({"role": "assistant", "content": reply_text})
    session["chat_history"] = history[-(MAX_HISTORY_TURNS * 2):]

    return jsonify({"reply": reply_text})


@chatbot_bp.route("/api/chat/reset", methods=["POST"])
def reset_chat():
    session.pop("chat_history", None)
    return jsonify({"status": "reset"})

