import sys


def offset(timestamp, bus):
    term = timestamp // bus

    return abs(timestamp - bus * (term + 1))


def next_bus(timestamp, buses):
    offsets = [offset(timestamp, bus) for bus in buses]
    min_offset = min(offsets)
    bus = buses[offsets.index(min_offset)]

    return bus, min_offset


def main(bus_schedule_file_path):
    with open(bus_schedule_file_path) as bus_schedule_file:
        timestamp = int(bus_schedule_file.readline())
        buses = [
            int(bus) for bus in bus_schedule_file.readline().split(",") if bus != "x"
        ]

    bus_id, wait_time = next_bus(timestamp, buses)
    response = bus_id * wait_time
    print(f"id * time: {response}")


if __name__ == "__main__":
    main(sys.argv[1])
