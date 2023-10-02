import requests
def get_equipo(equipo: str, verbose: bool = False) -> dict:
    url = f"https://apiprod.elhospital.com/es/api/v1/content/product/{equipo}"
    user_agent = {'User-agent': 'Mozilla/5.0'}
    r = requests.get(url=url, headers=user_agent).json()

    for i in range(16):
        producto = r['rows'][i]['image']['alt']
        descripcion = r['rows'][i]['summary']
        titulo = r['rows'][i]['title']
        publicado = r['rows'][i]['published']
        if verbose:
            print(f"{titulo} {producto} {descripcion} {publicado}")
    return {
        titulo,
        producto,
        descripcion,
        publicado
    }