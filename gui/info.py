from resource.variables import MEDIUM_FONT_SIZE, TEXT_MARGIN

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QLabel


class Info(QLabel):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        self.setStyleSheet(f'font-size: {MEDIUM_FONT_SIZE}px')
        self.setAlignment(Qt.AlignmentFlag.AlignRight)
        self.setMargin(TEXT_MARGIN)
