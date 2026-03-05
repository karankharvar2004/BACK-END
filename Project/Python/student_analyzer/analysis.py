import pandas as pd
import numpy as np


def analyze_data():

    df = pd.read_csv("students.csv")

    # Show all student data
    print("\nStudent Data:")
    print(df.to_string(index=False))

    print("\n========== CLASS STATISTICS ==========")
    print("Average Marks:", np.mean(df["Average"]))
    print("Highest Marks:", np.max(df["Total"]))
    print("Lowest Marks:", np.min(df["Total"]))
    print("======================================")

def search_student():

    roll = input("Enter roll number: ")

    df = pd.read_csv("students.csv")

    result = df[df["Roll"].astype(str) == roll]

    if not result.empty:
        print("\nStudent Found:")
        print(result.to_string(index=False))    
    else:
        print("Student not found")


def find_topper():

    df = pd.read_csv("students.csv")

    topper = df.loc[df["Total"].idxmax()]

    print("\n🏆 Class Topper")
    print(topper.to_string())

def show_ranking():

    import pandas as pd

    df = pd.read_csv("students.csv")

    # Sort students by total marks
    df = df.sort_values(by="Total", ascending=False)

    # Create ranking column
    df["Rank"] = range(1, len(df) + 1)

    print("\n========== STUDENT RANKINGS ==========")
    print(df[["Rank", "Name", "Total"]].to_string(index=False))
    print("======================================")