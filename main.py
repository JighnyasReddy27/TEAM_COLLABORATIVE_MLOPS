import os

NOTES_FILE = "notes.txt"

def delete_note():
    # notes = read_notes()
    if not notes:
        print("No notes to delete.")
        return
    view_notes()
    try:
        num = int(input("Enter the note number to delete: "))
        if 1 <= num <= len(notes):
            removed = notes.pop(num - 1)
            with open(NOTES_FILE, "w") as f:
                for note in notes:
                    f.write(note + "\n")
            print(f"Deleted note: {removed}")
        else:
            print("Invalid note number.")
    except ValueError:
        print("Please enter a valid number.")

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
    delete_note()

if __name__ == "__main__":
    main()