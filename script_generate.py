import csv
from faker import Faker

fake = Faker()

def generate_csv(filename, num_records):
    with open(filename, 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['first_name', 'last_name', 'address', 'date_of_birth']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for _ in range(num_records):
            writer.writerow({
                'first_name': fake.first_name(),
                'last_name': fake.last_name(),
                'address': fake.address().replace('\n', ' '),
                'date_of_birth': fake.date_of_birth().strftime('%Y-%m-%d')
            })

if __name__ == "__main__":
    generate_csv('data.csv', 1000000)