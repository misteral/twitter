import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
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
    if frame == 0:
        plt.plot([], [], color='skyblue', marker='o')  # Initialize an empty plot
        plt.xlabel('Date')
        plt.ylabel('Number of Users')
        plt.title(f'Twitter Achievements Visualization - {current_date}')
        plt.xticks(rotation=45)
        plt.tight_layout()
        # Set the x and y axis limits
        plt.xlim(np.datetime64(min(dates), 'D') - np.timedelta64(1, 'D'), np.datetime64(max(dates), 'D') + np.timedelta64(1, 'D'))
        plt.ylim(min(user_counts), max(user_counts))
    else:
        plt.plot(dates[:frame], user_counts[:frame], color='skyblue', marker='o')

# Example usage:
if __name__ == '__main__':
    sample_achievements = {
        '2023-11-25': 405,
        '2023-11-23': 386,
        '2023-11-22': 374,
        '2023-11-21': 240,
        '2023-11-20': 186,
        '2023-11-17': 150,
        '2023-11-15': 123,
        '2023-11-12': 99,
    }

    # Convert string dates to datetime64 for proper sorting and plotting
    dates = np.array(sorted(sample_achievements.keys()), dtype='datetime64')
    user_counts = np.array([sample_achievements[date] for date in dates])

    fig, ax = plt.subplots(figsize=(10, 5))
    ani = FuncAnimation(fig, update, frames=len(dates), repeat=False)
    ani.save('twitter_achievement.mp4', writer='ffmpeg', fps=1)
    plt.show()
