import requests
import os

# Define the URL for the POST request
url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key='
url += str(os.environ.get("GOOGLE_API_KEY"))

# Create a dictionary for headers
headers = {
    "Content-Type": "application/json",  # Adjust content type as needed (e.g., application/xml)
}

q = "Explain how AI works, respond in HTML not Markdown" 
# Prepare the data to be sent (can be JSON, string, etc.)
data = '{"contents":[{"parts":[{"text":"' + q + '"}]}]}'

# Send the POST request with headers and data
response = requests.post(url, headers=headers, data=data)

# Check the response status code
if response.status_code == 200:
  # Access the response data (if any)
  response_data = response.json()
  print(response_data["candidates"][0]["content"]["parts"][0]["text"])
else:
  print("Error! Response code:", response.status_code)
  print(response.json())
