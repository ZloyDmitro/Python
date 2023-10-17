global_var = ["Im a global variable"]
print(global_var)
def localFunc(global_var):
    print(id(global_var))
    global_var.append("New String")
    global_var.append([2,2,4,6])
    print(global_var)
localFunc(global_var)
print(global_var)
print(id(global_var))


def print_user_profile(gender="female", first="Jane", last="Doe", pictures=[]):
    profile_info = f"The user {first} {last} has the following pictures:"
    profile_info = profile_info + "\n common_header.png"
    print(profile_info)

    if pictures: #alternative len if let(pictures==0)
        for x in pictures:
            print(x)

test_data1 = {
    "gender": "male",
    "last": "Brown",
    "pictures": ["holidays1.png", "easter_grandma.png"]
}
test_data2 = {
    "first": "Alicia",
    "last": "Schmidt"
}
test_data3 = {
    "last": "Korkov",
    "pictures": ["sunset.png"]
}
print_user_profile(**test_data1)
print_user_profile(**test_data2)
print_user_profile(**test_data3)