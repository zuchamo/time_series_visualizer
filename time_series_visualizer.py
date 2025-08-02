import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the data
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Clean by removing top and bottom 2.5%
low_cut = df["value"].quantile(0.025)
high_cut = df["value"].quantile(0.975)
df_clean = df[(df["value"] >= low_cut) & (df["value"] <= high_cut)]

def draw_line_plot():
    fig, ax = plt.subplots(figsize=(14, 6))
    ax.plot(df_clean.index, df_clean["value"], color="red", linewidth=1)
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    fig.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    df_bar = df_clean.copy()
    df_bar["year"] = df_bar.index.year
    df_bar["month"] = df_bar.index.month_name()

    df_pivot = df_bar.pivot_table(
        values="value", index="year", columns="month", aggfunc="mean"
    ).reindex(columns=[
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ])

    fig = df_pivot.plot(kind="bar", figsize=(12, 8)).figure
    plt.xlabel("Years")
    plt.ylabel("Average Page Views")
    plt.legend(title="Months")
    fig.savefig("bar_plot.png")
    return fig

def draw_box_plot():
    df_box = df_clean.copy().reset_index()
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime('%b')
    df_box["month_num"] = df_box["date"].dt.month
    df_box = df_box.sort_values("month_num")

    fig, axes = plt.subplots(1, 2, figsize=(16, 6))
    sns.boxplot(x="year", y="value", data=df_box, ax=axes[0])
    axes[0].set_title("Year-wise Box Plot (Trend)")
    axes[0].set_xlabel("Year")
    axes[0].set_ylabel("Page Views")

    sns.boxplot(x="month", y="value", data=df_box, ax=axes[1])
    axes[1].set_title("Month-wise Box Plot (Seasonality)")
    axes[1].set_xlabel("Month")
    axes[1].set_ylabel("Page Views")

    fig.savefig("box_plot.png")
    return fig
