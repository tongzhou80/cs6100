import csv
import random
import faker

# number of rows
N = 100_000

fake = faker.Faker()

def gen_well_formed(filename="people.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "age", "city"])  # header

        for i in range(N):
            # Randomly insert invalid ages
            if random.random() < 0.1:
                age = random.randint(0, 60)
            else:
                age = random.randint(0, 100)

            writer.writerow([
                i,
                fake.name(),
                age,
                fake.city()
            ])

'''
todo: to also generate rows with missing columns.
'''
def gen_malformed(filename="people_malformed.csv"):
    with open(filename, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["id", "name", "age", "city"])  # header

        for i in range(N):
            # Randomly insert invalid ages
            if random.random() < 0.01:  
                age = "" if random.random() < 0.5 else "NaN"
                #age = random.randint(0, 60)
            else:
                age = random.randint(0, 100)

            writer.writerow([
                i,
                fake.name(),
                age,
                fake.city()
            ])

if __name__ == "__main__":
    gen_well_formed()
    gen_malformed()