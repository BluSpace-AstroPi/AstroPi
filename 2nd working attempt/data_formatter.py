input_file = 'data_tester.txt'
output_file = 'formatted_data_tester.txt'


with open(input_file, "r") as f_in, open(output_file, "w") as f_out:
    for line in f_in:
        split_line = line.strip().split(",")
        date_time = split_line[4].split(" ")
        formatted_date_time = date_time[0] + "T" + date_time[1].split(".")[0]
        split_line[4] = formatted_date_time
        formatted_line = ",".join(split_line)
        f_out.write(formatted_line + "\n")
