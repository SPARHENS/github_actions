import csv
import json
import pathlib

def csv_to_json(csv_path, json_path):
    with open(csv_path, "r", encoding="utf-8") as csv_file:
        data = list(csv.DictReader(csv_file))
    with open(json_path, "w", encoding="utf-8") as json_file:
        json.dump(data, json_file, indent=4)
    print(f"json file : {str(json_path).split("/")[-1]} \u2705")

if __name__ == "__main__":
       root_dir = pathlib.Path(__file__).resolve().parents[0]
       for file in ["test_add", "test_sub"]:
            csv_path = str(root_dir) + f"/test/data/{file}.csv"
            json_path = str(root_dir) + f"/test/data/{file}.json"
            csv_to_json(csv_path, json_path)
