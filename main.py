# Student Marks Visualization

import csv
import matplotlib.pyplot as plt

names = []
marks = []

with open("marks.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        names.append(row["name"])
        marks.append(int(row["marks"]))

plt.bar(names, marks)
plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Student Marks Visualization")

plt.show()
