import google.generativeai as genai

genai.configure(api_key="your-api-key-here")

model = genai.GenerativeModel("gemini-pro")
response = model.generate_content("What is today's date?")
print(response.text)
