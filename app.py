import os

import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("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")


def generate_prompt(job_title, keyword1, keyword2):
    prompt_template = "We are looking for a {job_title} to join our team. The ideal candidate should have experience in {keyword1} and {keyword2}. {static_sentence}"

    static_sentence = "Plak hier de standaard-zin."  # Replace with your actual sentence

    prompt = prompt_template.format(
        job_title=job_title,
        keyword1=keyword1,
        keyword2=keyword2,
        static_sentence=static_sentence
    )

    return prompt


@app.route("/", methods=("GET", "POST"))
def index():
    if request.method == "POST":
        job_title = request.form["job_title"]
        keyword1 = request.form["keyword1"]
        keyword2 = request.form["keyword2"]

        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=generate_prompt(job_title, keyword1, keyword2),
            temperature=0.6,
        )

        return redirect(url_for("index", result=response.choices[0].text))

    result = request.args.get("result")
    return render_template("index.html", result=result)

if __name__ == '__main__':
    app.run()