import utm


def clean_coords(c):
    i = 0
    lat = 0
    resultado = []
    while i < len(c):
        if i % 2 == 0:
            long = c[i]
        else:
            lat = c[i]
            resultado.append((lat, long))
        i += 1

    return resultado


def lat_to_utm(coords):
    resultado = []
    for par in coords:
        resultado.append(utm.from_latlon(par[0], par[1]))
    return resultado


def utm_to_xy(coords):
    resultado = []
    for c in coords:
        x = c[0]
        y = c[1]
        resultado.append((x,y))
    return resultado
