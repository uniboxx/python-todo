import streamlit as st
from functions import fileToList, add_todo
from functools import partial

todos = fileToList()
bounded_add_todo = partial(add_todo, st, todos)


st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(
    label="",
    placeholder="Add new todo...",
    on_change=bounded_add_todo,
    key="new_todo",
)
