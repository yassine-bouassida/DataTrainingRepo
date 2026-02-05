import base64
import io
import sqlite3

import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

from utils import get_sqlite_path

st.set_page_config(page_title="Visualization Lab", page_icon="🎨", layout="wide")

st.title("Visualization Lab")
st.caption("Step 4: Visualize data from the database.")

db_path = get_sqlite_path()
conn = sqlite3.connect(db_path)

try:
    df = pd.read_sql_query("SELECT * FROM demo_data", conn)
finally:
    conn.close()

if df.empty:
    st.warning("Database is empty. Load data in SQLite Explorer first.")
    st.stop()

st.write("Preview")
st.dataframe(df.head(20), use_container_width=True)

chart_type = st.selectbox(
    "Chart type",
    ["Line", "Bar", "Scatter", "Histogram", "Box", "Moving Average", "Cumulative Sum"],
)

# Filter groups for charts where it makes sense.
groups_all = sorted(df["group_name"].unique())
enable_group_filter = chart_type in ["Line", "Bar", "Scatter", "Box"]
selected_groups = groups_all
if enable_group_filter:
    selected_groups = st.multiselect(
        "Groups to include",
        options=groups_all,
        default=groups_all,
        help="Filter specific groups for grouped charts.",
    )
    if not selected_groups:
        st.info("Select at least one group to visualize.")
        st.stop()

# Common controls
step_size = st.slider(
    "Sample every N rows",
    min_value=1,
    max_value=50,
    value=10,
    step=1,
    help="Use this to downsample large datasets. Default is every 10 rows.",
)

# Controls that only apply to specific charts
color_scheme = None
if chart_type in ["Line", "Bar", "Scatter", "Box"]:
    color_scheme = st.selectbox(
        "Color scheme",
        ["tab10", "tab20", "Set2", "viridis", "plasma", "cividis"],
    )

rolling_window = None
if chart_type == "Moving Average":
    rolling_window = st.slider(
        "Moving average window",
        min_value=3,
        max_value=100,
        value=10,
        step=1,
        help="Used only for Moving Average chart.",
    )

# Filter and downsample to reduce visual clutter.
df_filtered = df[df["group_name"].isin(selected_groups)].copy()
df_sampled = df_filtered.iloc[::step_size].copy()

# Build a Matplotlib chart so we can control color scales and encodings.
# Note: Matplotlib doesn't provide built-in tooltips like Altair/Plotly.
groups = sorted(df_sampled["group_name"].unique())
palette = plt.get_cmap(color_scheme) if color_scheme else plt.get_cmap("tab10")
colors = {g: palette(i / max(1, len(groups) - 1)) for i, g in enumerate(groups)}

fig, ax = plt.subplots()

if chart_type == "Line":
    for g in groups:
        sub = df_sampled[df_sampled["group_name"] == g]
        ax.plot(sub["id"], sub["value"], label=g, color=colors[g], linewidth=1.5)
    ax.set_xlabel("id")
    ax.set_ylabel("value")
elif chart_type == "Bar":
    means = df_sampled.groupby("group_name", sort=False)["value"].mean()
    ax.bar(means.index, means.values, color=[colors[g] for g in means.index])
    ax.set_xlabel("group")
    ax.set_ylabel("mean(value)")
    ax.tick_params(axis="x", rotation=30)
elif chart_type == "Scatter":
    for g in groups:
        sub = df_sampled[df_sampled["group_name"] == g]
        ax.scatter(
            sub["value"],
            sub["value_b"],
            label=g,
            color=colors[g],
            alpha=0.7,
            s=40,
        )
    ax.set_xlabel("value")
    ax.set_ylabel("value_b")
elif chart_type == "Histogram":
    ax.hist(
        df_sampled["value"],
        bins=20,
        color=palette(0.5),
        alpha=0.85,
        edgecolor="white",
    )
    ax.set_xlabel("value")
    ax.set_ylabel("count")
elif chart_type == "Box":
    data = [df_sampled[df_sampled["group_name"] == g]["value"] for g in groups]
    ax.boxplot(data, labels=groups, patch_artist=True)
    ax.set_xlabel("group")
    ax.set_ylabel("value")
    ax.tick_params(axis="x", rotation=30)
elif chart_type == "Moving Average":
    sorted_df = df_sampled.sort_values("id")
    series = sorted_df["value"].rolling(rolling_window).mean()
    # Drop initial NaNs so the line is visible right away.
    mask = series.notna()
    ax.plot(sorted_df.loc[mask, "id"], series[mask], color=palette(0.7))
    ax.set_xlabel("id")
    ax.set_ylabel(f"value (rolling mean, window={rolling_window})")
else:
    series = df_sampled.sort_values("id")["value"].cumsum()
    ax.plot(df_sampled.sort_values("id")["id"], series, color=palette(0.7))
    ax.set_xlabel("id")
    ax.set_ylabel("cumulative value")

ax.legend(title="group", fontsize="small")
ax.grid(alpha=0.2)

st.pyplot(fig, use_container_width=True)

st.caption(
    "Options: switch to Plotly for interactive hover, or add facets by group."
)

# -----------------------------
# Downloads: PNG and HTML
# -----------------------------
png_buffer = io.BytesIO()
fig.savefig(png_buffer, format="png", dpi=150, bbox_inches="tight")
png_bytes = png_buffer.getvalue()

st.download_button(
    label="Download graph as PNG",
    data=png_bytes,
    file_name="chart.png",
    mime="image/png",
)

# Simple HTML wrapper with embedded base64 PNG.
img_b64 = base64.b64encode(png_bytes).decode("utf-8")
html = f"""<!doctype html>
<html>
  <head><meta charset="utf-8"><title>Streamlit Chart</title></head>
  <body>
    <h3>Streamlit Chart Export</h3>
    <img src="data:image/png;base64,{img_b64}" alt="chart"/>
  </body>
</html>
""".encode("utf-8")

st.download_button(
    label="Download graph as HTML",
    data=html,
    file_name="chart.html",
    mime="text/html",
)
