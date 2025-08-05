import sys
from resource.variables import ICON_PATH

from PySide6.QtGui import QIcon
from PySide6.QtWidgets import QApplication

from gui.buttons import ButtonsGrid
from gui.display import Display
from gui.info import Info
from gui.main_window import MainWindow
from gui.styles import setupTheme

if __name__ == '__main__':
    # Create app
    app = QApplication(sys.argv)
    window = MainWindow()

    # Theme
    setupTheme(app)

    # Set app icon
    app.setWindowIcon(QIcon(str(ICON_PATH)))

    # Info
    info = Info('25.53 ^ 2.0')
    window.addToLayout(info)

    # Display
    display = Display()
    window.addToLayout(display)

    # Grid
    buttonsGrid = ButtonsGrid()
    window.vLayout.addLayout(buttonsGrid)

    # Execute everything
    window.adjustFixedSize()
    window.show()
    app.exec()
