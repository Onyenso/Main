import cs50
from sys import argv, exit

# Check number of command line arguements
if len(argv) != 2:
    print("Incorrect number of command-line arguements")

else:
    # Connect to SQL database
    database = cs50.SQL("sqlite:///students.db")

    rows = database.execute("SELECT first, middle, last, birth FROM students WHERE house = ? ORDER BY last, first", argv[1])

    for x in rows:
        if x['middle'] != None:
            
            print(f"{x['first']} {x['middle']} {x['last']}, born {x['birth']}")
        
        else:
            print(f"{x['first']} {x['last']}, born {x['birth']}")
