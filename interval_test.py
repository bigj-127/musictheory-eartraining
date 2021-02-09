from pygame_midi import *
from random import choice, randint

interval_lens = {'m2', 'M2', 'm3', 'M3', 'P4', 'TT', 'P5', 'm6', 'M6', 'm7', 'M7', 'P8'}

def interval_test():
    root_note_index = randint(0,25)
    root_note = NOTES[12 + root_note_index]
    interval = choice(MEDIUM_INTERVALS)
    interval_note = NOTES[12 + root_note_index + INTERVALS_DICT[interval]]

    play_note(root_note, STRINGS)
    play_note(interval_note, STRINGS)

    print('Enter the interval you just heard')
    print("or enter 'H' for help")

    while True:
        response = input('Enter here: ')

        if response == 'Q':
            print('That interval was ', interval)
            print('Quitting...')
            return False

        elif response == 'N':
            print('That interval was ', interval)
            return True

        elif response == 'R':
            print('Replaying the notes')
            play_note(root_note, STRINGS)
            play_note(interval_note, STRINGS)
            print()

        elif response in interval_lens:
            if response == interval:
                print('Correct!')
                print('Get ready for the next interval')
                print()
                return True

            else:
                print("Sorry that wasn't correct. Try again")
                print("Enter 'R' to hear the notes again")
                print()


        elif response == 'H':
            print('Enter the interval between the two notes you heard')
            print("The options are: \n\t'm2': minor second\n\t'M2': major second\n\t'm3': minor third\n\t'M3': major third\n\t'P4': perfect fourth\n\t'TT': tritone\n\t'P5': perfect fifth\n\t'm6': minor sixth\n\t'M6': major sixth\n\t'm7': minor seventh\n\t'M7': major seventh\n\t'P8': octave")
            print("Enter 'R' to hear the notes again")
            print("Enter 'N' to hear a new interval")
            print("Enter 'Q' to quit")
            print()


        else:
            print('You entered something invalid')
            print("Please enter an interval or enter 'H' for help")
            print()


def main():
    try:
        setup_pygame_midi(STRINGS)
        while interval_test():
            pass
    finally:
        close_pygame_midi()


if __name__ == '__main__':
    main()