#this is necessary for my Send_Email function to work
#project
import smtplib

#This function, with the help of the Navigate_Menu function gets an email adress from one of the five dictionaries and returns it 
def Get_Email(department,dict):
    user_input = [""]
    department.show_faculty()
    user_input = input('Please select one of the following: ')
    Navigate_Menu(department,user_input)
    user_input += input('\n Please select one of the following: ')
    reciver = dict[user_input]
    return reciver


def Navigate_Menu(x,user_input):
    if user_input == '1':
        x.show_chair()
    if user_input == '2':
        x.show_Professors()
    if user_input == '3':
        x.show_Assistant_Professors()
    if user_input == '4':
        x.show_Associate_Professors()
    if user_input == '5':
        x.show_lectures()
    if user_input == '6':
        x.show_staff()

#This was the closest I could do in terms of validating user input because this program only takes in string input
#This is heavly reliant on the user spelling their major correctly (caps and spaces do not matter)
def Manipulate_User_Input(name_of_major):
    name_of_major = name_of_major.lower()
    name_of_major = name_of_major.replace(" ", "")
    return name_of_major

#This was created with the help of youtube. I will post the link to the video as part of my submission
#The only changes that were made was that I placed it in a function(added arguments,etc)
def Send_Email(email_address,email_password,recipient,subject,body):
    with smtplib.SMTP('smtp.gmail.com',587) as smtp:
        smtp.ehlo()
        smtp.starttls()
        smtp.ehlo()

        #logins user into there personal email address
        smtp.login(email_address,email_password)

        msg = f'Subject: {subject}\n\n{body}'

        smtp.sendmail(email_address,recipient, msg) 

