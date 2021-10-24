new_user = input("Enter Username: ")
insta_users = ['john1', 'elvis2', 'adam2', 'elon', 'david', 'neil', 'philips', 'Jonas']


if (new_user in insta_users):
    print("Username has taken. Please choose different username")
else:
    print("Username has Created!")
    insta_users.append(new_user)
    print(insta_users)
        



