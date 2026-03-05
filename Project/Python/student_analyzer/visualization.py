import pandas as pd
import matplotlib.pyplot as plt


def show_graph():

    df = pd.read_csv("students.csv")

    plt.figure(figsize=(8,5))

    plt.bar(df["Name"], df["Total"])

    plt.title("Student Total Marks Comparison")
    plt.xlabel("Students")
    plt.ylabel("Total Marks")

    plt.xticks(rotation=30)

    plt.tight_layout()

    plt.show()


def subject_graph():

    df = pd.read_csv("students.csv")

    subjects = ["Math", "Science", "English"]

    averages = [
        df["Math"].mean(),
        df["Science"].mean(),
        df["English"].mean()
    ]

    plt.bar(subjects, averages)

    plt.title("Subject Average Marks")
    plt.ylabel("Marks")

    plt.show()