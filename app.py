from flask import Flask, request, jsonify
from openai import OpenAI
import json
import os

# Load course content
with open("../tds/tds_course_content.json", "r", encoding="utf-8") as f:
    course_data = json.load(f)

# Initialize OpenAI client (use your key here or set env var)
client = OpenAI(
    api_key="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",  # 👈 Replace with your key
    base_url="https://openrouter.ai/api/v1"
)

# Initialize Flask app
app = Flask(__name__)

@app.route("/ask")
def ask():
    question = request.args.get("q", "")
    if not question:
        return jsonify({"error": "Missing question"}), 400

    context = "\n".join(course_data[:50])  # You can adjust how much content is passed
    prompt = f"""You are a virtual assistant for the TDS course. 
Use the following course content to help answer questions:\n{context}\n"""

    try:
        response = client.chat.completions.create(
            model="openai/gpt-3.5-turbo",  # or use "mistralai/mistral-7b-instruct"
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": question}
            ]
        )
        answer = response.choices[0].message.content
        return jsonify({"answer": answer})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Run Flask app
if __name__ == "__main__":
    app.run(debug=True)
