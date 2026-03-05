import csv
import os

def save_student(student):

    file_exists = os.path.isfile("students.csv")

    with open("students.csv", "a", newline="") as file:

        writer = csv.writer(file)

        # create header if file doesn't exist
        if not file_exists:
            writer.writerow([
                "Name","Roll","Math","Science","English","Total","Average","Grade"
            ])

        writer.writerow([
            student.name,
            student.roll,
            student.marks[0],
            student.marks[1],
            student.marks[2],
            student.total(),
            student.average(),
            student.grade()
        ])