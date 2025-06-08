# with open("sample.txt","r") as file:
#     for line in file:
#         print(line)
# with open("sample.txt","r") as f:
#     for _ in range(3):
#         print(f.readline().strip())


# with open("sample.txt","r") as file:
#
#     #print(file.readlines()) #.readline() will return a list of line in the file
#
#     for i in file.readlines()[1:]:
#         print(i.strip())

# with open("feedback.txt","a") as f:
#     f.write(input("enter a feedback here:"))


with open("sample.txt","r") as f:

    while True:
        line = f.readline()

        if not line:
            break
        print(line.strip())

