import os
import time

def homelogo () : 
    os.system('cls')
    print('STUDENT MANAGER'.center(60,'='))



def homepage() :
    homelogo()
    

    print("""
    1. ADD STUDENT
    2. VIEW STUDENTS 
    3. SEARCH STUDENT 
    4. UPDATE STUDENT
    5. DELET STUDENT 
    6. EXIT...
        """)
    entry = input('Choose a option >> ')


    while True : 

        if  entry == '1' : 
            homelogo()
            print('add student'.title().center(40, '_'))
            addstudent()

        elif entry == '2' : 
            homelogo()
            print('\nSEE THE INFOS OF THE STUDENTS')
            print('-'*50)
            view_students()
            break
        
        elif entry == '3':
            homelogo()
            search_student()
            break
        
        elif entry == '4' :
            homelogo()
            update()
            break



def addstudent() :
    data = [
    "STUDENT NAME",
    "STUDENT'S AGE",
    "FATHER'S NAME",
    "MOTHER'S NAME",
    "STUDENT'S CLASS",
    "STUDENT'S ID",
]
    with open("adding_new_students.txt", "a" , encoding='UTF-8') as f:
        while True : 
            for i in data :
                student_info = input(f"{i}      : ").strip()

                if student_info =='' :
                    student_info = 'null'
                    f.write(f"{i}   : {student_info}\n")
                    continue

                f.write(f"{i}       : {student_info}\n") 
            f.write("•" * 60 + "\n")


            print('\nsaving data...')
            time.sleep(2)
            print('data saved successfully\n')
            a = input('DO YOU WANT TO CONTINUE ? (Y/N) >>')
            x ="y n Y N".split()

            while True : 

                if a not in x : 
                    print('\nPLEASE TYPE EITHER (Y) OR (N)')
                    time.sleep(2)
                    a = input('DO YOU WANT TO CONTINUE ? (Y/N) >>')

                elif a == 'n' or a=='N':
                    print('OK...')
                    input('enter any key to go back...')
                    f.close()
                    homepage()   

                elif a == 'Y' or a=='y' : 
                    time.sleep(0.5)
                    break
            break



def view_students():

    try : 
        with open('adding_new_students.txt' , 'r' ) as f : 
            infos = f.read()
            print (infos)

            while True : 
                w = input("enter 0 to return.. ")
                if w =='0' :
                    homepage()

                else : 
                    print('please type - 0 ')
              
    except FileNotFoundError : 
        print('file not found')


def search_student() :
    with open('adding_new_students.txt', 'r', encoding='UTF-8') as f:
        data = f.readlines()
    print('type 0 to return homepage.')
    
    while True :
            search = input('Enter the ID of the student >>> ').strip()
            found = False

            if search == '0' : 
                homepage()
            
            else:
                for i , line in enumerate(data) : 
                    if search in line : 
                        found = True
                        start = max(0,i-6)
                        for j in range (start , i+2) :
                            print(data[j])
                        break   
                
            if not found: 
                print(f'PLEASE TYPE 0 IF YOU WANT TO RETURN HOME PAGE...\nBECAUSES THESE {search}  IS NOT FOUND\n ELSE TYPE A VALID ID') 






def update():
    homelogo()
    print('UPDATE THE INFOS OF THE STUDENT\n')

    with open('adding_new_students.txt', 'r', encoding='UTF-8') as f:
        data = f.readlines()

    search = input('Enter the ID of the student >>> ').strip()

    found = False

    for i, line in enumerate(data):
        if search in line:
            found = True
            start = i - 5

            print()
            for j in range(start, i + 1):
                print(data[j], end='')

            print("""
1. NAME
2. AGE
3. FATHER'S NAME
4. MOTHER'S NAME
5. STUDENT'S CLASS
6. STUDENT'S ID
""")

            choice = input('SELECT OPTION >> ')

            if choice.isdigit() and 1 <= int(choice) <= 6:

                new_value = input('ENTER NEW VALUE >> ')

                line_no = start + int(choice) - 1

                label = data[line_no].split(':')[0]

                data[line_no] = f"{label:<20}: {new_value}\n"

                with open('adding_new_students.txt', 'w', encoding='UTF-8') as f:
                    f.writelines(data)

                print("\nUPDATED SUCCESSFULLY.")
            break

    if not found:
        print("STUDENT NOT FOUND.")

    input("\nPRESS ENTER TO RETURN...")


            
homepage()
