# Chord-Search-Tool

Chord Search Tool is a Python command-line application designed for musicians to identify chords based on different constraints.

## Features

- **Chromatic Mode**: Search through all chromatic chords for chords containing at least three specified notes.
- **Scale Mode**: Search through all chords in a specific key and scale containing at least one specified note.
- **Applied Chords**: Support for searching secondary/applied chords within a scale.
- **Roman Numeral Support**: Toggle between standard chord names and Roman Numeral analysis.
- **Voicing Constraints**: Filter chords by their top and bottom notes.
- **Inversion Aware**: Searches through all inversions of chords to find chords that fit the specified filters.

## Installation

Clone the repository using git:
```bash
git clone https://github.com/sebslape/Chord-Search-Tool.git
cd Chord-Search-Tool
```

## Usage

Run the tool using Python:
```bash
python3 main.py [mode] [arguments] [flags]
```

### Chromatic Mode

Search for all chords that fit the constraints given.

| Flag | Long Form | Description |
| :--- | :--- | :--- |
| `-n` | `--notes` | A list of notes that the chords must contain (space-separated). |
| `-t` | `--top` | The note that must be at the top of the chord. |
| `-b` | `--bottom` | The note that must be at the bottom of the chord. |

**Note:** This mode requires at least 3 notes to be provided via the `-n` flag.

### Scale Mode

Search for all chords that fit the constraints given within a specific key.

**Positional Arguments:** `tonic` (e.g., C, A#) and `scale` (e.g., major, minor).

| Flag | Long Form | Description |
| :--- | :--- | :--- |
| `-n` | `--notes` | A list of notes that the chords must contain (space-separated). |
| `-t` | `--top` | The note that must be at the top of the chord. |
| `-b` | `--bottom` | The note that must be at the bottom of the chord. |
| `-a` | `--applied` | Search for applied (secondary) chords. |
| `-r` | `--roman` | Display results using Roman Numeral analysis. |

**Note:** This mode requires at least 1 note to be provided via the `-n` flag, `-t` flag, or `-b` flag.

## Examples

Search for a chromatic chord containing C, E, and G with E on top:

```bash
python3 main.py chromatic -n C E G -t E
```

Search for a chord in F Major with a G on the bottom:

```bash
python3 main.py scale F major -b G
```