from PyQt5.QtWidgets import QApplication, QMainWindow

from chord_degree_test_window_ui import Ui_ChordDegreeTestWindow
from constants import MAJOR_SCALES_DICT

from random import choice

class ChordDegreeTestWindow(QMainWindow):
    def __init__(self, parent_window=None):
        super(ChordDegreeTestWindow, self).__init__()
        self.parent_window = parent_window

        self.ui = Ui_ChordDegreeTestWindow()
        self.ui.setupUi(self)

        self.button_setup()
        self.toggle_enharmonics()

        self.no_keys_selected = False
        self.no_degrees_selected = False
        self.allowed_keys = {"C","D","G"}
        self.allowed_degrees = {"4", "5", "6"}
        self.chord_degree_test_setup()

        self.num_attempted = 0
        self.num_correct = 0

    def button_setup(self):
        self.ui.skip_button.clicked.connect(self.skip_button_clicked)

        self.chord_buttons = {}
        for b in self.ui.chord_buttonGroup.buttons():
            self.chord_buttons[b.accessibleName()] = b
            b.clicked.connect(lambda _, arg=b.accessibleName(): self.chord_button_clicked(arg))

        self.chord_buttons_enh = {}
        for b in self.ui.chord_buttonGroup_enh.buttons():
            self.chord_buttons_enh[b.accessibleName()] = b
            b.clicked.connect(lambda _, arg=b.accessibleName(): self.chord_button_clicked(arg))

        self.ui.enharmonic_switch.clicked.connect(self.toggle_enharmonics)

        for b in self.ui.keys_buttonGroup.buttons():
            b.clicked.connect(lambda _, arg=b: self.update_selected_keys(arg))

        for b in self.ui.degrees_buttonGroup.buttons():
            b.clicked.connect(lambda _, arg=b: self.update_selected_degrees(arg))

        self.ui.select_all_keys_button.clicked.connect(lambda: self.select_all_keys())
        self.ui.select_all_degrees_button.clicked.connect(lambda: self.select_all_degrees())

        self.ui.close_button.clicked.connect(self.close_window)

    def chord_degree_test_setup(self):
        if len(self.allowed_keys) == 0 or len(self.allowed_degrees) == 0:
            self.disable_everything()
        else:
            key = choice(list(self.allowed_keys))
            degree = choice(list(self.allowed_degrees))
            self.answer = MAJOR_SCALES_DICT[key][int(degree) - 1]

            self.ui.key_label.setText("Key: {}".format(key))
            self.ui.degree_label.setText("Degree: {}".format(degree))
            self.ui.output_label.setText("")

    def chord_button_clicked(self, response):
        self.num_attempted += 1
        if self.answer in response:
            self.ui.output_label.setText("Correct! Get ready for the next one")
            self.ui.output_label.setStyleSheet("color:green")
            self.num_correct += 1
            self.chord_degree_test_setup()
        else:
            self.ui.output_label.setText("Sorry that wasn't correct :( Try again")
            self.ui.output_label.setStyleSheet("color:red")

        self.ui.score_label.setText("Score: {}/{} ({}%)".format(self.num_correct, self.num_attempted, round(self.num_correct / self.num_attempted * 100, 2)))

    def skip_button_clicked(self):
        self.ui.output_label.setText("The correct answer was {}".format(self.answer))
        self.ui.output_label.setStyleSheet("color:black")
        self.chord_degree_test_setup()

    def toggle_enharmonics(self):
        switch = self.ui.enharmonic_switch.isChecked()
        for b in self.ui.chord_buttonGroup.buttons():
            b.setVisible(not switch)
        for b in self.ui.chord_buttonGroup_enh.buttons():
            b.setVisible(switch)

        if switch:
            self.ui.enharmonic_switch.setText("Turn off enharmonic equivalency")
        else:
            self.ui.enharmonic_switch.setText("Turn on enharmonic equivalency")


    def update_selected_keys(self, b):
        if b.isChecked():
            self.allowed_keys.add(b.accessibleName())

            if self.no_keys_selected:
                self.reenable_everything()
        else:
            self.allowed_keys.remove(b.accessibleName())

        self.update_checkboxes(1)
        self.chord_degree_test_setup()

    def update_selected_degrees(self, b):
        if b.isChecked():
            self.allowed_degrees.add(b.accessibleName())

            if self.no_degrees_selected:
                self.reenable_everything()
        else:
            self.allowed_degrees.remove(b.accessibleName())

        self.update_checkboxes(0)
        self.chord_degree_test_setup()

    def select_all_keys(self):
        switch = self.ui.select_all_keys_button.isChecked()
        change_list = set()
        for b in self.ui.keys_buttonGroup.buttons():
            b.setChecked(switch)
            change_list.add(b.accessibleName())

        if switch:
            self.allowed_keys = self.allowed_keys | change_list
            if self.no_keys_selected:
                self.reenable_everything()
        else:
            self.allowed_keys = self.allowed_keys - change_list

        self.update_checkboxes(1)
        self.chord_degree_test_setup()

    def select_all_degrees(self):
        switch = self.ui.select_all_degrees_button.isChecked()
        change_list = set()
        for b in self.ui.degrees_buttonGroup.buttons():
            b.setChecked(switch)
            change_list.add(b.accessibleName())

        if switch:
            self.allowed_degrees = self.allowed_degrees | change_list
            if self.no_degrees_selected:
                self.reenable_everything()
        else:
            self.allowed_degrees = self.allowed_degrees - change_list

        self.update_checkboxes(0)
        self.chord_degree_test_setup()

    def update_checkboxes(self, kd_switch):
        if kd_switch:
            switch = True
            for b in self.ui.keys_buttonGroup.buttons():
                if not b.isChecked():
                    switch = False
                    break
            self.ui.select_all_keys_button.setChecked(switch)
        else:
            switch = True
            for b in self.ui.degrees_buttonGroup.buttons():
                if not b.isChecked():
                    switch = False
                    break
            self.ui.select_all_degrees_button.setChecked(switch)

    def disable_everything(self):
        self.answer = None

        self.ui.key_label.setText("Key:")
        self.ui.degree_label.setText("Degree:")
        self.ui.key_label.setEnabled(False)
        self.ui.degree_label.setEnabled(False)

        self.ui.skip_button.setEnabled(False)

        if len(self.allowed_keys) == 0:
            self.no_keys_selected = True
            self.ui.output_label.setText("Please select at least one key")
        if len(self.allowed_degrees) == 0:
            self.no_degrees_selected = True
            self.ui.output_label.setText("Please select at least one degree")

        if self.no_keys_selected and self.no_degrees_selected:
            self.ui.output_label.setText("Please select at least one key and degree")

        self.ui.output_label.setStyleSheet("color:red")

    def reenable_everything(self):
        if len(self.allowed_keys) > 0:
            self.no_keys_selected = False
        if len(self.allowed_degrees) > 0:
            self.no_degrees_selected = False

        if not (self.no_keys_selected or self.no_degrees_selected):
            self.ui.skip_button.setEnabled(True)
            self.ui.key_label.setEnabled(True)
            self.ui.degree_label.setEnabled(True)
            self.ui.output_label.setText("")

            self.chord_degree_test_setup()


    def close_window(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()


if __name__ == "__main__":
    app = QApplication([])
    ChordDegreeTest = ChordDegreeTestWindow()
    ChordDegreeTest.show()
    app.exec_()