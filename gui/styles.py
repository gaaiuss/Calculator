from resource.variables import (DARKER_PRIMARY_COLOR, DARKEST_PRIMARY_COLOR,
                                PRIMARY_COLOR, WHITE_COLOR)

import qdarkstyle  # type: ignore
from PySide6.QtWidgets import QApplication

qss = f"""
    PushButton[cssClass="specialButton"] {{
        color: {WHITE_COLOR};
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    PushButton[cssClass="specialButton"]:hover {{
        color: {WHITE_COLOR};
        background: {DARKER_PRIMARY_COLOR};
    }}
    PushButton[cssClass="specialButton"]:pressed {{
        color: {WHITE_COLOR};
        background: {DARKEST_PRIMARY_COLOR};
    }}
"""


def setupTheme(app: QApplication):
    # Set qdarkstyle darkmode
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    # Replace QSS for further personalization
    app.setStyleSheet(app.styleSheet() + qss)
