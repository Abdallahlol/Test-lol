import os

def write_entry(filename, entry):
  """
  Writes a new diary entry to a text file.

  Args:
    filename: Name of the file to write to.
    entry: The diary entry text.
  """
  try:
    with open(filename, 'a') as file:
      file.write(f"\n{entry}")
    print("Entry saved successfully!")
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")
  except PermissionError:
    print("Permission denied to write to the file.")
