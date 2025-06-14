from flask import Flask, request, jsonify
from openai import OpenAI
import json
import os

# Load course content
with open("tds_course_content.json", "r", encoding="utf-8") as f:
    course_data = json.load(f)

# Initialize OpenAI client (use your key here or set env var)
client = OpenAI(
    api_key=os.getenv("OPENROUTER_API_KEY"),  # ✅ get from env
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
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
