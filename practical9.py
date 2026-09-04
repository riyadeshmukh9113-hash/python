# Student Marks Management System

marks = [70, 80, 65, 90]

# Display marks - Traversal
print("Original Marks:")
for mark in marks:
    print(mark)

# Insert a new mark
marks.insert(2, 75)

print("\n After Insertion:")
print(marks)

# Update a mark
marks[1] = 85

print("\n After Updating:")
print(marks)

# Delete a mark
marks.remove(65)

print("\n After Deletion:")
print(marks)