# Karvand_manager menue
import json
import os
path='data/karvands.json'
# Function for load json file and read it
def load_data():
    # creat data folder
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(path):
        data={
            "Bootcamp":{
                "title":"karvand Python",
                "year": 2026
            },
            "karvands":[]
        }
        save_data(data)
        return data
    with open (path,"r",encoding="utf-8") as file:
        return json.load(file)

def save_data(data):
    with open(path,"w",encoding="utf-8") as file:
        json.dump(data,file, ensure_ascii=False,indent=4)
    
def education_data ():
    degree=input("What is your education degree?\n")
    field=input("What is your fiels of study?")
    return {
        "degree":degree,
        "field":field
    }

def skills_data():
    skills=[]

    while True:
        name=input("Enter your skill name:(name or done) \n")
        if name.lower() =="done":
            break
        elif name.strip()=="":
            print("Name can not be empty")
            continue

        level=input("Enter the level of experties:\n ")
        while True:
            try:
                score=float(input("What is you score in this skill?\n"))
                if 0<=score<=100:
                    break
                print("The score is in appropriatr range (0-100)")

            except ValueError:
                print("Enter a valid number!")
        skills.append({
            "name":name,
            "level":level,
            "score":score
        })
    return skills

def add_karvand():
    data=load_data()
    id_max=0
    for karvand in data["karvands"]:
        if karvand["id"]>id_max:
            id_max=karvand["id"]
    karvand_id=id_max+1
    full_name=input("Enter your full name:\n")
    email_adress=input("Enter your email address:\n")
    city=input("Where do you live?\n")
    education=education_data()
    karvand_skills=skills_data()
    karvand={
        "id":karvand_id,
        "full_name":full_name,
        "email":email_adress,
        "city":city,
        "education":education,
        "skills":karvand_skills
    }
    data["karvands"].append(karvand)
    save_data(data)
    print(f"Karvand added, the id is {karvand_id}")

def karvands_info():
    data=load_data()
    if data["karvands"]==[]:
        print("The list is empty!")
        return
    for karvand in data["karvands"]:
        print("Karvand's id:", karvand["id"])
        print("Karvand's name:", karvand["full_name"])
        print("Email address:", karvand["email"])
        print("City:", karvand["city"])
        print("Degree of education:", karvand["education"]["degree"])
        print("Field of study:", karvand["education"]["field"])

        print("Skills:")
        for skill in karvand["skills"]:
            print("Skill name:" , skill['name'])
            print("Level:" , skill['level'])
            print("score:" , skill['score'])
            print("____________________\n")
        print("_______________________________________\n")

def edit_information():
    data=load_data()
    which_id=int(input("Do you want to change which id?\n"))
    all_id=[]
    for karvand in data["karvands"]:
        all_id.append(karvand["id"])

    if which_id not in all_id:
            print("This id is not valid!")
            return
    for karvand in data["karvands"]:
        if karvand["id"]==which_id:
            change=input("What do you want to change?\npress 1 for name.\npress 2 for email.\n press 3 for city.\npress 4 for education.\npress 5 for skills.")
            if change=="1":
                new_name=input("Enter the full name:\n")
                karvand["full_name"]=new_name
            elif change=="2":
                new_email=input("Enter the email:\n")
                karvand["email"]=new_email
            elif change=="3":
                new_city=input("Enter the city:\n")
                karvand["city"]=new_city
            elif change=="4":
                choice=input("Do you want to change degree or field? ")
                try:
                    if choice=="degree":
                        new_degree=input("Enter the degree:\n")
                        karvand["education"]["degree"]=new_degree
                    if choice=="field":
                        new_field=input("Enter the field:\n")
                        karvand["education"]["field"]=new_field
                except ValueError:
                    print("Enter a correct value!")
            elif change=="5":
                user_choice=input("Do you want to change all skills? (y/n)\n")
                try:
                    if user_choice=="y":
                        karvand["skills"]=skills_data()
                    if user_choice=="n":
                        user_ch=input(f"press 1 if you want to change the information about a specific skill.\n")
                        if user_ch=="1":
                            old=[]
                            old_skill=input("Enter your old skill's name:\n")
                            for choice in karvand["skills"]:
                                old.append(choice["name"])
                            if old_skill not in old:
                                print("Invalid input!")
                                return
                            for choice in karvand["skills"]:
                                if old_skill==choice["name"]:
                                    new_skill=input("Enter your new skill:\n")
                                    choice["name"]=new_skill
                                    other_choice=input("Do you want to change level and score?(press1)\n")
                                    if other_choice=="1":
                                        new_level=input("Enter your new level")
                                        new_score=float(input("Enter your new score"))
                                        choice["level"]=new_level
                                        choice["score"]=new_score                
                except ValueError:
                    print("Invalid input!")
            save_data(data)
            print("The information was updated!")
            return

def delet_function(id):
    data=load_data()
    for karvand in data["karvands"]:
        if karvand["id"]==id:
            data["karvands"].remove(karvand)
            save_data(data)
            print(f"Karvand with this id, {id} was removed!")
            return

def general_report():
    data=load_data()
    counter=0
    for karvand in data["karvands"]:
        counter=counter+1
    print(f"This bootcamp has {counter} of Karvands.")


while True:
    user_choice=input("Please press one of the keeys blow to do what you want.\nPress 1 to add karvand.\nPress 2 to show karvand.\nPress 3 to edit karvand.\nPress 4 to delete karvand.\nPress 5 to get report.\nPress 6 to exit.")
    if user_choice=="1":
        add_karvand()
    elif user_choice=="2":
        karvands_info()
    elif user_choice=="3":
        edit_information()
    elif user_choice=="4":
        user_id=int(input("Enter the id you want to delet.\n"))
        delet_function(user_id)
    elif user_choice=="5":
        general_report()
    elif user_choice=="6":
        break
    else:
        print("Invalid input!")
    

    
        
