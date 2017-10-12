import numpy as np

cities = {
    'Austin': ['-97°22\'30°15\''],
    'Brussels': ['4°21\'50°51\''],
    'Dormstadt': ['8°39\'49°52\''],
    'Krakow': ['19°56\'50°4\''],
    'London': ['-0°8\'51°30\''],
    'Pisa': ['10°21\'43°43\''],
    'Valencia': ['0°23\'39°28\''],
    'Zurich': ['8°33\'47°22\''],
    }

displacement_vectors = [
    ['120°6\'20°36\''],
    ['4°18\'-0°59\''],
    ['0°6\'-2°30\''],
    ['1°48\'-3°39\''],
    ['9°35\'6°21\''],
    ['-20°4\'1°26\''],
    ['0°31\'-12°2\''],
    ['-98°8\'-9°13\''],
    ]

def dms2dd(city):
    
    dd = float(degrees) + float(minutes)/60;
    return dd;





#cities = {
#    'Austin': (-97.75, 30.25),
#    'Brussels': (4.35, 50.85),
#    'Dormstadt': (8.65, 49.86),
#    'Krakow': (19.93, 50.06),
#    'London': (-0.13, 51.5),
#    'Pisa': (10.35, 43.716),
#    'Valencia': (0.383, 39.46),
#    'Zurich': (8.55, 47.36)
#    }
#
#displacement_vectors = [
#    [102.1, 20.6],
#    [4.3, -.99],
#    [-.1, -2.5],
#    [1.8, -3.65],
#    [9.58, 6.35],
#    [-20.06, 1.43],
#    [0.52, -12.03],
#    [-98.13, -9.22]
#    ]

def find_itinerary(cities, displacement_vectors, city):
#    for index, city in enumerate(cities):
#        print(index)
##    for city in cities:
#        for place in destinations:
    destinations = list(cities.keys())
    itinerary = []
#    total_cities = len(destinations) - 1
    
    for place in destinations:
        print('CITY', city)
        if list(np.subtract(cities[place], cities[city])) in displacement_vectors:
            itinerary.append(place)
            city = place
    
    return itinerary
        
    
#    print(city)
#    print([np.subtract(cities[place], cities[city]) for place in destinations])

print(find_itinerary(cities, displacement_vectors, 'Austin'))

#itinerary = [list(np.subtract(cities[place], cities[city])) for place in destinations] in displacement_vectors