import csv

def read_csv_column(file_path, column_index):
    """
    Reads a column from a CSV file and returns its contents as a list.

    Args:
        file_path (str): The path to the CSV file.
        column_index (int): The index of the column to read (0-indexed).

    Returns:
        list: The contents of the specified column as a list.
    """
    with open(file_path, 'r') as csv_file:
        reader = csv.reader(csv_file)
        column = []
        for row in reader:
            column.append(row[column_index])
        return column