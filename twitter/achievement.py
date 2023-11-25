import matplotlib.pyplot as plt
from datetime import datetime

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
    current_date = datetime.now().strftime("%Y-%m-%d")
    plt.title(f'Twitter Achievements Visualization - {current_date}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage:
if __name__ == '__main__':
    sample_achievements = {'user1': 10, 'user2': 15, 'user3': 5}
    visualize_achievement(sample_achievements)
