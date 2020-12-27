import sys

SIZE = 8
CYCLES = 6
ACTIVE, INACTIVE = True, False

ROW_COUNT = COLUMN_COUNT = CYCLES * 2 + SIZE
AISLE_COUNT = FTH_COUNT = CYCLES * 2 + 1


def read(cubes_file):
    pocket_dimension = [
        [
            [[INACTIVE for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
            for _ in range(AISLE_COUNT)
        ]
        for _ in range(FTH_COUNT)
    ]

    for row_index, line in enumerate(cubes_file):
        line = line.rstrip()
        for column_index, cube in enumerate(line):
            pocket_dimension[CYCLES][CYCLES][row_index + CYCLES][
                column_index + CYCLES
            ] = (ACTIVE if cube == "#" else INACTIVE)

    return pocket_dimension


def count_active_neighbors(
    pocket_dimension, fth_index, aisle_index, row_index, column_index
):
    active_cubes = 0

    for fth_offset in (-1, 0, 1):
        for aisle_offset in (-1, 0, 1):
            for row_offset in (-1, 0, 1):
                for column_offset in (-1, 0, 1):
                    if fth_offset == aisle_offset == row_offset == column_offset == 0:
                        continue

                    neighbor_fth_index = fth_index + fth_offset
                    neighbor_aisle_index = aisle_index + aisle_offset
                    neighbor_row_index = row_index + row_offset
                    neighbor_column_index = column_index + column_offset

                    if (
                        neighbor_fth_index < 0
                        or neighbor_fth_index >= FTH_COUNT
                        or neighbor_aisle_index < 0
                        or neighbor_aisle_index >= AISLE_COUNT
                        or neighbor_row_index < 0
                        or neighbor_row_index >= ROW_COUNT
                        or neighbor_column_index < 0
                        or neighbor_column_index >= COLUMN_COUNT
                    ):
                        continue

                    if (
                        pocket_dimension[neighbor_fth_index][neighbor_aisle_index][
                            neighbor_row_index
                        ][neighbor_column_index]
                        is ACTIVE
                    ):
                        active_cubes += 1

    return active_cubes


def next_state(pocket_dimension, fth_index, aisle_index, row_index, column_index):
    cube = pocket_dimension[fth_index][aisle_index][row_index][column_index]
    active_neighbors = count_active_neighbors(
        pocket_dimension, fth_index, aisle_index, row_index, column_index
    )
    if cube is ACTIVE:
        if active_neighbors in (2, 3):
            return ACTIVE
        else:
            return INACTIVE
    else:
        if active_neighbors == 3:
            return ACTIVE
        else:
            return INACTIVE


def cycle(pocket_dimension, cycles):
    cycled_pocket_dimension = [
        [
            [[INACTIVE for _ in range(COLUMN_COUNT)] for _ in range(ROW_COUNT)]
            for _ in range(AISLE_COUNT)
        ]
        for _ in range(FTH_COUNT)
    ]

    for _ in range(cycles):
        for fth_index in range(len(cycled_pocket_dimension)):
            for aisle_index in range(len(cycled_pocket_dimension[fth_index])):
                for row_index in range(
                    len(cycled_pocket_dimension[fth_index][aisle_index])
                ):
                    for column_index in range(
                        len(cycled_pocket_dimension[fth_index][aisle_index][row_index])
                    ):
                        cycled_pocket_dimension[fth_index][aisle_index][row_index][
                            column_index
                        ] = next_state(
                            pocket_dimension,
                            fth_index,
                            aisle_index,
                            row_index,
                            column_index,
                        )

        aux = cycled_pocket_dimension
        cycled_pocket_dimension = pocket_dimension
        pocket_dimension = aux

    return pocket_dimension


def count_active(pocket_dimension):
    count = 0
    for fth in pocket_dimension:
        for aisle in fth:
            for row in aisle:
                for cube in row:
                    if cube is ACTIVE:
                        count += 1

    return count


def main(cubes_file_path):
    with open(cubes_file_path) as cubes_file:
        pocket_dimension = read(cubes_file)

    pocket_dimension = cycle(pocket_dimension, CYCLES)
    active_cubes = count_active(pocket_dimension)
    print(f"active cubes: {active_cubes}")


if __name__ == "__main__":
    main(sys.argv[1])
