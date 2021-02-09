from PyQt5.QtWidgets import QApplication, QMainWindow

from interval_test_window_ui import Ui_IntervalTestWindow
from pygame_midi import setup_pygame_midi, close_pygame_midi, play_note
from constants import STRINGS, NOTES, EASY_INTERVALS, MEDIUM_INTERVALS, HARD_INTERVALS, INTERVALS_DICT

from random import choice, randint

class IntervalTestWindow(QMainWindow):
    def __init__(self, parent_window=None):
        super(IntervalTestWindow, self).__init__()
        self.parent_window = parent_window

        self.ui = Ui_IntervalTestWindow()
        self.ui.setupUi(self)

        self.button_setup()

        self.unplayed = True
        self.no_intervals_selected = False
        self.allowed_intervals = {"MAJOR_3RD", "PERFECT_5TH", "OCTAVE"}
        self.interval_test_setup()

        self.num_attempted = 0
        self.num_correct = 0

    def button_setup(self):
        self.ui.replay_button.clicked.connect(self.play_notes)
        self.ui.skip_button.clicked.connect(self.skip_button_clicked)

        self.interval_buttons = {}
        for b in self.ui.interval_buttonGroup.buttons():
            self.interval_buttons[b.accessibleName()] = b
            b.clicked.connect(lambda _, arg=b.accessibleName(): self.interval_button_clicked(arg))

        for b in self.ui.buttonGroup1.buttons() + self.ui.buttonGroup2.buttons():
            b.clicked.connect(lambda _, arg=b: self.update_selected(arg))

        self.ui.select_all.clicked.connect(lambda: self.update_multiple(self.ui.select_all, self.ui.buttonGroup1.buttons() + self.ui.buttonGroup2.buttons()))
        self.ui.select_all1.clicked.connect(lambda: self.update_multiple(self.ui.select_all1, self.ui.buttonGroup1.buttons()))
        self.ui.select_all2.clicked.connect(lambda: self.update_multiple(self.ui.select_all2, self.ui.buttonGroup2.buttons()))

        self.ui.close_button.clicked.connect(self.close_window)

    def interval_test_setup(self):
        if len(self.allowed_intervals) == 0:
            self.disable_everything()
        else:
            root_note_index = randint(0,33) - 9
            self.root_note = NOTES[12 + root_note_index]
            self.interval = choice(list(self.allowed_intervals))
            self.interval_note = NOTES[12 + root_note_index + INTERVALS_DICT[self.interval]]

            self.unplayed = True
            self.ui.replay_button.setText("Play Interval")
            self.ui.label.setText("Click 'Play Interval' to hear the interval")

    def play_notes(self):
        if self.unplayed:
            self.unplayed = False
            self.ui.label.setText("Select the interval you just heard")
            self.ui.replay_button.setText("Replay Interval")
            self.ui.output_label.setText("")

        play_note(self.root_note, STRINGS)
        play_note(self.interval_note, STRINGS)

    def interval_button_clicked(self, response):
        self.num_attempted += 1
        if response == self.interval:
            self.ui.output_label.setText("Correct! Get ready for the next one")
            self.ui.output_label.setStyleSheet("color:green")
            self.num_correct += 1
            self.interval_test_setup()
        else:
            self.ui.output_label.setText("Sorry that wasn't correct :( Try again")
            self.ui.output_label.setStyleSheet("color:red")

        self.ui.score_label.setText("Score: {}/{} ({}%)".format(self.num_correct, self.num_attempted, round(self.num_correct / self.num_attempted * 100, 2)))

    def skip_button_clicked(self):
        self.ui.output_label.setText("That was a {}".format(self.interval.replace("_", " ")))
        self.ui.output_label.setStyleSheet("color:black")
        self.interval_test_setup()

    def update_selected(self, b):
        if b.isChecked():
            self.interval_buttons[b.accessibleName()].setEnabled(True)
            self.allowed_intervals.add(b.accessibleName())

            if self.no_intervals_selected:
                self.reenable_everything()
        else:
            self.interval_buttons[b.accessibleName()].setEnabled(False)
            self.allowed_intervals.remove(b.accessibleName())

        self.update_checkboxes()
        self.skip_button_clicked()

    def update_multiple(self, select_b, buttons_list):
        switch = select_b.isChecked()
        change_list = set()
        for b in buttons_list:
            b.setChecked(switch)
            self.interval_buttons[b.accessibleName()].setEnabled(switch)
            change_list.add(b.accessibleName())

        if switch:
            self.allowed_intervals = self.allowed_intervals | change_list
            if self.no_intervals_selected:
                self.reenable_everything()
        else:
            self.allowed_intervals = self.allowed_intervals - change_list

        self.update_checkboxes()
        self.skip_button_clicked()

    def update_checkboxes(self):
        switch1 = True
        for b in self.ui.buttonGroup1.buttons():
            if not b.isChecked():
                switch1 = False
                break

        switch2 = True
        for b in self.ui.buttonGroup2.buttons():
            if not b.isChecked():
                switch2 = False
                break

        self.ui.select_all.setChecked(switch1 and switch2)
        self.ui.select_all1.setChecked(switch1)
        self.ui.select_all2.setChecked(switch2)

    def disable_everything(self):
        self.interval = None
        self.interval_note = None
        self.root_note = None

        self.ui.skip_button.setEnabled(False)
        self.ui.replay_button.setEnabled(False)

        self.no_intervals_selected = True

        self.ui.output_label.setText("Please select at least one interval")
        self.ui.output_label.setStyleSheet("color:red")

    def reenable_everything(self):
        self.no_intervals_selected = False

        self.ui.skip_button.setEnabled(True)
        self.ui.replay_button.setEnabled(True)

        self.ui.output_label.setText("")

        self.interval_test_setup()


    def close_window(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()


if __name__ == "__main__":
    try:
        setup_pygame_midi(STRINGS)
        app = QApplication([])
        IntervalTest = IntervalTestWindow()
        IntervalTest.show()
        app.exec_()
    finally:
        close_pygame_midi()