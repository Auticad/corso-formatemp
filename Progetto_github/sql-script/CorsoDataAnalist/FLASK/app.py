# Importa il modulo Flask
from flask import Flask

# Crea un'istanza di Flask
app = Flask(__name__)

# Crea una route che risponda a GET /
@app.route("/")

def hello_world():
    return "<p>Ciao mondo!</p>"

# Avvia la web app
if __name__ == "__main__":
    app.run(debug=True)