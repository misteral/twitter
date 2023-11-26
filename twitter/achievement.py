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

    # print(df_interpolated)

    # Plotting the interpolated data
    plt.figure(figsize=(10, 5))
    plt.plot(df_interpolated.index, df_interpolated['Users'], marker='o')
    plt.title('Interpolated User Data Over Time')
    plt.xlabel('Date')
    plt.ylabel('Number of Users')
    plt.grid(True)
    plt.tight_layout()
    plt.show()

    # Convert string dates to datetime64 for proper sorting and plotting
    # dates = np.array(sorted(sample_achievements.keys()), dtype='datetime64')
    # user_counts = np.array([sample_achievements[str(np.datetime_as_string(date, unit='D'))] for date in dates])

    # fig, ax = plt.subplots(figsize=(10, 5))

    # ani = FuncAnimation(fig, update, frames=len(dates), repeat=False)
    # ani.save('twitter_achievement.mp4', writer='ffmpeg', fps=1)
    # plt.show()
