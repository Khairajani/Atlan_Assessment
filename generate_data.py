import csv
from time import time
from faker import Faker

fake = Faker('en_GB')
RECORD_COUNT = 150000
#RECORD_COUNT = 100

# Function for generating csv file data 
def create_csv_file():
    with open('./data.csv', 'w', newline='') as csvfile:
        fieldnames = ['username', 'name', 'sex', 'address', 'mail', 'birthdate']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for i in range(RECORD_COUNT):
            profile = fake.simple_profile()
            #print(profile,type(profile))
            writer.writerow(profile)

if __name__ == '__main__':
    start = time()
    create_csv_file()
    elapsed = time() - start
    print('created csv file time: {}'.format(elapsed))
