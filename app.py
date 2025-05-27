import streamlit as st

# Set page config
st.set_page_config(page_title="Shooting Game", layout="centered")

# Ask player name
if "player_name" not in st.session_state:
    st.session_state.player_name = ""

if st.session_state.player_name == "":
    st.session_state.player_name = st.text_input("Enter your player name:", key="name_input")
    if st.session_state.player_name:
        st.success(f"Welcome, {st.session_state.player_name}! Press the button below to start the game.")
        st.button("Start Game")
else:
    st.markdown(f"### Welcome, **{st.session_state.player_name}** (Shooter with Army Cap & AK Gun)!")
    
    # Embed the HTML game
    with open("game.html", "r") as f:
        html_code = f.read()
    st.components.v1.html(html_code, height=600, scrolling=False)
