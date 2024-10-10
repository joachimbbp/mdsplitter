import os
import sys
main_note_path = sys.argv[1]

def dict_from_notes(main_text):
    notes = {}
    for note in main_text.split("\n\n"):
        (raw_title, body) = note.split("**\n")
        title = raw_title[2:-1]
        notes[title] = body
    return notes

def write_note(title, body, base_path):
    with open(f"{base_path}/{title}.md", 'w') as new_note:
        new_note.write(body)

def rewrite_main_note(notes, main_note_path):
    new_body_text = ""
    for note in notes:
        new_body_text += (f"- [[{note}]]\n")
    print(new_body_text)
    with open(main_note_path, 'w') as main_note:
        main_note.write(new_body_text) #weird that we don't need to overwrite the og note explicitly

with open(main_note_path, 'r') as main_note: #r+ for writing too
    notes = dict_from_notes(main_note.read())
    for note in notes:
        write_note(note, notes[note], os.path.dirname(main_note_path))
rewrite_main_note(notes, main_note_path)

print(notes)