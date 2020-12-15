def recite(numbers, last):
    previous_position = {}
    for index, number in enumerate(reversed(numbers)):
        previous_position[number] = index

    number = numbers[-1]
    turn = len(numbers)
    while turn != last:
        if number not in previous_position:
            previous_position[number] = 0
            number = 0
        else:
            aux = previous_position[number]
            previous_position[number] = 0
            number = aux

        for counter in previous_position:
            previous_position[counter] += 1
        turn += 1

    return number
