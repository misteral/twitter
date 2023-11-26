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

def visualization(df_interpolated):
    plt.figure(figsize=(10, 5))
    plt.plot(df_interpolated.index, df_interpolated['Users'], marker='o')
    plt.title('Interpolated User Data Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Users')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

def make_density_video(filename='output.mp4', fps=2, duration=5):
    # Use the loaded data for visualization
    # frames = fps * duration
    # df = interpolate_data(date_users)
    # sns.set(style="whitegrid")


    def make_frame(t):
        # Calculate the current frame number based on time and fps
        current_frame = int(t * fps)
        fig, ax = plt.subplots()

        # Ensure we do not exceed the length of the dataframe
        current_frame = min(current_frame, len(df) - 1)

        data = df.iloc[0:current_frame + 1]

        # Convert interpolated dates back to datetime for plotting
        # plot_dates = mdates.num2date(interpolated_dates[:frame_index])
        # Ensure that the length of plot_dates and the slice of interpolated_data match
        ax.plot(data.index, data['Users'], marker='', color='purple', linewidth=2)
        # # Print data for the current frame
        # print(f"Frame {frame_index}: {interpolated_data[frame_index, :frame_index]}")
        # ax.xaxis_date()  # Interpret the x-axis values as dates
        # fig.autofmt_xdate()  # Format the dates on the x-axis nicely
        # ax.set_xlim(dates[0], dates[-1])  # Set x-axis limit to show all dates
        # ax.set_ylim(0, max(data) + 10)  # Set y-axis limit
        # plt.close(fig)
        # No need to manually increment current_frame as it's calculated each time make_frame is called
        return mplfig_to_npimage(fig)

    # Remove the current_frame initialization as it's no longer needed outside make_frame
    animation = VideoClip(make_frame, duration=duration)
    animation.write_videofile(filename, fps=fps)

if __name__ == "__main__":

    df = interpolate_data(date_users)
    make_density_video()
    # visualization(df)
