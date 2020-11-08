from sys import argv, exit
import csv


def main():
    if len(argv) != 3:
        print("Incorrect number of command line arguements")
        exit(1)

    if len(argv) == 3:
        # cvx
        # vgd
        # cbd
        # dzc
        # database
        file = open(argv[2], "r")
    
        DNA = file.read()
        agatc = check('AGATC', DNA)
        ttttttct = check('TTTTTTCT', DNA)
        aatg = check('AATG', DNA)
        tctag = check('TCTAG', DNA)
        gata = check('GATA', DNA)
        tatc = check('TATC', DNA)
        gaaa = check('GAAA', DNA)
        tctg = check('TCTG', DNA)

        if argv[1] == "databases/large.csv":
    
            with open(argv[1], newline='') as csvfile:
                #csv.DictReader opens a csv file and transforms it to a dictionary. By defult, the first line of the csv file is used as the keys in the dictionary.
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for i in row:
                        if (int(row['AGATC']) == agatc and int(row['TTTTTTCT']) == ttttttct and int(row['AATG']) == aatg and int(row['TCTAG']) == tctag and
                                int(row['GATA']) == gata and int(row['TATC']) == tatc and int(row['GAAA']) == gaaa and int(row['TCTG']) == tctg):
                            print(row['name'])
                            exit(0)
                print('No match')
                exit(0)
    
        else:
    
            with open(argv[1], newline='') as csvfile:
                reader = csv.DictReader(csvfile)
                for row in reader:
                    for i in row:
                        if int(row['AGATC']) == agatc and int(row['AATG']) == aatg and int(row['TATC']) == tatc:
                            print(row['name'])
                            exit(0)
                        #print(f"{row[i]} ", end="")
                print('No match')
                exit(0)
    

def check(STR, things):
    streak = 0
    old_streak = 0
    new_streak = 0
        
    for c in things:
        part = things[old_streak:(old_streak + len(STR))]
        
        if part == STR:
            streak += 1
            old_streak += len(STR)
            part = things[old_streak:(old_streak + len(STR))]
            
            if part != STR:
            
                if streak > new_streak:
                    new_streak = streak
                
        else:
            part = things[old_streak:(old_streak + len(STR))]
            old_streak += 1
            
            if part != STR:
                streak = 0
                
    return new_streak


main()
