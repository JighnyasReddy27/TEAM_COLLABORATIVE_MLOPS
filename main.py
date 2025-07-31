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
    add_note()
    search_notes()
