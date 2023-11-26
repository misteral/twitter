import json
import seaborn as sns
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
import numpy as np

import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

# Load data from JSON file
with open('/Users/aleksandrbobrov/data/agents/twitter/twitter/sample_achievements.json', 'r') as file:
    date_users = json.load(file)

current_index = 0

def interpolate_data(date_users):
    """
    Interpolate missing dates in the dataset and round user counts to the nearest whole number.

    Args:
        date_users (dict): A dictionary with dates as keys and user counts as values.

    Returns:
        pandas.DataFrame: A DataFrame with dates as the index, interpolated and rounded user counts.
    """
    """
    Interpolate missing dates and round values to the nearest whole number.

    :param date_users: Dictionary with dates as keys and user counts as values.
    :return: DataFrame with interpolated and rounded values.
    """
    df = pd.DataFrame(list(date_users.items()), columns=['Date', 'Users'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    df_resampled = df.resample('4H').asfreq()  # Создание пропущенных дат
    return df_resampled.interpolate(method='time').round(0)  # Интерполяция значений и округление до целых чисел

def fps(duration):
    """
    Calculate the frames per second for the video based on the duration and the number of data points.

    Args:
        duration (int): The duration of the video in seconds.

    Returns:
        int: The number of frames per second.
    """
    return int(len(df)/duration)

def make_frame(t):
    """
    Generate a frame for the video at time t.

    Args:
        t (float): The time at which to generate the frame.

    Returns:
        numpy.ndarray: An image array representing the current frame.
    """
    global current_index

    sns.set(style="whitegrid")  # Set the seaborn style
    fig, ax = plt.subplots(figsize=(12, 6))
    plt.xticks(rotation=45)

    # Ensure we do not exceed the length of the dataframe
    data = df.iloc[0:current_index + 1]
    current_index = min(current_index + 1, len(df) - 1)

    # Initialize an empty plot with seaborn lineplot for better visuals
    sns.lineplot(data=df.iloc[0:0], x='Date', y='Users', ax=ax, color='skyblue', marker='o', linewidth=2.5)

    # Update plot with the current data
    sns.lineplot(data=data, x=data.index, y='Users', ax=ax, color='purple', marker='o', linewidth=2.5)

    # Set the title and labels with larger fonts
    ax.set_title(f'Twitter User Growth Visualization - {current_date}', fontsize=18, fontweight='bold')
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Number of Users', fontsize=14)

    # Improve the time representation on x-axis
    ax.xaxis.set_major_locator(mdates.DayLocator(interval=1))
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
    plt.xticks(rotation=45)

    # Set the x and y axis limits
    ax.set_xlim(min(df.index) - pd.Timedelta(days=1), max(df.index) + pd.Timedelta(days=1))
    ax.set_ylim(0, max(df['Users']) + 100)

    plt.tight_layout()
    return mplfig_to_npimage(fig)


def make_density_video(filename='output.mp4'):
    """
    Create a density plot video of Twitter user growth over time.

    Args:
        filename (str, optional): The name of the output video file. Defaults to 'output.mp4'.
    """
    # Use the loaded data for visualization
    # Remove the current_frame initialization as it's no longer needed outside make_frame
    animation = VideoClip(make_frame, duration=duration)
    animation.write_videofile(filename, fps=fps)

if __name__ == "__main__":
    current_date = datetime.now().strftime("%Y-%m-%d")
    df = interpolate_data(date_users)
    duration = 5
    fps = len(df)/duration
    # print(df)
    make_density_video()
    # visualization(df)
