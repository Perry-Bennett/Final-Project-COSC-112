from re import S


class Major():
    def __init__(self,name,credits,nom,):
        self.__name = name
        self.__credits = credits
        self.__name_of_major = nom

    def set_name(self,name):
        self.__name = name
    def set_credits(self,credits):
        self.__credits = credits
    def set_name_of_major(self,nom):
        self.__name_of_major = nom 
    def get_name(self):
        return self.__name
    def get_credits(self):
        return self.__credits
    def get_name_of_major(self,nom):
        return self.__name_of_major
    def Gretting(self):
        print('You have five departments to choose from: \n Computer Science \n Civil Engineering \n Electrical and Computer Engineering \n Industrial and Systems Engineering \n Mechatronics! \n')
        print('You are a', self.__name_of_major , 'major so lets go with that one. \n')
   

class computerscience(Major):
    def _init__(self,name,credits,nom):
        Major.__init__(self,name,credits,nom)

    def show_faculty(self):
        print(' Which faculty type would you like to contact?')
        print(' 1-Department Chair \n 2-Professors \n 3-Assistant Professors \n 4-Associate Professors \n 5-Lectures \n 6-Staff')    

    def show_chair(self):
        print('DEPARTMENT CHAIR: \n 1-Dr.Shuangbao "Paul" Wang')

    def show_Professors(self):
        print('DEPARTMENT PROFESSORS: \n 1-Dr.Mohamed Eltoweissy \n 2-Dr.Roshan Paudel')
        
    def show_Assistant_Professors(self):
        print('ASSITANT PROFESSORS: \n 1-Dr.Monireh Dabaghchian \n 2-Dr.Edward Dillon, Jr. \n 3-Dr.Monir Sharker \n 4-Dr.Naja Mack')
        
    def show_Associate_Professors(self):
        print('ASSOCIATE PROFESSORS: \n 1-Dr. Vojislav Stojkovic')   
    
    def show_lectures(self):
        print('LECTURES: \n 1-Dr. Gholam Khaksari \n 2-Grace Steele \n 3-Dr. Sam Tannouri')
        
    def show_staff(self):
        print('STAFF: \n 1-Wendy Smith')
        
        
class civilengineering(Major):
    def __init__(self,name,credits,nom):
        Major.__init__(self,name,credits,nom)

    def show_faculty(self):
        print(' Which faculty type would you like to contact?')
        print(' 1-Department Chair \n 2-N/A \n 3-Assistant Professors \n 4-Associate Professors \n 5-Lectures \n 6-Staff')    

    def show_chair(self):
        print('DEPARTMENT CHAIR: \n 1-Dr.Jiang Li') 

    def show_Professors(self):
        print('DEPARTMENT PROFESSORS: \n 1- N\A')  

    def show_Assistant_Professors(self):
        print('ASSITANT PROFESSORS: \n 1-Oludare Owolabi \n 2-Dong Hee Kang \n 3-Mehdi Shokouhian \n 4-Steve Efe \n 5-Yi Liu')

    def show_Associate_Professors(self):
        print('ASSOCIATE PROFESSORS: \n 1-James Hunter Jr. \n 2-Gbekeloluwa Oguntimein')

    def show_lectures(self):
        print('LECTURES: \n 1-Kiruthika Saminathan \n 2-Cecelia Wright Brown \n 3-Emad Gheibi \n 4-Adewole Oladele')    

    def show_staff(self):
        print('STAFF: \n 1-Vanessa Branch \n 2-Hye Jeong Lee \n 3-Samuel Kimani')
    
class electricalComputerengineering(Major):
    def __init__(self,name,credits,nom):
        Major.__init__(self,name,credits,nom)
    
    def show_faculty(self):
        print(' Which faculty type would you like to contact?')
        print(' 1-Department Chair \n 2-Professors \n 3-Assistant Professors \n 4-Associate Professors \n 5-Lectures \n 6-N/A')

    def show_chair(self):
        print('DEPARTMENT CHAIR: \n 1-Ms.April Lopez')

    def show_Professors(self):
        print('DEPARTMENT PROFESSORS: \n 1-Dr.Arlene Cole-Rhodes \n 2-Dr.Kevin T.Kornegay \n 3-Dr.Craig J.Scott \n 4-Dr.Michael G.Spencer \n 5-Dr.Carl White \n 6-Dr. Gregory M. Wilkins')

    def show_Assistant_Professors(self):
        print('ASSITANT PROFESSORS: \n 1-Dr.Tanvir Arafin \n 2-Dr. Getachew Befekadu \n 3-Dr.Cliston Cole \n 4-Dr.Duane Harvey')

    def show_Associate_Professors(self):
        print('ASSOCIATE PROFESSORS: \n 1-Dr. Yacob Astatke \n 2-Dr. Kemi Ladeji-Osias \n 3-Dr.Onyema Osuagwu \n 4-Dr. Farzad Moazzami \n 5-Dr. Kofi Nyarko  \n 6-Dr. Michel Reece \n 7-Dr.Ketchiozo Wandji')

    def show_lectures(self):
        print('LECTURES: \n 1-Dr.Deanna Bailey \n 2-Dr.Mulugeta Dugda \n 3-Mrs.LaDawn Partlow \n ')
    
    def show_staff(self):
        print('STAFF: \n 1-N/A')

class industrialsystemsengineering(Major):
    def __init__(self,name,credits,nom):
        Major.__init__(self,name,credits,nom)
    
    def show_faculty(self):
        print(' Which faculty type would you like to contact?')
        print(' 1-Department Chair \n 2-Professors \n 3-Assistant Professors \n 4-Associate Professors \n 5-Lectures \n 6-N/A')

    def show_chair(self):
        print('DEPARTMENT CHAIR: \n 1-Dr. Tridip Bardhan')

    def show_Professors(self):
        print('DEPARTMENT PROFESSORS: \n 1-Dr.Guangming Chen \n 2-Dr.Seong W. Lee \n 3-Dr.Masud Salimian')

    def show_Assistant_Professors(self):
        print('ASSITANT PROFESSORS: \n 1-Dr. Jessye Bemley Talley \n 2-Mr. Yaseen Mahmud')

    def show_Associate_Professors(self):
        print('ASSOCIATE PROFESSORS: \n 1-Dr. LeeRoy Bronner')

    def show_lectures(self):
        print('LECTURES: \n 1-Dr. Kayenda Johnson \n 2-Dr. Garfield Jones \n 3-Dr. Wa Tshibangu')

    def show_staff(self):
        print('STAFF: \n 1-N/A')


class mechatronics(Major):
    def __init__(self,name,credits,nom):
        Major.__init__(self,name,credits,nom)

    def show_faculty(self):
        print(' Which faculty type would you like to contact?')
        print(' 1-Department Chair \n 2-N/A \n 3-N/A \n 4-N/A \n 5-N/A \n 6-N/A')
    
    def show_chair(self):
        print('DEPARTMENT CHAIR: \n 1-Celeste Chavis')

    def show_Professors(self):
        print('DEPARTMENT PROFESSORS: \n N\A')
    
    def show_Assistant_Professors(self):
        print('ASSITANT PROFESSORS: \n N\A')

    def show_Associate_Professors(self):
        print('ASSOCIATE PROFESSORS: \n N\A')

    def show_lectures(self):
        print('LECTURES: \n N\A ')
    
    def show_staff(self):
        print('STAFF: \n 1-N/A')

    
    


    

    
    


    

    

    

    

    

    

    


    


    

    

    
    
    

    
    

    
