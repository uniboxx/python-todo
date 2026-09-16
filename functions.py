import os
import sys

FILEPATH = "todos.txt"


def resource_path(relative_path):
    """Ottiene il percorso assoluto della risorsa, funzionante sia in sviluppo che con PyInstaller"""
    try:
        # PyInstaller crea una cartella temporanea e memorizza il percorso in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")

    return os.path.join(base_path, relative_path)


def fileToList(filepath=FILEPATH):
    # documentation of this function
    """Reads a text file and returns a list of its lines"""
    if not os.path.exists(FILEPATH):
        with open("todos.txt", "w") as file:
            pass
    with open(filepath, "r") as file:
        # file.read() returns a string containing the entire file while splitlines() returns a list of lines while removing the line breaks
        list = file.read().splitlines()
        # or
        # list = [item.strip() for item in file.readlines()] # list comprehension
        # or
        # list = []
        # for item in file.readlines():
        #     list.append(item.strip())
        return list


def listToFile(list, filepath=FILEPATH):
    """Writes a list to a file"""

    with open(filepath, "w") as file:
        for item in list:
            file.write(f"{item}\n")
        # or
        # file.writelines([f"{item}\n" for item in list])


def update_window(window, list):
    window["todos"].update(values=list)
    window["todo"].update(value="")


def make_popup(sg, msg="Please select a todo"):
    sg.popup(msg, font=("Helvetica", 16))
