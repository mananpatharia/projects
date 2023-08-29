class NoteTakingApp:
    def __init__(self):
        self.notes = []

    def run(self):
        while True:
            print("\n=== Note Taking App ===")
            print("1. List Notes")
            print("2. Add Note")
            print("3. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                self.list_notes()
            elif choice == "2":
                self.add_note()
            elif choice == "3":
                print("Exiting the Note Taking App. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a valid option.")

    def list_notes(self):
        if not self.notes:
            print("No notes available.")
        else:
            print("=== Notes ===")
            for idx, note in enumerate(self.notes, start=1):
                print(f"{idx}. {note}")

    def add_note(self):
        note_text = input("Enter your note: ")
        self.notes.append(note_text)
        print("Note added successfully!")

if __name__ == "__main__":
    app = NoteTakingApp()
    app.run()
