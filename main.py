import requests
from io import BytesIO
from PIL import Image
import pygame
import sys
import os

from mapapi_PG import show_map

api_server = "http://static-maps.yandex.ru/1.x/"
lon = "37.530887"
lat = "55.703118"
delta = "0.5"

params = {
    "ll": ",".join([lon, lat]),
    "spn": ",".join([delta, delta]),
}

if __name__ == '__main__':
    response = requests.get(api_server, params=params)
    # Image.open(BytesIO(
    # response.content)).show()
    show_map(f'll={params["ll"]}&spn={params["spn"]}', map_type="map", add_params=None)
#map_request = "http://static-maps.yandex.ru/1.x/?ll=37.530887,55.703118&spn=0.002,0.002&l=map"
