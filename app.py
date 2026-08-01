from flask import Flask, render_template, send_from_directory
from dotenv import load_dotenv
from chatbot_routes import chatbot_bp

import os

load_dotenv()

app = Flask(__name__)
app.secret_key = os.environ.get("FLASK_SECRET_KEY", "dev-secret-change-me")
app.register_blueprint(chatbot_bp)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/resume/view')
def resume_view():
    return send_from_directory('resume', 'quamrulHoda_resume.pdf')


@app.route('/resume/download')
def resume_download():
    return send_from_directory('resume', 'quamrulHoda_resume.pdf',
                               as_attachment=True,
                               download_name='QuamrulHoda_Resume.pdf')


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    print(f'\n  🚀 Portfolio server running at:')
    print(f'  ➜ Local:   http://localhost:{port}')
    print(f'  ➜ Network: http://0.0.0.0:{port}\n')
    app.run(host='0.0.0.0', port=port, debug=True)
