users = {}
posts = []
post_id = 1

def create_user(username, email):
    if username in users:
        return f"Error: Username '{username}' already exists!"

    users[username] = {
        "username": username,
        "email": email,
        "followers": [],
        "following": [],
        "liked_posts": []
    }
    return f"User '{username}' created successfully!"

def create_post(username, content):
    global post_id

    if username not in users:
        return f"Error: User '{username}' does not exist!"

    post = {
        "id": post_id,
        "author": username,
        "content": content,
        "timestamp": "2026-06-04 10:00:00",
        "likes": 0
    }
    posts.append(post)
    post_id += 1
    return post

def view_feed(username):
    if username not in users:
        return f"Error: User '{username}' does not exist!"
    following_list = users[username]["following"]

    if not following_list:
        return f"--- Feed for {username} ---\nYou are not following anyone yet."

    feed = f"--- Feed for {username} ---\n"
    for post in posts:
        if post["author"] in following_list:
            feed += f"Author: {post['author']}\nContent: {post['content']}\nLikes: {post['likes']}\n\n"

    return feed

def like_post(username, post_id):
    if username not in users:
        return f"Error: User '{username}' does not exist!"
    
    post_found = False
    for post in posts:
        if post["id"] == post_id:
            post_found = True
            if post_id in users[username]["liked_posts"]:
                return f"Error: {username} has already liked post {post_id}!"
            
            users[username]["liked_posts"].append(post_id)
            post["likes"] += 1
            return f"{username} liked post {post_id}!"
    
    if not post_found:
        return f"Error: Post {post_id} does not exist!"

def follow_user(username, target_username):
    if username not in users:
        return f"Error: User '{username}' does not exist!"
    
    if target_username not in users:
        return f"Error: User '{target_username}' does not exist!"
    
    if username == target_username:
        return "Error: You cannot follow yourself!"
    
    if target_username in users[username]["following"]:
        return f"Error: {username} is already following {target_username}!"
    
    users[username]["following"].append(target_username)
    users[target_username]["followers"].append(username)
    return f"{username} is now following {target_username}!"

# Menu Loop
while True:
    print("\n--- Mini Twitter Menu ---")
    print("1. Create a new user")
    print("2. Create a post")
    print("3. View feed")
    print("4. Like a post")
    print("5. Follow a user")
    print("6. Exit")
    
    choice = input("Select an option (1-6): ")
    
    if choice == "1":
        username = input("Enter username: ")
        email = input("Enter email: ")
        print(create_user(username, email))
    
    elif choice == "2":
        username = input("Enter username: ")
        content = input("Enter post content: ")
        print(create_post(username, content))
    
    elif choice == "3":
        username = input("Enter username: ")
        print(view_feed(username))
    
    elif choice == "4":
        username = input("Enter username: ")
        post_id = int(input("Enter post ID: "))
        print(like_post(username, post_id))
    
    elif choice == "5":
        username = input("Enter username: ")
        target = input("Enter username to follow: ")
        print(follow_user(username, target))
    
    elif choice == "6":
        print("Goodbye!")
        break
    
    else:
        print("Invalid option. Please select 1-6.")
