import os

NOTES_FILE = "notes.txt"


def read_notes():
    if os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "r") as f:
            return [line.strip() for line in f]
    return []

def view_notes():
    notes = read_notes()
    if not notes:
        print("No notes found.")
    else:
        print("Your notes:")
        for idx, note in enumerate(notes, 1):
            print(f"{idx}. {note}")

def add_note():
    note = input("Enter your new note: ")
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    print("Note added!")

def search_notes():
    keyword = input("Enter a keyword to search for: ").lower()
    notes = read_notes()
    matches = [note for note in notes if keyword in note.lower()]
    if matches:
        print("Found notes:")
        for idx, note in enumerate(matches, 1):
            print(f"{idx}. {note}")
    else:
        print("No notes found containing that keyword.")

def main():
    # TEMP for testing; comment/uncomment as needed
    view_notes()
    add_note()
    search_notes()

if __name__ == "__main__":
    main()