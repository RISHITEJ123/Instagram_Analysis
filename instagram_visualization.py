import json
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load JSON data
def load_analysis_results(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Convert JSON data to DataFrame
def convert_to_dataframe(follower_analysis):
    data = []
    for user, details in follower_analysis.items():
        data.append([
            user,
            len(details["following_list"]),  # Corrected: Counting elements in following list
            len(details["followers_list"]),  # Corrected: Counting elements in followers list
            details["posts_by_following"]
        ])
    return pd.DataFrame(data, columns=["Username", "Following Count", "Followers Count", "Posts by Following"])

# Plot bar chart of followers vs following count
def plot_followers_vs_following(df):
    plt.figure(figsize=(12, 6))
    sns.barplot(x="Username", y="Following Count", data=df, color="blue", label="Following")
    sns.barplot(x="Username", y="Followers Count", data=df, color="orange", label="Followers")
    
    plt.xlabel("Instagram User")
    plt.ylabel("Count")
    plt.title("Followers vs Following Count per User")
    plt.xticks(rotation=45)
    plt.legend()
    plt.show()

# Plot distribution of posts by following members
def plot_posts_distribution(df):
    plt.figure(figsize=(10, 5))
    sns.histplot(df["Posts by Following"], bins=10, kde=True, color="green")
    
    plt.xlabel("Number of Posts by Following")
    plt.ylabel("Number of Users")
    plt.title("Distribution of Posts by Following Members")
    plt.show()

# Main function
def main():
    follower_analysis = load_analysis_results("follower_analysis.json")
    df = convert_to_dataframe(follower_analysis)
    
    print(df.head())  # Display first few rows to check data
    
    # Generate plots
    plot_followers_vs_following(df)
    plot_posts_distribution(df)

if __name__ == "__main__":
    main()
