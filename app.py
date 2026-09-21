from flask import Flask, render_template, request, jsonify
from openai import OpenAI

app = Flask(__name__)

client = OpenAI()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get("message", "")

    if not user_message:
        return jsonify({
            "error": "Please enter a message."
        }), 400

    response = client.responses.create(
        model="gpt-5.6-luna",

        tools=[
            {
                "type": "web_search"
            }
        ],

        instructions="""
        Your name is GEM.

        You are a friendly, intelligent AI assistant.

        Give clear and useful answers.

        When a question requires current information,
        use web search.

        Never pretend to know something you don't know.
        """,

        input=user_message
    )

    return jsonify({
        "reply": response.output_text
    })


if __name__ == "__main__":
    app.run(debug=True)