import pickle

# Define a sample array of student objects
students = [
    {"name": "abc", "id": 123},
    {"name": "bac", "id": 321}
]

# Store the array of student objects to a file
def store_student_array(student_array, filename):
    with open(filename, 'wb') as file:
        pickle.dump(student_array, file)

# Read the array of student objects from the file
def read_student_array(filename):
    with open(filename, 'rb') as file:
        student_array = pickle.load(file)
        return student_array

# Store the array of student objects to a file
store_student_array(students, 'student_array.pkl')

# Read the array of student objects from the file
retrieved_students = read_student_array('student_array.pkl')

# Print the retrieved array of student objects
for student in retrieved_students:
    print(student)