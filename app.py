
## https://python.plainenglish.io/deploy-your-python-flask-api-on-linux-based-azure-app-service-using-github-actions-5a54d5f9807
import flask
app = flask.Flask(__name__)

@app.route("/home")
def home():
    return "Flask API get endpoint running"

@app.route("/test")
def test():
    return "<h1>This is a test</h1>"

if __name__ == "__main__":
    app.run()