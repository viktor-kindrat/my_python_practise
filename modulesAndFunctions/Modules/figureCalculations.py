import math

def find_rectangle(a, b):
    return {
        "area": a * b,
        "perimeter": (a + b) * 2,
        "diagonal": math.sqrt(math.pow(a, 2) + math.pow(b, 2)),
        "radius_of_big_circle": 0.5 * math.sqrt(math.pow(a, 2) + math.pow(b, 2))
    }

def find_circle (r): 
    return {
        "area": math.pi * math.pow(r, 2),
        "length": 2 * math.pi * r,
        "diametr": r * 2
    }
