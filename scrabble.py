"""
Give a variable number of words, create a program to output the word with the maximum score, based on the following scoring system: 

The score of a word is calculated based on its character values, according to this table: 
e, a, i, o, n, r, t, l, s, u are equal 1 point 
d, g 2 points 
b, c, m, p 3 points 
f, h, v, w, y 4 points 
k 5 points 
j, x 8 points 
q, z 10 points 

The max length of a word is 10 letters. 

For example: 
input { "This",  "is", "a", "cool" , "Challenge" } 
output : Challenge
"""

#Dict. anlegen
wertung = {
    "e":1, "a":1, "i":1, "o":1, "n":1, "r":1, "t":1, "l":1, "s":1, "u":1, 
    "d":2, "g":2, 
    "b":3, "c":3, "m":3, "p":3, 
    "f":4, "h":4, "v":4, "w":4, "y":4,
    "k":5,
    "j":8, "x":8,
    "q":10, "z":10}


#Eingabe der Wörter
#Abfrage der Anzahl der Wörter
anzahl = input("Wie viele Wörter möchten Sie eingeben?: ")
anzahl = int(anzahl)

#Abfrageschleife der Wörter
wortliste = []
for i in range(anzahl):
    nr = int(i+1)
    wortliste.append(input("Bitte %d. Wort von %d eingeben: " % (nr, anzahl)))

#Großbuchstaben klein machen
wortliste = [element.lower() for element in wortliste]

print(wortliste)
summe = 0

for k, v in wertung.items():
    for i in wortliste[0]:
        if k == i:
                summe = summe + v

print(summe)
        










"""
wort1 = input("Bitte Wort Nr. 1 eingeben: ")
wort1 = wort1.lower()

wort2 = input("Bitte Wort Nr. 2 eingeben: ")
wort2 = wort2.lower()

wort3 = input("Bitte Wort Nr. 3 eingeben: ")
wort3 = wort3.lower()

wort4 = input("Bitte Wort Nr. 4 eingeben: ")
wort4 = wort4.lower()
"""