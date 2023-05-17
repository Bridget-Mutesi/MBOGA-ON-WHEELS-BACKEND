class Customer:
 
    def __init__(self):
        self.name=none
        self.email=none
        self.phone_number=none
        self.password=none
        self.location=none
        self. customers_data=[]
        
    def signUp(self):
        self.name= input('enter your name')
        self.email=input('enter your email')
        self.phone_number= input('enter your phone number')
        self.password= input('enter your password')
        self.customers_data.append([self.name,self.email,self.phone_number,self.password])
        print("signed up successfully")
        
    

    def login(self):
        self.email=input('enter your email')
         self.password= input('enter your password')
        self.location= input('enter your location')
        for customer in self.customers_data:
            if customer [1]==email and customer[2]==password:
                print(f"WELCOME TO MBOGA ON WHEELS {customer[0]})
            return
                print("INVALID EMAIL AND PASSWORD")
