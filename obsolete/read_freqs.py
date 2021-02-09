import csv

notes = []
note_freqs = {}

with open('note_frequencies.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        note, frequency = line[0], round(float(line[1]))
        if frequency > 37 and frequency < 32767:
            notes.append(note)
            note_freqs[note] = frequency