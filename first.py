from textual.app import App
from textual.widgets import Button, Footer, Header, Static


class TimeDisplay(Static):
    """custom time display"""


class Stopwatch(Static):
    def compose(self):
        yield Button("Start", variant="success")
        yield Button("Stop", variant="error")
        yield Button("Reset")
        yield TimeDisplay("00:00:00.00")


class StopwatchApp(App):
    BINDINGS = [
        ("d", "toggle_dark", "Toggle dark mode"),
    ]

    def compose(self):
        """what widget is this app composed of?"""
        yield Header(show_clock=True)
        yield Footer()
        yield Stopwatch()


if __name__ == "__main__":
    StopwatchApp().run()
