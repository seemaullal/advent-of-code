with open("../inputs/5.txt") as file:
    (
        seeds,
        soil,
        fertilizer,
        water,
        light,
        temperature,
        humidity,
        location,
    ) = [
        [int(value) for value in values.split(":")[1].strip().split()]
        for values in file.read().split("\n\n")
    ]
