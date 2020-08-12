import math


def calculate_distance(lat1: float, lng1: float, lat2: float, lng2: float) -> float:
    _radius = 6371e3
    pi_r = math.pi / 180
    fi1 = lat1 * pi_r
    fi2 = lat2 * pi_r
    df = (lat2 - lat1) * pi_r
    dl = (lng2 - lng1) * pi_r

    a = math.sin(df / 2) * math.sin(df / 2) + math.cos(fi1) * math.cos(fi2) * math.sin(dl / 2) * math.sin(dl / 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    distance = _radius * c
    return distance

