import csv #module

data = [
    ['Name', 'Age', 'Occupation'],
    ['John Doe', 30, 'Engineer'],
    ['Jane Smith', 25, 'Data Analyst'],
    ['Bob Johnson', 35, 'Teacher'],

]

csv_file_path = 'example.csv'

with open(csv_file_path, 'w', newline ='') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerows(data)

print(f'CSV file "{csv_file_path}" created successfully')
