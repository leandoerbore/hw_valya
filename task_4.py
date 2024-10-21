companions = ["Astarion", "Gale", "Karlach", "Lae'zel",
              "Shadowheart", "Wyll", "The Dark Urge", "Halsin",
              "Jaheira", "Minsc", "Minthara", "Alfira", "Losiir"]

# обычный
slice1 = companions[1:4]
print(slice1)

# С шагом в 2
slice2 = companions[1:12:2]
slice2.insert(4, companions[7])
print(slice2)

# С шагом в 3 с конца до начала
slice3 = companions[-2::-3]
print(slice3)

# Первый и последний (один шаг в длину списка)
slice4 = companions[::len(companions)-1]
print(slice4)

# Your code here ( • ᴗ - ) ✧

