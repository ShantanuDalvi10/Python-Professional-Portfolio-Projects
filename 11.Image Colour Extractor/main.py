from flask import Flask
from routes.colour_routes import color
app = Flask(__name__)

app.register_blueprint(color)






if __name__ == "__main__":
    app.run(debug=True)