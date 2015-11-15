#Erstes Programm von David Fürstenau

import random
random.seed()
level = 0
for i in range(1,11):
	a = random.randint(1,10*(level+1))
	b = random.randint(1,10*(level+1))
	c = a + b
	fehler = 1
	versuch = 0
	while versuch < 3 or fehler == 0:
		print("Die Aufgabe ist:", a, "+", b," Bitte eine Zahl eingeben:")
		versuch = versuch + 1
		z = input()
		try:
			zahl = int(z)
			if zahl == c:
				print("Das ist richtig")
				fehler = 0
				level = level + 1
				print("Du bist Level ", level)
				break
			elif zahl < 0 or zahl > 100:
				print(zahl, "ist ganz weit weg")
			elif c-1 <= zahl <= c+1:
				print(zahl, "ist ganz nahe dran")
			else:
				print(zahl, "ist falsch")
		except:
			print("falsche eingabe")
	print("Ergebnis: ", c)
	print("Anzahl versuche:", versuch)

print("Ende")
