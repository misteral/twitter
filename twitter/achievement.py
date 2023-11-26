import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from datetime import datetime, timedelta
import numpy as np
import seaborn as sns
import pandas as pd


def interpolate_data(date_users):
    """
    Interpolate missing dates and round values to the nearest whole number.

    :param date_users: Dictionary with dates as keys and user counts as values.
    :return: DataFrame with interpolated and rounded values.
    """
    df = pd.DataFrame(list(date_users.items()), columns=['Date', 'Users'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    df_resampled = df.resample('D').asfreq()  # Создание пропущенных дат
    return df_resampled.interpolate(method='time').round(0)  # Интерполяция значений и округление до целых чисел

# Function to update the plot for each frame
def update(frame):
    if frame == 0:
        plt.plot([], [], color='skyblue', marker='o')  # Initialize an empty plot
        plt.xlabel('Date')
        plt.ylabel('Number of Users')
        plt.title(f'Twitter Achievements Visualization - {current_date}')
        plt.xticks(rotation=45)
        # plt.tight_layout()
        # Set the x and y axis limits
        # plt.xlim(np.datetime64(min(dates), 'D') - np.timedelta64(1, 'D'), np.datetime64(max(dates), 'D') + np.timedelta64(1, 'D'))
        # plt.ylim(min(user_counts), max(user_counts))
    else:
        plt.plot(dates[:frame], user_counts[:frame], color='skyblue', marker='o')


# Example usage:
if __name__ == '__main__':
    # Define current_date at the module level
    current_date = datetime.now().strftime("%Y-%m-%d")

    date_users = {
        '2023-11-25': 405,
        '2023-11-23': 386,
        '2023-11-22': 374,
        '2023-11-21': 240,
        '2023-11-12': 99,
    }

    df_interpolated = interpolate_data(date_users)

    # Create the figure for the animation
    fig, ax = plt.subplots(figsize=(10, 5))

    # Create the animation
    ani = FuncAnimation(fig, update, frames=len(df_interpolated), repeat=False)
    ani.save('twitter_achievement.mp4', writer='ffmpeg', fps=1)
    plt.show()

