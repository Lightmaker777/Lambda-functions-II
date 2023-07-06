# Task 1

# Sorting list of tuples using Lambda. The sort() method of list objects has a parameter named 'key' that takes a function returning the value to use as a reference for the sorting.

subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
subject_marks.sort(key=lambda x: x[1])

print(subject_marks)
