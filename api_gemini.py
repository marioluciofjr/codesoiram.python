# API do Gemini

def api(secret: str):
  from google.colab import userdata
  import os

  api_key = userdata.get(secret)
  os.environ["GOOGLE_API_KEY"] = api_key

  print("API configurada")
