
def rocket_parts():
    return "payload, propellant, structure"

output = rocket_parts()
print(output)


def distance_from_earth(destination):
    if destination.lower() == 'moon':
        return "238,855"
    else:
        return "Unable to compute to that destination"

print(distance_from_earth('moon'))


def days_to_complete(distance, speed):
    hours = distance/speed
    return hours/24

total_days = days_to_complete(238855,75)
print(round(total_days))


def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank}
    """
    print(output)

generate_report(80, 70, 75)


from datetime import timedelta, datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")

print(arrival_time("Moon"))
print(arrival_time("Orbit", hours=0.13))


def variable_length(*args):
    print(args)

variable_length()
variable_length("one", "two")
variable_length(None)


def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"

print(sequence_time(4, 14, 18))
print(sequence_time(4, 14, 48))


def variable_key_length(**kwargs):
    print(kwargs)

variable_key_length(tanks=1, day="Wednesday", pilots=3)


def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission: ")
    for title, name in kwargs.items():
        print(f"{title}: {name}")

crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")


def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f"{name}: {value}")

fuel_report(main=50, external=100, emergency=60)
