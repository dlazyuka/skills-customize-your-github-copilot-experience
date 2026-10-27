import pandas as pd
import matplotlib.pyplot as plt

DATA_FILE = "sample-data.csv"


def load_data(file_path):
    df = pd.read_csv(file_path)
    print("Original dataset:")
    print(df.head())
    return df


def clean_data(df):
    # TODO: Standardize text values and fix inconsistent entries
    # TODO: Fill or remove missing values
    # TODO: Convert columns to appropriate types
    # TODO: Remove duplicate or invalid rows
    return df


def summarize_data(df):
    # TODO: Calculate summary statistics or group data by category
    print("\nSummary:")
    print(df.describe(include="all"))


def create_visualization(df):
    # TODO: Create a chart that highlights a pattern in the cleaned data
    plt.figure(figsize=(8, 5))
    plt.title("Student Data Overview")
    plt.xlabel("Category")
    plt.ylabel("Value")
    plt.show()


def main():
    df = load_data(DATA_FILE)
    df = clean_data(df)
    summarize_data(df)
    create_visualization(df)


if __name__ == "__main__":
    main()
