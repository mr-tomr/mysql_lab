# Create a CSV file which includes a randomly created people and their attributes.

import csv
import random
from faker import Faker

# Initialize Faker library
fake = Faker()

# Define the CSV file path and column names
csv_file = 'users.csv'
column_names = ['id', 'firstname', 'lastname', 'phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'notes']

# Generate 50 random user records
test_users = []
for i in range(1, 51):
    firstname = fake.first_name()
    lastname = fake.last_name()
    phone = fake.phone_number()
    address1 = fake.street_address()
    address2 = fake.secondary_address()
    city = fake.city()
    state = fake.state()
    zipcode = fake.zipcode()
    notes = fake.text(max_nb_chars=100)
    
    user = [i, firstname, lastname, phone, address1, address2, city, state, zipcode, notes]
    test_users.append(user)

# Write the data to the CSV file
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Write the column names
    writer.writerow(column_names)
    
    # Write the test user records
    writer.writerows(test_users)

print(f"CSV file '{csv_file}' created successfully with 25 randomly generated user records.")
