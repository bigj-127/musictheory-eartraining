from PyQt5.QtWidgets import QApplication, QMainWindow

from chord_relation_test_window_ui import Ui_ChordRelationTestWindow
from pygame_midi import setup_pygame_midi, close_pygame_midi, play_chord
from constants import STRINGS, BASIC_NOTES, NOTES, INTERVALS_DICT, CHORDS_DICT

from random import choice, randint

class ChordRelationTestWindow(QMainWindow):
    def __init__(self, parent_window=None):
        super(ChordRelationTestWindow, self).__init__()
        self.parent_window = parent_window

        self.ui = Ui_ChordRelationTestWindow()
        self.ui.setupUi(self)

        self.button_setup()

        self.unplayed = True
        self.no_relations_selected = False
        self.allowed_chords = {'MAJOR_2ND':set(), 'MAJOR_3RD':set(), 'PERFECT_4TH':{'MAJOR_CHORD'}, 'PERFECT_5TH':{'MAJOR_CHORD'}, 'MAJOR_6TH':{'MINOR_CHORD'}, 'MAJOR_7TH':set()}
        self.chord_relation_test_setup()

        self.num_attempted = 0
        self.num_correct = 0

    def button_setup(self):
        self.ui.replay_button.clicked.connect(self.play_chords)
        self.ui.skip_button.clicked.connect(self.skip_button_clicked)

        self.relation_buttons = {}
        for b in self.ui.relation_buttonGroup.buttons():
            self.relation_buttons[b.accessibleName()] = b
            b.clicked.connect(lambda _, arg=b.accessibleName(): self.relation_button_clicked(arg))

        for b in self.ui.select_buttonGroup.buttons():
            b.clicked.connect(lambda _, arg=b: self.update_selected(arg))

        self.ui.select_all.clicked.connect(lambda: self.update_all())

        self.ui.close_button.clicked.connect(self.close_window)

    def chord_relation_test_setup(self):
            self.key_root = choice(BASIC_NOTES)

            self.chord_interval = choice(list(self.allowed_chords.keys()))
            while len(self.allowed_chords[self.chord_interval]) == 0:
                self.chord_interval = choice(list(self.allowed_chords.keys()))

            self.chord_root = self.key_root + INTERVALS_DICT[self.chord_interval]
            self.chord_quality = choice(list(self.allowed_chords[self.chord_interval]))
            self.answer = self.chord_interval + ' ' + self.chord_quality

            self.unplayed = True
            self.ui.replay_button.setText("Play Chords")
            self.ui.label.setText("Click 'Play Chords' to hear the two chords")

    def play_chords(self):
        if self.unplayed:
            self.unplayed = False
            self.ui.label.setText("Select the relationship you just heard")
            self.ui.replay_button.setText("Replay Chords")
            self.ui.output_label.setText("")

        play_chord(self.key_root, CHORDS_DICT['MAJOR_CHORD'], STRINGS)
        play_chord(self.chord_root, CHORDS_DICT[self.chord_quality], STRINGS)

    def relation_button_clicked(self, response):
        self.num_attempted += 1
        if response == self.answer:
            self.ui.output_label.setText("Correct! Get ready for the next one")
            self.ui.output_label.setStyleSheet("color:green")
            self.num_correct += 1
            self.chord_relation_test_setup()
        else:
            self.ui.output_label.setText("Sorry that wasn't correct :( Try again")
            self.ui.output_label.setStyleSheet("color:red")

        self.ui.score_label.setText("Score: {}/{} ({}%)".format(self.num_correct, self.num_attempted, round(self.num_correct / self.num_attempted * 100, 2)))

    def skip_button_clicked(self):
        output_answer = (self.chord_quality.split('_')[0]).title() + ' ' + (self.chord_interval.split('_')[1]).lower()
        self.ui.output_label.setText("That was a {}".format(output_answer))
        self.ui.output_label.setStyleSheet("color:black")
        self.chord_relation_test_setup()

    def update_selected(self, b):
        switch = b.isChecked()
        self.relation_buttons[b.accessibleName()].setEnabled(switch)
        chord_interval, chord_quality = b.accessibleName().split(' ')

        if switch:
            self.allowed_chords[chord_interval].add(chord_quality)

            if self.no_relations_selected:
                self.reenable_everything()
        else:
            self.allowed_chords[chord_interval].remove(chord_quality)

            disable_switch = True
            for ci in self.allowed_chords:
                if len(self.allowed_chords[ci]) > 0:
                    disable_switch = False
                    break
            if disable_switch:
                self.disable_everything()
            else:
                self.update_checkboxes()
                self.skip_button_clicked()

    def update_all(self):
        switch = self.ui.select_all.isChecked()
        for b in self.ui.select_buttonGroup.buttons():
            b.setChecked(switch)
            self.relation_buttons[b.accessibleName()].setEnabled(switch)
            chord_interval, chord_quality = b.accessibleName().split(' ')
            if switch:
                self.allowed_chords[chord_interval].add(chord_quality)
            else:
                self.allowed_chords[chord_interval].remove(chord_quality)

        if switch:
            if self.no_relations_selected:
                self.reenable_everything()
            self.skip_button_clicked()
        else:
            self.disable_everything()

    def update_checkboxes(self):
        switch = True
        for b in self.ui.select_buttonGroup.buttons():
            if not b.isChecked():
                switch = False
                break
        self.ui.select_all.setChecked(switch)

    def disable_everything(self):
        self.no_relations_selected = True

        # self.key_root = None
        # self.chord_root = None
        # self.chord_interval = None
        # self.chord_quality = None
        # self.answer = None

        self.ui.skip_button.setEnabled(False)
        self.ui.replay_button.setEnabled(False)

        self.ui.output_label.setText("Please select at least one relationship")
        self.ui.output_label.setStyleSheet("color:red")

    def reenable_everything(self):
        self.no_relations_selected = False

        self.ui.skip_button.setEnabled(True)
        self.ui.replay_button.setEnabled(True)

        self.ui.output_label.setText("")

        self.chord_relation_test_setup()


    def close_window(self):
        if self.parent_window:
            self.parent_window.show()
        self.close()


if __name__ == "__main__":
    try:
        setup_pygame_midi(STRINGS)
        app = QApplication([])
        ChordRelationTest = ChordRelationTestWindow()
        ChordRelationTest.show()
        app.exec_()
    finally:
        close_pygame_midi()