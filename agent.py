import os, json, env
import datetime
from google import genai
from google.genai import types

# 1. Setup API Client
# Try to get the key from either common environment variable name

api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
if not api_key:
    raise ValueError("GEMINI_API_KEY environment variable is not set.")

client = genai.Client(api_key=api_key)

# 2. Filter for 'pro' models and sort to find the latest
models = client.models.list()
pro_models = [
    getattr(m, 'name', '') for m in models
    if getattr(m, 'name', '').startswith('models/gemini')
    and 'pro' in getattr(m, 'name', '').lower()
    and not any(x in getattr(m, 'name', '').lower() for x in ['image', 'lyria', 'banana'])
]
latest_pro = sorted(pro_models)[-1] if pro_models else "gemini-2.5-pro"

def build_project_from_readme():
    # 1. Read the human's requirements
    with open("README.md", "r") as f:
        requirements = f.read()

    prompt = f"""
    Act as a Senior Software Architect. Build a complete, production-ready 
    project base based on these requirements:
    {requirements}

    OUTPUT REQUIRES:
    1. A directory structure.
    2. Full source code for every file.
    3. Integration between all components.

    Return ONLY a JSON object:
    {{
      "files": [
        {{"path": "src/main.py", "content": "..."}},
        {{"path": "pyproject.toml", "content": "..."}},
        {{"path": "Dockerfile", "content": "..."}},
        {{"path": "Makefile", "content": "..."}}
      ]
    }}
    """
    
    response = client.models.generate_content(
        model=latest_pro,
        contents=prompt,
        config=types.GenerateContentConfig(
            response_mime_type="application/json",
            temperature=0.2
        )
    )

    data = json.loads(response.text)
    for file in data['files']:
        path = os.path.join("proposed_build", file['path'])
        os.makedirs(os.path.dirname(path), exist_ok=True)
        with open(path, "w") as f:
            f.write(file['content'])

if __name__ == "__main__":
    build_project_from_readme()
