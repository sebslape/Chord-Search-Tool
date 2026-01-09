import argparse
from search_for_chord import search_for_chord

def main():
    parser = argparse.ArgumentParser(description="A command-line utility to search for chords.")
    parser.add_argument("bass_note", help="The bass note to look for in chords.")
    parser.add_argument("key", help="The key of the song.")
    parser.add_argument("scale", help="The scale of the song.")
    parser.add_argument("-t", "--top-note", help="The top note to look for in chords.")

    args = parser.parse_args()
    search_for_chord(args.bass_note, args.top_note, args.key, args.scale)

if __name__ == "__main__":
    main()