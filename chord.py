roman_numerals = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
}

chord_structure_base_quality = {
    "triad": "5",
    "sus2": "5",
    "sus4": "5",
    "7th": "7",
    "7th sus2": "7",
    "7th sus4": "7",
    "9th": "9"
}

chord_structure_extension_notation = {
    "triad": "",
    "sus2": "sus2",
    "sus4": "sus4",
    "7th": "",
    "7th sus2": "sus2",
    "7th sus4": "sus2",
    "9th": ""
}

inversion_bass_quality = {
    ("5", "1"): "⁶",
    ("5", "2"): "⁶₄",
    ("7", "1"): "⁶₅",
    ("7", "2"): "⁴₃",
    ("7", "3"): "⁴₂"
}

applied_chord_quality = {
    "IV": "IV",
    "V": "V",
    "VII": "vii°"
}

class Chord:
    def __init__(self, root, scale_degree, quality, inversion, applied):
        self.root = root
        self.scale_degree = scale_degree
        self.quality = quality
        self.base_quality = chord_structure_base_quality[quality]
        self.applied = applied
        self.inversion = inversion
    
    def get_quality(self):
        quality_notation = ""
        if (self.inversion != 0):
            quality_notation = inversion_bass_quality[(self.base_quality, str(self.inversion))]
        else:
            quality_notation = chord_structure_base_quality[self.quality] if chord_structure_base_quality[self.quality] != "5" else ""
        
        extention = chord_structure_extension_notation[self.quality]

        return quality_notation + extention
    
    def roman_numeral(self):
        output = ""

        quality = self.get_quality()

        if self.applied != 0:
            output += f"{applied_chord_quality[roman_numerals[self.applied]]}{quality}/{roman_numerals[self.scale_degree]}"
        else:
            output += f"{roman_numerals[self.scale_degree]}{quality}"
        
        return output
    
    def __repr__(self):
        return self.roman_numeral()
