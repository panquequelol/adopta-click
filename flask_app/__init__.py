from flask import Flask

app = Flask(__name__)

app.secret_key = "Este es mi texto secreto"

app.config['UPLOAD_FOLDER'] = 'flask_app/static/form_data/'