#!/usr/bin/env python3
"""MiMo README Generator - Auto-create READMEs."""
import os, pathlib
from openai import OpenAI

client = OpenAI(api_key=os.getenv("MIMO_API_KEY"), base_url="https://api.xiaomimimo.com/v1")

def generate(d="."):
    files = [str(f) for f in pathlib.Path(d).rglob("*") if f.is_file()][:50]
    r = client.chat.completions.create(model="mimo-v2.5-pro", messages=[
        {"role": "system", "content": "Professional README: title, description, features, install, usage, license."},
        {"role": "user", "content": f"Files: {chr(10).join(files)}"}])
    return r.choices[0].message.content

if __name__ == "__main__":
    with open("README.md", "w") as f: f.write(generate())
    print("README.md generated!")
