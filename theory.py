ALL_NOTES = ["C","C#","D","D#","E","F","F#","G","G#","A","A#","B"]

SCALES = {
    "major": [0, 2, 4, 5, 7, 9, 11],
    "minor": [0, 2, 3, 5, 7, 8, 10],
    "dorian": [0, 2, 3, 5, 7, 9, 10],
    "phrygian": [0, 1, 3, 5, 7, 8, 10],
    "lydian": [0, 2, 4, 6, 7, 9, 11],
    "mixolydian": [0, 2, 4, 5, 7, 9, 10],
    "locrian": [0, 1, 3, 5, 6, 8, 10]
}

# Chords built using the scale notes
CHORD_STRUCTURES = {
    "triad": [0, 2, 4],
    "sus2": [0, 1, 4],
    "sus4": [0, 3, 4],
    "7th": [0, 2, 4, 6],
    "7th sus2": [0, 1, 4, 6],
    "7th sus4": [0, 3, 4, 6],
    "9th": [0, 2, 4, 6, 8],
}

CHROMATIC_CHORD_STRUCTURES = {
    "major": [0, 4, 7],
    "minor": [0, 3, 7],
    "diminished": [0, 3, 6],
    "augmented": [0, 4, 8],
    "sus2": [0, 2, 7],
    "sus4": [0, 5, 7],
    "major 7th": [0, 4, 7, 11],
    "minor 7th": [0, 3, 7, 10],
    "dominant 7th": [0, 4, 7, 10],
    "major 9th": [0, 4, 7, 11, 14],
    "minor 9th": [0, 3, 7, 10, 14],
    "dominant 9th": [0, 4, 7, 10, 14],
}

CHROMATIC_CHORD_STRUCTURES_NAMES = {
    (0, 4, 7): "major",
    (0, 3, 7): "minor",
    (0, 3, 6): "diminished",
    (0, 4, 8): "augmented",
    (0, 2, 7): "sus2",
    (0, 5, 7): "sus4",
    (0, 4, 7, 11): "major 7th",
    (0, 3, 7, 10): "minor 7th",
    (0, 4, 7, 10): "dominant 7th",
    (0, 4, 7, 11, 14): "major 9th",
    (0, 3, 7, 10, 14): "minor 9th",
    (0, 4, 7, 10, 14): "dominant 9th",
}

CHORD_STRUCTURE_BASE_QUALITY = {
    "triad": "5",
    "sus2": "5",
    "sus4": "5",
    "7th": "7",
    "7th sus2": "7",
    "7th sus4": "7",
    "9th": "9"
}

CHORD_STRUCTURE_EXTENSION_NOTATION = {
    "triad": "",
    "sus2": "sus2",
    "sus4": "sus4",
    "7th": "",
    "7th sus2": "sus2",
    "7th sus4": "sus2",
    "9th": ""
}

INVERSION_BASS_QUALITY = {
    ("5", "1"): "⁶",
    ("5", "2"): "⁶₄",
    ("7", "1"): "⁶₅",
    ("7", "2"): "⁴₃",
    ("7", "3"): "⁴₂"
}

APPLIED_CHORD_QUALITY = {
    "IV": "IV",
    "V": "V",
    "VII": "vii°"
}

ROMAN_NUMERALS = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
}
