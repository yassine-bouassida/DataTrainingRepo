import streamlit as st

from utils import generate_synthetic_data, df_to_csv_bytes, EXPECTED_COLUMNS

st.set_page_config(page_title="Data Generator", page_icon="📈", layout="wide")

st.title("Data Generator")
st.caption("Step 1: Generate data and download it as a CSV.")

# A simple layout pattern: st.columns creates side-by-side containers.
# Each widget inside a column renders in that column only.
col1, col2, col3 = st.columns(3)
with col1:
    # Sliders return a value immediately on change; the script reruns and
    # downstream code uses the latest value.
    rows = st.slider("Rows", min_value=100, max_value=5000, value=1000, step=100)
    seed = st.number_input("Random Seed", min_value=0, max_value=10_000, value=42)
with col2:
    # Sliders are an easy way to expose numeric parameters without forms.
    noise = st.slider("Noise", min_value=0.0, max_value=20.0, value=5.0, step=0.5)
    categories = st.slider("Groups", min_value=2, max_value=10, value=4)
with col3:
    # Checkboxes return True/False and are great for optional features.
    include_text = st.checkbox("Include text column", value=True)

# Cached generator
# Option: remove caching if you want data to regenerate on every rerun.
df = generate_synthetic_data(rows, seed, noise, include_text, categories)

# Keep the latest generated data in session state so other pages can use it.
st.session_state["generated_df"] = df

st.write("Preview")
st.dataframe(df.head(20), use_container_width=True)

st.write("Summary statistics")
st.dataframe(df.describe(include="all"), use_container_width=True)

# Download button: you can pass a callable for deferred generation.
# Example:
# data=lambda: df_to_csv_bytes(df)
csv_bytes = df_to_csv_bytes(df)

st.download_button(
    label="Download CSV",
    data=csv_bytes,
    file_name="synthetic_data.csv",
    mime="text/csv",
)

st.info(
    "The generated CSV uses this schema: "
    + ", ".join([f"`{c}`" for c in EXPECTED_COLUMNS])
)
