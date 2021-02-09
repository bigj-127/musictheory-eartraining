from read_freqs import *
import winsound as ws
from time import sleep

def scale(root, steps, arpeggio=None, reverse=True):

    index = notes.index(root)
    scale_notes = [root]
    for step in steps:
        index += step
        scale_notes.append(notes[index])

    if reverse:
        for step in reversed(steps):
            index -= step
            scale_notes.append(notes[index])

    if arpeggio:
        for step in arpeggio:
            index += step
            scale_notes.append(notes[index])

        for step in reversed(arpeggio):
            index -= step
            scale_notes.append(notes[index])

    print('Notes:')
    print(scale_notes)

    for note in scale_notes:
        ws.Beep(note_freqs[note], 1000)

def major_scale(root):
    print('Major Scale')
    steps = [2,2,1,2,2,2,1]
    arpeggio = [4,3,5]
    scale(root, steps, arpeggio)

def harmonic_minor_scale(root):
    print('Harmonic Minor Scale')
    steps = [2,1,2,2,1,3,1]
    arpeggio = [3,4,5]
    scale(root, steps, arpeggio)

def natural_minor_scale(root):
    print('Natural Minor Scale')
    steps = [2,1,2,2,1,2,2]
    arpeggio = [3,4,5]
    scale(root, steps, arpeggio)

def melodic_minor_scale(root):
    print('Melodic Minor Scale')
    steps = [2,1,2,2,2,2,1,-2,-2,-1,-2,-2,-1,-2]
    arpeggio = [3,4,5]
    scale(root, steps, arpeggio, reverse=False)

def pentatonic_scale(root):
    print('Pentatonic Scale')
    steps = [2,2,3,2,3]
    scale(root, steps)

def blues_scale(root):
    print('Blues Scale')
    steps = [3,2,1,1,3,2]
    scale(root, steps)

def mary(root):
    print('Mary Had a Little Lamb')
    steps = [-2,-2,2,2,0,0,-2,0,0,2,3,0,-3,-2,-2,2,2,0,0,0,-2,0,2,-2,-2]
    scale(root, steps)

def song(root):
    # I Feel It Coming
    steps = [-3,-4,2,0,5,-3,-4,2,-2,0,7,-3,-4,2,0,5,-3,-4,2,-2,0]
    scale(root, steps)

root = 'C5'
major_scale(root)
# harmonic_minor_scale(root)
# natural_minor_scale(root)
# melodic_minor_scale(root)
# blues_scale(root)
# pentatonic_scale(root)
# song(root)