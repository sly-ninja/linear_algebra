import numpy as np
#np.set_printoptions(precision=4)
import re 

def convert_to_decimal(dms):
    """
    takes in coordinate strings
    returns array pf coordinates as decimals
    """
    coordinates = re.split('[°\'"]+', dms)
    WE = abs(float(coordinates[0])) + abs(float(coordinates[1])/60)
    NS = abs(float(coordinates[2])) + abs(float(coordinates[3])/60)

    if '-' in (coordinates[0] or coordinates[1]):
        WE *= -1
    if '-' in (coordinates[2] or coordinates[3]):
        NS *= -1
        
    return [WE, NS]


def update_dict(cities):
    """
    takes in dictionary of cities and their corresponding coordinates
    returns updated dictionary with coordinates in decimals
    """
    for city in cities:
        cities[city] = convert_to_decimal(cities[city])
    
    return cities


def update_list(displacement_vectors):
    """
    takes in an array of coordinate strings
    returns array of coordinates in decimals
    """
    vector_list = [convert_to_decimal(vector) for vector in displacement_vectors]
    
    return np.array(vector_list)


def find_itinerary(city_list, vector_array, city):
    """
    function to determine itinerary based on a list of displacement vectors
    takes in a list of cities and list of displacement vectors and starting city
    returns a list of cities in itinerary 
    """
    destinations = list(city_list.keys())
    itinerary = []
    
    for place in destinations:
        print('CITY', city)
        if np.subtract(city_list[place], city_list[city]).tolist() in vector_array:
            itinerary.append(place)
            city = place
    
    return itinerary



cities = {
    'Austin': '-97°45\'30°15\'',
    'Brussels': '4°21\'50°51\'',
    'Dormstadt': '8°39\'49°52\'',
    'Krakow': '19°56\'50°4\'',
    'London': '-0°8\'51°30\'',
    'Pisa': '10°21\'43°43\'',
    'Valencia': '0°23\'39°28\'',
    'Zurich': '8°33\'47°22\'',
    }

displacement_vectors = [
    '120°6\'20°36\'',
    '4°18\'-0°59\'',
    '0°6\'-2°30\'',
    '1°48\'-3°39\'',
    '9°35\'6°21\'',
    '-20°4\'1°26\'',
    '0°31\'-12°2\'',
    '-98°8\'-9°13\'',
    ]

city_list = update_dict(cities)
vector_list = update_list(displacement_vectors)
print(find_itinerary(city_list, vector_list, 'Austin'))



#vector_list = [
#    [120.1, 20.6],
#    [4.3, -0.9833333333333333],
#    [0.1, -2.5],
#    [1.8, -3.65],
#    [9.583333333333334, 6.35],     
#    [-20.066666666666666, 1.4333333333333333],
#    [0.5166666666666667, -12.033333333333333],
#    [-98.13333333333334, -9.216666666666667]
#    ]

# =============================================================================
# #cities = {
# #    'Austin': (-97.75, 30.25),
# #    'Brussels': (4.35, 50.85),
# #    'Dormstadt': (8.65, 49.86),
# #    'Krakow': (19.93, 50.06),
# #    'London': (-0.13, 51.5),
# #    'Pisa': (10.35, 43.716),
# #    'Valencia': (0.383, 39.46),
# #    'Zurich': (8.55, 47.36)
# #    }
# #
# #displacement_vectors = [
# #    [102.1, 20.6],
# #    [4.3, -.99],
# #    [-.1, -2.5],
# #    [1.8, -3.65],
# #    [9.58, 6.35],
# #    [-20.06, 1.43],
# #    [0.52, -12.03],
# #    [-98.13, -9.22]
# #    ]
# 
# def find_itinerary(cities, displacement_vectors, city):
# #    for index, city in enumerate(cities):
# #        print(index)
# ##    for city in cities:
# #        for place in destinations:
#     destinations = list(cities.keys())
#     itinerary = []
# #    total_cities = len(destinations) - 1
#     
#     for place in destinations:
#         print('CITY', city)
#         if list(np.subtract(cities[place], cities[city])) in displacement_vectors:
#             itinerary.append(place)
#             city = place
#     
#     return itinerary
#         
#     
# #    print(city)
# #    print([np.subtract(cities[place], cities[city]) for place in destinations])
# 
# #print(find_itinerary(cities, displacement_vectors, 'Austin'))
# 
# #itinerary = [list(np.subtract(cities[place], cities[city])) for place in destinations] in displacement_vectors
# =============================================================================
