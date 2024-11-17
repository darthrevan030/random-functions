word = input()

count_o = word.count("o")
count_z = word.count("z")

if 2 * count_z == count_o:
    print("Yes")
else:
    print("No")