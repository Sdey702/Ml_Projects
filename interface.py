from flask import Flask
import config

app = Flask(__name__)

# we have to import route classes from rout packege 
from route import main_route
from route import medicle_insurence_route


if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.PORT_NUMBER)
