import os
import openai
OPEN_API_KEY = "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"
openai.api_key = os.getenv("OPEN_API_KEY")
openai.Image.create(
  prompt="Laptop",
  n=1,
  size="256x256"
)


# response = openai.Image.create(
#   prompt="Laptop",
#   n=1,
#   size="256x256"
# )
# image_url = response['data'][0]['url']