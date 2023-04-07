import os
import openai

OPENAI_API_KEY = "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"
openai.api_key = os.getenv("OPENAI_API_KEY")
response = openai.Image.create(
  prompt="a white siamese cat",
  n=1,
  size="1024x1024"
)
url = "https://api.openai.com/v1/images/generations"
image_url = response['data'][0][url]