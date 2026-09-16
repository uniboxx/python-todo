import streamlit as st
from functions import fileToList, add_todo, listToFile
from functools import partial

todos = fileToList()
bounded_add_todo = partial(add_todo, st, todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for index, todo in enumerate(todos):
    key = f"todo-{index+1}"
    checkbox = st.checkbox(todo, key=key)
    if checkbox:
        todos.pop(index)
        listToFile(todos)
        del st.session_state[key]
        st.rerun()

st.text_input(
    label="",
    placeholder="Add new todo...",
    on_change=bounded_add_todo,
    key="new_todo",
)
