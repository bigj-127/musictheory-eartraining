import time

import pygame.midi
from constants import *

player = None
channels = {}

def initialize():
    pygame.midi.init()
    global player
    player = pygame.midi.Output(0)

def set_instruments(instruments=None):
    global channels

    if not instruments:
        instruments = SOME_INSTRUMENTS

    if type(instruments) == int:
        instruments = [instruments]

    add_on = len(channels)
    for chann, instr in enumerate(instruments):
        chann += add_on
        if chann > 15:
            print("All available channels have been used")
            break
        channels[instr] = chann
        player.set_instrument(instr, chann)

def setup_pygame_midi(instruments=None):
    initialize()
    set_instruments(instruments)

def close_pygame_midi():
    global player
    del player
    pygame.midi.quit()

def main():
    try:
        setup_pygame_midi()
        play()
    finally:
        close_pygame_midi()

def play_note(note, instr, length=1):
    if type(length) != int or length < 0:
        length = 1

    if instr not in channels:
        set_instruments([instr])
    channel = channels[instr]

    player.note_on(note, 127, channel)
    time.sleep(length)
    player.note_off(note, 127, channel)

def play_scale(root, scale, instr, length=1):
    for n in scale:
        play_note(root + n, instr, length)

def play_arpeggio(root, chord, instr, length=1):
    for n in chord:
        play_note(root + n, instr, length)

def play_chord(root, chord, instr, length=1):
    if type(length) != int or length < 0:
        length = 1

    if instr not in channels:
        set_instruments([instr])
    channel = channels[instr]

    for n in chord:
        player.note_on(root + n, 127, channel)

    time.sleep(length)

    for n in chord:
        player.note_off(root + n, 127, channel)

def play():

    ROOT = C
    INSTR = STRINGS

    play_note(ROOT, INSTR)

    play_scale(ROOT, MAJOR_SCALE, INSTR)
    time.sleep(1)

    play_arpeggio(ROOT, MAJOR_CHORD, INSTR)
    time.sleep(1)

    play_chord(ROOT, MAJOR_CHORD, INSTR)
    time.sleep(1)


if __name__ == '__main__':
    main()