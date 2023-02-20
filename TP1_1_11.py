
infraction = [
("Edward", "Elric", 5),
("Izumi", "Curtis", 9),
("King", "Bradley", 0),
("Maes", "Hughes", 4)
]

sort = sorted(infraction, key = lambda x: x[2], reverse = True)

print(sort)