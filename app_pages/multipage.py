"""A small framework for combining several Streamlit pages into one app."""
import streamlit as st


class MultiPage:
    """Manage a collection of dashboard pages behind a sidebar menu."""

    def __init__(self, app_name: str) -> None:
        self.pages = []
        self.app_name = app_name
        st.set_page_config(
            page_title=self.app_name,
            page_icon="🚗",
            layout="wide",
        )

    def add_page(self, title: str, func) -> None:
        """Register a page: a title and the function that renders it."""
        self.pages.append({"title": title, "function": func})

    def run(self) -> None:
        """Render the sidebar menu and the selected page."""
        st.title(self.app_name)
        page = st.sidebar.radio(
            "Navigation",
            self.pages,
            format_func=lambda page: page["title"],
        )
        page["function"]()
