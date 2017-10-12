import numpy as np

cities = {
    'Austin': (-97.75, 30.25),
    'Brussels': (4.35, 50.85),
    'Dormstadt': (8.65, 49.86),
    'Krakow': (19.93, 50.06),
    'London': (-0.13, 51.5),
    'Pisa': (10.35, 43.716),
    'Valencia': (0.383, 39.46),
    'Zurich': (8.55, 47.36)
    }

displacement_vectors = [
    [102.1, 20.6],
    (4.3, -.983),
    (-.1, -2.5),
    (1.8, -3.65),
    (9.583, 6.35),
    (-20.06, 1.43),
    (0.516, -12.03),
    (-98.13, -9.216)
    ]

destinations = cities.keys()

for city in cities:
    
    for place in destinations:
        if np.subtract(cities[place], cities[city]) in any(displacement_vectors):
            print(place)
    
#    print(city)
#    print([np.subtract(cities[place], cities[city]) for place in destinations])
