# Mustang Books Streamlit App

This folder contains a Streamlit recreation of the Figma/React export.

## Run locally

```bash
pip install -r requirements.txt
streamlit run app.py
```

## Deploy on Streamlit Community Cloud

1. Create a GitHub repository.
2. Upload `app.py` and `requirements.txt` to the repo root.
3. Go to Streamlit Community Cloud and create a new app from that repo.
4. Set the main file path to `app.py`.

## Notes

- The Google Form embed URLs are defined near the top of `app.py`.
- The book inventory is currently hardcoded in `BOOKS`. For a production app, replace it with a Google Sheets or database connection.
