from chord import ScaleChord, ChromaticChord
from theory import ALL_NOTES, SCALES, CHORD_STRUCTURES, CHROMATIC_CHORD_STRUCTURES

def build_scale_chord(chord_structure, bass_note, scale_notes):
    note_index = scale_notes.index(bass_note)
    return [scale_notes[(note_index + interval) % 7] for interval in chord_structure]

def build_chromatic_chord(chord_structure, bass_note):
    note_index = ALL_NOTES.index(bass_note)
    return [ALL_NOTES[(note_index + interval) % 12] for interval in chord_structure]

def get_notes_of_scale(tonic, scale_name):
    tonic_note_index = ALL_NOTES.index(tonic)
    return [ALL_NOTES[(tonic_note_index + interval) % 12] for interval in SCALES[scale_name]]

def chord_to_structure(chord):
    chord_structure = []

    offset = ALL_NOTES.index(chord[0]) # Offset by the first note
    previous_note_integer = None
    for note in chord:
        note_integer = ALL_NOTES.index(note) - offset

        if previous_note_integer != None and note_integer < previous_note_integer:
            note_integer += 12 # Increase the note up an octave
        
        chord_structure.append(note_integer)
        previous_note_integer = note_integer
    
    print(chord_structure)

    return

def get_matching_scale_chords(chord_notes, chord_structure_name, scale_degree, applied_degree, notes, bass_note, top_note):
    matches = []
    notes_num = len(chord_notes)
    max_inversions = notes_num if notes_num <= 4 else 1

    for inversion in range(max_inversions):
        inverted_chord = chord_notes[inversion:] + chord_notes[:inversion]
        chord_bass_note = inverted_chord[0]
        chord_top_note = inverted_chord[-1]

        if ((bass_note == None or chord_bass_note == bass_note) and
            (top_note == None or chord_top_note == top_note) and
            (notes == None or all(note in chord_notes for note in notes))):
            matches.append(ScaleChord(chord_notes[0], scale_degree, chord_structure_name, inversion, applied_degree, inverted_chord))
    
    return matches

def get_matching_chromatic_chords(chord_notes, chord_structure_name, notes, bass_note, top_note):
    matches = []
    notes_num = len(chord_notes)
    max_inversions = notes_num if notes_num <= 4 else 1

    for inversion in range(max_inversions):
        inverted_chord = chord_notes[inversion:] + chord_notes[:inversion]
        chord_bass_note = inverted_chord[0]
        chord_top_note = inverted_chord[-1]

        if ((bass_note == None or chord_bass_note == bass_note) and
            (top_note == None or chord_top_note == top_note) and
            (notes == None or all(note in chord_notes for note in notes))):
            matches.append(ChromaticChord(chord_notes[0], chord_structure_name, inversion, inverted_chord))
    
    return matches

def search_chromatic_chords(bass_note, top_note, notes):
    chords = []
    for chord_structure_name, chord_structure in CHROMATIC_CHORD_STRUCTURES.items():
        for note in ALL_NOTES:
            chord_notes = build_chromatic_chord(chord_structure, note)

            chords.extend(
                get_matching_chromatic_chords(chord_notes, chord_structure_name, notes, bass_note, top_note)
            )
    
    print("----Chords----")
    if (chords == None):
        print("None")
    else:
        for chord in chords:
            print(chord)

def search_scale_chords(bass_note, top_note, notes, tonic, scale_name, applied, roman):
    diatonic_chords = []
    applied_chords = []
    scale_notes = get_notes_of_scale(tonic, scale_name)

    # Diatonic Chords
    for chord_structure_name, chord_structure in CHORD_STRUCTURES.items():
        for scale_degree, note in enumerate(scale_notes, start=1):
            diatonic_chord_notes = build_scale_chord(chord_structure, note, scale_notes)
            
            diatonic_chords.extend(
                get_matching_scale_chords(diatonic_chord_notes, chord_structure_name, scale_degree, 0, notes, bass_note, top_note)
            )

            if not applied:
                continue

            # Get the major scale where the note is the tonic
            applied_scale_notes = get_notes_of_scale(note, "major")

            # Get the IV of, V of, and vii of chords
            for applied_scale_degree, applied_note in enumerate(applied_scale_notes, start=1):
                if (applied_scale_degree not in [4,5,7]):
                    continue
                
                applied_chord_notes = build_scale_chord(chord_structure, applied_note, applied_scale_notes)
                
                applied_chords.extend(
                    get_matching_scale_chords(applied_chord_notes, chord_structure_name, scale_degree, applied_scale_degree, notes, bass_note, top_note)
                )
    
    print("----Diatonic Chords----")
    if (diatonic_chords == None):
        print("None")
    else:
        for chord in diatonic_chords:
            if (roman == True):
                print(chord.display_roman_numerals())
            else:
                print(chord)

    if applied:
        print("----Applied Chords----")
        if (applied_chords == None):
            print("None")
        else:
            for chord in applied_chords:
                print(chord)

    return diatonic_chords + applied_chords
