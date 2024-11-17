import itertools

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

combos = list(itertools.combinations(FLAVORS, 2))

for i in combos:
    print(f"{i[0]}, {i[1]}")