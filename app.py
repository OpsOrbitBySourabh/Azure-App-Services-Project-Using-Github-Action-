from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! Flask deployed to Azure App Service via GitHub Actions (OIDC)."


@app.route("/healthz")
def healthz():
    return {"status": "ok"}, 200
# IMPORTANT for Azure
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000)
