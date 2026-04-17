#Matplotlib

import matplotlib.pyplot as plt
#students=["aasha","rohan","pooja","aayushi","namo"]
#scores=[50,70,90,80,90]
# plt.plot(students,scores)
# plt.title("Student Scores")
# plt.xlabel("Students")
# plt.ylabel("Scores")
# plt.show()


# plt.bar(students,scores)
# plt.title("Student Scores")
# plt.xlabel("Student Name")
# plt.ylabel("Score")
# plt.show()

# plt.pie(scores, labels=students, autopct="%1.1f%%")
# plt.title("Student Scores")
# plt.show()

# Create a line graph to display the marks of the following students:
# Names: Asha, Rohan, Meena, Kunal
# Marks: 70, 85, 65, 90
# Write a Python program to draw a bar chart showing student scores and add:
# Title
# X-axis label
# Y-axis label
# Using Matplotlib, draw a pie chart for the following marks:
# Math: 40
# Science: 30
# English: 20
# Computer: 10

#Names=[ "Asha", "Rohan", "Meena", "Kunal"]
#Marks=[ 70, 85, 65, 90]
# plt.plot(Names,Marks)
# plt.title("Marks")
# plt.xlabel("Names")
# plt.ylabel("Marks")
# plt.show()

# plt.bar(Names,Marks)
# plt.title( "Marks")
# plt.xlabel("Names")
# plt.ylabel("Marks")
# plt.show()

subject=["Math","Science","English","Computer"]
Marks=[40,30,20,10]
plt.pie(Marks, labels=subject, autopct="%1.1f%%")
plt.title("Subject Marks")
plt.show()












