from flask import Flask, render_template, request
import google.generativeai as genai
import os

app = Flask(__name__)
genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/query')
def query():
    q = request.args.get('q') + " (use HTML to format the response)"
    response = model.generate_content(q)
    return response.text

if __name__ == '__main__':
    app.run(debug=True)