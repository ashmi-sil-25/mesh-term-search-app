"""Streamlit frontend for displaying MeSH term search suggestions."""

import streamlit as st
import requests

st.set_page_config(page_title="MeSH Search", layout="centered")
st.markdown(
    "<h2 style='text-align: center;'>🔍 MeSH Term Search</h2>",
    unsafe_allow_html=True
)

# Initialize session state for selected term
if "selected_term" not in st.session_state:
    st.session_state.selected_term = None

# Input field
query = st.text_input("Start typing a MeSH term...")

# Reset selected term when new input is typed
if query and st.session_state.selected_term:
    st.session_state.selected_term = None

# Only query backend if input is 3+ characters
if query and len(query.strip()) >= 3:
    try:
        response = requests.get(
            f"http://localhost:8000/search?term={query.lower()}",
            timeout=5
        )

        if response.status_code == 200:
            results = response.json()

            if results:
                st.markdown("### Suggestions:")
                for item in results:
                    if st.button(f"{item['term']}"):
                        st.session_state.selected_term = item["term"]
                        st.rerun()  # Refresh UI with details

            else:
                st.markdown(
                    "<p style='color:gray;'>No matches found.</p>",
                    unsafe_allow_html=True
                )

        else:
            st.error("Error fetching suggestions from backend.")

    except requests.RequestException as err:
        st.error(f"Network error: {err}")

# Show details for selected term
if st.session_state.selected_term:
    st.markdown(f"### 📋 Details for: {st.session_state.selected_term}")

    try:
        detail_response = requests.get(
            f"http://localhost:8000/term-details?term={st.session_state.selected_term}",
            timeout=5
        )

        if detail_response.status_code == 200:
            info = detail_response.json()
            for key, value in info.items():
                st.markdown(f"**{key}**: {value}")
        else:
            st.warning("No details found.")

    except requests.RequestException as err:
        st.error(f"Failed to load details: {err}")
