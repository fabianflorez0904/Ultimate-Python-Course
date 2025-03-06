class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __eq__(self, otro):  # equal ==
        return self.lat == otro.lat and self.lon == self.lon

    def __ne__(self, otro):  # not equal !=
        return self.lat != otro.lat and self.lon != self.lon

    def __lt__(self, otro):  # Less Than <
        return self.lat + self.lon < otro.lat + otro.lon

    def __le__(self, otro):  # Less or Equal
        return self.lat + self.lon <= otro.lat + otro.lon


# <__main__.Coordenadas object at 0x00000220BFAE5E80>
# En donde esta guardada en espacion en memoria
coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords >= coords2)
