# List Array

# student_list = ['Manish', 'Sudip','Swarnim', 'Atut']
# student_set = {'Ram', 'Shyam'}
# student_dict = {'name':'Ram', 'age': 25}
# for i in range(len(student_list)):
#     print(student_list[i])
# student_list.append("Ram")
# print(student_list)
# student_set.add('Manish')
# print(student_set)
# for i in student_dict:
#     print(i, '--',student_dict[i])


# #check if the given username exists?

# user1 = [
#     ['Ram', 'ram123', '12345'],
#     ['Shyam', 'shyam', '54321'],
#     ['hari', 'Hari', '1111'],
# ]
# un = input('Enter username')

# for i in user1:
#     if un in i:
#         print('sucessful')
#         break
# else:
#     print('username not correct')
user: [
    {'name': 'Ram', 'username': 'ram123', 'password': '123'},
    {'name': 'Shyam', 'username': 'Shyam123', 'password': '123'},
    ]
um = input('Enter username')
pw = input('Enter password')
for i in user:
    if um == i['username']:
        if pw == i['password']:
            print("you are logged in")
        else:
            print('wrong credentials')
        break
else:
    print('Doesnt exist')

