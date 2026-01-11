from chord import Chord

all_notes = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

scales = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 8, 10],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "phrygian": [0, 1, 3, 5, 7, 8, 10],
    "lydian": [0, 2, 4, 6, 7, 9, 11],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "locrian": [0, 1, 3, 5, 6, 8, 10]
}

def build_chord(chord_structure, bass_note, scale_notes=None):
    note_index = scale_notes.index(bass_note)
    chord = [scale_notes[(note_index + i) % 7] for i in chord_structure]
    
    return chord

# Chords built using the scale notes
scale_chord_structures = {
    "triad": [0, 2, 4],
    "sus2": [0, 1, 4],
    "sus4": [0, 3, 4],
    "7th": [0, 2, 4, 6],
    "7th sus2": [0, 1, 4, 6],
    "7th sus4": [0, 3, 4, 6],
    "9th": [0, 2, 4, 6, 8],
}

def get_notes_of_scale(tonic, scale_name):
    tonic_note_index = all_notes.index(tonic)
    scale = scales[scale_name]
    scale_notes = []

    for scale_note in scale:
        scale_notes.append(all_notes[(scale_note + tonic_note_index) % 12])
    
    return scale_notes

def chord_to_structure(chord):
    chord_structure = []

    offset = all_notes.index(chord[0]) # Offset by the first note
    previous_note_integer = None
    for note in chord:
        note_integer = all_notes.index(note) - offset

        if previous_note_integer != None and note_integer < previous_note_integer:
            note_integer += 12 # Increase the note up an octave
        
        chord_structure.append(note_integer)
        
        previous_note_integer = note_integer
    
    print(chord_structure)

    return

def search_for_chord(bass_note, top_note, tonic, scale_name):
    diatonic_chords = []
    applied_chords = []
    scale_notes = get_notes_of_scale(tonic, scale_name)

    # Diatonic Chords
    for chord_structure_name in scale_chord_structures:
        chord_structure = scale_chord_structures[chord_structure_name]
        for scale_degree, note in enumerate(scale_notes, start=1):
            chord = build_chord(chord_structure, note, scale_notes)

            chord_bass_note = chord[0]
            chord_top_note = chord[-1]

            #print(f"Current chord: {chord}")

            if (chord_bass_note == bass_note and (top_note == None or chord_top_note == top_note)):
                diatonic_chords.append(Chord(chord_bass_note, scale_degree, chord_structure_name, 0, 0))

            # Get inversions too if the chord has four or less notes
            if (len(chord_structure) <= 4):
                for inversion in range(1,len(chord)):
                    inverted_chord = chord[inversion:] + chord[:inversion]
                    #print(f"Current chord: {inverted_chord} inversion {inversion}")

                    chord_bass_note = inverted_chord[0]
                    chord_top_note = inverted_chord[-1]

                    if (chord_bass_note == bass_note and (top_note == None or chord_top_note == top_note)):
                        diatonic_chords.append(Chord(chord_bass_note, scale_degree, chord_structure_name, inversion, 0))
    
    # Applied Chords
    for chord_structure_name in scale_chord_structures:
        chord_structure = scale_chord_structures[chord_structure_name]
        for scale_degree, note in enumerate(scale_notes, start=1):
            # Get the major scale where the note is the tonic
            applied_scale_notes = get_notes_of_scale(note, "major")

            # Get the IV of, V of, and vii of chords
            for applied_scale_degree, applied_note in enumerate(applied_scale_notes, start=1):
                if (applied_scale_degree not in [4,5,7]):
                    continue
                
                chord = build_chord(chord_structure, applied_note, applied_scale_notes)

                chord_bass_note = chord[0]
                chord_top_note = chord[-1]

                #print(f"Current chord: {chord}")

                if (chord_bass_note == bass_note and (top_note == None or chord_top_note == top_note)):
                    applied_chords.append(Chord(chord_bass_note, scale_degree, chord_structure_name, 0, applied_scale_degree))

                # Get inversions too if the chord has four or less notes
                if (len(chord_structure) <= 4):
                    for inversion in range(1,len(chord)):
                        inverted_chord = chord[inversion:] + chord[:inversion]
                        #print(f"Current chord: {inverted_chord} inversion {inversion}")

                        chord_bass_note = inverted_chord[0]
                        chord_top_note = inverted_chord[-1]

                        if (chord_bass_note == bass_note and (top_note == None or chord_top_note == top_note)):
                            applied_chords.append(Chord(chord_bass_note, scale_degree, chord_structure_name, inversion, applied_scale_degree))
    
    print("----Diatonic Chords----")
    print(diatonic_chords if diatonic_chords else "None")

    print("----Applied Chords----")
    print(applied_chords if applied_chords else "None")

    return diatonic_chords + applied_chords
