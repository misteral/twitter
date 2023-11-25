import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime
import numpy as np

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
    plt.plot(dates, user_counts, color='skyblue', marker='o') # Use marker to indicate each data point on the line
    plt.xlabel('Date')
    plt.ylabel('Number of Users')
    current_date = datetime.now().strftime("%Y-%m-%d")
    plt.title(f'Twitter Achievements Visualization - {current_date}')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# Function to update the plot for each frame
def update(frame):
    plt.cla()  # Clear the current axes
    plt.plot(dates[:frame], user_counts[:frame], color='skyblue', marker='o')
    plt.xlabel('Date')
    plt.ylabel('Number of Users')
    plt.title(f'Twitter Achievements Visualization - {current_date}')
    plt.xticks(rotation=45)
    plt.tight_layout()

# Example usage:
if __name__ == '__main__':
    sample_achievements = {
        '2023-01-01': 10,
        '2023-01-02': 15,
        '2023-01-03': 5,
        '2023-01-04': 12,
        '2023-01-05': 8,
        '2023-01-06': 17
    }
    dates = np.array(list(sample_achievements.keys()), dtype='datetime64')
    user_counts = list(sample_achievements.values())
    current_date = datetime.now().strftime("%Y-%m-%d")

    fig, ax = plt.subplots(figsize=(10, 5))
    ani = FuncAnimation(fig, update, frames=len(dates), repeat=False)
    ani.save('twitter_achievement.mp4', writer='ffmpeg', fps=1)
    plt.show()
