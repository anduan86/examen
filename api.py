import requests
from flask import Flask
from flask import request
from consulta import get_equipo

app = Flask(__name__)


@app.route("/api/")
def api():
    equipos = requests.args.get('equipos')
    equipos = equipos.split(',')

    result = []
    for t in equipos:
        result.append(get_equipo(t))
    return get_equipo(equipo)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
