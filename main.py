import csv

class Node():
    def __init__(self, datum):
        self.data = datum
        self.next = None
    def getData(self):
        return self.data
    def __str__(self):
        return str(self.data)
class LinkedList():
    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0
    def insertAtTail(self, datum):
        new_node = Node(datum)
        if self._tail == None:
            self._tail= new_node
            self._head = new_node
        else:
            print(self._head,'',self._head.next)
            print(self._tail,'',self._tail.next)
            self._tail.next = new_node
            print(self._head,'',self._head.next)
            print(self._tail,'',self._tail.next)
            self._tail = self._tail.next
            print(self._head,'',self._head.next)
            print(self._tail,'',self._tail.next)

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
    Grade = []
    degree = [3.0, 3.0, 3.0, 3.0, 3.0]
    sum_degree = 0
    subject = 0
    degree_product_grade = 0
    GPA = 0
    if file_name == "test.csv":
        subject = 1
    elif file_name == "618214.csv":
        subject = 2
    elif file_name == "618222.csv":
        subject = 3
    elif file_name == "618224.csv":
        subject = 4
    elif file_name == "618250.csv":
        subject = 5

    with open(file_name, 'r') as csvfile_r:
        csv_reader = csv.reader(csvfile_r)
        Columns = next(csv_reader)
        #print(Columns)
        for data in csv_reader:
            if data != []:
                data_list.append(data)

        print(data_list)
    
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
                    merge_sort(data_list)
                    break
        else:
            break

        print(data_list)

    with open(file_name, 'w', newline='') as csvfile_w:
        csv_writer = csv.writer(csvfile_w)
        csv_writer.writerow(list(Columns))
        csv_writer.writerows(data_list)

    with open('testt.csv', 'r') as csvfile_r_grade:
        csv_reader_grade = csv.reader(csvfile_r_grade)
        Columns_grade = next(csv_reader_grade)
        for grade in csv_reader_grade:
            if grade != []:
                Grade.append(grade)

    for grades in range(len(Grade)):
        Grade[grades][subject] = check_grade(data_list[grades][7])
        for calculate in range(1,6):
            set_degree_product_grade = degree_product_grade
            number_grade = check_grade(Grade[grades][calculate])
            degree_product_grade += number_grade*degree[calculate-1]
            if set_degree_product_grade != degree_product_grade:
                sum_degree += degree[calculate-1]
        GPA = degree_product_grade/sum_degree
        degree_product_grade = 0
        Grade[grades][6] = GPA

    print(Grade)

    with open('testt.csv', 'w', newline='') as csvfile_w_grade:
        csv_writer_grade = csv.writer(csvfile_w_grade)
        csv_writer_grade.writerow(list(Columns_grade))
        csv_writer_grade.writerows(Grade)

def merge(A, p, q, r):
    # If A is a list, slicing creates a copy.
    #print(A)
    if type(A) is list:
        left = A[p: q+1]
        #print("Left : ",left)
        right = A[q+1: r+1]
        #print("Right : ",right)
    # Otherwise a is a np.array, so create a copy with list().
    else:
        left = list(A[p: q+1])
        right = list(A[q+1: r+1])

    i = 0 # index into left sublist/subarray
    j = 0 # index into right sublist/subarray
    k = p # index into a[p: r+1]
    # Combine the two sorted sublists
    # by inserting into A
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            A[k] = left[i]
            i += 1
        else:
            A[k] = right[j]
            j += 1
        #print(f"k: {k} A: {A}")
        k += 1
    # After going through the left or right sublist, copy the 
    # remainder of the other to the end of the list/array.
    if i < len(left): # copy remainder of left
        A[k: r+1] = left[i:]
    if j < len(right): # copy remainder of right
        A[k: r+1] = right[j:]

def merge_sort(A, p=0, r=None):
    if r is None:
        r = len(A) - 1
    if p >= r:
        return
    q = (p+r)//2
    merge_sort(A, p, q)
    merge_sort(A, q+1, r)
    merge(A, p, q, r)

def calculate_score(add_data_list):
    total = 0
    for score in range(5):
        total += int(add_data_list[score+1])
    add_data_list[6] = total
    add_data_list[7] = check_grade(total)

def check_grade(grade_or_score):
    if str(grade_or_score).isalpha() or grade_or_score == '-':
        if grade_or_score == 'A':
            return 4.0
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
        elif grade_or_score == 'F' or grade_or_score == '-':
            return 0.0
        
    elif str(grade_or_score).isnumeric():
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
        
    else:
        return grade_or_score
        

if __name__ == '__main__':
    main()
    
    