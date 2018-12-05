import sys

# try:
#      print(sys.argv[1])
# except IndexError:
#      print("Zapomniałeś podać nazwe pliku")

_, file_in, file_out = sys.argv

lista=[]

with open(file_in) as f:
    unique_email = set()
    for line in f:
        line = line.lower()
        for i in line:
            if i == " ":
                line = line.strip(" ")
                # print(line)

    # @
        if line.count("@") == 1:
            unique_email.add(line)

        # lista += line
        # print(lista)

emails = sorted(unique_email)

with open(file_out, "w") as f:
    for email in emails:
        f.write(email + "\n")
print(file_out)

