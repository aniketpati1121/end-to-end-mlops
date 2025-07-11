class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.loggedin = False
        self.menu()

    def menu (self):
        user_input = input("""Welcome to chatbook !! How would you like to proceed ?
                           1. Press 1 to Signup
                           2. Press 2 to signin
                           3. Press 3 to write a post
                           4. Press 4 to message a friend
                           5. Press any other key to exit
                           
                           
                           -> """)   
        

        if user_input == "1":
            self.signup()
        elif user_input == "2":
            self.signin()
        elif user_input == "3":
            self.my_post()
        elif user_input =="4":
            self.sendmsg()
        #elif user_input =="2":
            #pass
        else:
            exit()


    
    def signup(self):
        email = input ("enter your email here -> ")
        pwd = input ("setup your password here -> ")
        self.username = email
        self.password = pwd
        print("You have signed up successfully !!")
        print("\n")
        self.menu()



    def signin(self):
        if self.username=='' and self.password=='':
            print("Please signup first by pressing 1 in the main menu")
        else:
            uname = input("enter your email/username here ->")
            pwd = input ("enter your password here ->") 
            if self.username==uname and self.password==pwd:
              print("you have signed in succesfully !!") 
            else:
                print("Please input correct credentails..")
        print("\n")
        self.menu()   



    def my_post(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            print(f"Following content has been posted -> {txt}")
        else:  
            print("You need to signin first to post something...")  
        print("\n")
        self.menu()



    def sendmsg(self):
        if self.loggedin==True:
            txt = input("Enter your message here -> ")
            frnd = input ("whom to send a messsage ? ->")
            print(f"Your message has been sent to {frnd}") 
        else:  
            print("You need to signin first to post something...")  
        print("\n")
        self.menu()
    





user1 = chatbook() 
        
        
        
