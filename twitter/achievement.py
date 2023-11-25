import matplotlib.pyplot as plt
from datetime import datetime

def visualize_achievement(user_achievements):
    """
    Visualize Twitter achievements using a bar chart.

    :param user_achievements: A dictionary with user names as keys and achievements as values.
    """
    # Dates of achievements
    dates = list(user_achievements.keys())
    # Number of users who achieved something on that date
    user_counts = list(user_achievements.values())

    # Create a bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(dates, user_counts, color='skyblue')
    plt.xlabel('Date')
    plt.ylabel('Number of Users')
    current_date = datetime.now().strftime("%Y-%m-%d")
    plt.title(f'Twitter Achievements Visualization - {current_date}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Example usage:
if __name__ == '__main__':
    sample_achievements = {
        '2023-01-01': 10,
        '2023-01-02': 15,
        '2023-01-03': 5
    }
    visualize_achievement(sample_achievements)
