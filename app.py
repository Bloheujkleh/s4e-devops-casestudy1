from flask import Flask, request, render_template
import openai
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

client = openai.OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)

@app.route("/", methods=["GET", "POST"])
def index():
    code = None
    title = None
    if request.method == "POST":
        prompt = request.form["prompt"]
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {
                    "role": "system", 
                    "content": (
                        "You are a Python code generator assistant. "
                        "You generate Python classes based on the user's prompt.\n"
                        "Strictly respond in the following format:\n\n"
                        "Title: <A short and meaningful title related to the user's request>\n\n"
                        "```python\n"
                        "<A valid Python class that inherits from 'Task' and includes 'run' and 'calculate_score' methods>\n"
                        "```\n\n"
                        "Rules:\n"
                        "- Always include the title starting with 'Title:'.\n"
                        "- Always output Python code inside triple backticks (```python ... ```).\n"
                        "- The class must inherit from 'Task'.\n"
                        "- The class must contain 'run' and 'calculate_score' methods.\n"
                        "- Do not include any greetings, explanations, or additional text.\n"
                        "- Only output the title and the code."
                    )
                },
                {"role": "user", "content": prompt}
            ]
        )
        answer = response.choices[0].message.content.strip()

        if "Title:" in answer and "```python" in answer:
            title_part, code_part = answer.split("```python", 1)
            title = title_part.replace("Title:", "").strip()
            code = code_part.replace("```", "").strip()

    return render_template("index.html", code=code, title=title)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
