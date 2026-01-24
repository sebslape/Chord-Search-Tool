import argparse
from search_for_chord import search_scale_chords, search_chromatic_chords

def main():
    # Create a parent parser and add the top and bottom arguments
    parent_parser = argparse.ArgumentParser(add_help=False)
    parent_parser.add_argument("-t", "--top", type=str, required=False, help="The top note to look for in chords.")
    parent_parser.add_argument("-b", "--bottom", type=str, required=False, help="The bottom note to look for in chords.")
    parent_parser.add_argument("-n", "--notes", nargs="*", required=False)

    parser = argparse.ArgumentParser(description="A command-line utility to search for chords.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # Add the chromatic subparser
    chromatic_parser = subparsers.add_parser(
        "chromatic", 
        parents=[parent_parser], 
        help="Search all chromatic chords"
    )

    # Add the scale subparser
    scale_parser = subparsers.add_parser(
        "scale", 
        parents=[parent_parser], 
        help="Search chords in a scale"
    )
    scale_parser.add_argument("tonic", type=str, help="The tonic of the scale to search through.")
    scale_parser.add_argument("scale", type=str, help="The scale to search through.")
    scale_parser.add_argument("-a", "--applied", action='store_true', required=False)
    
    args = parser.parse_args()

    if (args.command == "scale"):
        # You must choose at least a bottom, top, or a note the chord must contain
        if (args.bottom or args.top or args.notes):
            search_scale_chords(args.bottom, args.top, args.notes, args.tonic, args.scale, args.applied)
        else:
            print("You need to specify at a bottom, top, or a note in a scale mode search.")
    else:
        # You must choose at least 3 notes the chord must contain
        if (args.notes and len(args.notes) >= 3):
            search_chromatic_chords(args.bottom, args.top, args.notes)
        else:
            print("You need to specify at least 3 notes in a chromatic mode search.")

if __name__ == "__main__":
    main()