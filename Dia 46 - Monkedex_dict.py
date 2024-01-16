import time, os

monkedex = {}

def pretty_print(dict):
    print(f"\tName\tType\tHP\tMP\tAttack")
    for key, value in dict.items():
        print(f"{key: ^12}|{value["Type"]: ^10}|{value["HP"]: ^5}|{value["MP"]: ^5}|{value["Attack"]: ^4}")
        
    # for value in dict.values():
        # print(value, end=" | ")

while True:
    print("MonkeBeast Full-on")
    name = input("Name: ").capitalize()
    monke_type = input("Type: ").capitalize()
    move = input("Move: ").capitalize()
    hp = int(input("HP: "))
    mp = int(input("HP: "))
    monkedex[name] = {"Type": monke_type, "HP": hp, "MP": mp, "Attack": move}
    
    option = input("Another monkebeast? s/n: ").strip()
    if option[0] == "n":
        os.system("cls")
        break
    else:
        time.sleep(1)
        os.system("cls")

print("-----------------------------------------------------")
pretty_print(monkedex)
print("-----------------------------------------------------")
    