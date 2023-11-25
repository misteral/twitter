import matplotlib.pyplot as plt

def visualize_achievement(user_achievements):
    """
    Visualize Twitter achievements using a bar chart.

    :param user_achievements: A dictionary with user names as keys and achievements as values.
    """
    # Names of users
    users = list(user_achievements.keys())
    # Corresponding achievements
    achievements = list(user_achievements.values())

    # Create a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(users, achievements, color='skyblue')
    plt.xlabel('Users')
    plt.ylabel('Achievements')
    plt.title('Twitter Achievements Visualization')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage:
# visualize_achievement({'user1': 10, 'user2': 15, 'user3': 5})
