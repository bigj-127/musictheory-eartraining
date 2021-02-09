from PyQt5.QtWidgets import QApplication, QMainWindow

from ui_templates.chord_id_test_window_ui import Ui_ChordIDTestWindow
from pygame_midi import setup_pygame_midi, close_pygame_midi, play_chord, play_arpeggio
from constants import STRINGS, CHORDS_DICT, BASIC_NOTES

from random import choice

class ChordIDTestWindow(QMainWindow):
    def __init__(self, parent_window=None):
        super(ChordIDTestWindow, self).__init__()
        self.parent_window = parent_window

        self.ui = Ui_ChordIDTestWindow()
        self.ui.setupUi(self)

        self.button_setup()

        self.chord_unplayed = True
        self.arpeggio_unplayed = True
        self.no_chords_selected = False
        self.allowed_chords = {"MAJOR_CHORD", "MINOR_CHORD"}
        self.chord_test_setup()

        self.num_attempted = 0
        self.num_correct = 0

    def button_setup(self):
        self.ui.skip_button.clicked.connect(self.skip_button_clicked)
        self.ui.play_chord_button.clicked.connect(self.play_chord_button_clicked)
        self.ui.play_arpeggio_button.clicked.connect(self.play_arpeggio_button_clicked)

        self.chord_buttons = {}
        for b in self.ui.chord_buttonGroup.buttons():
            self.chord_buttons[b.accessibleName()] = b
            b.clicked.connect(lambda _, arg=b.accessibleName(): self.chord_button_clicked(arg))

        for b in self.ui.buttonGroup1.buttons() + self.ui.buttonGroup2.buttons() + self.ui.buttonGroup3.buttons():
            b.clicked.connect(lambda _, arg=b: self.update_selected(arg))

        self.ui.select_all.clicked.connect(lambda: self.update_multiple(self.ui.select_all, self.ui.buttonGroup1.buttons() + self.ui.buttonGroup2.buttons() + self.ui.buttonGroup3.buttons()))
        self.ui.select_all1.clicked.connect(lambda: self.update_multiple(self.ui.select_all1, self.ui.buttonGroup1.buttons()))
        self.ui.select_all2.clicked.connect(lambda: self.update_multiple(self.ui.select_all2, self.ui.buttonGroup2.buttons()))
        self.ui.select_all3.clicked.connect(lambda: self.update_multiple(self.ui.select_all3, self.ui.buttonGroup3.buttons()))

        self.ui.close_button.clicked.connect(self.close_window)

    def chord_test_setup(self):
        if len(self.allowed_chords) == 0:
            self.disable_everything()
        else:
            self.selected_chord = choice(list(self.allowed_chords))
            self.chord_intervals = CHORDS_DICT[self.selected_chord]
            self.root_note = choice(BASIC_NOTES)

            self.chord_unplayed = True
            self.arpeggio_unplayed = True
            self.ui.play_chord_button.setText("Play Chord")
            self.ui.play_arpeggio_button.setText("Play Individual Notes")
            self.ui.label.setText("Select a button below to hear the chord or notes")

    def play_chord_button_clicked(self):
        if self.chord_unplayed:
            self.chord_unplayed = False
            self.ui.label.setText("Select the correct chord")
            self.ui.play_chord_button.setText("Replay Chord")
            self.ui.output_label.setText("")

        play_chord(self.root_note, self.chord_intervals, STRINGS)

    def play_arpeggio_button_clicked(self):
        if self.arpeggio_unplayed:
            self.arpeggio_unplayed = False
            self.ui.label.setText("Select the correct chord")
            self.ui.play_arpeggio_button.setText("Replay Notes")
            self.ui.output_label.setText("")

        play_arpeggio(self.root_note, self.chord_intervals, STRINGS)

    def chord_button_clicked(self, response):
        self.num_attempted += 1
        if response == self.selected_chord:
            self.ui.output_label.setText("Correct! Get ready for the next one")
            self.ui.output_label.setStyleSheet("color:green")
            self.num_correct += 1
            self.chord_test_setup()
        else:
            self.ui.output_label.setText("Sorry that wasn't correct :( Try again")
            self.ui.output_label.setStyleSheet("color:red")

        self.ui.score_label.setText("Score: {}/{} ({}%)".format(self.num_correct, self.num_attempted, round(self.num_correct / self.num_attempted * 100, 2)))

    def skip_button_clicked(self):
        self.ui.output_label.setText("That was a {}".format(self.selected_chord.replace("_", " ")))
        self.ui.output_label.setStyleSheet("color:black")
        self.chord_test_setup()

    def update_selected(self, b):
        if b.isChecked():
            self.chord_buttons[b.accessibleName()].setEnabled(True)
            self.allowed_chords.add(b.accessibleName())

            if self.no_chords_selected:
                self.reenable_everything()
        else:
            self.chord_buttons[b.accessibleName()].setEnabled(False)
            self.allowed_chords.remove(b.accessibleName())

        self.update_checkboxes()
        self.skip_button_clicked()

    def update_multiple(self, select_b, buttons_list):
        switch = select_b.isChecked()
        change_list = set()
        for b in buttons_list:
            b.setChecked(switch)
            self.chord_buttons[b.accessibleName()].setEnabled(switch)
            change_list.add(b.accessibleName())

        if switch:
            self.allowed_chords = self.allowed_chords | change_list
            if self.no_chords_selected:
                self.reenable_everything()
        else:
            self.allowed_chords = self.allowed_chords - change_list

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

        switch3 = True
        for b in self.ui.buttonGroup3.buttons():
            if not b.isChecked():
                switch3 = False
                break

        self.ui.select_all.setChecked(switch1 and switch2 and switch3)
        self.ui.select_all1.setChecked(switch1)
        self.ui.select_all2.setChecked(switch2)
        self.ui.select_all3.setChecked(switch3)

    def disable_everything(self):
        self.selected_chord = None
        self.chord_intervals = None
        self.root_note = None

        self.ui.skip_button.setEnabled(False)
        self.ui.play_chord_button.setEnabled(False)
        self.ui.play_arpeggio_button.setEnabled(False)

        self.no_chords_selected = True

        self.ui.output_label.setText("Please select at least one chord")
        self.ui.output_label.setStyleSheet("color:red")

    def reenable_everything(self):
        self.no_chords_selected = False

        self.ui.skip_button.setEnabled(True)
        self.ui.play_chord_button.setEnabled(True)
        self.ui.play_arpeggio_button.setEnabled(True)

        self.ui.output_label.setText("")

        self.chord_test_setup()

    def close_window(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()


if __name__ == "__main__":
    try:
        setup_pygame_midi(STRINGS)
        app = QApplication([])
        ChordIDTest = ChordIDTestWindow()
        ChordIDTest.show()
        app.exec_()
    finally:
        close_pygame_midi()