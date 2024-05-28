from flask import Flask, render_template
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/stream')
def stream():
    response = model.generate_content("What is the meaning of life?", stream=True)
    for chunk in response:
        return chunk.text