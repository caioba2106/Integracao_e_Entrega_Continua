from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return {"mensagem": "API funcionando corretamente"}

@app.route("/status")
def status():
    return {"status": "ok"}, 200

@app.route("/status")
def status():
    return {"status": "erro"}, 500

if __name__ == "__main__":
    app.run(debug=True)
