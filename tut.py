cars = [
    {
        "name": "Supra",
        "brand": {
            "name": "Toyota",
            "country": "Japan"
        }
    },
    {
        "name": "Yaris GR",
        "brand": {
            "name": "Toyota",
            "country": "Japan"
        }
    },
    {
        "name": "Civic",
        "brand": {
            "name": "Honda",
            "country": "Japan"
        }
    },
    {
        "name": "TT",
        "brand": {
            "name": "Audi",
            "country": "Germany"
        }
    },
]

def carFilt(brandName, countryOfOrigin = 0):
    filtered = []
    for x in cars:
        if x["brand"]["name"] == brandName and x["brand"]["country"] == countryOfOrigin:
            filtered.append(x)
    return filtered

print(carFilt("Toyota", "Japan"))