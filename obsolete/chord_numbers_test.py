from random import randint, choice
from constants import MAJOR_SCALES_DICT

# def read_in_scales(white_notes_only=False):
#     allowed_scales = {}
#     with open('scales.txt', 'r') as f:
#         lines = f.readlines()
#         for line in lines:
#             root, scale = line.split(':')
#             if white_notes_only and len(root) > 1:
#                 continue
#             scale = scale.rstrip('\n')
#             scale = scale.replace(' ', '')
#             scale = scale.split(',')

#             allowed_scales[root] = scale

#     return allowed_scales

wn_input = input("Would you like only white note keys? (y/n): ")
ec_input = input("Would you like only easy chord intervals? (y/n): ")
print()

white_notes_only = wn_input == 'y'
lower, upper = (4, 6) if ec_input == 'y' else (2, 8)

if white_notes_only:
    allowed_scales = [k for k in MAJOR_SCALES_DICT.keys() if len(k) == 1]
else:
    allowed_scales = list(MAJOR_SCALES_DICT.keys())

while True:
    selected_key = choice(allowed_scales)
    print('Key: ', selected_key)
    chord = randint(lower, upper)
    print('Chord: ', chord)
    answer = MAJOR_SCALES_DICT[selected_key][chord - 1]
    # print('Answer: ', answer)
    print("What chord corresponds to the interval above for this key?")
    response = input("Response: ")

    if response == 'q':
        print('The correct answer was', answer, '\n')
        break
    elif response == 'n':
        print('The correct answer was', answer, '\n')
        continue
    elif response == answer:
        print('Correct!\n')
        # print('Time for the next one')
    else:
        print('Sorry the correct answer was', answer, '\n')