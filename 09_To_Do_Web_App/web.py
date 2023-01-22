import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    text = st.session_state['new_todo']
    if len(text.strip()) > 1:
        todo = st.session_state['new_todo'].strip() + '\n'
        todos.append(todo)
        functions.write_todos(todos)    



st.title("My Todo App")
st.subheader("This is todo app")
st.write("This app is to improve your productivity")


for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label=" ", placeholder="Add new to do", on_change=add_todo, key='new_todo')
