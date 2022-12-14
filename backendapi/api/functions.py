from math import radians, cos, sin, asin, sqrt


def get_port_ip(request):
    port = request.get_port()

    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')

    return ip, port


def haversine(lon1, lat1, lon2, lat2):
    # convert decimal degrees to radians
    lon1, lat1, lon2, lat2 = map(radians, [lon1, lat1, lon2, lat2])

    # haversine formula
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * asin(sqrt(a))
    r = 6371  # Radius of earth in kilometers. Use 3956 for miles
    return c * r


center_point = [{'lat': -7.7940023, 'lng': 110.3656535}]
test_point = [{'lat': 49.84241662861016, 'lng': 24.035976611107227}]

lat1 = center_point[0]['lat']
lon1 = center_point[0]['lng']
lat2 = test_point[0]['lat']
lon2 = test_point[0]['lng']

radius = 1.00  # in km

a = haversine(lon1, lat1, lon2, lat2)

# print('Distance (km) : ', a)
# if a <= radius:
#     print('Inside the area')
# else:
#     print('Outside the area')
