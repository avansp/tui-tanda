from textual.app import App, ComposeResult
from textual.widgets import Header, Footer


class TextViewerApp(App):
    """Just a simple text viewer."""

    BINDINGS = [("d", "toggle_dark", "Toggle dark mode")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app"""
        yield Header()
        yield Footer()


if __name__ == "__main__":
    TextViewerApp.run()
