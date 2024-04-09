
# # Define a list of student records
# student_records = [
#     {"name": "Alice", "grade": 85},
#     {"name": "Bob", "grade": 91},
#     {"name": "Charlie", "grade": 78},
#     {"name": "David", "grade": 95},
#     {"name": "Eve", "grade": 88}
# ]

# # min function


# def min_grade(records):
#     if not records:
#         return None
#     min_record = records[0]
#     for record in records:
#         if record["grade"] < min_record["grade"]:
#             min_record = record
#     return min_record

# # max function


# def max_grade(records):
#     if not records:
#         return None
#     max_record = records[0]
#     for record in records:
#         if record["grade"] > max_record["grade"]:
#             max_record = record
#     return max_record

# # findgt function (find greater than)


# def find_gt(records, threshold):
#     result = []
#     for record in records:
#         if record["grade"] > threshold:
#             result.append(record)
#     return result

# # findlt function (find less than)


# def find_lt(records, threshold):
#     result = []
#     for record in records:
#         if record["grade"] < threshold:
#             result.append(record)
#     return result


# # Test the functions
# print("Minimum grade:")
# print(min_grade(student_records))

# print("\nMaximum grade:")
# print(max_grade(student_records))

# print("\nStudents with grades greater than 85:")
# print(find_gt(student_records, 85))

# print("\nStudents with grades less than 80:")
# print(find_lt(student_records, 80))


# Define a list of student records
student_records = [
    {"name": "Alice", "grade": 85},
    {"name": "Bob", "grade": 91},
    {"name": "Charlie", "grade": 78},
    {"name": "David", "grade": 95},
    {"name": "Eve", "grade": 88}
]

# Sort the student records based on grades (in descending order)
sorted_records = []
for record in student_records:
    if not sorted_records:
        sorted_records.append(record)
    else:
        for i, sorted_record in enumerate(sorted_records):
            if record["grade"] > sorted_record["grade"]:
                sorted_records.insert(i, record)
                break
        else:
            sorted_records.append(record)

# Display the sorted student records
for record in sorted_records:
    print(f"Name: {record['name']}, Grade: {record['grade']}")
