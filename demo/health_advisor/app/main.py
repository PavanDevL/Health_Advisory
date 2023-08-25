# main.py
from flask import Flask, render_template, request
from .config import Config
import openai
from app import app
openai.api_key = Config.get_openai_key()

@app.route("/", methods=["GET", "POST"])
def index():
    advice = ""
    
    if request.method == "POST":
        user_goals = request.form.get("goals")
        
        # Use OpenAI's GPT-3 to generate personalized advice based on user input
        response = openai.Completion.create(
            engine="davinci", 
            prompt=user_goals + "\nAdvice:",
            max_tokens=100
        )
        advice = response.choices[0].text.strip()

    return render_template("index.html", Advice=advice)

if __name__ == "__main__":
    app.run(debug=True)
