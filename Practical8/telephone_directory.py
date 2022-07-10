# Program to make telephone directory 

def find_num(name):
    print(name, ":", d[name])

def replace_num(name, num):
    d[name] = num
    print("Directory is updated\n", name, ":", d[name])

def replace_name(name, num):
    for key, value in d.items():
        if num == value:
            d[name] = d[key]
            del d[key]
            break
    print("Directory is updated\n", name, ":", d[name])

d = {'Rohit':  4536752067,
     'Tanu': 6956542475,
     'Raj':  5439627979,
     'Prathamesh': 4857952545,
     'Sahil':  6890392545,
     }

find_num('Raj')
replace_num('Ash', 9546776254)
replace_name('Sid', 5439627979)