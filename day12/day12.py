current_direction = 'east'
horizontal_position = 0
vertical_position = 0
directions = [[direction[0], int(direction[1:])] for direction in open('day12_input.txt')]
for direction, distance in directions:
    if direction == 'F':
        if current_direction == 'east':
            horizontal_position += distance
        elif current_direction == 'west':
            horizontal_position -= distance
        elif current_direction == 'north':
            vertical_position += distance
        elif current_direction == 'south':
            vertical_position -= distance
    elif direction == 'N':
        vertical_position += distance
    elif direction == 'S':
        vertical_position -= distance
    elif direction == 'E':
        horizontal_position += distance
    elif direction == 'W':
        horizontal_position -= distance
    elif direction == 'R':
        while distance > 0:
            if current_direction == 'north':
                current_direction = 'east'
            elif current_direction == 'east':
                current_direction = 'south'
            elif current_direction == 'south':
                current_direction = 'west'
            elif current_direction == 'west':
                current_direction = 'north'
            distance -= 90
    elif direction == 'L':
        while distance > 0:
            if current_direction == 'north':
                current_direction = 'west'
            elif current_direction == 'east':
                current_direction = 'north'
            elif current_direction == 'south':
                current_direction = 'east'
            elif current_direction == 'west':
                current_direction = 'south'
            distance -= 90
print('horizontal position', horizontal_position, 'vertical position', vertical_position) 
print('part 1 manhattan distance', abs(horizontal_position) + abs(vertical_position))
