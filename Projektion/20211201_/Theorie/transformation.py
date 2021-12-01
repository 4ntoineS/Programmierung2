##"https://www.swisstopo.admin.ch/fr/cartes-donnees-en-ligne/calculation-services/navref.html"  swisstopo 

from pyproj import Transformer

t = Transformer.from_crs("EPSG:2056", "EPSG:4326")

resultat = t.transform(2_600_000, 1_200_000)

print(resultat)

swisstopo = [46.95108277187109, 7.43863242087181]

print(resultat[0] - swisstopo[0])
print(resultat[1] - swisstopo[1])