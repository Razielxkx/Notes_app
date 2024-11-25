"""Main program"""

import src.notebook as Notebook
import streamlit as st


def update_textbox():
    """This will update the session state based on the selected value"""
    selected_value = st.session_state.notes_dropdown
    st.session_state.note_title = f"You selected: {selected_value}"


if __name__ == "__main__":

    # st.sidebar("Notes")
    if "note_title" not in st.session_state:
        st.session_state.note_title = ""

    note_title = st.text_input("Note title")
    note_message = st.text_area("Note message")
    _note = Notebook.Note("", "")
    notes = _note.read_notes()
    dropdown_options = []

    if st.button("Save"):
        _note.title = note_title
        _note.messages = note_message
        _note.write_note_to_file()

    for item in notes:
        note_text = item.split("\n")
        note_text = [text for text in note_text if text]
        if not note_text:
            break
        note_title = note_text[0]
        note_message = " ".join(note_text[1:])
        dropdown_options.append(note_title)

    st.selectbox(
        "Choose an option:",
        dropdown_options,
        key="notes_dropdown",
        on_change=update_textbox  # Trigger this function on change
    )
