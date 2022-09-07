planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

print("The first planet is", planets[0])
print("The second planet is", planets[1])
print("The third planet is", planets[2])

planets[3] = "Red Planet"
print("Mars is also known as", planets[3])

number_of_planets = len(planets)
print("There are", number_of_planets, "planets in the solar system.")

planets.append("Pluto")
number_of_planets = len(planets)
print("There are actually", number_of_planets, "planets in the solar system.")

planets.pop()  # Goodbye, Pluto
number_of_planets = len(planets)
print("No, there are definitely", number_of_planets, "planets in the solar system.")

print("The last planet is", planets[-1])
print("The penultimate planet is", planets[-2])

jupiter_index = planets.index("Jupiter")
print("Jupiter is the", jupiter_index + 1, "planet from the sun")

planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
planets_before_earth = planets[0:2]
print(planets_before_earth)

planets_after_earth = planets[3:8]
print(planets_after_earth)

planets_after_earth = planets[3:]
print(planets_after_earth)

amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)

regular_satellite_moons.sort(reverse=True)
print("The regular satellite moons of Jupiter are", regular_satellite_moons)


# from time import sleep

# countdown = [4, 3, 2, 1, 0]

# for number in countdown:
#     print(number)
#     sleep(1)  # Wait 1 second
# print("Blast off!! 🚀")

new_planet = ''
planets = []
# planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]

# while new_planet.lower() != 'done':
#     if new_planet:
#         planets.append(new_planet)
#     new_planet = input('Enter a new planet, or done if done: ')

# for planet in planets:
#     print(planet)


planet = {
    'name': 'Earth',
    'moons': 1
}

print(planet.get("name"))
print(planet["name"])

planet.update({
    'name': 'Jupiter',
    'moons': 79
})

print(planet["name"])
print(planet["moons"])

planet["diameter (km)"] = {
    'polar': 133709,
    'equatorial': 142984
}

print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
print(f'{planet["name"]} has {planet["moons"]} moon(s)')

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}

for key in rainfall.keys():
    print(f'{key}: {rainfall[key]} cm')

if 'december' in rainfall:
    rainfall["december"] = rainfall["december"] + 1
else:
    rainfall["december"] = 1

total_rainfall = 0
for value in rainfall.values():
    if value:
        total_rainfall += value

print(f'There was {total_rainfall} cm in the last quarter')

planet_moons = {
    "mercury": 0,
    "venus": 0,
    "earth": 1,
    "mars": 2,
    "jupiter": 79,
    "saturn": 82,
    "uranus": 27,
    "neptune": 14,
    "pluto": 5,
    "haumea": 2,
    "makemake": 1,
    "eris": 1
}

moons = planet_moons.values()
total_planets = len(planet_moons.keys())

print(moons)
print(total_planets)

average_moons = sum(moons) / total_planets
print(f'Each planet has an average of {average_moons} moons')
