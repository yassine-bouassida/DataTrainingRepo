import sqlite3

import pandas as pd
import streamlit as st

from utils import EXPECTED_COLUMNS, get_sqlite_path

st.set_page_config(page_title="SQLite Explorer", page_icon="🗄️", layout="wide")

st.title("SQLite Explorer")
st.caption("Step 3: Load data into the database (requires an imported CSV).")

db_path = get_sqlite_path()

uploaded_df = st.session_state.get("uploaded_df")

if not isinstance(uploaded_df, pd.DataFrame):
    st.warning("No imported CSV found. Go to CSV Explorer and upload data first.")
else:
    st.write("Data ready to load into DB")
    st.dataframe(uploaded_df.head(50), use_container_width=True)

    conn = sqlite3.connect(db_path)
    cur = conn.cursor()

    # Ensure the table has the expected schema. If it doesn't, recreate it.
    cur.execute("PRAGMA table_info(demo_data)")
    existing_cols = [row[1] for row in cur.fetchall()]

    expected_cols = ["id", "value", "value_b", "group_name", "value_bin"]
    if existing_cols and existing_cols != expected_cols:
        cur.execute("DROP TABLE IF EXISTS demo_data")
        conn.commit()
        existing_cols = []

    if not existing_cols:
        cur.execute(
            """
            CREATE TABLE IF NOT EXISTS demo_data (
                id INTEGER PRIMARY KEY,
                value REAL,
                value_b REAL,
                group_name TEXT,
                value_bin INTEGER
            )
            """
        )
        conn.commit()

    col1, col2 = st.columns(2)
    with col1:
        if st.button("Load data into DB"):
            cur.execute("DELETE FROM demo_data")
            conn.commit()

            to_insert = uploaded_df[EXPECTED_COLUMNS].rename(
                columns={"group": "group_name"}
            )
            cur.executemany(
                "INSERT INTO demo_data (id, value, value_b, group_name, value_bin) "
                "VALUES (?, ?, ?, ?, ?)",
                to_insert.itertuples(index=False, name=None),
            )
            conn.commit()
            st.success("Loaded data into DB.")

    with col2:
        if st.button("Empty DB"):
            cur.execute("DELETE FROM demo_data")
            conn.commit()
            st.success("Database table emptied.")

    data = pd.read_sql_query("SELECT * FROM demo_data LIMIT 100", conn)
    st.write("Current DB contents")
    st.dataframe(data, use_container_width=True)

    conn.close()
