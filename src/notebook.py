"""Notebook module"""

import os

class Note:
    """Note class"""

    def __init__(self, messages: str, title: str):
        self.path = "result.txt"
        self.title = title
        self.messages = messages


    def write_note_to_file(self):
        with open(self.path, "a") as fa:
            fa.write(f"{self.title}\n")
            fa.write(f"{self.messages}\n-------------------\n")



    def read_notes(self):
        with open(self.path, "r") as fr:
            message = fr.read()
            return message.split("-------------------")
