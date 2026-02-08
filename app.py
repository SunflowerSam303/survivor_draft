import streamlit as st
import random
import os

# --- Base Directory ---
BASE_DIR = os.path.dirname(__file__)  # folder where app.py is located

st.set_page_config(page_title="Survivor 50 Snake Draft", layout="wide")

# --- Survivor Players with Age + Notes ---
PLAYERS = [
    {"name": "Jenna Lewis-Dougherty", "age": 48, "notes": "Borneo & All-Stars legend", "img": os.path.join(BASE_DIR, "images", "JennaLewisDougherty.webp")},
    {"name": "Colby Donaldson", "age": 51, "notes": "Australian Outback icon, challenge beast", "img": os.path.join(BASE_DIR, "images", "ColbyDonaldson.webp")},
    {"name": "Stephenie LaGrossa Kendrick", "age": 46, "notes": "Palau underdog, Guatemala runner-up", "img": os.path.join(BASE_DIR, "images", "StephenieLaGrossaKendrick.webp")},
    {"name": "Cirie Fields", "age": 55, "notes": "Strategic legend, multi-season fan favorite", "img": os.path.join(BASE_DIR, "images", "CirieFields.webp")},
    {"name": "Ozzy Lusth", "age": 44, "notes": "Survival master, 5-time player", "img": os.path.join(BASE_DIR, "images", "OzzyLusth.webp")},
    {"name": "Coach Wade", "age": 53, "notes": "The Dragon Slayer, iconic personality", "img": os.path.join(BASE_DIR, "images", "BenjaminCoachWade.webp")},
    {"name": "Aubry Bracco", "age": 39, "notes": "Kaoh Rong strategist", "img": os.path.join(BASE_DIR, "images", "AubryBracco.webp")},
    {"name": "Chrissy Hofbeck", "age": 36, "notes": "Hustlers finalist, social strategist", "img": os.path.join(BASE_DIR, "images", "ChrissyHofbeck.webp")},
    {"name": "Christian Hubicki", "age": 39, "notes": "Puzzle genius, David vs Goliath", "img": os.path.join(BASE_DIR, "images", "ChristianHubicki.webp")},
    {"name": "Angelina Keeley", "age": 35, "notes": "Bold negotiator, DvG", "img": os.path.join(BASE_DIR, "images", "AngelinaKeeley.webp")},
    {"name": "Mike White", "age": 54, "notes": "White Lotus creator, DvG runner-up", "img": os.path.join(BASE_DIR, "images", "MikeWhite.webp")},
    {"name": "Rick Devens", "age": 41, "notes": "Edge of Extinction comeback king", "img": os.path.join(BASE_DIR, "images", "RickDevens.webp")},
    {"name": "Jonathan Young", "age": 33, "notes": "Survivor 42 physical force", "img": os.path.join(BASE_DIR, "images", "JonathanYoung.webp")},
    {"name": "Dee Valladares", "age": 29, "notes": "Winner of Survivor 45", "img": os.path.join(BASE_DIR, "images", "DeeValladares.webp")},
    {"name": "Emily Flippen", "age": 30, "notes": "Survivor 45 growth arc", "img": os.path.join(BASE_DIR, "images", "EmilyFlippen.webp")},
    {"name": "Q Burdette", "age": 31, "notes": "Survivor 46 chaos energy", "img": os.path.join(BASE_DIR, "images", "QBurdette.webp")},
    {"name": "Tiffany Ervin", "age": 34, "notes": "Survivor 46 standout", "img": os.path.join(BASE_DIR, "images", "TiffanyErvin.webp")},
    {"name": "Charlie Davis", "age": 27, "notes": "Survivor 46 runner-up", "img": os.path.join(BASE_DIR, "images", "CharlieDavis.webp")},
    {"name": "Genevieve Mushaluk", "age": 32, "notes": "Survivor 47 strategist", "img": os.path.join(BASE_DIR, "images", "GenevieveMushaluk.webp")},
    {"name": "Kamilla Karthigesu", "age": 31, "notes": "Survivor 48 athlete", "img": os.path.join(BASE_DIR, "images", "KamillaKarthigesu.webp")},
    {"name": "Kyle Fraser", "age": 31, "notes": "Winner of Survivor 48", "img": os.path.join(BASE_DIR, "images", "KyleFraser.webp")},
    {"name": "Joe Hunter", "age": 46, "notes": "Survivor 48 competitor", "img": os.path.join(BASE_DIR, "images", "JoeHunter.webp")},
    {"name": "Rizo Velovic", "age": 25, "notes": "Survivor 49 idol tactician", "img": os.path.join(BASE_DIR, "images", "RizoVelovic.webp")},
    {"name": "Savannah Louie", "age": 31, "notes": "Winner of Survivor 49", "img": os.path.join(BASE_DIR, "images", "SavannahLouie.webp")},
]

ROUNDS = 4
DRAFTER_COUNT = 6

# --- Helpers ---
def format_player(p):
    return f"{p['name']} (Age {p['age']}) — {p['notes']}"

def build_snake_order(drafters):
    order = []
    for r in range(ROUNDS):
        if r % 2 == 0:
            order.extend(drafters)
        else:
            order.extend(reversed(drafters))
    return order

# --- Session State Init ---
if "drafters" not in st.session_state:
    st.session_state.drafters = [f"Player {i}" for i in range(1, DRAFTER_COUNT + 1)]

if "draft_started" not in st.session_state:
    st.session_state.draft_started = False

if "available_players" not in st.session_state:
    st.session_state.available_players = PLAYERS.copy()

if "picks" not in st.session_state:
    st.session_state.picks = {}

if "turn" not in st.session_state:
    st.session_state.turn = 0

if "draft_order" not in st.session_state:
    st.session_state.draft_order = []

# --- Title ---
st.title("🏝️ Survivor 50 Snake Draft")

# --- Setup Drafter Names ---
if not st.session_state.draft_started:
    st.header("Enter Drafter Names")
    for i in range(DRAFTER_COUNT):
        name = st.text_input(f"Drafter {i+1}", value=st.session_state.drafters[i], key=f"name_{i}")
        st.session_state.drafters[i] = name

    if st.button("🎲 Randomize Draft Order"):
        st.session_state.drafters = st.session_state.drafters.copy()
        random.shuffle(st.session_state.drafters)
        st.rerun()

    if st.button("🚀 Start Draft"):
        st.session_state.picks = {d: [] for d in st.session_state.drafters}
        st.session_state.draft_order = build_snake_order(st.session_state.drafters)
        st.session_state.draft_started = True
        st.rerun()

# --- Draft Phase ---
else:
    if st.session_state.turn < len(st.session_state.draft_order):
        current = st.session_state.draft_order[st.session_state.turn]
        st.subheader(f"🎯 Current Turn: **{current}**")
        player_options = [format_player(p) for p in st.session_state.available_players]
        choice = st.selectbox("Choose a Survivor player:", player_options)

        if st.button("Draft Player"):
            selected_index = player_options.index(choice)
            selected_player = st.session_state.available_players.pop(selected_index)
            st.session_state.picks[current].append(selected_player)
            st.session_state.turn += 1
            st.rerun()

    # --- Show last drafted player ---
    if st.session_state.turn > 0:
        last_drafter = st.session_state.draft_order[st.session_state.turn - 1]
        last_pick = st.session_state.picks[last_drafter][-1]
        st.image(last_pick["img"], width=150)
        st.caption(f"{last_pick['name']} — Age {last_pick['age']}\n{last_pick['notes']}")

    # --- Undo Button ---
    if st.button("↩️ Undo Last Pick") and st.session_state.turn > 0:
        st.session_state.turn -= 1
        last_drafter = st.session_state.draft_order[st.session_state.turn]
        last_pick = st.session_state.picks[last_drafter].pop()
        st.session_state.available_players.append(last_pick)
        st.rerun()

    # --- Draft Board ---
    st.markdown("---")
    st.header("📋 Draft Board")
    cols = st.columns(DRAFTER_COUNT)
    for i, drafter in enumerate(st.session_state.drafters):
        with cols[i]:
            st.subheader(drafter)
            for pick in st.session_state.picks[drafter]:
                st.image(pick["img"], width=100)
                st.write(pick["name"])

    # --- Remaining Players ---
    st.markdown("---")
    st.header("🧍 Available Players")
    for p in st.session_state.available_players:
        st.write(format_player(p))
