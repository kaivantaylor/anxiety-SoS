from infinite_update import infinite_update
import csv

infinite_update()

with open(r"C:\\Users\speedykai\Desktop\hophacks2019\Kaivan\CSV\heartrate.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader: # row is the addresses individually from the csv csv_file
        print(row[0])
