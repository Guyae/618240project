import csv

def main(): 
    while True:
        file_name = ""
        choice = welcome()
        if choice == '1':
            file_name = "618214.csv"
        elif choice == '2':
            file_name = "618222.csv"
        elif choice == '3':
            file_name = "618224.csv"
        elif choice == '4':
            file_name = "618240.csv"
        elif choice == '5':
            file_name = "618250.csv"
        elif choice == '6':
            file_name = "GPA.csv"
        else:
            return
        
        # Ask user that what user want to pull or add data 
        if file_name != "GPA.csv":
            while True:
                print()
                print("Do you want to pull/add")
                ask_pull_add = input(">").lower()
                if ask_pull_add == 'add' or ask_pull_add == 'pull':
                    break
                else:
                    print()
                    print("--- Please enter 'ADD' or 'EDIT' ---")
                    
            if ask_pull_add == 'pull':
                pull_data(file_name)
            elif ask_pull_add == 'add':
                add_data(file_name)
        else:
            pull_data(file_name)

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
        number_list = [str(number+1) for number in range(7)]        # สร้าง number_list มาเก็บตัวเลข 1-7 คือจำนวนตัวเลือกข้อโปรแกรม
        print('Enter your subject (1-7):')
        choice = input('> ')
        if choice.isdecimal():
            if choice in number_list:
                break
            else:
                print('--- Please enter number 1-7 ---')
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
        print("""What do you want to know
              1.Q1
              2.Mid
              3.Q2
              4.Final
              5.Attendance
              6.Total
              7.Grade
              8.All""")
        p=int(input(">"))
        if p==8:
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
        else:
            if choice == "1":
                    for row in data_list:
                        print(row[0],row[p])
            elif choice == "2":
                student_id = input("Enter student ID: ")
                found = 0
                for row in data_list:
                    if row[0] == student_id:
                        print(row[0],row[p])
                        found = 1
                if found ==0:
                    gotoadd_data_or_not(file_name)
                     
def gotoadd_data_or_not(file_name):
    x=input("Do you want to add/edit data?:").lower()
    if x=="yes":
        add_data(file_name)
    elif x== "no":
        welcome()            

def check_isnumberic(string):
    return str(string).isnumeric    # เช็คว่าค่าที่รับมาเป็นตัวเลขหรือป่าว

def add_data(file_name):
    Columns = ['Student ID', 'Q1', 'Mid', 'Q2', 'Final', 'Attendance', 'Total', 'Grade']
    # กำหนด  Columns = ['Student ID', 'Q1', 'Mid', 'Q2', 'Final', 'Attendance', 'Total', 'Grade'] เพื่อเป็น Columns
    data_list = []                                              # กำหนด data_list เพื่อรับค่าข้อมูลในไฟล์ชื่อ file_name ( ชื่อวิชานั้นๆ )
    Grade = []                                                  # กำหนด Grade เพื่อรับค่าข้อมูลในไฟล์ GPA.csv 
    degree = [3.0, 3.0, 3.0, 3.0, 3.0]                          # กำหนด degree เพื่อกำหนดหน่วยกิตของวิชานั้นๆ โดยต้องกรอกเรียงวิชาตามหน้าที่เราเลทอกวิชา
    sum_degree = 0                                              # กำหนด sum_degree เพื่อนรับผลรวมหน่วยกิตวิชาที่นำมาคำนวณหาหน่วยกิต
    subject = 0                                                 # กำหนด subject เพื่อรับค่าว่าวิชาไหนเลขอะไร
    degree_product_grade = 0                                    # กำหนด degree_product_grade เพื่อหาผลคูณระหว่างเกรดที่ได้กับหน่วยกิตวิชานั้นๆ
    GPA = 0                                                     # กำหนด GPA เพื่อรับค่า GPA ที่คำนวณได้ แล้วนำไปใส่ใน Grade ต่อไป
    if file_name == "618214.csv":
        subject = 1
    elif file_name == "618222.csv":
        subject = 2
    elif file_name == "618224.csv":
        subject = 3
    elif file_name == "618240.csv":
        subject = 4
    elif file_name == "618250.csv":
        subject = 5

    with open(file_name, 'r') as csvfile_r:                     # กำหนด csvfile_r เป็น open(file_name, 'r')
        csv_reader = csv.reader(csvfile_r)                      # กำหนด csv_reader ว่าจะทำการอ่านข้อมูลในไฟล์
        try:
            Columns = next(csv_reader)                          
            # กำหนด Columns เก็บค่าของหัวตารางไว้ แล้วเช็คว่า error หรือป่าว           
            # => จะเกิดในกรณีไม่มีข้อมูลในไฟล์ที่สร้างขึ้นมาจาก
        except StopIteration:   
            pass                                                # ถ้าเกิด StopIteration จะผ่านไปเลย
        if Columns == ['๏ปฟ']:                                 # ถ้า Columns == ['๏ปฟ'] => จะเกิดในกรณีไม่มีข้อมูลในไฟล์ที่สร้างขึ้นมาจาก excel
            Columns = ['Student ID', 'Q1', 'Mid', 'Q2', 'Final', 'Attendance', 'Total', 'Grade']
            # กำหนด  Columns = ['Student ID', 'Q1', 'Mid', 'Q2', 'Final', 'Attendance', 'Total', 'Grade'] ใหม่อีกครั้ง
        
        for data in csv_reader:                                 # วนข้อมูลใน csv_reader ที่อ่านค่ามา
            if data != []:                                      # เช็คว่า data != [] ใช่มั้ย
                calculate_score(data)                           # คำนวณเกรดที่มีคะแนนอยู่แล้ว
                data_list.append(data)                          # ถ้าใช่ เอา data ใส่เข้าใน data_list   
            else:
                pass

        print(data_list)
    
    while True:
        print()
        print('''Enter your data :
Student ID | Q1 | Mid | Q2 | Final | Attendance | Total = '-' | Grade = '-'
or enter 'Quit' for close''')
        enter_data = input('>').lower()
        if enter_data != 'quit':                                # เช็คว่า enter_data ไม่เท่ากับ 'quit' ใช่มั้ย
            enter_data_list = enter_data.split(' ')
            print(enter_data_list)
            print(len(data))
            for search in range(len(data_list)):                # วนรหัส นศ 
                if enter_data_list[0] == data_list[search][0]:  # วนรหัส นศ ว่ามีรหัสนั้นอยู่แล้วมั้ย
                    data_list[search] = enter_data_list         # ถ้ามีอยู่แล้ว ให้ข้อมูลที่เป็นรหัส นศ นั้นๆ = ข้อมูลใหม่
                    calculate_score(data_list[search])          # เสร็จแล้วคำนวณเกรด
                    print()
                    print("--- Editing is complete ---")
                    print(data_list[search])
                    break                                       # เมื่อเสร็จแล้วจะไปรหัส นศ ต่อไป
                elif search == (len(data_list)-1):              # เช้คว่าวนจนรอบสุดท้ายหรือยัง
                    for index in range(len(data_list[search])): 
                        if calculate_score(enter_data_list):    # ใน calculate_score มี try, except คอยเช็คว่าพิมพ์ข้อมูลครบ หรือว่าพิมพ์ข้อมูลที่คำนวณได้หรือไม่
                            data_list.append(enter_data_list)   # ถ้าใช่ให้นำไปใส่ใน data_list
                            merge_sort(data_list)               # เสร็จแล้วเรียงรหัส นศ
                            print()
                            print("--- Adding data is complete ---")
                            print(data_list)                    
                            break                               # เมื่อเสร็จแล้วจะไปรหัส นศ ต่อไป
                        else:
                            break
                else:
                    continue

        else:                                                   # ถ้าพิมพ์ 'quit' จะจบการกรอกข้อมูล
            break

    print(data_list)
    print()
    print()

    with open(file_name, 'w', newline='') as csvfile_w:     # กำหนด csvfile_w เป็น open(file_name, 'w', newline='')
        csv_writer = csv.writer(csvfile_w)                  # กำหนดให้ csv_writer ว่าจะทำการเขียนข้อมูลลงใน csv
        csv_writer.writerow(list(Columns))    
        # เขียนใส่ไฟล์ชื่อ file_name
        #              
        # จะเป็นการเขียนลงใน csv โดยการเอาข้อมูลทุกตัวมาเขียนใน 1 บรรทัด
        # เช่น Columns = ['Student ID','Q1','Mid','Q2','Final','Attendance','Total','Grade']
        # เอาข้อมูลทุกตัวมาเขียน 1 บรรทัด => Student ID,Q1,Mid,Q2,Final,Attendance,Total,Grade
        csv_writer.writerows(data_list)  
        # เขียนใส่ไฟล์ชื่อ file_name
        #   
        # จะเป็นการเขียนลงใน csv โดยการเอาข้อมูลจากใน list 1 ชุด แล้วมาแยกข้อมูล index ย่อย 
        # เช่น list_ = [[2,3],[4,5]] จะเอา list_[0] มาก่อนแล้วเขียนให้ครบ 1 บรรทัด => 2,3                     

    with open('GPA.csv', 'r') as csvfile_r_grade:
        csv_reader_grade = csv.reader(csvfile_r_grade)
        Columns_grade = next(csv_reader_grade)
        for grade in csv_reader_grade:
            if grade != []:
                Grade.append(grade)

        for unknown in data_list:                           # เอารหัส นศ ใน data_list ไปเช็คใน Grade ว่ามีรหัสนี้ยัง ถ้ายังให้ใส่เข้าไปใน Grade
            find = 0
            for find_unknown_in_grade in Grade:
                if unknown[0] != find_unknown_in_grade[0]:  # ถ้าเช็คแล้วไม่เจอก็ผ่านไป
                    continue
                else:
                    find += 1                               # ถ้าเจอก็จะให้ค่า find = 1 เพื่อบอกว่าเจอค่าแล้ว
                
            if find == 0:                                   # ถ้าไมเจอรหัสนั้นๆใน Grade ก็ใส่ไปใน Grade
                for_contain = []                            # กำหนด for_contain มารับค่า
                for_contain.append(unknown[0])              # นำรหัส นศ ไปใส่ใน for_contain
                for index in range(1,7):                    # range(1,7) คือจำนวนช่องคะแนนของแต่ละวิชา เรากำหนดให้ทุกวิชาช่องคะแนนเท่ากัน
                    for_contain.append('-')                 # นำ '-' ใส่เข้าไป 6 รอบ
                Grade.append(for_contain)                   # ได้ค่า for_contain ที่สมบูรณ์ จึงนำไปใส่ใน Grade
                
    print(Grade)
    print()
    print()
    print(data_list)
            
    for grades in range(len(Grade)):
        sum_degree = 0                                                  # กำหนด sum_degree ไว้รับค่าผลรวมของหน่วยกิตที่นำมาคำนวณ สมมติในตารางมี 4 วิชาก็จะใช้ หน่วยกิต 4 วิชา
        degree_product_grade  = 0                                       # กำหนดค่า degree_product_grade ไว้รับค่าเกรดที่ได้ * หน่วยกิตวิชานั้นๆ
        try:
            Grade[grades][subject] = data_list[grades][7]               # ทำให้ใน Grade เก็บค่าเกรดเป็นตำอักษรในวิชานั้นๆ
        except IndexError:
            print()
            print("--- There is no data in this file ---")              # ถ้า IndexError จะแจ้งว่าไม่มีข้อมูลในไฟล์
            break
        for calculate in range(1,6):
            number_grade = check_grade(Grade[grades][calculate])        # แปลงเกรดตัวอักษรเป็น ตัวเลข   
            degree_product_grade += number_grade*degree[calculate-1]    # เอาเกรดที่เป็นตัวเลข*หน่วยกิต 
            if Grade[grades][calculate] != '-':                         # เช็คเกรดที่นำเข้ามา ไม่ใช่ '-' ใช่มั้ย
                sum_degree += degree[calculate-1]                       # sum_degree หรือผลรวมหน่วยกิต จะบวกหน่วยกิตวิชานั้นๆ
        try:                                                            # เช็คว่า หารได้หรือไม่
            GPA = degree_product_grade/sum_degree                       # สุตรคำนวณ GPA คือผลรวมของเกรดที่ได้*หน่วยกิตวิชานั้นๆ หารด้วย ผลรวมหน่วยกิต
        except ZeroDivisionError:                                       # ถ้าเป็น 0/0 จะ error 
            GPA = 0                                                     # จึงกำหนดให้ GPA = 0
        Grade[grades][6] = GPA                                          # นำ GPA ไปใส่ใน Grade 

    print()
    print()
    print(Grade)

    with open('GPA.csv', 'w', newline='') as csvfile_w_grade:         # กำหนด csvfile_w_grade เป็น open(file_name, 'w', newline='')
        csv_writer_grade = csv.writer(csvfile_w_grade)                  # กำหนดให้ csv_writer ว่าจะทำการเขียนข้อมูลลงใน csv
        csv_writer_grade.writerow(list(Columns_grade))                  # เขียนใส่ไฟล์ GPA.csv โดยเอาข้อมูลทุกตัวเขียนใน 1 บรรทัด
        csv_writer_grade.writerows(Grade)                               # เขียนใส่ไฟล์ GPA.csv โดยเอาข้อมูลแต่ละตัวเขียน 1 แถว

    print("--- Adding or Editing is complete ---")

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

    # เดี๋ยวมาเพิ่มเช้ค total ว่ามากกว่า 100 ป่าว เพื่อป้องกันการกรอกคะแนนเกิน

    total = 0
    try:                                                     # เอาโค้ดที่ต้องการเช็คเข้าไปใน try 
        for score in range(5):
            total += int(add_data_list[score+1])            # บวกคะแนนรวม
        add_data_list[6] = total                            
        add_data_list[7] = check_grade(total)               # กำหนดให้ add_data_list[7] = check_grade(total) เข้าไปเช้คเกรด ว่าได้เกรดเท่าไหร่
    except IndexError:                                      # ถ้าเราใส่ข้อมูลไม่ครบ จะขึ้นว่า "--- Please enter whole data ---"  
        print("--- Please enter whole data ---")
        return False
    except ValueError:                                      # ถ้าเราใส่ข้อมุลที่ไม่สามารถคำนวณได้ จะขึ้นว่า "--- Please enter follow our from data ---"
        print("--- Please enter follow our from data ---")
        return False
    else:
        return True

def check_grade(grade_or_score):
    if str(grade_or_score).isprintable():           # เช้คว่าค่าที่รับเข้ามาแล้วกำหนดให้เป็น str สามารถแสดงผลทางหน้าจอได้ป่าว
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
        
    if str(grade_or_score).isnumeric():             # เช็คว่าค่าที่รับเข้ามาแล้วกำหนดให้เป็น str เป็นตัวเลขหรือไม่
        if int(grade_or_score) >= 80:
            return 'A'
        elif 75 <= int(grade_or_score) < 80:
            return 'B+'
        elif 70 <= int(grade_or_score) < 75:
            return 'B'
        elif 65 <= int(grade_or_score) < 70:
            return 'C+'
        elif 60 <= int(grade_or_score) < 65:
            return 'C'
        elif 55 <= int(grade_or_score) < 60:
            return 'D+'
        elif 50 <= int(grade_or_score) < 55:
            return 'D'
        elif int(grade_or_score) < 50:
            return 'F'

if __name__ == '__main__':
    main()
    #
    