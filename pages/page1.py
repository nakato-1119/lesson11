import streamlit as st

st.title("マイクラ 地形生成コマンド")
if st.button("地形生成ができるコマンドって？"):
    st.success("/fillコマンドと/setblockコマンドです。")
    st.success("解説：/fillコマンドは指定した範囲を特定のブロックで埋めるコマンドです。石を置いたり空気を置いて削ることもできます。")
    st.success("解説：/setblockコマンドは数字と置きたいブロックを入れることでランダムな地形を生成してくれます。")
    st.error("注意：これらのコマンドは間違えて広範囲を削ってしまったりと、失敗するかもしれません。バックアップを取ることをお勧めします。")
    st.error("参考:portal.jp.net")