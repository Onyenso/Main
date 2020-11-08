import csv
import cs50
from sys import argv, exit

# Check number of command-line arguements
if len(argv) != 2:

    print("Incorrect Number of command-line arguements")
    exit(1)

else:
    # Setup SQL database
    database = cs50.SQL("sqlite:///students.db")

    with open(argv[1], "r") as file:

        reader = csv.DictReader(file)

        for row in reader:
            # Split names for each row
            names = row["name"].split(" ")

            if len(names) == 2:
                database.execute("INSERT INTO students (first, last, house, birth) VALUES (?, ?, ?, ?)",
                                 names[0], names[1], row['house'], row['birth'])

            if len(names) == 3:
                database.execute("INSERT INTO students (first, middle, last, house, birth) VALUES (?, ?, ?, ?, ?)",
                                 names[0], names[1], names[2], row['house'], row['birth'])
    exit(0)
