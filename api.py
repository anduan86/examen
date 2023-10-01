from flask import Flask
from consulta import get_equipo
app = Flask(__name__)

@app.route("/api/")
def api():
    return get_equipo("medisono")

if __name__ == "__main__":
    app.run(host="0.0.0.0",port=5000,debug=True)