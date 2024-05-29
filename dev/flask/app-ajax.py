from flask import Flask, render_template, session, request
import google.generativeai as genai
import os

app = Flask(__name__)
app.secret_key = os.urandom(16)
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')
chunks = []

@app.route('/')
def home():
    return render_template('ajax.html')

@app.route("/query")
def query():
    q = request.args.get('q')
    response = model.generate_content(q, stream=True)
    for chunk in response:
        chunks.append(chunk.text)
    return render_template('ajax.html')

@app.route('/stream')
def stream():
    if 'index' in session:
        if  int(session['index']) < len(chunks) - 1:
            session['index'] += 1
            return str(chunks[session['index']])
        else:
            return "END"
    else:
        session['index'] = -1
        return ""