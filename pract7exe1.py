text = input("Enter the text: ")

at_count = text.count("@")
dot_count = text.count(".")
exclamation_count = text.count("!")

print("@ occurrences:", at_count)
print(". occurrences:", dot_count)
print("! occurrences:", exclamation_count)

total = at_count + dot_count + exclamation_count
print("Total special symbols:", total)