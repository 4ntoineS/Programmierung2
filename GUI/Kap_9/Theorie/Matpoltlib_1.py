import matplotlib.pyplot as plt
import numpy as np

x = np.linspace(0, 2*np.pi, 20)  ## un segment tous les 20 -> courbe +/- régulière
y1 = np.sin(x)
y2 = np.cos(x)

plt.plot(x, y1, "ro-")  ## "ro-" -> Farbe der Kurve ist rot, "ko-" -> ist schwarz
plt.plot(x, y2, "ko-")

plt.title("Hier kommt der Titel")
plt.xlabel("x")
plt.ylabel("y")

plt.axis("equal")
plt.show()