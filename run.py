import argparse
import csv
import random 
from pathlib import Path, PurePath

def generate_csv(path):
    with open(path, 'w') as csvfile:
        writer = csv.writer(csvfile)
        for i in range(100):
            writer.writerow([random.randint(1,100), random.randint(1,100)])

def run_multi_sum(path, generate_file=False):
    if generate_file:
        generate_csv(path)

    new_values = []

    with open(path, 'r') as csvfile:
        reader = csv.reader(csvfile)
        
        for row in reader:
            if len(row) >= 2:
                new_dict = {
                "value1": row[0],
                "value2": row[1],
                "product": (int(row[0]) * int(row[1])),
                "sum": (int(row[0]) + int(row[1]))
                } 
                new_values.append(new_dict)

    Path("computed").mkdir(parents=True, exist_ok=True)
    pp = PurePath(path)
    with open(f'computed/{pp.name}', 'w') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=["value1", "value2", "product", "sum"])
        writer.writeheader()
        writer.writerows(new_values)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="path to a csv file")
    parser.add_argument("-g", "--generate", help="generate a file for testing", action="store_true")
    the_args = parser.parse_args()
    if the_args.path.lower().endswith(".csv"):
        run_multi_sum(the_args.path, generate_file=the_args.generate)
    else:
        print('The specified path does not end in .csv')


if __name__ == "__main__":
    main()