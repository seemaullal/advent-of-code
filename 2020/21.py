import sys
from collections import Counter

input_file = sys.argv[1] if len(sys.argv) > 1 else "inputs/21.txt"

with open(input_file) as file:
    foods = []
    for food in file.readlines():
        ingredients, allergens = food.strip().split(" (contains ")
        ingredients = set(ingredients.split(" "))
        allergens = set(allergens[:-1].split(", "))
        foods.append((ingredients, allergens))

ingredient_count = Counter()
all_ingredients = set()
all_allergens = set()
for ingredients, allergens in foods:
    all_ingredients = all_ingredients | ingredients
    all_allergens = all_allergens | allergens
    ingredient_count.update(ingredients)

possible_allergens = {ingredient: set(all_allergens) for ingredient in all_ingredients}
for ingredients, allergens in foods:
    for allergen in allergens:
        for ingredient in all_ingredients:
            if (
                ingredient not in ingredients
                and allergen in possible_allergens[ingredient]
            ):
                possible_allergens[ingredient].remove(allergen)


def part_1():
    not_allergen_count = 0
    for ingredient in all_ingredients:
        if len(possible_allergens[ingredient]) == 0:
            not_allergen_count += ingredient_count[ingredient]
    return not_allergen_count


def part_2():
    result = {}
    ingredients_with_allergens = {
        ingredient: allergens
        for ingredient, allergens in possible_allergens.items()
        if len(allergens) > 0
    }
    while len(result) != len(all_allergens):
        for ingredient, allergens in ingredients_with_allergens.items():
            if len(allergens) == 1:
                result[ingredient] = allergens.pop()
        for ingredient, allergens in ingredients_with_allergens.items():
            updated_allergens = set()
            for allergen in allergens:
                if allergen not in result.values():
                    updated_allergens.add(allergen)
            ingredients_with_allergens[ingredient] = updated_allergens
    return ",".join(sorted(result, key=lambda k: result[k]))


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
