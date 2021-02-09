from random import choice

from pygame_midi import *

allowed_combinations = {'PERFECT_4TH':['MAJOR_CHORD'], 'PERFECT_5TH':['MAJOR_CHORD'], 'MAJOR_6TH':['MINOR_CHORD'], 'MAJOR_2ND':['MINOR_CHORD']}

def chord_identification_test():
    answer = choice(EASY_CHORDS_LIST)
    selected_chord = CHORDS_DICT[answer]

    # root_note = choice(NOTES[:-1 * selected_chord[-1]])
    root_note = choice(BASIC_NOTES)

    print(answer)
    play_arpeggio(root_note, selected_chord, STRINGS)
    play_chord(root_note, selected_chord, STRINGS)
    time.sleep(1)

def chord_relation_test():
    interval = choice(EASY_INTERVAL_CHORDS)

    chord_quality = choice(allowed_combinations[interval])
    chord_ints = CHORDS_DICT[chord_quality]

    root1 = root_note = choice(BASIC_NOTES)
    root2 = root1 + INTERVALS_DICT[interval]

    play_chord(root1, MAJOR_CHORD, STRINGS)
    time.sleep(1)
    play_chord(root2, chord_ints, STRINGS)
    time.sleep(1)
    play_chord(root1, MAJOR_CHORD, STRINGS)

    # print(interval)
    # print(chord_quality)
    print(chord_quality.split('_')[0], interval.split('_')[1])


if __name__ == '__main__':
    try:
        setup_pygame_midi(STRINGS)
        chord_relation_test()
    finally:
        close_pygame_midi()

