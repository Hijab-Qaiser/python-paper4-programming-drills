cities = [
    "Faisalabad",
    "Hyderabad",
    "Islamabad",
    "Karachi",
    "Lahore",
    "Multan",
    "Peshawar",
    "Quetta",
    "Rawalpindi",
    "Sialkot",
]  # string array


city_name = input(f"Enter a city name ")  # string variable


def binary_search_city(city_name):
    UB = len(cities) - 1  # integer variable
    LB = 0  # integer variable

    while LB <= UB:
        MP = int((UB + LB) / 2)  # integer variable

        if cities[MP].lower() == city_name.lower():
            return True
        elif city_name.lower() < cities[MP].lower():
            UB = MP - 1
        else:
            LB = MP + 1
    return False


print(binary_search_city(city_name))
