#from shapely import geometry
from shapely.geometry import Point
import shapely.wkt
import matplotlib.pyplot as plt

FHNW = Point([7.6140785,47.5394361])
#print(FHNW.wkt)

aiportSion = Point([46.22289784931113, 7.337911311639002])


FHNW2 = shapely.wkt.loads("POINT (47.5394361 7.6140785)")
#print(FHNW2.wkt)

file = open("C:/Users/antoi/Desktop/Programmierung2/Projektion/20211201_/schweiz.wkt")
schweiz_zeichenkette = file.read()


schweiz = shapely.wkt.loads(schweiz_zeichenkette)


"""
for geometry in schweiz.geoms:
    x,y = geometry.exterior.xy
    plt.plot(x,y)

plt.show()
"""

if FHNW.within(schweiz):
    print("FHNW ist in der CH")