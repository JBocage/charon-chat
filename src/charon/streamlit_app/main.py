import streamlit as st

from charon.utils.chatbot import chat_completion
from charon.utils.history import (
    get_history,
    list_history_entries,
    new_history,
    save_history,
)

st.title("charon")

with st.sidebar:
    st.title("charon")
    st.markdown("A simple chat history manager")
    chat_history = st.selectbox("Chat history", list_history_entries())

    new_history_name = st.text_input("New history name")

    new_history_placeholder = st.empty()
    if new_history_name:
        if new_history_placeholder.button("Create new history"):
            new_history(new_history_name)
            chat_history = new_history_name

if chat_history:
    history = get_history(chat_history)

    for entry in history:
        if entry["role"] == "system":
            _, c, _ = st.columns([1, 20, 1])
            c.warning(entry["content"])
        elif entry["role"] == "assistant":
            c, _ = st.columns([10, 1])
            c.success(entry["content"])
        elif entry["role"] == "user":
            _, c = st.columns([1, 10])
            c.info(entry["content"])

    new_entry_placeholder = st.empty()
    new_entry = new_entry_placeholder.text_input("New entry", key=len(history))
    if new_entry:
        new_entry_placeholder.empty()
        history = save_history(
            chat_history,
            history + [{"role": "user", "content": new_entry}],
        )
        _, c = st.columns([1, 10])
        c.info(new_entry)

        with st.spinner("Assistant is thinking..."):
            cmpl = chat_completion(history + [{"role": "user", "content": new_entry}])

            save_history(
                chat_history,
                history
                + [{"role": "assistant", "content": cmpl.choices[0].message.content}],
            )

        _, c = st.columns([10, 1])
        c.success(cmpl.choices[0].message.content)

        st.rerun()
