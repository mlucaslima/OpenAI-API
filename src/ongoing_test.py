import openai
import json
from dotenv import load_dotenv
import os

# Load environment variables from the .env file
load_dotenv()

# Access the API key from the environment
api_key = os.getenv("MY_API_KEY")

# Print to verify it's working (for debugging)
print(api_key)