notes = ['A', 'A#/Bb', 'B', 'C', 'C#/Db', 'D', 'D#/Eb', 'E', 'F', 'F#/Gb', 'G', 'G#/Ab']

class Note():

    def __init__(self, name, accidental=0):
        self.name = name[0]

        if len(name) > 2:
            name = break_enharmonic(name)
        if len(name) > 1:
            if name[1] == 'b':
                self.accidental = -1
            if name[1] == '#':
                self.accidental = 1

    def __add__(self, other):
        if type(other) == int:
            index = notes.index(self.name)
            index += other
            index //= len(notes)
            return Note(notes[index])

    def __sub__(self, other):
        return self()

    def __str__(self):
        sign = 'b' if accidental < 0 else '#'
        sign *= abs(accidental)

        return name + sign


