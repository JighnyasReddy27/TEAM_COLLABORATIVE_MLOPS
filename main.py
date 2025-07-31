def add_note():
    note = input("Enter your new note: ")
    with open(NOTES_FILE, "a") as f:
        f.write(note + "\n")
    print("Note added!")

def main():
    add_note()
