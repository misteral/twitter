import json
import seaborn as sns
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip, mplfig_to_npimage
import numpy as np

# Load data from JSON file
with open('sample_achievements.json', 'r') as file:
    sample_data = json.load(file)
achievements_data = np.array(list(sample_data.values()))

def make_density_video(filename='output.mp4', fps=30, duration=5):
    # Use the loaded data for visualization
    data = achievements_data
    sns.set(style="whitegrid")

    def make_frame(t):
        fig, ax = plt.subplots()
        ax.hist(data, bins=30, density=True, alpha=0.75)
        ax.set_xlim(data.min(), data.max())
        # ax.set_ylim(0, None) # This line may not be necessary with hist, but can be adjusted if needed.
        plt.close(fig)
        return mplfig_to_npimage(fig)

    animation = VideoClip(make_frame, duration=duration)
    animation.write_videofile(filename, fps=fps)
if __name__ == "__main__":
    make_density_video()
