import BloodBanks


class Application:

    ##Dict of Username : Password
    Login_Details = {"Admin_" : "@Admin"}

    ##User Data of Username : {Name, Age, BloodType, city}
    User_Data = {"Admin_" : {"Name" : "Admin", "Age" : "--", "Blood_Type" : "--", "city" : "--"}}

    ##Register for Blood Donation User Data of UserName : {Name, Age, BloodType, city}
    Registered_User = {}

    def Log_in_options(self):
        ch = int(input("Enter 1 to Create an Account, Enter 2 to sign-in :"))

        if ch == 2:
            self.Sign_in()
            
        elif ch == 1:
            self.CreateAcc()
            
        else:
            print("Invalid Input")

    def Sign_in(self):
        username = str(input("Enter Username : "))
        password = str(input("Enter password : "))

        if username in self.Login_Details and self.Login_Details[username] == password:
            print("Log-in successful")
            ##Show User-Data
            print(self.User_Data[username])
            ##Show Reg. for Donation and Search BloodGr
            if username == "Admin_":
                self.Admin()
            else:
                ch = int(input("Enter 1 to Register for Blood Donation, Enter 2 to Search for Blood Group : "))
                if ch == 1:
                    self.Register_for_Donation(username)
                elif ch == 2:
                    self.Request_for_blood(username)
                else:
                    print("Invalid choice")

        else:
            print("Wrong Credentials..")

    def CreateAcc(self):
        username = str(input("Choose a Username : "))
        if username in self.Login_Details:
            print("Username Already exist!")
            print("Try Logging-in")
            self.Sign_in()
    
        else:
            password = str(input("Choose Password : "))
            self.Login_Details[username] = password
            print("Fill up your details : ")
            Name = str(input("Enter Name : "))
            Age = int(input("Enter Age : "))
            blood_type = str(input("Enter Blood Group : "))
            city = str(input("Enter City : "))
            self.User_Data[username] = {"Name" : Name, "Age" : Age, "Blood_Type" : blood_type, "city" : city}
            print("Account Created Successfull..")
            print("Plase Log-in to your Account")
            self.Sign_in()
            return
    
    def Register_for_Donation(self, username):
        if username in self.User_Data:
            print("Please Wait while Registration is in Process...")
            Name = self.User_Data[username]["Name"]
            Age = self.User_Data[username]["Age"]
            bloodtype = self.User_Data[username]["Blood_Type"]
            city = self.User_Data[username]["city"]
            self.Registered_User[username] = {"Name" : Name, "Age" : Age, "Blood_type" : bloodtype, "city" : city}
            
            if city in BloodBanks.BloodBanks().city_donor:
                BloodBanks.BloodBanks().city_donor[city][Name] = bloodtype
            print("Registration Successful\nThank You")

    def Request_for_blood(self, username):
        bloodtype = str(input("Enter Blood Group : "))
        stock = BloodBanks.BloodBanks().BloodRequest(bloodtype)
        if stock == 1:
            ch = int(input("Enter 1 to send Request for this Blood Group : "))
            if ch == 1:
                print("Request Sent")
                city = self.User_Data[username]["city"]

                if city in BloodBanks.BloodBanks().Blood_request:
                    
                    if bloodtype in BloodBanks.BloodBanks().Blood_request[city]:
                        BloodBanks.BloodBanks().Blood_request[city][bloodtype] += 1
                    else:
                        BloodBanks.BloodBanks().Blood_request[city][bloodtype] = 1
                else :
                    print("No such record found for the Area")

    def Admin(self):
        ch = int(input("Enter 1 to see list of Donors, 2 to check Blood Request : "))
        
        if ch == 1:
            city = str(input("Enter City Name : "))
            if city in BloodBanks.BloodBanks().city_donor:
                print(BloodBanks.BloodBanks().city_donor[city])
            else:
                print("No such Record found for the city")
            
        elif ch ==2:
            city_ = str(input("Enter city Name to check Blood Request"))
            if city_ in BloodBanks.BloodBanks().Blood_request:
                print(BloodBanks.BloodBanks().Blood_request[city_])
            
            else:
                print("No such Record found for the city")
        else:
            print("Invalid Choice")


A = Application()
A.Log_in_options()