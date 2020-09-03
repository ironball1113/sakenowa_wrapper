import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sakenowa_wrapper import SakenowaAPI


sakenowa_flavor_charts = SakenowaAPI("flavor-charts")
dic = sakenowa_flavor_charts.make_dic()
df_copy = sakenowa_flavor_charts.set_df(dic).copy()

col_rename = {
    "f1": "Fruity",
    "f2": "Mellow",
    "f3": "Heavy",
    "f4": "Mild",
    "f5": "Dry",
    "f6": "Light",
}


brand_id = 2
renamed_cols = list(df_copy.rename(columns=col_rename).columns)[1:]
flavor_values = df_copy.query("brandId == @brand_id").values.tolist()[0][1:]


def plot_polar(labels, values, imgname):
    angles = np.linspace(0, 2 * np.pi, len(labels) + 1, endpoint=True)
    values = np.concatenate((values, [values[0]]))
    fig = plt.figure()
    ax = fig.add_subplot(111, polar=True)
    ax.plot(angles, values, "o-")
    ax.fill(angles, values, alpha=0.25)
    ax.set_thetagrids(angles[:-1] * 180 / np.pi, labels)
    fig.savefig(imgname)
    plt.close(fig)


plot_polar(renamed_cols, flavor_values, "flavor.png")
