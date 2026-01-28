name = input ("enter the full name : ")

emailID = input ("enter the email ID : ")

mobile_number = input ("enter mobile number : ")

age = int(input ("enter age : "))

if name[0]!= " " and name [len(name)-1] != " " and name.count(" ") >=1 and " "in name:

    if emailID.count("@") >=1 and emailID.count(".") >=1 and emailID[0] != '@':

        if mobile_number[0] !="0" and mobile_number.isdigit() and len(mobile_number)==10 :

            if age>=18 and age<=60 :

                print ("User profile is VALID")

            else:
                print ("User profile is INVALID")

        else:
            print ("User profile is INVALID")

    else:
        print ("User profile is INVALID")

else:
    print ("User profile is INVALID")
