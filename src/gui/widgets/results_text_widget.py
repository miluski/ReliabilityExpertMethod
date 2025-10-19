from PyQt5.QtWidgets import QTextEdit
from PyQt5.QtGui import QFont, QFontMetrics


class ResultsTextWidget:
    """Manages the text display widget for results"""

    def __init__(self):
        self.text_edit = QTextEdit()
        self._setup_widget()

    def _setup_widget(self):
        """Setup text widget properties"""
        self.text_edit.setReadOnly(True)
        self.text_edit.setPlainText("Wyniki obliczeń pojawią się tutaj po naciśnięciu 'Oblicz'")
        self._setup_font()

    def _setup_font(self):
        """Setup monospace font with wide columns"""
        font = QFont("Courier New", 14)
        self.text_edit.setFont(font)
        self._setup_tab_stops(font)

    def _setup_tab_stops(self, font):
        """Setup tab stop width for better column spacing"""
        metrics = QFontMetrics(font)
        tab_width = 10 * metrics.horizontalAdvance(' ')
        self.text_edit.setTabStopDistance(tab_width)

    def get_widget(self):
        """Get the QTextEdit widget"""
        return self.text_edit

    def set_text(self, text):
        """Set display text"""
        self.text_edit.setPlainText(text)

    def get_text(self):
        """Get current text"""
        return self.text_edit.toPlainText()
