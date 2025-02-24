from machinetranslation import translator
from flask import Flask, render_template, request
#import json

app = Flask(__name__)


@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.english_to_french(textToTranslate)
    # return "Translated text to French"
    return "Translated text to French: " + translated_text


@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    translated_text = translator.french_to_english(textToTranslate)
    # returns "Translated text to English"
    return "Translated text to English: " + translated_text


@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template("index.html")


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
