def recite(numbers, last):
    previous_position = {}
    for index, number in enumerate(numbers):
        previous_position[number] = -index

    number = numbers[-1]
    turn = len(numbers)
    while turn != last:
        print(turn, number)
        if number not in previous_position:
            previous_position[number] = -(turn - 1)
            number = 0
        else:
            aux = (turn - 1) + previous_position[number]
            previous_position[number] = -(turn - 1)
            number = aux

        turn += 1

    return number
