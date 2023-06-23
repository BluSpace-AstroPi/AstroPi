from haversine import haversine, Unit

def find_nearest_city(latitude, longitude, city_data):
    distances = []
    for city in city_data:
        city_name, city_latitude, city_longitude = city
        # Convert latitude and longitude to float values
        city_latitude = float(city_latitude)
        city_longitude = float(city_longitude)

        # Calculate the distance using haversine formula
        distances.append(haversine((latitude, longitude), (city_latitude, city_longitude), unit=Unit.MILES))
    smallest_distance = min(distances)
    nearest_city = city_name

    return nearest_city, round(smallest_distance)  # Round the distance to the nearest mile

# Example usage:
coordinates_filename = 'astropi_coordinates.txt'  # Name of the text file containing the coordinates
cities_filename = 'formatted_city_coordinates.txt'  # Name of the text file containing city name, latitude, and longitude data
output_filename = 'nearest_cities.txt'  # Name of the output file to save the results

# Read the coordinates from the text file
with open(coordinates_filename, 'r') as coordinates_file:
    astro_data = []

    for line in coordinates_file:

        latitude, longitude = line.split(' ')
        
        astro_info = [latitude, longitude]

        astro_data.append(astro_info)
    


# Open the text file
with open(cities_filename, 'r') as file:
    city_data = []

    # Iterate over each line in the file
    for line in file:
    
        city_name, city_latitude, city_longitude = line.split(',')

        # Create an array with the city name, latitude, and longitude
        city_info = [city_name, city_latitude, city_longitude]

        # Append the city data to the main array
        city_data.append(city_info)


# Prepare the output file
output_lines = []

# Iterate over each set of coordinates
coordinate_count = 0
for line in astro_data:

    latitude, longitude = line
    # Convert latitude and longitude to float values
    latitude = float(latitude)
    longitude = float(longitude)
    
    nearest_city, distance = find_nearest_city(latitude, longitude, city_data)
    output_line = f"Coordinates: {latitude}, {longitude}\tNearest City: {nearest_city}\tDistance: {distance} miles\n"
    output_lines.append(output_line)
    coordinate_count += 1
    coordinate_percentage = ((coordinate_count) / (len(astro_data))) * 100
    print(f"{round(coordinate_percentage)}%")

# Write the results to the output file
with open(output_filename, 'w') as output_file:
    output_file.writelines(output_lines)
