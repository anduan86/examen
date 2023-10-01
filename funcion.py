import requests

equipos = ['ultrasonido', 'monitor', 'flat+panel', 'rayos+x', 'resonancia']

def get_equipo(equipo, verbose: bool = False):
    url = "https://apiprod.elhospital.com/es/api/v1/content/product/{equipo}"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=user_agent).json()
    i=0
    for i in range(16):
        producto = r['rows'][i]['image']['alt']
        descripcion = r['rows'][i]['summary']
        titul = r['rows'][i]['title']
        publicado=r['rows'][i]['published']
        if verbose:
            print(f"{titul} {producto} {descripcion} {publicado}")
    return producto

for t in equipos:
    get_equipo(equipo=t, verbose=True)
