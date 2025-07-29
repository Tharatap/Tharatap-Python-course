"""
Personal Information Manager 

#Create a tuple to store a person's basic info: (name, age, city, country)
#Create a list to store their hobbies

Allow the user to:

Display all information
Add new hobbies
Remove hobbies
Update age (by creating a new tuple)

"""
'''
# Complete this program
def personal_info_manager():
    # Create initial person tuple
    person = ("", 0, "", "")  # name, age, city, country
    hobbies = []
    
    # Your code here
    pass

if __name__ == "__main__":
    personal_info_manager()
'''
def personal_info_manager():
    person = ("Tharatap",19,"Chonburi","TH")
    hobbies = []
    while True:
        
        print("\n")
        chose = int(input("please select menu \n1.Show personal information \n2.Input hobby \n3.Delet hobbies" \
        "\n4. Edit age \n5.Exit\n Select : "))
        #ดูข้อมูล
     
        if chose == 1:
            
            print(f"Name : {person[0]}")
            print(f"Age : {person[1]}")
            print(f"City : {person[2]}")
            print(f"Contry: {person[3]}")
            print(f"hobby: {hobbies}")

        #input hobby
        elif chose == 2:
            hobby = input("What is your new hobbies: ")
            hobbies.append(hobby)
        
        # ลบข้อมูล
        elif chose == 3:
            hobbies.pop()

            
        #แปลงอายุ
        elif chose == 4:
            person_list = list(person) # แปลง tuples เป็น list เพื่อให้สามารถแก้ไขข้อมูลได้
            age = input("How old are you: ")
            person_list[1] = age
        
        elif chose == 5:
            break
        else:
            print("Error number please Select menu again")
personal_info_manager()
