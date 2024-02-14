''' This program registers students name and ID number for an event. 
    Once the list of students is complete a register can be created, 
    as a text file ready to be printed. Check menu options for more info'''

import os
if not os.path.exists("list_of_students.txt"):
    with open("list_of_students.txt", "w") as default_file:
        pass
# Reads in data to carry on adding more entries to the list
with open('list_of_students.txt', 'r') as file:
    students_list = file.readlines()
students_data = {}
for student in students_list:
    name, id = student.split(',')    
    students_data[name] = id.strip('\n')
def save():
    # Work progress is saved in text file list_of_students.txt
    line_to_write = ''
    for name, id in students_data.items():
        line_to_write += name + ',' + str(id) + '\n'
    with open('list_of_students.txt', 'w') as file:
            file.write(line_to_write)    
    
menu = '''Select one of the following options below:
a   - Add a student to database
s   - Save your progress
v   - View all entries
d   - Delete entry
gr  - Generate attendance register
e   - Exit the program
    '''
print(menu)
all_students_registered = False
while not all_students_registered:  
    try:
        user_in = input(': ')                       
        if user_in == 'a':
            print('Enter student data in the following format:\
            \nJohn Smith, 123456  or select r to return to main menu')
            continue        
        elif user_in == 's':
            save()
            print('Data saved, add more entries or select r to return to main menu')
            continue     
        elif user_in == 'd':
            student_name = input('Insert student name and press enter to delete from database\n: ')
            if student_name in students_data.keys():
                del students_data[student_name]
                print('The entry has been deleted from database.')                
            else:
                print('The name not found in database')            
            print(menu) 
            continue
        elif user_in == 'r':
            print(menu)
            continue
        elif user_in == 'v':            
            names_list = [name for name in students_data.keys()]
            names_list.sort()
            all_entries = 'No\tstudent name and ID number\n'
            for i, name in enumerate(names_list):
                all_entries += f'{i}\t{name},{students_data[name]}\n'            
            print(all_entries)
            print('Select d to delete or r to go back to main menu')
            continue
        elif user_in == 'gr':
            # Students register with ID numbers and space for signature
            line_to_write = f'No\tStudent ID\t\tSignature\n'
            for i, id in enumerate(students_data.values()):
                line_to_write += f'{i}\t{id}\t\t................\n'
            with open('reg_form.txt', 'w') as file:
                file.write(line_to_write)
        elif user_in == 'e':
            save()
            all_students_registered = True  
            print('Goodbye')  
        else:
            name, id = user_in.split(',')
            students_data[name] = id
    except ValueError:
        print('Incorrect entry')
        continue
