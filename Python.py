import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#Getting data from the datafile
def load_data(file_path):
    try:
        data = pd.read_csv(file_path)
        return data
    except Exception as e:
        print(f"Error loading file: {e}")
        return None

# chekcking and reading data 
def explore_data(df):
    print("\nBasic Info:")
    print(df.info())  #Writes data that are not blank fields
    
    print("\nSummary Statistics:")
    print(df.describe())  # writes a summary of the data that are numbers 
    
    print("\nMissing Values:")
    print(df.isnull().sum())  # checks if any values are missing 

    print("\nUnique values per column:")
    print(df.nunique())  # prints the number of unique values 
    
# Cleans data file by checking if values is missing 
def clean_data(df):
    
    df = df.fillna(0)  # fills missing values with 0
    
    
    df = df[df['PlayTimeHours'] > 0]  # removes data if play time is negative or zero 
    
    return df

# Manipulating the data
def manipulate_data(df):
    
    df['TotalPlayTimeMinutes'] = df['PlayTimeHours'] * 60  # Converting hours to minutes
    df['Engaged'] = df['EngagementLevel'].apply(lambda x: 1 if x == 'High' else 0)  # Binary engagement flag
    
    return df

# Visual represtation
def visualize_data(df):
    # Distribution of Play Time
    plt.figure(figsize=(10, 6))
    sns.barplot(x='Gender' ,y='AchievementsUnlocked', data=df)
    plt.title('Distribution of PlayTimeHours')
    plt.xlabel('PlayTime (hours)')
    plt.ylabel('0')
    plt.show()

    # Sessions Per Week vs Avg Session Duration
    plt.figure(figsize=(10 ,6))
    sns.scatterplot(x='SessionsPerWeek', y='AvgSessionDurationMinutes', data=df, hue='GameGenre')
    plt.title('Sessions Per Week vs Avg Session Duration')
    plt.xlabel('Sessions Per Week')
    plt.ylabel('Avg Session Duration (minutes)')
    plt.show()

# Save cleaned data to a new CSV file
def save_cleaned_data(df, output_file):
    df.to_csv(output_file, index=False)
    print(f"Cleaned data saved to {output_file}")

if __name__ == "__main__":
    # File path
    file_path = 'online_gaming_behavior_dataset.csv'  # Replace with the path to your CSV file
    output_file = 'cleaned_online_gaming_behavior_dataset.csv'

    # Load Data
    df = load_data(file_path)
    
    # Exploratory Data Analysis (EDA)
    if df is not None:
        explore_data(df)

        # Clean Data
        df_cleaned = clean_data(df)

        # Data Manipulation
        df_manipulated = manipulate_data(df_cleaned)

        # Visualize Data
        visualize_data(df_manipulated)

        # Save cleaned and manipulated data
        save_cleaned_data(df_manipulated, output_file)
