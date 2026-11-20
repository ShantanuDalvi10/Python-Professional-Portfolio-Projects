from flask import Flask,redirect,url_for
from config import Config
from routes.routes import stats

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(stats)

@app.route("/")
def home():
    return redirect(url_for("stats.home"))

if __name__=="__main__":
    app.run(debug=True)