import streamlit as st


class MultiPage:
    """A small framework that turns a set of functions into a multi-page app."""

    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name
        st.set_page_config(page_title=app_name, page_icon="🚗", layout="wide")

    def add_page(self, title, func):
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.sidebar.title(self.app_name)
        page = st.sidebar.radio(
            "Navigate", self.pages, format_func=lambda p: p["title"]
        )
        page["function"]()
