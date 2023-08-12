import csv

def main(): 
    filename = ""
    choice = welcome()
    print(choice)
    if choice == 1:
        filename = "test.csv"
    elif choice == 2:
        filename = "618214.csv"
    elif choice == 3:
        filename = "618222.csv"
    elif choice == 4:
        filename = "618224.csv"
    elif choice == 5:
        filename = "618250.csv"
    elif choice == 6:
        filename = "GPA.csv"
    
    print("Do you want to pull/add : ")
    ask_pull_add = input(">").lower
    add_data(filename)
    if ask_pull_add == 'pull':
        pull_data(filename)
    elif ask_pull_add == 'add':
        add_data(filename)

def welcome():
    print('''-------------------- Calculate Grade Program --------------------
                Choose subject :
                1. 618240-165 DATA STRUCTURES AND ALGORITHMS
                2. 618214-165 ELECTRICAL ENGINEERING MATHEMATICS II
                3. 618222-165 ELECTRIC CIRCUIT ANALYSIS
                4. 618224-165 ELECTRONIC DEVICES AND CIRCUIT DESIGN
                5. 618250-165 DIGITAL CIRCUITS AND LOGIC DESIGN
                6. GPA
                7. Quit''')
    while True:
        print('Enter your subject (1-7):')
        choice = input('> ')
        if not choice.isdecimal():
            print('Please enter a number.')
        else:
            break  # Exit the loop once a valid number is entered.  
    return choice

def pull_data(filename):
    pass

def add_data(filename):
    print("Hello")

def sort_data():
    pass

def calculate_score():
    pass

def check_grade():
    pass

if __name__ == '__main__':
    main()
    
    