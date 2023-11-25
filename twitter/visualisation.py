import json
import seaborn as sns
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
from moviepy.video.io.bindings import mplfig_to_npimage
import numpy as np

import matplotlib.dates as mdates
from datetime import datetime

# Load data from JSON file
with open('sample_achievements.json', 'r') as file:
    sample_data = json.load(file)
# Convert dates from string to datetime objects, sort them and interpolate
dates = [datetime.strptime(date, "%Y-%m-%d") for date in sample_data.keys()]
dates, achievements_data = zip(*sorted(zip(dates, sample_data.values())))
# Convert dates to matplotlib date format for interpolation
mpl_dates = mdates.date2num(dates)

def make_density_video(filename='output.mp4', fps=10, duration=5):
    # Use the loaded data for visualization
    data = np.array(achievements_data)
    sns.set(style="whitegrid")

    # Calculate the number of frames
    num_frames = duration * fps
    # Create arrays to store interpolated data
    interpolated_data = np.zeros((num_frames, len(data)))
    interpolated_dates = np.zeros(num_frames)

    # Generate time points for original and interpolated data
    original_time_points = np.linspace(0, 1, len(data))
    interpolated_time_points = np.linspace(0, 1, num_frames)

    # Interpolate data and dates for the graph that changes from left to right
    for i, t in enumerate(interpolated_time_points):
        interpolated_data[i] = np.interp(t, original_time_points, data)
        interpolated_dates[i] = np.interp(t, original_time_points, mpl_dates)

    def make_frame(t):
        frame_index = int(t * fps)
        fig, ax = plt.subplots()
        # Convert interpolated dates back to datetime for plotting
        plot_dates = mdates.num2date(interpolated_dates[:frame_index])
        # Ensure that the length of plot_dates and the slice of interpolated_data match
        ax.plot(plot_dates, interpolated_data[:frame_index + 1, frame_index], marker='', color='purple', linewidth=2)
        # Print data for the current frame
        print(f"Frame {frame_index}: {interpolated_data[frame_index, :frame_index]}")
        ax.xaxis_date()  # Interpret the x-axis values as dates
        fig.autofmt_xdate()  # Format the dates on the x-axis nicely
        ax.set_xlim(dates[0], dates[-1])  # Set x-axis limit to show all dates
        ax.set_ylim(0, max(data) + 10)  # Set y-axis limit
        plt.close(fig)
        return mplfig_to_npimage(fig)

    animation = VideoClip(make_frame, duration=duration)
    animation.write_videofile(filename, fps=fps)
if __name__ == "__main__":
    make_density_video()
