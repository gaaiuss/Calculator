import math
from resource.utils import isEmpty, isNumOrDot, isValidNumber
from resource.variables import MEDIUM_FONT_SIZE
from typing import TYPE_CHECKING

from PySide6.QtCore import Slot
from PySide6.QtWidgets import QGridLayout, QPushButton

if TYPE_CHECKING:
    from gui.display import Display
    from gui.info import Info
    from gui.main_window import MainWindow


class Button(QPushButton):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.configStyle()

    def configStyle(self):
        font = self.font()
        font.setPixelSize(MEDIUM_FONT_SIZE)
        self.setFont(font)
        self.setMinimumSize(75, 75)


class ButtonsGrid(QGridLayout):
    def __init__(
        self, display: 'Display', info: 'Info', window: 'MainWindow',
            * args, **kwargs
    ):
        super().__init__(*args, **kwargs)

        self._gridMask = [
            ['C', '◀', '^', '/'],
            ['7', '8', '9', '*'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['N',  '0', '.', '='],
        ]

        self.display = display
        self.info = info
        self.window = window
        self._equation = ''
        self._leftNumber = None
        self._rightNumber = None
        self._operator = None

        self.equation = ''
        self._makeGrid()

    @property
    def equation(self):
        return self._equation

    @equation.setter
    def equation(self, value):
        self._equation = value
        self.info.setText(value)

    def _makeGrid(self):
        self.display.eqPressed.connect(self._equal)
        self.display.delPressed.connect(self.display.backspace)
        self.display.clearPressed.connect(self._clear)
        self.display.inputPressed.connect(self._insertToDisplay)
        self.display.operatorPressed.connect(self._configLeftOperation)

        for rowNumber, row in enumerate(self._gridMask):
            for columnNumber, buttonText in enumerate(row):
                button = Button(buttonText)
                if not isNumOrDot(buttonText) and not isEmpty(buttonText):
                    button.setProperty('cssClass', 'specialButton')
                    self._configSpecialButton(button)
                else:
                    button.setProperty('cssClass', 'normalButton')

                self.addWidget(button, rowNumber, columnNumber)

                slot = self._makeSlot(self._insertToDisplay, buttonText)
                self._connectButtonClicked(button, slot)

    def _connectButtonClicked(self, button, slot):
        button.clicked.connect(slot)

    def _configSpecialButton(self, button):
        buttonText = button.text()

        if buttonText == 'C':
            self._connectButtonClicked(button, self._clear)

        if buttonText == '◀':
            self._connectButtonClicked(button, self.display.backspace)

        if buttonText == 'N':
            self._connectButtonClicked(button, self._negativeNumber)

        if buttonText in '+-/*^':
            self._connectButtonClicked(
                button,
                self._makeSlot(self._configLeftOperation, buttonText)
            )

        if buttonText == '=':
            self._connectButtonClicked(button, self._equal)

    @Slot()
    def _makeSlot(self, func, *args, **kwargs):
        @Slot()
        def realSlot():
            func(*args, **kwargs)
        return realSlot

    @Slot()
    def _negativeNumber(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        newNumber = float(displayText) * -1
        self.display.setText(str(newNumber))

    @Slot()
    def _insertToDisplay(self, text):
        newDisplayValue = self.display.text() + text

        if not isValidNumber(newDisplayValue):
            return

        self.display.insert(text)

    @Slot()
    def _clear(self):
        self._leftNumber = None
        self._rightNumber = None
        self._operator = None
        self.equation = ''
        self.display.clear()

    @Slot()
    def _configLeftOperation(self, text):
        displayText = self.display.text()  # _left number
        self.display.clear()

        # if person clicked in a operator before clicking a number
        if not isValidNumber(displayText) and self._leftNumber is None:
            return

        if self._leftNumber is None:
            self._leftNumber = float(displayText)

        self._operator = text
        self.equation = f'{self._leftNumber} {self._operator}'

    @Slot()
    def _equal(self):
        displayText = self.display.text()

        if not isValidNumber(displayText):
            return

        self._rightNumber = float(displayText)
        self.equation = f'{self._leftNumber} {self._operator}' \
            f' {self._rightNumber}'

        result = 'error'
        try:
            if '^' in self.equation:
                result = math.pow(self._leftNumber, self._rightNumber)
            else:
                result = eval(self.equation)
        except ZeroDivisionError:
            self._showError('Zero Division Error')
        except OverflowError:
            self._showError('Number too large')

        self.display.clear()
        self.info.setText(f'{self.equation} = {result}')

        self._leftNumber = result
        self._rightNumber = None

        if result == 'error':
            self._leftNumber = None

    def _showError(self, msg: str):
        msgBox = self.window.makeMsgBox()
        msgBox.setText(msg)
        msgBox.setIcon(msgBox.Icon.Critical)
        # msgBox.setInformativeText('NkjnssncnnfnJSKJBXCNLKNLKWIANiNDNNnkkndknfensjnndsneflknesldnflknlenlfnelkndnflknlenlfnelkndnflknlenlfnelkndnflknlenlfnelkndnflknlenlfnelkn')
        msgBox.setStandardButtons(
            msgBox.StandardButton.Ok |
            msgBox.StandardButton.Cancel
        )

        msgBox.exec()
        # result = msgBox.exec()

        # if result == msgBox.StandardButton.Ok:
        #     print('User clicked OK')
        # elif result == msgBox.StandardButton.Cancel:
        #     print('User clicked Cancel')
