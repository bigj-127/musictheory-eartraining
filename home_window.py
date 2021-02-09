# NEXT STEPS
# Fix the disabling ish
# Test all the tests
# Format the layouts for small screen (should be generally applicable)
# Look into prettying up the UI
# Look into making it an executable and how to export

# pyuic command
# pyuic5 -x [input ui file] -o [output py file]


from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_templates.home_window_ui import Ui_HomeWindow

from interval_test_window import IntervalTestWindow
from chord_id_test_window import ChordIDTestWindow
from chord_degree_test_window import ChordDegreeTestWindow
from chord_relation_test_window import ChordRelationTestWindow

from pygame_midi import setup_pygame_midi, close_pygame_midi
from constants import STRINGS

import os
os.environ["QT_AUTO_SCREEN_SCALE_FACTOR"] = "1"

class HomeWindow(QMainWindow):
    def __init__(self):
        super(HomeWindow, self).__init__()

        self.ui = Ui_HomeWindow()
        self.ui.setupUi(self)

        self.button_setup()

    def button_setup(self):
        self.ui.interval_test_button.clicked.connect(lambda: self.run_test(IntervalTestWindow))
        self.ui.chord_id_test_button.clicked.connect(lambda: self.run_test(ChordIDTestWindow))
        self.ui.chord_degree_test_button.clicked.connect(lambda: self.run_test(ChordDegreeTestWindow))
        self.ui.chord_relation_test_button.clicked.connect(lambda: self.run_test(ChordRelationTestWindow))

        self.ui.close_button.clicked.connect(self.close)

    def run_test(self, test_window_class):
        self.test_window = test_window_class(self)
        self.hide()
        self.test_window.show()


if __name__ == "__main__":
    try:
        setup_pygame_midi(STRINGS)
        app = QApplication([])
        Home = HomeWindow()
        Home.show()
        app.exec_()
    finally:
        close_pygame_midi()