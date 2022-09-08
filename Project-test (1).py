import major

def main():
    #move all function to another file 
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
    
    def Get_Email(department,dict):
        user_input = [""]
        department.show_faculty()
        user_input = input('Please select one of the following: ')
        Navigate_Menu(department,user_input)
        user_input += input('\n Please select one of the following: ')
        reciver = dict[user_input]
        #this line below is for testing purposes only ( if we can succussfly grab any email weve done it)
        #eventually wil be switched to a return statement 
        print(reciver)

    #move all these to a dictionary file
    comp_sci_dict = {'11':'shuanghua.wang@gmail.com','21':'Mohamed.Eltoweissy@morgan.edu', '22':'Roshan.Paudel@morgan.edu','31':'Monireh.Dabaghchian@morgan.edu', '32':'Edward.Dillon@morgan.edu', '33':'Monir.Sharker@morgan.edu','34':'Naja.Mack@morgan.edu','41':'Vojislav.Stojkovic@morgan.edu','51':'Gholam.Khaksari@morgan.edu','52':'Grace.Steele@morgan.edu','53':'Sam.Tannouri@morgan.edu', '61':'Wendy.Smith@morgan.edu'}
    civil_eng_dict = {'11':'Jiang.li@morgan.edu','31':'oludare.owolabi@morgan.edu','32':'Donghee.kang@morgan.edu','33':'Mehdi.shokouhian@morgan.edu','34':'steve.efe@morgan.edu','35':'yi.liu@morgan.edu','41':'James.hunter@morgan.edu','42':'gbeke.oguntimein@morgan.edu','51':'Kiruthika.Saminathan@morgan.edu','52':'cecelia.wrightbrown@morgan.edu','53':'cecelia.wrightbrown@morgan.edu','54':'adewolesimon.oladele@morgan.edu','61':'vanessa.branch@morgan.edu','62':'hyejeong.lee@morgan.edu', '63':'Samuel.Kimani@morgan.edu'}
    ec_engineering_dict = {'11':'ecedept@morgan.edu','21':'arlene.colerhodes@morgan.edu', '22':'kevin.kornegay@morgan.edu' , '23':'craig.scott@morgan.edu', '24':'michael.spencer@morgan.edu', '25':'carl.white@morgan.edu', '26':'gregory.wilkins@morgan.edu', '31':'mdtanvir.arafin@morgan.edu', '32':'getachew.befekadu@morgan.edu', '33':'cliston.cole@morgan.edu', '34':'duane.harvey@morgan.edu', '41':'yacob.astatke@morgan.edu ', '42':'jumoke.ladeji-osias@morgan.edu', '43':'onyema.osuagwu@morgan.edu', '44':'farzad.moazzami@morgan.edu', '45':'kofi.nyarko@morgan.edu', '46':'michel.reece@morgan.edu', '47':'ketchiozo.wandji@morgan.edu', '51':'deanna.bailey@morgan.edu', '52':'mulugeta.dugda@morgan.edu', '53':'ladawn.biddle@morgan.edu'}
    ise_engineering_dict = {'11':'tridip.bardhan@morgan.edu','21':'guangming.chen@morgan.edu','22':'seong.lee@morgan.edu','23':'masud.salimian@morgan.edu','31':'jessye.bemleytalley@morgan.edu','32':'yaseen.mahmud@morgan.edu','41':'leeroy.bronner@morgan.edu','51':'kayenda.johnson@morgan.edu','52':'garfield.jones@morgan.edu','53':'wamuzemba.tshibangu@morgan.edu'}


    name = input('Enter Name: ')
    email = input('Enter Email: ')
    password = input("Enter Password: ")
    credits = input('How many credits do you have: ')
    name_of_major = input('Enter Major: ')
    print('\n')
    
    #name = major.Major(name,credits,name_of_major)
    title = major.Major(name,credits,name_of_major)
    title.Gretting()
    

    #turn this into a function for strealining user input for use
    name_of_major = name_of_major.lower()
    name_of_major = name_of_major.replace(" ", "")

    if name_of_major == 'computerscience':
        comp_sci = major.computerscience(name,credits,name_of_major)
        Get_Email(comp_sci,comp_sci_dict)
        
    if name_of_major == 'civilengineering':
        civil_eng = major.civilengineering(name,credits,name_of_major)
        Get_Email(civil_eng,civil_eng_dict)

    if name_of_major == 'electricalengineering' or name_of_major == 'computerengineering':
        ec_engineering = major.electricalComputerengineering(name,credits,name_of_major)
        Get_Email(ec_engineering,ec_engineering_dict)
    
    if name_of_major == 'industrialengineering' or name_of_major == 'systemengineering':
        ise_engineering = major.industrialsystemsengineering(name,credits,name_of_major)
        Get_Email(ise_engineering,ise_engineering_dict)



    
        

        

        


main()