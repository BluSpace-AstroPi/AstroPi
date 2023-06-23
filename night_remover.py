def delete_lines_with_word(filename, word):
    # Step 1: Open the text file in read mode
    with open(filename, 'r') as file:
        # Step 2: Create an empty list to store the updated rows
        updated_rows = []
        
        # Step 3: Iterate over each line in the text file
        for line in file:
            # Step 4: Check if the specific word exists in the line
            if word in line:
                # Step 5: If the word is found, skip that line
                continue
            
            # Step 6: If the word is not found, add the line to the list of updated rows
            updated_rows.append(line)
    
    # Step 7: Close the file
        
    # Step 8: Open the same file in write mode
    with open(filename, 'w') as file:
        # Step 9: Write the updated rows to the file
        file.writelines(updated_rows)
    
    # Step 10: Close the file

# Example usage:
delete_lines_with_word('data_tester.txt', 'Night')
print("Complete!")