import streamlit as st
import pandas as pd

from utils import df_to_csv_bytes, EXPECTED_COLUMNS, validate_schema

st.set_page_config(page_title="CSV Explorer", page_icon="📄", layout="wide")

st.title("CSV Explorer")
st.caption("Step 2: Import a CSV that matches the generated schema.")

# Provide an example CSV download to guide schema alignment.
example_df = st.session_state.get("generated_df")
if isinstance(example_df, pd.DataFrame):
    st.download_button(
        label="Download Example CSV (from generated data)",
        data=df_to_csv_bytes(example_df),
        file_name="example_schema.csv",
        mime="text/csv",
    )
else:
    st.info("Generate data first to enable the example CSV download.")

# File upload; default max upload size is 200MB (configurable in config.toml).
uploaded = st.file_uploader("Upload a CSV", type=["csv"])

if uploaded:
    df = pd.read_csv(uploaded)
    is_valid, missing = validate_schema(df)

    if not is_valid:
        st.error(
            "Uploaded CSV does not match the expected schema. "
            "Missing columns: " + ", ".join([f"`{c}`" for c in missing])
        )
    else:
        # Save validated data to session state for downstream steps.
        st.session_state["uploaded_df"] = df

    st.write("Preview")
    st.dataframe(df.head(50), use_container_width=True)

    st.write("Columns")
    st.write(list(df.columns))

    st.write("Summary statistics")
    st.dataframe(df.describe(include="all"), use_container_width=True)
else:
    st.info("Upload a CSV to explore it here.")
