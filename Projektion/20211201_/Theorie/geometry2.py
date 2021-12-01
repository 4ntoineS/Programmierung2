from shapely.geometry import Point
import shapely.wkt
import matplotlib.pyplot as plt

wkt1 = "POLYGON (( -5 -5, 5 -5, 5 5, -5 5, -5 -5))"
wkt2 = "POLYGON ((1 -1, 4 -1, 4 1, 1 1, 1 4, -1 4, -1 1, -4 1, -4 -1, -1 -1, -1 -4, 1 -4, 1 -1))"

quadrat = shapely.wkt.loads(wkt1)
kreuz = shapely.wkt.loads(wkt2)

if kreuz.within(quadrat):
    print("alles ok")

x1,y1 = quadrat.exterior.xy
x2,y2 = kreuz.exterior.xy

plt.plot(x1,y1, "ko-")
plt.plot(x2,y2, "ro-")
plt.axis("equal")

plt.show()

kreuzquadtrat = kreuz.union(quadrat)
print(kreuzquadtrat.wkt)

s2 = kreuz.intersection(quadrat)

s3 = kreuz.symmetric_difference(quadrat)
print(s3.wkt)

#plt.plot()