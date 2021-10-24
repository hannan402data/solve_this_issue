new_user = input("Enter Username: ")
insta_users = ['hannan1', 'abdullah2', 'khizer4', 'saad3', 'rumesa2', 'laiba4', 'rubaina1', 'danish4']


if (new_user in insta_users):
    print("Username has taken. Please choose different username")
else:
    print("Username has Created!")
    insta_users.append(new_user)
    print(insta_users)
        



