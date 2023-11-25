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
# Convert dates from string to datetime objects and sort them
dates = [datetime.strptime(date, "%Y-%m-%d") for date in sample_data.keys()]
dates, achievements_data = zip(*sorted(zip(dates, sample_data.values())))

def make_density_video(filename='output.mp4', fps=30, duration=5):
    # Use the loaded data for visualization
    data = np.array(achievements_data)
    sns.set(style="whitegrid")

    def make_frame(t):
        fig, ax = plt.subplots()
        ax.bar(dates, data, width=0.8, align='center', alpha=0.75)
        ax.xaxis_date()  # Interpret the x-axis values as dates
        fig.autofmt_xdate()  # Format the dates on the x-axis nicely
        ax.set_ylim(0, max(data) + 10)  # Set y-axis limit
        plt.close(fig)
        return mplfig_to_npimage(fig)

    animation = VideoClip(make_frame, duration=duration)
    animation.write_videofile(filename, fps=fps)
if __name__ == "__main__":
    make_density_video()
