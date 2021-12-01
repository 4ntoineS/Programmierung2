from pyproj import Transformer

t = Transformer.from_crs("EPSG:2056", "EPSG:4326")


file = open("C:/Users/antoi/Desktop/Programmierung2/Projektion/20211201_/PLZO_CSV_LV95.csv", encoding="utf-8")

next(file)      ##erste Zeile des files wird ignoriert


#Ortschaftsname;PLZ;Zusatzziffer;Gemeindename;BFS-Nr;Kantonskürzel;E;N;Sprache
for data in file:
    data = data.rstrip().split(";")

    name = data[0]
    E = float(data[6])
    N = float(data[7])
    resultat = t.transform(E,N)
    print(name, resultat)