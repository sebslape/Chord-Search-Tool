from theory import CHORD_STRUCTURE_BASE_QUALITY, CHORD_STRUCTURE_EXTENSION_NOTATION, INVERSION_BASS_QUALITY, APPLIED_CHORD_QUALITY

ROMAN_NUMERALS = {
    1: "I",
    2: "II",
    3: "III",
    4: "IV",
    5: "V",
    6: "VI",
    7: "VII",
}

class Chord:
    def __init__(self, root, scale_degree, quality, inversion, applied):
        self.root = root
        self.scale_degree = scale_degree
        self.quality = quality
        self.base_quality = CHORD_STRUCTURE_BASE_QUALITY[quality]
        self.applied = applied
        self.inversion = inversion
    
    def get_quality(self):
        quality_notation = ""
        if (self.inversion != 0):
            quality_notation = INVERSION_BASS_QUALITY[(self.base_quality, str(self.inversion))]
        else:
            quality_notation = CHORD_STRUCTURE_BASE_QUALITY[self.quality] if CHORD_STRUCTURE_BASE_QUALITY[self.quality] != "5" else ""
        
        extention = CHORD_STRUCTURE_EXTENSION_NOTATION[self.quality]

        return quality_notation + extention
    
    def roman_numeral(self):
        output = ""

        quality = self.get_quality()

        if self.applied != 0:
            output += f"{APPLIED_CHORD_QUALITY[ROMAN_NUMERALS[self.applied]]}{quality}/{ROMAN_NUMERALS[self.scale_degree]}"
        else:
            output += f"{ROMAN_NUMERALS[self.scale_degree]}{quality}"
        
        return output
    
    def __repr__(self):
        return self.roman_numeral()
