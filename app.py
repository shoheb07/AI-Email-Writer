from flask import Flask, render_template, request
from openai import OpenAI

app = Flask(__name__)

client = OpenAI(api_key="YOUR_API_KEY")

@app.route("/", methods=["GET", "POST"])
def home():

    email = ""

    if request.method == "POST":

        prompt = request.form["prompt"]

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {
                    "role": "user",
                    "content":
                    f"Write a professional email: {prompt}"
                }
            ]
        )

        email = response.choices[0].message.content

    return render_template(
        "index.html",
        email=email
    )

if __name__ == "__main__":
    app.run(debug=True)
