#Aufgabe 1: Strings und Input
text1 = input("Welches Projekt möchtest du umbenennen?")

text2 = " - Digital"

print(text1 + text2)

#Es folgt aufgabe zwei: Bedinungen
k = int(input("Wie viel Tassen Kaffee hattest du heute? "))

if 4 <= k <=8:
    print(f"Ich hatte {k} Kaffee. Man kann mit mir sprechen.")

elif k <= 3:
    print("Ich hatte noch nicht genug Kaffee. Komm später wieder.")

else:
    print("das war zu viel")

#Es folgt Aufgabe 3: Schleifen
n = 0

while n < 8:
    print(f"Die Kaffemenge {n} ist vertretbar")
    n = n + 1

else:
    print("zu viel Kaffee")
