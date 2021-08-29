##Hospital vs Blood-type, donor vs city vs BLood-type 

class BloodBanks:

    hospital_bloodtype = {"Dharwad Hospital" : {"city" : "Dharwad", "A+" : 10, "A-" : 20, "B+" : 20}}
    
    city_donor = {"Dharwad" : {"Rajesh" : "A+", "Mukesh" : "O+"}}
    
    Blood_request = {"Dharwad" : {"A+" : 0, "A-" : 0, "B+" : 0, "B-" : 0, "AB+" : 0, "AB-" : 0, "O+" : 0, "O-" : 0}}
    
    BloodType_ = {'A+' : {'city' : 'Dharwad', 'stock' : 200, 'hospital' : "Dharwad Hospital"}}

    def Show_hospital_bloodtype(self):
        Hospital = str(input("Enter Hospital Name to see Blood Availability : "))
        if Hospital in self.hospital_bloodtype:
            print(self.hospital_bloodtype[Hospital])
            return
        else:
            print("No such record found!")
            return
    
    def show_city_donor(self):
        city = str(input("Enter City Name to check Blood Availability : "))
        if city in self.city_donor:
            print(self.city_donor[city])
            return
        else:
            print("No such Record found!")
            return

    def Add_hospital(self):
        hospital = str(input("Enter Hospital Name : "))
        city = str(input("Enter City : "))
        print("Enter total stock")
        A = int(input("A+ : "))
        A_ = int(input("A- : "))
        B = int(input("B+ : "))
        B_ = int(input("B- : "))
        AB = int(input("AB+ : "))
        AB_ = int(input("AB- : "))
        O = int(input("O+ : "))
        O_ = int(input("O- : "))
        self.hospital_bloodtype[hospital]["city"] = city
        self.hospital_bloodtype[hospital]["A"] = A
        self.hospital_bloodtype[hospital]["A-"] = A_
        self.hospital_bloodtype[hospital]["B"] = B
        self.hospital_bloodtype[hospital]["B-"] = B_
        self.hospital_bloodtype[hospital]["AB+"] = AB
        self.hospital_bloodtype[hospital]["AB-"] = AB_
        self.hospital_bloodtype[hospital]["O+"] = O
        self.hospital_bloodtype[hospital]["O-"] = O_
        return

    def BloodRequest(self, bloodType):
        if bloodType in self.Blood_request:
            if self.BloodType_[bloodType]['stock'] == 0:
                print("Sorry, Currently out of stock")
                return 0
            else:
                print("Stock : ", self.BloodType_[bloodType])
                return 1
    
    def show_bloodRequest(self):
        print("Total Blood Request from all Registred city : ")
        print(self.Blood_request)
        return

    def show_bloodType_details(self, blood_type):
        if self.BloodType_[blood_type]['stock'] == 0:
            print("Sorry, Currently We are Out of stock")
            return 0
        else:
            print(self.BloodType_[blood_type])
            return 1