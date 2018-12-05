# import sys
#
# try:
#     print(sys.argv[1])
# except IndexError:
#     print("Zapomniałeś podać nazwe pliku")

file_name =

login = {}
logout = {}
user_total_time = {}

with open(file_name) as f:
    for line in f:
        # print(i)
        line = line.split(";")
        user, action, time_str = line.spli(";")
        time = int(time)

        # user = line[0]
        # action = line[1]
        # time = line[2]
        # time = int(time)
        # print(action)
        if action == "LOGIN":
            login[user] = time
            # if login[user] != None:
            #     time = time + int(login[user])
            # login[user]=time
        #                  rozwiazanie cool:
        #     out[user] = out.get[user,0] - time



        elif action == "LOGOUT":
            # logout - login
            time_temp = time - login[user]
            user_total_time[user] = user_total_time.get(user, 0) + time_temp
            # int(logout[user])
            # logout[user]=time

            # rozwizanie cooo
            # out[user] = out.get(user, 0) + time
        return out

for user, time in user_total_time.items():
    print(f" - {user}: {time}")

print(login)
print(logout)




