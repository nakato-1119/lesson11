import streamlit as st

st.title("マイクラ ブロック ID")
st.error("注意：他のサイトとはまとめ方が違うので予めご了承ください。")
st.subheader("木のコマンド")
if st.button("オーク"):
    st.success("oak")
if st.button("トウヒ"):
    st.success("spruce")
if st.button("シラカバ"):
    st.success("birch")
if st.button("ジャングル"):
    st.success("jungle")
if st.button("アカシア"):
    st.success("acacia")
if st.button("ダークオーク"):
    st.success("dark_oak")
if st.button("ペールオーク"):
    st.success("pale_oak")
if st.button("マングローブ"):
    st.success("mangrove")
if st.button("サクラ"):
    st.success("cherry")
if st.button("真紅の木"):
    st.success("crimson")
if st.button("歪んだ幹"):
    st.success("warped")

st.subheader("ブロックのコマンド")
if st.button("木材"):
    st.success("planks")
if st.button("ハーフブロック"):
    st.success("slab")
if st.button("石"):
    st.success("stone")
if st.button("丸石"):
    st.success("cobblestone")
if st.button("苔むした丸石"):
    st.success("mossy_cobblestone")
if st.button("土"):
    st.success("dirt")

st.subheader("無名なアイテムのコマンド")
if st.button("コマンドブロック付きのトロッコ"):
    st.success("command_block_minecart")
if st.button("空気"):
    st.success("air")
if st.button("ジグソーブロック"):
    st.success("jigsaw")
st.success("木によって違うブロックは木のIDとブロックのIDを合わせて使ってください。[例：オークの木材ならオークと木材のIDを合わせてoak_planks]間は[_]で。")