import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from dotenv import load_dotenv
import os

load_dotenv()
DATA_PATH = os.environ.get("DATA_PATH")

data = pd.read_csv(DATA_PATH)

if __name__ == "__main__":
    # plot data
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=data, x="Time", y="Percent Full", hue="Day")
    plt.title("Density Data")
    plt.xlabel("Time")
    plt.ylabel("Percent Full")
    plt.xticks(rotation=45)
    plt.show()