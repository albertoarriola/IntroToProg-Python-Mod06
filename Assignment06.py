# ------------------------------------------------------------------------------------------ #
# Title: Assignment06
# Desc: This lab demonstrates using input and output to a file, functions and classes
# Change Log: (Who, When, When)
#   Alberto Arriola, 2/28/2025, Created script
#   Alberto Arriola, 3/1/2025, Added comments
# ------------------------------------------------------------------------------------------ #

# Constants
MENU: str = """---- Course Registration Program ----
  Select from the following menu:
   1. Register a student for a course
   2. Show current data
   3. Save data to a file
   4. Exit the program
-------------------------------------"""                    # String constant containing the Menu with choices for the user
FILE_NAME: str = "Enrollments.json"                         # String constant containing the name of the external json file

# Variables
file: object = None                                         # Object variable for external file
menu_choice: str = " "                                      # String variable containing the user's menu selection
students: list = [dict [str, str, str]]                     # List variable for collecting all the entered student information

import json                                                 # import json module

# Define Classes

class FileProcessor:
    """
    A collection of processing layer functions that work with Json files

    ChangeLog: (Who, When, What)
    Alberto Arriola, 2/28/2025, Created Class
    """
    @staticmethod
    def read_data_from_file(file_name: str):
        """
        This function opens an external JSON file and reads the data
        into a List of Dictionaries.
        ChangeLog: (Who, When, What)
        Alberto Arriola, 2/28/2025, Created function
        :parameters: file_name: name of external JSON file
        :return: student_list: List of Dictionaries containing student information
        """
        student_list: list = []                                                                 # declare local student_list List variable to store student registration information read from external file
        try:                                                                                    # try statement for exception handling
            file = open(file_name, "r")                                                         # External json file is opened with 'r' read argument, file_name is passed in as a parameter
        except FileNotFoundError as e:                                                          # except statement catches FileNotFoundError
            IO.output_error_message(f"File \"{FILE_NAME}\" does not exist.", e)        # call to output_error_message function in IO class sending message and error parameters
        except Exception as e:                                                                  # except statement catches nonspecific error
            IO.output_error_message("An unexpected error occurred.", e)                # call to output_error_message function in IO class sending message and error parameters
        else:                                                                                   # else statement executed if except statements are not triggered(no errors occur)
            student_list = json.load(file)                                                      # Contents of external file are loaded into the local student_list List variable using the json.load() function
            file.close()                                                                        # External json file is closed
        return student_list                                                                     # value of student_list is returned to main program

    @staticmethod
    def write_data_to_file(file_name: str, student_data: list):
        """
        This function opens an external JSON file and writes the student
        registration data to the file.
        ChangeLog: (Who, When, What)
        Alberto Arriola, 2/28/2025, Created function
        :parameters: file_name: name of external JSON file,
        student_data: List of Dictionaries containing student information
        :return: None
        """
        if not student_data:                                                                    # Nested if statement triggered if the student_data List variable contains no data
            print("There is no student data to upload.")                                        # User is notified that no student data exists to be uploaded
        else:                                                                                   # else statement for nested if statement is triggered if student_data List variable contains data
            file = open(file_name, "w")                                                         # External json file with name equal to file_name String variable is opened with 'w' write argument and assigned to the file Object variable
            try:                                                                                # try statement for exception handling
                json.dump(student_data, file)                                                   # json.dump function is used to upload contents of student_data List variable to external json file
            except NameError as e:                                                              # except statement catches NameError
                IO.output_error_message("An error occurred because the file name for the write function is incorrect.", e)  # call to output_error_message function in IO class sending message and error parameters
            except Exception as e:                                                              # except statement catches any unexpected error
                IO.output_error_message("An unexpected error occurred.", e)            # call to output_error_message function in IO class sending message and error parameters

            file.close()                                                                        # External json file is closed
            for student in student_data:                                                        # Nested for Loop iterates for each student item in the student_data List variable
                print(f"{student["FirstName"]} {student["LastName"]} has "
                        f"been registered for {student["CourseName"]}.")                        # F string is used to format printout of first name, last name and course name
            print()                                                                             # Extra print() line for formatting

class IO:
    """
    A collection of presentation layer functions that manage user input and output
    ChangeLog: (Who, When, What)
    Alberto Arriola, 2/28/2025, Created Class
    """
    @staticmethod
    def output_error_message(message: str, error: Exception = None):
        """
        This function displays error messages to the user
        ChangeLog: (Who, When, What)
        Alberto Arriola, 2/28/2025, Created function
        : parameters: message = error message in the form of a string,
        error = Exception
        : return: None
        """
        print(message, end="\n")                                                                # passed in error message is printed followed by a newline
        if error is not None:                                                                   # if statement triggered if error parameter is passed into the output_error_message function
            print("-- Technical Error Message -- ")                                             # error message banner is displayed
            print(error, error.__doc__, type(error), sep='\n')                                  # Python error information is displayed
        print()                                                                                 # Extra print() line for formatting

    @staticmethod
    def input_menu_choice(menu_display: str):
        """
        This function retrieves the user's menu selection.
        ChangeLog: (Who, When, What)
        Alberto Arriola, 2/28/2025, Created function
        :parameters: menu_display = menu String from constant MENU
        :return: user_selection: String containing user's menu selection
        """
        user_selection: str = ""                                                                # user_selection String variable is declared to contain the user's menu choice

        while True:                                                                             # while Loop continues to execute until valid menu selection is made
            print()                                                                             # Extra print() line for formatting
            IO.output_menu(menu_display)                                                        # output_menu function in IO class is called to display menu of selections
            user_selection = input("Please make a selection: ")                                 # input function used to asked user to make a menu selection; result is assigned to user_selection variable
            if user_selection not in ("1,2,3,4"):                                               # nested if statement is triggered if user input is invalid
                print("Please select 1, 2, 3 or 4.")                                            # print statement tells the user to make a valid entry
                continue                                                                        # continue statement returns program to start of while Loop; menu is displayed again and user is asked to make a selection
            else:                                                                               # else statement is triggered if user enters a valid selection
                break                                                                           # break statement exits the while Loop
        print()                                                                                 # Extra print() line for formatting
        return user_selection                                                                   # value stored in user_selection is returned to the main program

    @staticmethod
    def output_menu(menu_display: str):
        """
        This function prints out the selection Menu.
        ChangeLog: (Who, When, What)
        Alberto Arriola, 2/28/2025, Created function
        :parameters: menu_display: menu String displaying menu selections
        :return: None
        """
        print(menu_display)                                                                     # value of menu_display String is displayed

    @staticmethod
    def input_student_data(student_list: list):
        """
        This function asks the user to enter student information and
        appends it to the existing list of student information.
        ChangeLog: (Who, When, What)
        Alberto Arriola, 2/28/2025, Created function
        :parameters: student_list: List of Dictionaries containing student data
        :return: student_list: List of Dictionaries containing student data
        """
        # variables local to the function
        student_first_name: str = " "                                                           # String variable containing the student's first name
        student_last_name: str = " "                                                            # String variable containing the student's last name
        course_name: str = " "                                                                  # String variable containing the course name
        student_data: dict[str, str] = {}                                                       # Dictionary variable for collecting entered student information

        while True:                                                                             # while Loop continues to execute if the user enters a first name with at least one non-alpha character
            try:                                                                                # try statement for exception handling
                student_first_name = input("Enter the student's first name: ")                  # input() asks user to enter student's first name and assigns answer to student_first_name string variable
                if not student_first_name.isalpha():                                            # if statement checking if student_first_name contains non-alpha characters
                    raise ValueError()                                                          # ValueError is thrown if student_first_name contains non-alpha characters
            except ValueError as e:                                                             # except statement catches ValueError as e
                IO.output_error_message("The student's first name should only contain letters.")  # output_error_message function in IO class is called to display error message(s)
            except Exception as e:                                                              # except statement catches any error other than ValueError as e
                IO.output_error_message("An unexpected error occurred.", e)            # output_error_message function in IO class is called to display error message(s)
                continue                                                                        # continue statement returns user to start of while Loop to enter student's first name again
            else:                                                                               # else statement is triggered when user enters student_first_name without any non-alpha characters
                break                                                                           # code breaks out of while Loop when user enters a student's first name without any non-alpha characters

        while True:                                                                             # while Loop continues to execute if the user enters a last name with at least one non-alpha character
            try:                                                                                # try statement for exception handling
                student_last_name = input("Enter the student's last name: ")                    # input() asks user to enter student's last name and assigns answer to student_last_name string variable
                if not student_last_name.isalpha():                                             # if statement checking if student's last name contains non-alpha characters
                    raise ValueError()                                                          # Exception message for when student's last name contains non-alpha characters
            except ValueError as e:                                                             # Exception is thrown if student's last name contains non-alpha characters
                IO.output_error_message("The student's last name should only contain letters.")  # output_error_message function in IO class is called to display error message(s)
            except Exception as e:                                                              # except statement catches any error other than ValueError as e
                IO.output_error_message("An unexpected error occurred.", e)            # output_error_message function in IO class is called to display error message(s)
                continue                                                                        # continue statement returns user to start of while Loop to enter student's last name again
            else:                                                                               # else statement is triggered when user enters a student's last name without any non-alpha characters
                break                                                                           # code breaks out of while Loop when user enters a student's first name without any non-alpha characters

        course_name = input("Enter the course name: ")                                          # input() asks user to enter course name and assigns answer to course_name string variable
        student_data = {"FirstName": student_first_name,
                        "LastName": student_last_name,
                        "CourseName": course_name}                                              # student_first_name, student_last_name, course_name KeyName Value pairs added to the student_data Dictionary variable
        student_list.append(student_data)                                                       # contents of student_data Dictionary variable are appended to students List variable
        print()                                                                                 # Extra print() line for formatting
        return(student_list)                                                                    # value in student_list List variable is returned to the main program

    @staticmethod
    def output_student_courses(student_info: list):
        """
        This function displays current student information.
        ChangeLog: (Who, When, What)
        Alberto Arriola, 2/28/2025, Created function
        :parameters student_info: List of Dictionaries containing student data
        :return: None
        """
        if not student_info:                                                                    # Nested if statement triggered if the student_info List variable contains no data
            print("There is no student data to display.")                                       # User is notified that no student data exists to be displayed
        else:                                                                                   # else statement for nested if statement triggered if student_info List variable contains data
            print()                                                                             # Extra print() line for formatting
            print("The current data is: ")                                                      # Header is printed to notify user of the current student registration data
            for student in student_info:                                                        # Nested for loop iterates for each student item in the student_info List variable
                print(student["FirstName"], student["LastName"]
                      + ", " + student["CourseName"])                                           # Information for each student in the student_info List variable is printed out
            print()                                                                             # Extra print() line for formatting


# open and read from json file
students = FileProcessor.read_data_from_file(FILE_NAME)                                         # read_data_from_file function in class FileProcessor is called; returned value is assigned to students List variable

while (True):                                                                                   # while loop starts so that the program runs until the user chooses to exit

    menu_choice = IO.input_menu_choice(MENU)                                                    # input_menu_choice function in class IO is called and MENU String constant is passed in as a parameter; returned string value is assigned to the menu_choice string variable

# Selection 1. Register a student for a course
    if (menu_choice == "1"):                                                                    # if statement triggered when user enters "1" from the menu
        students = IO.input_student_data(students)                                              # input_student_data function in IO class is called and value of students List variable is passed in as a parameter; returned List value is assigned to students List variable
# Selection 2. Show current data
    elif (menu_choice == "2"):                                                                  # elif statement triggered when user enters "2" from the menu
        IO.output_student_courses(students)                                                     # output_student_courses function in IO class is called and value of students List variable is passed in as a parameter
# Selection 3. Save data to a file
    elif (menu_choice == "3"):                                                                  # elif statement triggered when user enters "3" from the menu
        FileProcessor.write_data_to_file(FILE_NAME, students)                                   # write_data_to_file function in FileProcessor class is called and value of constant MENU string variable and students List variable are pass in as parameters
# Selection 4. Exit the program
    elif (menu_choice == "4"):                                                                  # elif statement triggered when user enters "4" from the menu
        print("Goodbye!")                                                                       # print() 'Goodbye!'
        break                                                                                   # break statement stops the while loop and ends the program
