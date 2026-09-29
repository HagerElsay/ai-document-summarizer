import urllib.request
import urllib.error
import json

# Read API key from your private file
with open("api_key.txt", "r") as f:
    API_KEY = f.read().strip()

# Read your document
with open("document.txt", "r") as f:
    document = f.read()

url = "https://api.openai.com/v1/responses"

data = {
    "model": "gpt-5.6-luna",
    "input": "Summarize this document clearly and briefly:\n\n" + document
}

request_data = json.dumps(data).encode("utf-8")

request = urllib.request.Request(
    url,
    data=request_data,
    headers={
        "Content-Type": "application/json",
        "Authorization": "Bearer " + API_KEY
    },
    method="POST"
)

try:
    with urllib.request.urlopen(request) as response:
        result = json.loads(response.read().decode("utf-8"))
        print("\n===== AI SUMMARY =====\n")
        print(result["output"][0]["content"][0]["text"])

except urllib.error.HTTPError as e:
    print("API Error:", e.code)
    print(e.read().decode("utf-8"))
