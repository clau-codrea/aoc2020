import sys


def read_schedule(bus_schedule_file):
    bus_schedule_file.readline()
    elements = bus_schedule_file.readline().split(',')
    
    buses = []
    for offset, element in enumerate(elements):
        if element != 'x':
            buses.append((int(element), offset))

    sorted_buses = list(reversed(sorted(buses, key=lambda x: x[0])))

    return [(bus[0], bus[1] - sorted_buses[0][1]) for bus in sorted_buses]


def compute_closest_offsets(bus, multiple):
    term = multiple // bus
    return (term * bus - multiple, (term + 1) * bus - multiple)


def actual(timestamp, buses):
    first_bus = min(buses, key=lambda x: x[1])
    return timestamp + first_bus[1]


def common_timestamp(buses):
    max_bus = buses[0][0]
    buses = buses[1:]
    
    done, invalid = False, False
    multiple = 0
    while not done:
        multiple += max_bus
        for bus in buses:
            offsets = compute_closest_offsets(bus[0], multiple)
            if not any(offset == bus[1] for offset in offsets):
                invalid = True
                break
        if invalid:
            invalid = False
            continue
        else:
            done = True
            
    return actual(multiple, buses)


def main(bus_schedule_file_path):
    with open(bus_schedule_file_path) as bus_schedule_file:
        buses = read_schedule(bus_schedule_file)

    timestamp = common_timestamp(buses)
    print(f"timestamp: {timestamp}")


if __name__ == "__main__":
    main(sys.argv[1])
