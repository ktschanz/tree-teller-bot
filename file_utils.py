import json
import csv


def write_file(file, data):
    file = open(file, 'w')
    file.write(data)
    file.close()


def read_json_file(file):
    with open(file, encoding="utf8") as f:
        s = f.read()
        data = json.loads(s)
    return data


def read_csv(file_path):
    with open(file_path, encoding='utf8', newline='') as f:
        reader = csv.reader(f)
        data = [tuple(row) for row in reader]
        return data

