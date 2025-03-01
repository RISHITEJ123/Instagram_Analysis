import json

# Load JSON data
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Extract following list
def get_following_list(following_data):
    return set(user["string_list_data"][0]["value"] for user in following_data["relationships_following"])

# Extract followers list
def get_followers_list(followers_data):
    return set(user["string_list_data"][0]["value"] for user in followers_data)

# Get mutual followers
def get_mutual_followers(following, followers):
    return following.intersection(followers)

# Dummy function to simulate fetching user details (replace with actual API calls if needed)
def fetch_follower_details(username):
    import random
    return {
        "following_count": random.randint(50, 1000),  # Simulating random following count
        "followers_count": random.randint(100, 5000),  # Simulating random follower count
        "posts_count": random.randint(5, 100)  # Simulating random post count
    }

# Analyze followers' details
def analyze_followers(mutual_followers):
    follower_data = {}
    for user in mutual_followers:
        details = fetch_follower_details(user)
        follower_data[user] = {
            "following_count": details["following_count"],
            "followers_count": details["followers_count"],
            "posts_count": details["posts_count"]
        }
    return follower_data

# Sort by number of followers
def sort_by_followers(follower_data):
    return sorted(follower_data.items(), key=lambda x: x[1]["followers_count"], reverse=True)

# Filter accounts with most posts
def filter_top_posters(follower_data, top_n=5):
    return sorted(follower_data.items(), key=lambda x: x[1]["posts_count"], reverse=True)[:top_n]

# Calculate average followers
def calculate_average_followers(follower_data):
    total_followers = sum(data["followers_count"] for data in follower_data.values())
    return total_followers / len(follower_data) if follower_data else 0

# Identify trends (basic insights)
def identify_trends(follower_data):
    avg_followers = calculate_average_followers(follower_data)
    high_followers = [user for user, data in follower_data.items() if data["followers_count"] > avg_followers]
    return {
        "average_followers": avg_followers,
        "top_followed_accounts": high_followers
    }

# Main function
def main():
    following_data = load_json("following.json")
    followers_data = load_json("followers_1.json")

    following = get_following_list(following_data)
    followers = get_followers_list(followers_data)

    print(f"Total Following: {len(following)}")
    print(f"Total Followers: {len(followers)}")

    mutual_followers = get_mutual_followers(following, followers)
    print(f"Mutual Followers: {len(mutual_followers)}")

    follower_analysis = analyze_followers(mutual_followers)

    sorted_followers = sort_by_followers(follower_analysis)
    top_posters = filter_top_posters(follower_analysis)
    avg_followers = calculate_average_followers(follower_analysis)
    trends = identify_trends(follower_analysis)

    # Save results to JSON
    with open("follower_analysis.json", "w", encoding="utf-8") as file:
        json.dump({
            "sorted_followers": sorted_followers,
            "top_posters": top_posters,
            "average_followers": avg_followers,
            "trends": trends
        }, file, indent=4)

    print("Analysis saved in follower_analysis.json")

if __name__ == "__main__":
    main()
