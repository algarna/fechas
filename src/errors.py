
# open("/path/to/mars.jpg")

try:
    open("config.txt")
except FileNotFoundError:
    print("Couldn't find the config.txt file!")


def load_config(path):
    try:
        # loaded_config = open(path)
        loaded_config = """# Rocket Ship Configuration File!
        fuel_tanks=4
        oxygen_tanks=3
        initial_propulsion_level=84
        $ End of file"""
    except FileNotFoundError as err:
        print("Couldn't find the config.txt file!", err)

    parsed_config = {}
    for line in loaded_config.split("\n"):
        try:
            key, value = line.split("=")
            parsed_config[key] = value
        except ValueError:
            print(f"Unable to parse {line}")
    print(parsed_config)

load_config("aaa")


def water_left(astronauts, water_left, days_left):
    for argument in [astronauts, water_left, days_left]:
        try:
            argument / 10
        except TypeError:
            raise TypeError(f"All arguments must be of type int, but received: {argument} as {type(argument)}")
    daily_usage = astronauts * 11
    total_usage = daily_usage * days_left
    total_water_left = water_left - total_usage
    if total_water_left < 0:
        raise RuntimeError(f"There is not enough water for {astronauts} after {days_left} days!")
    return f"Total water left after {days_left} days is: {total_water_left} liters"

print(water_left(5, 1000, 2))


true_values = ["yes", "y"]
false_values = ["no", "n"]

def str_to_bool(value):
    if isinstance(value, str):
        value = value.lower()
        if value in true_values:
            return True
        elif value in false_values:
            return False
        else:
            raise ValueError("Invalid value")
    else:
        raise TypeError("Invalid argument type")

print(str_to_bool(100))
print(str_to_bool("nnnn"))
print(str_to_bool("N"))
print(str_to_bool("yes"))