# Unofficial Streamlit Introduction

This is an **unofficial, code-first introduction to Streamlit**, created by **Yassine Bouassida** to help learn and use Streamlit effectively within this project.

The goal is not to be a full tutorial, but a practical reference that demonstrates core Streamlit features through usage.

Covered topics include:
- Data generation and basic analysis
- CSV download and upload
- Interactive visualizations and controls
- SQLite loading and persistence
- Caching and session state


## Setup
```powershell
cd "\streamlit intro"
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

## Run
```powershell
streamlit run Intro.py
```

## App Structure
- `app.py`: Navigation (custom sidebar)
- `pages/`: Multi-page Streamlit sections
- `utils.py`: Shared helpers (data generation, CSV utilities)

## SQLite Notes
- Default SQLite file: `streamlit_intro.db` (created in the project folder)
- SQLAlchemy is required for `st.connection(..., type="sql")`
- You can optionally configure `.streamlit/secrets.toml`:

```toml
[connections.sqlite_local]
url = "sqlite:///streamlit_intro.db"
```

## Optional Dependencies
- If `faker` is not installed, the app falls back to basic text generation.
- If `sqlalchemy` is missing, the app uses `sqlite3` directly.
