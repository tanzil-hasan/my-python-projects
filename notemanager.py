import os 
import time 

def logo () : 
    os.system('cls')
    print(r""" _                          
 __      _____| | ___ ___  _ __ ___   ___ 
 \ \ /\ / / _ \ |/ __/ _ \| '_ ` _ \ / _ \
  \ V  V /  __/ | (_| (_) | | | | | |  __/
   \_/\_/ \___|_|\___\___/|_| |_| |_|\___|
                                          (version- 1.03) """)

    print('='*57)  

def main_page() :
    while True: 
        logo()
        print("""\t \x1b[33m       1) ADD NOTES\n
                2) VIEW NOTES\n
                3) EXIT...\n \x1b[00m""")

        choice =input( '\x1b[33m Write >> ')  

        if choice == '1':
            logo()
            print('\n             ADD YOUR NOTES  HERE')
            print('\n             TYPE X TO EXIT \n')
            add_note()

        elif choice == '2':
            logo()
            print('\n \x1b[32m     SEE YOUR NOTES \x1b[00m')
            print('_'*30+'\n')
            view_note()
            
        elif choice == '3' : 
            print('\x1b[34m     PROGRAMME CLOSED  \x1b[00m')
            break

        else : 
            print('UNSUPPORTED OPTION.\nWRITE ACCORDING TO THE FOLLOWING ORDER')
            time.sleep(1.5)


def add_note () :
    i = 1
    while True : 
        write_ = input(f"{i}) ")
        i += 1

        if write_ == 'x' or write_ == 'X' : 
            print('CLOSING...')
            time.sleep(1.5)
            break

        elif write_ == '' :
            continue

        with open('note.txt' , 'a' , encoding='UTF-8') as f : 
            f.write(write_.strip() + '\n')
    print("Saved!")

def view_note () : 
    try : 
        with open('note.txt') as f : 
            data = f.read()
            print(data)
            input('PRESS ENTER KEY TO RETUTN HOME PAGE...')

    except FileNotFoundError:
        print('file does not exist')
        input('PRESS ENTER KEY TO RETUTN HOME PAGE...')

main_page()
