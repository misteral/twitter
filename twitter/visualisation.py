import seaborn as sns
import matplotlib.pyplot as plt
from moviepy.editor import VideoClip
import numpy as np

def make_density_video(data, filename='output.mp4', fps=30, duration=5):
    sns.set(style="whitegrid")

    def make_frame(t):
        fig, ax = plt.subplots()
        sns.kdeplot(data, ax=ax, bw_adjust=t/duration + 0.1)
        ax.set_xlim(data.min(), data.max())
        ax.set_ylim(0, None)
        plt.close(fig)
        return mplfig_to_npimage(fig)

    animation = VideoClip(make_frame, duration=duration)
    animation.write_videofile(filename, fps=fps)
