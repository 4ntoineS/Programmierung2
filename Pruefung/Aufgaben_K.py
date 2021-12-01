# was ist eine Klassendefinition?
#
#       Eine Klassendefinition ist ein Bauplan für eine Klasse
#       in dem alle Atributte und Methoden definiert sind.

#       Bsp.)
class Haus():
        def __init__(self, hoehe, wohnungen):
                self.hoehe = hoehe
                self.wohnungen = wohnungen
                pass

# Was sind Instanzen?
        
#       Bsp.)
Haus1 = Haus(10.5, 4)
Haus2 = Haus(33, 16)
print(Haus2)

# -----------------------------------------------------------------------------
# Was sind magishce Methoden in Python
# und für was können diese verwendet werden?

"""Magische Methoden sind spezielle Methoden, die einer Klasse besondere Fähigkeiten geben.
Sie sind desshalb magisch, weil sie nicht direkt aufgerufen werden müssen.
Jene Methoden sind von Python schon vordefiniert.
Die Benennung dieser Methoden beginnen und enden mit 2 underscores
BSP.:
__init__  ->> ist der Konstruktor
__str__   ->> Zeichenkette wird generiert, um mit der print() Funktion diese auszugeben
..."""


# -----------------------------------------------------------------------------
# Implementieren Sie eine Klasse Stadt in Python.
# Diese ist durch folgendes UML Diagram gegeben:

class Stadt:
        def __init__(self, name, einwohner, land, koordinate):
            self.name = name
            self.einwohnerzahl = einwohner
            self.land = land
            self.koordinate = koordinate
            pass

        def __str__(self) -> str:
            return f"Stadt: {self.name}; Land: {self.land}"
            pass
# "Koordinate und "land" sind vom Datentyp "tuple" resp. "str".
# Weshalb wäre es sinnvoll für diese eingene Klassen einzuführen

"""Land:
        Das Land wird für jede Stadt neu definiert. Besser wäre hier mit zu arbeiten,
        da dann der Ländername nur einmal eingetippt werden muss.
        Wenn man alle Einträge von Hand eintippt schleicht sich schnell ein Tippfehler ein.
        Als Beispiel.: Tippe ich aus versehen Schwiz anstatt Schweiz ein, so funktionieren
        alle Länderspezifischen Abfragen nicht mehr.
Koordinate:
        Wenn die Koordinaten eine eigene Klasse wären, so können Beispielsweise 
        Koordinatentransformationen in dieser Klasse definiert und automatisiert werden."""

# -----------------------------------------------------------------------------

# Erstellen Sie mit Python eine Klasse Dreieck welche mit einem sinnvollen
# Konstruktor instanziiert werden kann.

"""Voraussetzung hier: Klasse Punkt, Strecke und Dreieck in der Gleichen Datei."""

# -----------------------------------------------------------------------------
# Implementieren Sie folgendes GUI

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

layout = QFormLayout()
event = QLineEdit()
calendar = QCalendarWidget()
button = QPushButton("OK")

layout.addRow("Event-Name", event)
layout.addRow("Datum", calendar)
layout.addRow(button)

# -----------------------------------------------------------------------------
# Implementieren Sie folgende GUI-Applikation. Der Betrag in Schweizer Franken
# kann im QLineEdit eingegeben werden. Nach klicken auf den Button "umrechnen" wird
# der Betrag in Euro als QLabel angezeigt.

from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

### Siehe Aufgaben Fabrice ###

######################################
# Was wird automatisch aufgerufe, wenn eine neue
# Instanz einer Klasse erstellt wird?
""" Ja: Der Konstruktor
  Nein: Die Klasse
        eine None- Methode
        eine Methode, welche den Wert zurückgibt.
"""

# Was ist die Aufgabe dieses Programms?
# ...

# Welche Aussagen sind wahr?
""" Ja: init(3).__add__(2) gibt 5
        Es können mehrere Instanzen aus derselben Klasse erzeugt werden
        Wird eine Klasse vererbt, so muss der Konstruktor der vererbten Klasse mit super().__init__() manuell aufgerufen werden.
  Nein: Klassen gibt es nicht in Python.
"""

# Integer in Römische Zahl (int_to_roman(num))
### Siehe Aufgaben Fabrice ###

# Wahr oder Falsch
""" Wahr: - In numpy können einzelne Arrays nur einen einzigen Datentypen enthalten.
          - Das Modul "matplotlib" muss zusätzlich installiert werden, es gehört nicht zum Standardumfang von Python
          - mit dem Qt Designer können GUI erstellt werden. Diese werden in XML basierten ui-Files gespeichert.
  Falsch: - Dieses Programm stürzt nach der Installation von numpy ab: ???
          - In Numpy wird mit np.arange(1,5) folgendes array erstellt:
                array([1,2,3,4,5])

"""
