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
    else:
        return
    
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
        add_data(file_name)

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
                        
def add_data(file_name):
    data_list = []
    with open(file_name, 'r') as csvfile_r:
        csv_reader = csv.reader(csvfile_r)
        Columns = next(csv_reader)
        #print(Columns)
        for i in csv_reader:
            if i != []:
                data_list.append(i)
    
    while True:
        print()
        print('''Enter your data :
Student ID | Q1 | Mid | Q2 | Final | Attendance | Total = '-' | Grade = '-'
or enter 'Quit' for close''')
        enter_data = input('>').lower()
        if enter_data != 'quit':
            enter_data_list = enter_data.split(' ')
            for search in range(len(data_list)):
                if enter_data_list[0] == data_list[search][0]:
                    data_list[search] = enter_data_list
                    calculate_score(data_list[search])
                    print(data_list[search])
                    break
                else:
                    calculate_score(enter_data_list)
                    data_list.append(enter_data_list)
                    break
        else:
            break

        print(data_list)

    with open(file_name, 'w', newline='') as csvfile_w:
        csv_writer = csv.writer(csvfile_w)
        csv_writer.writerow(list(Columns))
        csv_writer.writerows(data_list)

def sort_data():
    # ฝากเอา merge sort มาใส่ที
    pass

def calculate_score(add_data_list):
    total = 0
    for score in range(5):
        total += int(add_data_list[score+1])
    add_data_list[6] = str(total)
    add_data_list[7] = check_grade(total)

def check_grade(grade_or_score):
    if str(grade_or_score).isalpha():
        if grade_or_score == 'A':
            return 4.00
        elif grade_or_score == 'B+':
            return 3.5
        elif grade_or_score == 'B':
            return 3.0
        elif grade_or_score == 'C+':
            return 2.5
        elif grade_or_score == 'C':
            return 2.0
        elif grade_or_score == 'D+':
            return 1.5
        elif grade_or_score == 'D':
            return 1.0
        elif grade_or_score == 'F':
            return 0.0
        
    elif str(grade_or_score).isnumeric:
        if grade_or_score >= 80:
            return 'A'
        elif 75 <= grade_or_score < 80:
            return 'B+'
        elif 70 <= grade_or_score < 75:
            return 'B'
        elif 65 <= grade_or_score < 70:
            return 'C+'
        elif 60 <= grade_or_score < 65:
            return 'C'
        elif 55 <= grade_or_score < 60:
            return 'D+'
        elif 50 <= grade_or_score < 55:
            return 'D'
        elif grade_or_score < 50:
            return 'F'
        

if __name__ == '__main__':
    main()
 #
    