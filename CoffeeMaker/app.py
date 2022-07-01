import matplotlib.pyplot as plt
import database
import charts

MENU_PROMPT = """--- Coffee Bean App ---

Please choose one of these options:

1) Add a new bean
2) See all bean
3) Find bean by name
4) See which preparation method is best for bean
5) Best ratings
6) Delete an entry
7) Exit

Your selection:
"""

def menu():
    connection = database.connect()
    database.create_tables(connection)

    while (user_input := input(MENU_PROMPT)) != "7":
        if user_input == "1":
            add_bean(connection)

        elif user_input == "2":
            print_all(connection)

        elif user_input == "3":
            print_bean_by_name(connection)

        elif user_input == "4":
            print_best_method(connection)
        
        elif user_input == "5":
            methods_to_ratings = database.get_methods_to_ratings(connection)
            charts.methods_to_ratings_bar(methods_to_ratings)
            plt.show()
        
        elif user_input == "6":
            """delete coffee entry"""
            delete_bean(connection)

        else:
            print("Invalid input, please try again")
        print()

def add_bean(connection):
    name = input("Enter bean name: ")
    method = input("Enter how you've prepared it: ")
    rating = int(input("Enter your rating score (0-100): "))
    database.add_bean(connection, name.lower(), method.lower(), rating)

def print_all(connection):
    beans = database.get_all_beans(connection)
    for bean in beans:
        print(f"{bean[1]} ({bean[2]} - {bean[3]}/100)")

def print_bean_by_name(connection):
    name = input("Enter bean name: ").lower()
    beans = database.get_beans_by_name(connection, name)
    for bean in beans:
        print(f"{bean[1].capitalize()} ({bean[2]} - {bean[3]}/100)")

def print_best_method(connection):
# try:
    name = input("Enter bean name to find: ")
    best_method = database.get_best_prepartion_for_bean(connection, name.lower())
    print(f"The best prepartion method for {name.capitalize()} is {best_method[2]}")
# except:
    # print(f"There is no {name} entry")

def delete_bean(connection):
    name = input("Enter bean name to delete: ").lower()
    database.delete_bean(connection, name)

menu()