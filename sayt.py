import os

from dotenv import load_dotenv
from flask import Flask, jsonify, render_template, request
from gigachat import GigaChat

app = Flask(__name__)
load_dotenv()
giga = GigaChat(credentials=os.getenv("CRED"), ca_bundle_file=os.getenv("SERT_PATH"))


def send_to_gigachat(message):
    for _ in range(2):
        try:
            response = giga.chat(message)
            return response.choices[0].message.content
        except Exception as e:
            print(f"Ошибка при выполнении запроса к GigaChat: {e}")
            giga.get_token()
    return "Ошибка при выполнении запроса к GigaChat."


@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")


@app.route("/process", methods=["POST"])
def process_request():
    text_input = request.form.get("input_text")
    try:
        result = send_to_gigachat(text_input)
        return jsonify({"result": result})
    except Exception as e:
        return jsonify({"error": str(e)})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
