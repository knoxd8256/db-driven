To_Name = input("To: \n")
To_Address_row1 = input("Address Row 1: \n")
To_Address_row2 = input("Address Row 2: \n")
To_City = input("City: \n")
To_State = input("State: \n")
To_ZIP = input("ZIP Code: \n")

From_Name = input("From: \n")
From_Address_row1 = input("Address Row 1: \n")
From_Address_row2 = input("Address Row 2: \n")
From_City = input("City: \n")
From_State = input("State: \n")
From_ZIP = input("ZIP Code: \n")

print(" ___________________________________________________________________")
print("|")
print("|", To_Name)
print("|", To_Address_row1)
if To_Address_row2:
    print("|", To_Address_row2)
print("|", To_City + ",", To_State, To_ZIP)

print("|                                        ", From_Name)
print("|                                        ", From_Address_row1)
if From_Address_row2:
    print("|                                        ", From_Address_row2)
print("|                                        ", From_City + ",", From_State, From_ZIP)
print("|___________________________________________________________________")