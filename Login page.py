i=0
while i<=5:
    import getpass
    name=input("Enter your Name: ") 
    Email=input("Enter Your Email: ")
    password=getpass.getpass("Enter your Password: ")
    def profile():
        print('''Name:Shukur Alam
        Father Name: Mosarof Hossain
        Mother Name: Kuslsuma Begom
        Date of Birth: 3.03.2003
        Hometown: Hajiganj
        Post: Hajiganj
        Your enter password ::61178393483''')
    if Email == 'shukuralom1234@gmail.com' and password == "shukur1234":
        print("                             ---login successfil---                                       ")
        profile()
        break
    else:
        print("Error try again")
        i=i+1