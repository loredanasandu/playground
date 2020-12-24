""" 
Selects a column from input csv files named input1.csv, input2.csv... and stored in the csv_files directory.
Creates output csv files named output1.csv, output2.csv,... and stores them in the csv_files directory.
The output files contain a specified number of first lines unchanged from the input files and the selected column.
"""

column_to_select = 1    # Range starting by 0
number_of_unchanged_lines = 6   # A positive non-zero number


for i in range(1,4):
    with open("csv_files/input{}.csv".format(i), "r") as f_input:
        with open("csv_files/output{}.csv".format(i), "w") as f_output:
            lines = f_input.readlines()
            for line in lines[:number_of_unchanged_lines]:
                f_output.write(line)

            for line in lines[number_of_unchanged_lines:]:
                values = line.split(",")
                f_output.write(values[column_to_select])
                f_output.write("\n")
