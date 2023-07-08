import csv
import random
import names

num_rows = 10

headers = ['name','batting', 'bowling', 'fielding', 'wicket_keeping', 'running', 'experience']

def get_random_number():
    return round(random.triangular(0.7, 1), 2)

with open('players_two.csv', mode="w", newline='') as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    for _ in range(num_rows):
        writer.writerow([names.get_full_name(gender="male"), 
                         get_random_number(), get_random_number(),
                         get_random_number(), get_random_number(), 
                         get_random_number(), get_random_number()])