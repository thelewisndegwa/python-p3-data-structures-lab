spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]

def get_names(spicy_foods):
    names = []
    for food in spicy_foods:
        names.append(food["name"])
    return names
    pass

def get_spiciest_foods(spicy_foods):
    spiciest_foods = []
    for food in spicy_foods:
        if (food["heat_level"]) > 5:
            spiciest_foods.append(food)
    return spiciest_foods
    pass

def print_spicy_foods(spicy_foods):
    for food in spicy_foods:
        heat_level_emojis = "🌶" * food["heat_level"]
        print(f"{food['name']} ({food['cuisine']}) | Heat Level: {heat_level_emojis}")
    pass

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for food in spicy_foods:
        if food["cuisine"] == cuisine:
            return food
    return None
    pass

def print_spiciest_foods(spicy_foods):
    spiciest_foods = get_spiciest_foods(spicy_foods)
    print_spicy_foods(spiciest_foods)
    pass

def get_average_heat_level(spicy_foods):
    total_heat_level = 0
    num_foods = len(spicy_foods)
    
    for food in spicy_foods:
        total_heat_level += food["heat_level"]
    
    if num_foods > 0:
        average = total_heat_level / num_foods
        return int(average)
    else:
        return 0
    pass

def create_spicy_food(spicy_foods, new_spicy_food):
    return spicy_foods + [new_spicy_food]
    pass