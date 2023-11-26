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
    Interpolate missing dates and round values to the nearest whole number.

    :param date_users: Dictionary with dates as keys and user counts as values.
    :return: DataFrame with interpolated and rounded values.
    """
    df = pd.DataFrame(list(date_users.items()), columns=['Date', 'Users'])
    df['Date'] = pd.to_datetime(df['Date'])
    df.set_index('Date', inplace=True)
    df.sort_index(inplace=True)
    df_resampled = df.resample('12H').asfreq()  # Создание пропущенных дат
    return df_resampled.interpolate(method='time').round(0)  # Интерполяция значений и округление до целых чисел

def visualization(df_interpolated):
    plt.figure(figsize=(10, 5))
    plt.plot(df_interpolated.index, df_interpolated['Users'], marker='o')
    plt.title('Interpolated User Data Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Users')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def fps(duration):
    return int(len(df)/duration)

def make_frame(t):
    global current_index
    # Calculate the current frame number based on time and fps
    # print(f"current_t: {t}")
    # print(f"current_index: {current_index}")

    fig, ax = plt.subplots()

    # Ensure we do not exceed the length of the dataframe

    data = df.iloc[0:current_index + 1]

    if current_index > len(df):
        current_index = min(current_index, len(df) - 1)
    else:
        current_index = current_index + 1
    # if current_frame == 0:
    plt.plot([], [], color='skyblue', marker='o')  # Initialize an empty plot
    plt.xlabel('Date')
    plt.ylabel('Number of Users')
    plt.title(f'Twitter Achievements Visualization - {current_date}')
    plt.xticks(rotation=45)
    plt.tight_layout()

    # Set the x and y axis limits
    plt.xlim(min(df.index) - pd.Timedelta(days=1), max(df.index) + pd.Timedelta(days=1))
    plt.ylim(0, max(df['Users']+100))
    # else:
    plt.plot(data.index, data['Users'], marker='', color='purple', linewidth=2)

    return mplfig_to_npimage(fig)


def make_density_video(filename='output.mp4'):
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
