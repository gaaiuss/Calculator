from resource.variables import (DARKER_PRIMARY_COLOR, DARKER_SECONDARY_COLOR,
                                DARKEST_PRIMARY_COLOR, DARKEST_SECONDARY_COLOR,
                                PRIMARY_COLOR, SECONDARY_COLOR, WHITE_COLOR)

import qdarkstyle  # type: ignore
from PySide6.QtWidgets import QApplication

qss = f"""
    QPushButton[cssClass="specialButton"] {{
        color: {WHITE_COLOR};
        background: {PRIMARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="specialButton"]:hover {{
        color: {WHITE_COLOR};
        background: {DARKER_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="specialButton"]:pressed {{
        color: {WHITE_COLOR};
        background: {DARKEST_PRIMARY_COLOR};
    }}
    QPushButton[cssClass="normalButton"] {{
        color: {WHITE_COLOR};
        background: {SECONDARY_COLOR};
        border-radius: 5px;
    }}
    QPushButton[cssClass="normalButton"]:hover {{
        color: {WHITE_COLOR};
        background: {DARKER_SECONDARY_COLOR};
    }}
    QPushButton[cssClass="normalButton"]:pressed {{
        color: {WHITE_COLOR};
        background: {DARKEST_SECONDARY_COLOR};
    }}
"""


def setupTheme(app: QApplication):
    # Set qdarkstyle darkmode
    app.setStyleSheet(qdarkstyle.load_stylesheet_pyside6())

    # Replace QSS for further personalization
    app.setStyleSheet(app.styleSheet() + qss)
