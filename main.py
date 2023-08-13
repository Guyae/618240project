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
    
    # Ask user that what user want to pull or add data 
    while True:
        print()
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
        while True:
            print('''Do you want to add new data or edit data?  
                  1. Add new data
                  2. Edit data''')
            add_edit = input('>')
            if add_edit == '1' or add_edit == '2':
                break
            else:
                print()
                print('--- Please enter add or edit ---')
        add_data(file_name, add_edit)

def welcome():
    print('''-------------------- Calculate Grade Program --------------------
                Choose subject :
                1. 618214-165 ELECTRICAL ENGINEERING MATHEMATICS II
                2. 618222-165 ELECTRIC CIRCUIT ANALYSIS
                3. 618224-165 ELECTRONIC DEVICES AND CIRCUIT DESIGN
                4. 618240-165 DATA STRUCTURES AND ALGORITHMS
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
    with open(file_name, 'r') as csv_file:
        data_list=[]
        csv_reader = csv.reader(csv_file)
        for i in csv_reader:
              if i != []:
                data_list.append(i)
                pass
    if data_list == []:
        gotoadd_data_or_not(file_name)
    else:
        print('''Do you want to pull everyone's data or only some student?
        1.Everyone 
        2.Enter student ID ''')  
        choice = input(">")
        if choice == "1":
                for row in data_list:
                    print(row)
        elif choice == "2":
            student_id = input("Enter student ID: ")
            found = 0
            for row in data_list:
                if row[0] == student_id:
                    print(row)
                    found = 1
            if found ==0:
                gotoadd_data_or_not(file_name)
                
            
def gotoadd_data_or_not(file_name):
    x=input("Do you want to add/edit data?:").lower()
    if x=="yes":
        add_data(file_name)
    elif x== "no":
        welcome()
        
            
                        
def add_data(file_name, add_or_edit):
    data_list = []
    with open(file_name, 'r+') as csvfile:
        csv_reader = csv.reader(csvfile)
        csv_writer = csv.writer(csvfile)
        Columns = next(csv_reader)
        print(Columns)
        for i in csv_reader:
            if i != []:
                data_list.append(i)
        print(data_list)
    
    if add_or_edit == '1':
        while True:
            print()
            print('''Enter your data :
    Student ID | Q1 | Mid | Q2 | Final | Attendance | Total | Grade
    or enter 'Quit' for close''')
            enter_data = input('>').lower()

            if enter_data == 'quit':
                break
        
    elif add_or_edit == '2':
        pass

def sort_data():
    pass

def calculate_score():
    pass

def check_grade():
    pass

if __name__ == '__main__':
    main()
    
    