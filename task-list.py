import os

# Function to display the task menu
def display_menu():
    print("\n=== Task List Manager ===")
    print("1. Add a new task")
    print("2. Remove a task")
    print("3. View tasks")
    print("4. Exit")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice
