from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():

@app.route("/sobre")
def sobre():

if __name__ == "__main__":
    app.run(debug=True)