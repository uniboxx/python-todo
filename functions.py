import os
import sys

FILEPATH = "todos.txt"


def add_todo(st, todos):
    todo = st.session_state["new_todo"].strip().capitalize()
    todos.append(todo)
    listToFile(todos)
    st.session_state["new_todo"] = ""


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
