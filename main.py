from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Nestle, This app is running on OpenShift 4.8 in W2K VMware environment. Welcome to Version 1.0 !"
