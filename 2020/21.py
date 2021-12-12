from collections import Counter

with open("inputs/21.txt") as file:
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


def part_1():
    possible_allergens = {
        ingredient: set(all_allergens) for ingredient in all_ingredients
    }
    for ingredients, allergens in foods:
        for allergen in allergens:
            for ingredient in all_ingredients:
                if (
                    ingredient not in ingredients
                    and allergen in possible_allergens[ingredient]
                ):
                    possible_allergens[ingredient].remove(allergen)
    not_allergen_count = 0
    for ingredient in all_ingredients:
        if len(possible_allergens[ingredient]) == 0:
            not_allergen_count += ingredient_count[ingredient]
    return not_allergen_count


def part_2():
    pass


print(f"Part 1: {part_1()}")
print(f"Part 2: {part_2()}")
