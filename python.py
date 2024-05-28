import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('GOOGLE_API_KEY'))
model = genai.GenerativeModel('gemini-1.5-flash')

response = model.generate_content("What is the meaning of life?", stream=True)

for chunk in response:
  print(chunk.text, end="")