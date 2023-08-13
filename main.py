import csv

def main(): 
    file_name = ""
    choice = welcome()
    if choice == '1':
        file_name = "test.csv"
    elif choice == '2':
        file_name = "618214.csv"
    elif choice == '3':
        file_name = "618222.csv"
    elif choice == '4':
        file_name = "618224.csv"
    elif choice == '5':
        file_name = "618250.csv"
    elif choice == '6':
        file_name = "GPA.csv"
    
    while True:
        print("Do you want to pull/add")
        ask_pull_add = input(">").lower()
        if ask_pull_add == 'add' or ask_pull_add == 'pull':
            break
        else:
            print()
            print("--- Please enter add or edit ---")
            
    if ask_pull_add == 'pull':
        pull_data(file_name)
    elif ask_pull_add == 'add':
        add_data(file_name)

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
        number_list = [str(number+1) for number in range(7)]
        print('Enter your subject (1-7):')
        choice = input('> ')
        if choice.isdecimal():
            if choice in number_list:
                break
            else:
                print('--- Please enter number 1-7  ---')
                print()
        else:
            print('--- Please enter a number ---')
            print()
    return choice

def pull_data(file_name):
    pass

def add_data(file_name):
    data_list = []
    with open(file_name, 'r+') as csvfile:
        csv_reader = csv.reader(csvfile)
        for i in csv_reader:
            if i != []:
                data_list.append(i)
        print(data_list)

    while True:
        print('Do you want to add/edit data?')
        add_edit = input('>')
        if add_edit == 'add' or add_edit == 'edit':
            break
        else:
            print()
            print('--- Please enter add or edit ---')

def sort_data():
    pass

def calculate_score():
    pass

def check_grade():
    pass

if __name__ == '__main__':
    main()
    
    