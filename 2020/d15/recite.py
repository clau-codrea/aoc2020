def recite(numbers, last):
    previous_position = {}
    for index, number in enumerate(numbers):
        previous_position[number] = -index

    number = numbers[-1]
    turn = len(numbers) - 1
    while turn < last - 1:
        if number not in previous_position:
            previous_position[number] = -turn
            number = 0
        else:
            aux = turn + previous_position[number]
            previous_position[number] = -turn
            number = aux

        turn += 1

    return number
