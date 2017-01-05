import utm
from ponto import *

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
        p = Ponto()
        p.tuple_to_point(utm.from_latlon(par[0], par[1]))
        resultado.append(p)
    return resultado


def utm_to_lat(pto):
    return utm.to_latlon(pto.x, pto.y, zone_letter=pto.zone, zone_number=pto.number)
