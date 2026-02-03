from theory import CHORD_STRUCTURE_BASE_QUALITY, CHORD_STRUCTURE_EXTENSION_NOTATION, INVERSION_BASS_QUALITY, APPLIED_CHORD_QUALITY, ROMAN_NUMERALS

from utility import get_ordinal

class Chord:
    def __init__(self, root, quality, inversion, notes):
        self.root = root
        self.quality = quality
        self.inversion = inversion
        self.notes = notes
    
    def __str__(self):
        pass

class ChromaticChord(Chord):
    def __init__(self, root, quality, inversion, notes):
        super().__init__(root, quality, inversion, notes)
    
    def __str__(self):
        notes_list = ', '.join(self.notes)
        if self.inversion > 0:
            return f"{self.root} {self.quality} {get_ordinal(self.inversion)} inversion [{notes_list}]"
        else:
            return f"{self.root} {self.quality} [{notes_list}]"

class ScaleChord(Chord):
    def __init__(self, root, scale_degree, quality, inversion, applied, notes):
        super().__init__(root, quality, inversion, notes)
        self.base_quality = CHORD_STRUCTURE_BASE_QUALITY[quality]
        self.scale_degree = scale_degree
        self.applied = applied
    
    def get_quality(self):
        quality_notation = ""
        if (self.inversion != 0):
            quality_notation = INVERSION_BASS_QUALITY[(self.base_quality, str(self.inversion))]
        else:
            quality_notation = CHORD_STRUCTURE_BASE_QUALITY[self.quality] if CHORD_STRUCTURE_BASE_QUALITY[self.quality] != "5" else ""
        
        extention = CHORD_STRUCTURE_EXTENSION_NOTATION[self.quality]

        return quality_notation + extention
    
    def get_roman_numeral(self):
        output = ""

        if self.applied != 0:
            output += f"{APPLIED_CHORD_QUALITY[ROMAN_NUMERALS[self.applied]]}/{ROMAN_NUMERALS[self.scale_degree]}"
        else:
            output += f"{ROMAN_NUMERALS[self.scale_degree]}"
        
        return output

    def get_roman_numeral_with_quality(self):
        output = ""
        quality = self.get_quality()

        if self.applied != 0:
            output += f"{APPLIED_CHORD_QUALITY[ROMAN_NUMERALS[self.applied]]}{quality}/{ROMAN_NUMERALS[self.scale_degree]}"
        else:
            output += f"{ROMAN_NUMERALS[self.scale_degree]}{quality}"
        
        return output
    
    def display_roman_numerals(self):
        notes_list = ', '.join(self.notes)
        return f"{self.get_roman_numeral_with_quality()} [{notes_list}]"
    
    def __str__(self):
        notes_list = ', '.join(self.notes)
        if self.inversion > 0:
            return f"{self.root} {self.quality} ({self.get_roman_numeral()}) {get_ordinal(self.inversion)} inversion [{notes_list}]"
        else:
            return f"{self.root} {self.quality} ({self.get_roman_numeral()}) [{notes_list}]"