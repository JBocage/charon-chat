import streamlit as st

from charon.utils.chatbot import chat_completion
from charon.utils.config import CONFIG
from charon.utils.history import (
    delete_history,
    get_history,
    list_history_entries,
    new_history,
    save_history,
)

st.title(CONFIG["ASSISTANT_NAME"])

with st.sidebar:
    st.markdown("A simple chat history manager")
    chat_history = st.selectbox("Chat history", list_history_entries())

    if chat_history:
        if st.button("Delete conversation"):
            delete_history(chat_history)
            st.rerun()

    new_history_name = st.text_input("New history name")
    new_history_placeholder = st.empty()
    if new_history_name:
        if new_history_placeholder.button("Create new history"):
            new_history(new_history_name)
            st.rerun()

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

    new_messages_placeholder = st.empty()
    new_entry_placeholder = st.empty()

    c1, c2 = new_entry_placeholder.columns([1, 4])
    model_type = c1.selectbox("Model", ["gpt-3.5-turbo", "gpt4"])

    new_entry = c2.text_input("New entry", key=f"{chat_history}{len(history)}")
    if new_entry:
        new_entry_placeholder.empty()
        history = save_history(
            chat_history,
            history + [{"role": "user", "content": new_entry}],
        )
        _, c = new_messages_placeholder.columns([1, 10])
        c.info(new_entry)

        with st.spinner("Assistant is thinking..."):
            cmpl = chat_completion(history + [{"role": "user", "content": new_entry}])

            save_history(
                chat_history,
                history
                + [{"role": "assistant", "content": cmpl.choices[0].message.content}],
            )

        _, c = new_messages_placeholder.columns([10, 1])
        c.success(cmpl.choices[0].message.content)

        st.rerun()

else:
    st.warning(
        "No chat history available\nPlease create a new history from the sidebar"
    )
