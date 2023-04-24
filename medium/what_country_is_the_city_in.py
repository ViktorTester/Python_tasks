countries = {
    "Sweden": ["Stockholm", "Göteborg", "Malmö"],
    "Norway": ["Oslo", "Bergen", "Trondheim"],
    "England": ["London", "Birmingham", "Manchester"],
    "Germany": ["Berlin", "Hamburg", "Munich"],
    "France": ["Paris", "Marseille", "Toulouse"]
}

city = input()
counter = 0

for key, value in countries.items():
    if city in value:
        print(f'INFO: {city} is a city in {key}')
        break
    else:
        counter += 1

if counter == len(countries):
    print(f'ERROR: Country for {city} not found')

# The input is the name of the city in the city variable.
# The program finds which country the entered city belongs to.