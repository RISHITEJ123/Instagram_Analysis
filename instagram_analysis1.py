import json

# Load JSON data
def load_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)

# Extract following list
def get_following_list(following_data):
    return {user["string_list_data"][0]["value"]: user["string_list_data"][0]["href"] for user in following_data["relationships_following"]}

# Extract followers list
def get_followers_list(followers_data):
    return {user["string_list_data"][0]["value"]: user["string_list_data"][0]["href"] for user in followers_data}

# Dummy function to simulate fetching post counts
def fetch_post_count(username):
    import random
    return random.randint(5, 100)  # Simulating random post count

# Analyze followers
def analyze_followers(followers, following):
    follower_data = {}
    
    for user in followers.keys():
        # Assuming all users in following are in the dataset (since JSON does not contain their followers/following lists)
        following_list = [u for u in following.keys() if u.startswith(user[:3])]  # Dummy logic for demonstration
        followers_list = [u for u in followers.keys() if u.startswith(user[:3])]  # Dummy logic for demonstration
        
        # Calculate posts made by accounts in your following list
        post_count = sum(fetch_post_count(u) for u in following_list)

        follower_data[user] = {
            "following_list": following_list,
            "followers_list": followers_list,
            "posts_by_following": post_count
        }

    return follower_data

# Main function
def main():
    following_data = load_json("following.json")
    followers_data = load_json("followers_1.json")

    following = get_following_list(following_data)
    followers = get_followers_list(followers_data)

    print(f"Total Following: {len(following)}")
    print(f"Total Followers: {len(followers)}")

    follower_analysis = analyze_followers(followers, following)

    # Save results to JSON
    with open("follower_analysis.json", "w", encoding="utf-8") as file:
        json.dump(follower_analysis, file, indent=4)

    print("Analysis saved in follower_analysis.json")

if __name__ == "__main__":
    main()
