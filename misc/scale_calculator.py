"""
File: minor_key.py
Author: Nathaniel Wise
Date: 17 OCT 2021
Section: 32
Email: nwise2@umbc.edu
Description: Calculates a harmonic minor scale starting on a user-supplied note.
"""

MUSICAL_NOTES = ['C', 'D\u266d', 'D', 'E\u266d', 'E', 'F', 'G\u266d', 'G', 'A\u266d', 'A', 'B\u266d', 'B']

HARMONIC_MINOR_SCALE = [2, 1, 2, 2, 1, 3, 1]  # semitone = 1, tone = 2, trisemitone = 3
MAJOR_SCALE = [2, 2, 1, 2, 2, 2, 1]
NATURAL_MINOR_SCALE =  [2, 1, 2, 2, 1, 2, 2]
ASCENDING_MELODIC_MINOR_SCALE = [2, 1, 2, 2, 2, 2, 1]
DESCENDING_MELODIC_MINOR_SCALE = [2, 2, 1, 2, 2, 1, 2]


def get_note(user_note):
    is_note = False

    while not is_note:
        user_note = user_note.upper()

        if " FLAT" in user_note:  # Converts "FLAT" to "♭ (\u266d)".
            user_note = user_note.split(" ")
            user_note.remove("FLAT")
            user_note.append("\u266d")
            user_note = "".join(user_note)

        if user_note in MUSICAL_NOTES:
            is_note = True

        elif user_note == "QUIT":  # Let them stop
            return user_note

        else:  # Force the user to enter a note from the scale.
            print("There is no starting note %s." % user_note)
            user_note = input("Enter a starting note (C, D flat): ")

    return user_note


def starting_index(user_note):  # Figure out where in MUSICAL_NOTES to start
    for i in range(len(MUSICAL_NOTES)):
        if user_note == MUSICAL_NOTES[i]:
            return i
        else:
            i += 1


def major_scale(first_note):
    musical_notes = MUSICAL_NOTES * 2  # Elongate scale to avoid range errors
    user_note_list = [musical_notes[first_note]]  # Start list to keep notes in scale
    next_note = first_note  # Rename to avoid confusion
    for i in range(0, len(MAJOR_SCALE)):
        user_note_list = user_note_list + [musical_notes[next_note + MAJOR_SCALE[i]]]  # Put next note in list
        next_note = next_note + int(MAJOR_SCALE[i])  # Interval dictated by major scale sequence
    return user_note_list


def natural_minor_scale(first_note):
    musical_notes = MUSICAL_NOTES * 2  # Elongate scale to avoid range errors
    user_note_list = [musical_notes[first_note]]  # Start list to keep notes in scale
    next_note = first_note  # Rename to avoid confusion
    for i in range(0, len(NATURAL_MINOR_SCALE)):
        user_note_list = user_note_list + [musical_notes[next_note + NATURAL_MINOR_SCALE[i]]]  # Put next note in list
        next_note = next_note + int(NATURAL_MINOR_SCALE[i])  # Interval dictated by natural minor scale sequence
    return user_note_list


def harmonic_minor_scale(first_note):
    musical_notes = MUSICAL_NOTES * 2  # Elongate scale to avoid range errors
    user_note_list = [musical_notes[first_note]]  # Start list to keep notes in scale
    next_note = first_note  # Rename to avoid confusion
    for i in range(0, len(HARMONIC_MINOR_SCALE)):
        user_note_list = user_note_list + [musical_notes[next_note + HARMONIC_MINOR_SCALE[i]]]  # Put next note in list
        next_note = next_note + int(HARMONIC_MINOR_SCALE[i])  # Interval dictated by harmonic minor scale sequence
    return user_note_list


def ascending_melodic_minor_scale(first_note):
    musical_notes = MUSICAL_NOTES * 2  # Elongate scale to avoid range errors
    user_note_list = [musical_notes[first_note]]  # Start list to keep notes in scale
    next_note = first_note  # Rename to avoid confusion
    for i in range(0, len(ASCENDING_MELODIC_MINOR_SCALE)):
        user_note_list = user_note_list + [musical_notes[next_note + ASCENDING_MELODIC_MINOR_SCALE[i]]]  # Put next note in list
        next_note = next_note + int(ASCENDING_MELODIC_MINOR_SCALE[i])  # Interval dictated by ascending melodic minor scale sequence
    return user_note_list


def descending_melodic_minor_scale(first_note):
    musical_notes = MUSICAL_NOTES * 2  # Elongate scale to avoid range errors
    user_note_list = [musical_notes[first_note]]  # Start list to keep notes in scale
    next_note = first_note  # Rename to avoid confusion
    for i in range(0, len(DESCENDING_MELODIC_MINOR_SCALE)):
        user_note_list = user_note_list + [musical_notes[next_note + DESCENDING_MELODIC_MINOR_SCALE[i]]]  # Put next note in list
        next_note = next_note + int(DESCENDING_MELODIC_MINOR_SCALE[i])  # Interval dictated by descending melodic minor scale sequence
    return user_note_list


if __name__ == '__main__':

    print("1. Major Scale")
    print("2. Natural Minor Scale")
    print("3. Harmonic Minor Scale")
    print("4. Ascending Melodic Minor Scale")
    print("5. Descending Melodic Minor Scale")

    end_program = False
    while not end_program:  # Keep going until user enters "QUIT"
        which_scale = int(input("What scale would you like to calculate? "))
        user_note = get_note(input("Enter a starting note (C, D flat): "))

        if user_note == "QUIT":
            end_program = True

        else:
            if which_scale == 1:
                start = starting_index(user_note)  # Find out what note to start on
                final_scale = major_scale(start)

            elif which_scale == 2:
                start = starting_index(user_note)  # Find out what note to start on
                final_scale = natural_minor_scale(start)

            elif which_scale == 3:
                start = starting_index(user_note)  # Find out what note to start on
                final_scale = harmonic_minor_scale(start)

            elif which_scale == 4:
                start = starting_index(user_note)  # Find out what note to start on
                final_scale = ascending_melodic_minor_scale(start)
                5
            elif which_scale == 5:
                start = starting_index(user_note)  # Find out what note to start on
                final_scale = descending_melodic_minor_scale(start)
            user_scale = " ".join(final_scale)
            print(user_scale)

    # harmonic_minor_scale(starting_index(user_note))
    # print(" ".join(harmonic_minor_scale(starting_index(get_note(input("Enter a starting note (C, D flat): "))))))
