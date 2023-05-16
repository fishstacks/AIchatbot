from flask import Flask, request, jsonify
from rasa.core.agent import Agent

app = Flask(__name__)

agent = Agent.load("./models/20230428-162253-searing-spitz.tar.gz")  


@app.route("/webhooks/chat", methods=["POST"])
def get_response():
    print("Received request:", request.json)
    request_data = request.json
    response = agent.handle_text(request_data["message"])  
    print("Sending response:", response)
    return jsonify(response)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5006)  
