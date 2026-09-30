from unittest import result

import requests
Url ="http://localhost:11434/api/generate"

data = {"model": "llama3.2:1b", "prompt": "Explain the python in simple terms.", "stream": False}
response = requests.post(Url, json=data)
result = response.json()
print(result["response"])