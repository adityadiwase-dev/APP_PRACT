with open(r"F:\MIT-ADT\SEM3\APP\Codes\data.txt", "r") as file:
    lines = file.readlines()

print("Total number of lines:", len(lines))

first_two = lines[:2]

with open(r"F:\MIT-ADT\SEM3\APP\Codes\output.txt", "w") as file:
    file.writelines(first_two)

print("First two lines:")
print(first_two)

print("Data written to output.txt")
