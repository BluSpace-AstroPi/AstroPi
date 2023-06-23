input_file = "nearest_cities.txt"  # Replace with the actual input file name
output_file = "output.txt"  # Replace with the desired output file name

with open(input_file, 'r') as file_in, open(output_file, 'w') as file_out:
    for line in file_in:
        # Extract latitude, longitude, city, and distance from the line
        parts = line.split('\t')
        coordinates = parts[0].split(': ')[1].split(', ')
        latitude = float(coordinates[0])
        longitude = float(coordinates[1])
        city = parts[1].split(': ')[1]
        distance = float(parts[2].split(': ')[1].split(' miles')[0])
        
        # Check if the distance is above 200 miles
        if distance > 300:
            continue  # Skip this line
            
        # Write the line to the output file
        file_out.write(line)

# Display a message once the operation is complete
print("File processing completed. Output saved in", output_file)

