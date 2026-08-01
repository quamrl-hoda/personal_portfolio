"""
resume_data.py
Holds Quamrul Hoda's resume content and the system prompt used to ground
the portfolio chatbot. Edit RESUME_TEXT whenever the resume changes.
"""

RESUME_TEXT = """
QUAMRUL HODA
Phone: +91-7851819968 | Email: qhoda489@gmail.com | LinkedIn | GitHub

EDUCATION
I K Gujral Punjab Technical University, Kapurthala, Punjab (2023 - Present)
B.Tech - Computer Science and Engineering (AI/ML) | CGPA: 7.1/10

EXPERIENCE
CodeAlpha - Machine Learning Intern (Remote) | 1st - 30th July 2025
- Designed and deployed a Restaurant Price Prediction system using supervised ML algorithms,
  building an end-to-end retrieval and evaluation pipeline for structured output and model reliability.
- Applied CatBoost and anomaly detection to handle high-cardinality features and identify outliers,
  improving system correctness and prediction robustness.
- Built full ML pipeline using Python, Scikit-learn, and Pandas covering data ingestion,
  feature engineering, model training, and evaluation frameworks.

TECHNICAL SKILLS
Languages & Async: Python, async programming, SQL
AI & NLP: Transformer Architecture, NLP, LLMs, Prompt Engineering, Embeddings, RAG Systems,
  Vector Databases (FAISS, Pinecone, Chroma), LLM Evaluation, Fine-Tuning
Agentic & Multi-Agent AI: LangChain, LangGraph, Agentic Workflows, Context Engineering,
  Multi-Agent Systems, OpenAI API
MLOps & Tools: FastAPI, PostgreSQL, Docker, MLflow, DVC, Git, GitHub, CI/CD Pipelines,
  Redis, MongoDB, Unit Testing, Integration Testing
ML/DL Frameworks: Scikit-learn, TensorFlow/Keras, PyTorch, XGBoost, LightGBM, CatBoost, YOLO,
  HuggingFace Transformers, Anomaly Detection

PROJECTS
1. AI Chatbot - RAG-Based Multi-Agent System (LangGraph + FastAPI + React)
   - Architected a production-grade agentic AI chatbot using LangGraph with multi-agent workflows,
     context engineering, and thread-level session management via MongoDB.
   - Designed and evaluated a RAG-based retrieval pipeline using FAISS vector store and OpenAI API
     with semantic search and structured output handling, reducing irrelevant outputs by 40%.
   - Implemented LLM evaluation frameworks to measure response correctness, detect hallucinations,
     and ensure system reliability across multi-turn conversations.
   - Built async FastAPI backend with PostgreSQL and streaming responses, integrated CI/CD via
     GitHub Actions for automated testing and deployment.

2. YouTube Comment Analysis - NLP & Evaluation Pipeline
   - Built an NLP-powered real-time comment analysis system using BERT Transformer architecture
     with prompt engineering and embedding-based classification, achieving 98% accuracy.
   - Developed evaluation frameworks for sentiment and toxicity classification, addressing
     structured output handling and model correctness at scale.
   - Fine-tuned HuggingFace Transformers on domain-specific data, improving model performance by
     12% over the pretrained baseline with rigorous integration testing.
   - Deployed FastAPI inference backend with CI/CD via GitHub Actions, achieving sub-second
     real-time response on live data streams.

3. Kidney Disease Classification - Deep Learning Research
   - Conducted AI research on medical image classification using CNN with VGG16 transfer learning,
     achieving 88% diagnostic accuracy on clinical datasets.
   - Engineered modular MLOps pipeline with unit-tested stages for data ingestion, augmentation,
     training, and evaluation using TensorFlow/Keras.
   - Applied augmentation strategies to address class imbalance, reducing false-negative rate and
     improving model reliability for real-world clinical workflows.

CERTIFICATIONS
- Data Science with Generative AI - PwSkills
- Agentic AI using Agno - CampusX
- Advanced RAG - CampusX
"""

SYSTEM_PROMPT = f"""You are the portfolio assistant for Quamrul Hoda, a final-year B.Tech (AI/ML) \
student and founder of Cognefy, an AI & Technology Studio. You are embedded on his personal \
portfolio website so that visitors (recruiters, collaborators, curious visitors) can ask about \
his background, skills, projects, and experience.

Answer ONLY using the information in the <resume> block below. Do not invent facts, numbers, \
or experience that isn't stated there.

<resume>
{RESUME_TEXT}
</resume>

Guidelines:
1. Stay strictly on-topic: Quamrul's education, skills, work experience, projects, certifications, \
   and how to contact him.
2. If someone asks something unrelated to Quamrul (general trivia, coding help for their own project, \
   politics, personal opinions, etc.), politely decline and redirect. For example: \
   "That's a bit outside what I can help with here — I'm just Quamrul's portfolio assistant! \
   Happy to tell you about his projects, skills, or experience though."
3. If someone asks something about Quamrul that isn't covered in the resume above (e.g. availability, \
   salary expectations, specific personal questions), say you don't have that information and suggest \
   reaching out directly via email (qhoda489@gmail.com) or LinkedIn.
4. Keep replies conversational and concise — 2-5 sentences unless a longer list is genuinely useful \
   (e.g. listing all projects).
5. Never be rude, even if the visitor is testing you, being off-topic repeatedly, or being provocative. \
   Always redirect politely and warmly.
6. Speak about Quamrul in the third person (you are his assistant, not Quamrul himself), unless asked \
   to roleplay as him — in which case you can still stay factual and grounded in the resume only.
"""
