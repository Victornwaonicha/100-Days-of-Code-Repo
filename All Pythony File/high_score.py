# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇

# Initialize a variable to store the maximum value
max_number = student_scores[n]

# Iterate through the list
for score in student_scores:
    if score > max_number:
        max_number = score

print(f"The highest score in the class is: {max_number}")