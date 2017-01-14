import csv

with open('signnames.csv', newline='') as f:
    reader = csv.DictReader(f)
    sign_id_to_name = {int(row['ClassId']): row['SignName'] for row in reader}
