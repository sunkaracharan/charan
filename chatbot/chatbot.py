import os
import requests

class Chat:
    def __init__(self):
        pass

    def bot(self, prompt):
        API_URL = "https://router.huggingface.co/v1/chat/completions"
        headers = {
            "Authorization": "Bearer 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",  # Consider using os.environ for security
        }

        def query(payload):
            response = requests.post(API_URL, headers=headers, json=payload)
            if not response.ok:
                raise Exception(f"API Error: {response.status_code} {response.text}")
            return response.json()

        response = query({
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "model": "openai/gpt-oss-20b:together"
        })
        try:
            # Get the main content
            content = response["choices"][0]["message"]["content"]
            # Only keep the first line, strip whitespace, and remove extra newlines
            single_line = content.strip().replace('\n', ' ')
            # Optionally, keep only the first sentence (up to the first period)
            # import re
            # match = re.match(r"^(.*?\.)", single_line)
            # if match:
            #     single_line = match.group(1)
            return single_line
        except Exception:
            raise Exception(f"Unexpected API response: {response}")
