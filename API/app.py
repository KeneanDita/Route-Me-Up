from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, World!"


@app.route("/drinks")
def drinks():
    return {"drinks": ["coffee", "tea", "water"]}


if __name__ == "__main__":
    app.run(debug=True)
