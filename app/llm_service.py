import os
import json
import re
import requests

HF_API_TOKEN = os.getenv("ai_log")

HF_MODEL_URL = "https://router.huggingface.co/v1/chat/completions"

headers = {
    "Authorization": f"Bearer {HF_API_TOKEN}",
    "Content-Type": "application/json",
}


def analyze_logs_with_llm(logs: str):
    prompt = f"""
You are an expert SRE engineer.

Analyze the following logs and respond ONLY with valid JSON.
Do not include explanation or markdown.
Do not include any text outside JSON.

Logs:
{logs}

Return strictly in this format (ALL FIELDS MUST BE STRINGS except confidence):

{{
  "incident_type": "string",
  "severity": "low | medium | high | critical",
  "affected_service": "string",
  "root_cause": "short explanation in 1-2 sentences",
  "suggested_fix": "short actionable fix in 1-2 sentences",
  "confidence": 0.0
}}
"""

    payload = {
        "model": "mistralai/Mistral-7B-Instruct-v0.2",
        "messages": [{"role": "user", "content": prompt}],
        "max_tokens": 800,
        "temperature": 0.1,
    }

    response = requests.post(HF_MODEL_URL, headers=headers, json=payload)

    if response.status_code != 200:
        print("HF API Error:", response.text)
        return {
            "incident_type": "HF API Error",
            "severity": "Unknown",
            "affected_service": "Unknown",
            "root_cause": response.text,
            "suggested_fix": "Check HuggingFace API",
            "confidence": 0.0,
        }

    result = response.json()

    generated = result["choices"][0]["message"]["content"]

    print("===== RAW MODEL OUTPUT =====")
    print(generated)
    print("============================")

    try:
        json_match = re.search(r"\{.*\}", generated, re.DOTALL)

        if json_match:
            clean_json = json_match.group()
            return json.loads(clean_json)
        else:
            raise ValueError("No JSON found in model output")

    except Exception as e:
        print("Parsing failed:", str(e))

        return {
            "incident_type": "Parsing Error",
            "severity": "Unknown",
            "affected_service": "Unknown",
            "root_cause": generated[:500],
            "suggested_fix": "Manual review required",
            "confidence": 0.3,
        }
