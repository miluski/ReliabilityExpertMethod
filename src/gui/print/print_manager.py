from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class PrintManager:
    """Handles printing operations"""

    def __init__(self, parent_widget):
        self.parent = parent_widget

    def print_text(self, text_widget):
        """Print text using system print dialog"""
        printer = self._create_printer()
        dialog = self._create_dialog(printer)

        if dialog.exec_() == QPrintDialog.Accepted:
            text_widget.print_(printer)

    def _create_printer(self):
        """Create printer instance"""
        return QPrinter(QPrinter.HighResolution)

    def _create_dialog(self, printer):
        """Create print dialog"""
        return QPrintDialog(printer, self.parent)
