import streamlit as st

if 'memo' not in st.session_state:
    st.session_state.memo = ""

input_memo=st.text_input("メモ帳")
if input_memo != "":
    st.session_state.memo=input_memo
st.write(st.session_state.memo)