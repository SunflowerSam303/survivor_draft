import streamlit as st
import random
import os
import base64

# --- Base Directory ---
BASE_DIR = os.path.dirname(__file__)

st.set_page_config(page_title="Survivor 50 Snake Draft", layout="wide")

# ---------- IMAGE HELPER ----------
def get_base64_image(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

# ---------- SURVIVOR HERO HEADER ----------
logo_path = os.path.join(BASE_DIR, "images", "survivor50logo.webp")
logo_base64 = get_base64_image(logo_path)

st.markdown(f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@600;800&display=swap');

/* ---------- JUNGLE BACKGROUND (fixed) ---------- */
.stApp {{
    background-image: url("https://images.unsplash.com/photo-1501785888041-af3ef285b470");
    background-size: cover;
    background-attachment: fixed;
    background-position: center;
}}

/* Light cinematic overlay so jungle is visible */
.stApp::before {{
    content: "";
    position: fixed;
    inset: 0;
    background: rgba(0,0,0,0.35);
    z-index: -1;
}}

/* ---------- HEADER (no box, clean logo) ---------- */
.survivor-header {{
    position: relative;
    width: 100%;
    margin-bottom: 30px;
}}

.survivor-header img {{
    width: 100%;
    display: block;
    border-radius: 0px;
    box-shadow: none;
}}

.overlay {{
    position: absolute;
    inset: 0;
    background: linear-gradient(to bottom, rgba(0,0,0,0.15), rgba(0,0,0,0.55));
}}

.survivor-title {{
    position: absolute;
    bottom: 28px;
    left: 50%;
    transform: translateX(-50%);
    font-family: 'Cinzel', serif;
    font-size: clamp(32px, 6vw, 64px);
    font-weight: 800;
    color: #ffd27a;
    letter-spacing: 3px;
    text-align: center;
    animation: fireGlow 2.2s ease-in-out infinite alternate;
}}

@keyframes fireGlow {{
    from {{ text-shadow: 0 0 10px #ff9900, 0 0 20px #ff5500; }}
    to {{ text-shadow: 0 0 18px #ffcc00, 0 0 35px #ff2200; }}
}}

/* ---------- CONTENT PANELS (semi transparent so jungle shows) ---------- */
div[data-testid="stVerticalBlock"] > div {{
    background: rgba(25, 22, 18, 0.82);
    backdrop-filter: blur(6px);
    border-radius: 14px;
    padding: 18px 22px;
    box-shadow: 0 8px 30px rgba(0,0,0,0.7);
    border: 1px solid rgba(255,255,255,0.08);
    margin-bottom: 18px;
    color: #f5e6c8;
}}

h1, h2, h3, label, p, span {{
    font-family: 'Cinzel', serif;
    color: #f5e6c8 !important;
}}

/* Buttons */
.stButton>button {{
    background: linear-gradient(#5a3f17, #3b2a10);
    color: #f5e6c8;
    border-radius: 8px;
    border: 1px solid #2a1d0a;
    font-weight: bold;
}}

.stSelectbox div[data-baseweb="select"] {{
    background-color: #2b261d;
    color: #f5e6c8;
    border-radius: 8px;
}}

</style>

<div class="survivor-header">
    <img src="data:image/png;base64,{logo_base64}">
    <div class="overlay"></div>
    <div class="survivor-title">SURVIVOR 50 SNAKE DRAFT</div>
</div>
""", unsafe_allow_html=True)

# ---------- PLAYERS ----------
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

def format_player(p):
    return f"{p['name']} (Age {p['age']}) — {p['notes']}"

def build_snake_order(drafters):
    order = []
    for r in range(ROUNDS):
        order.extend(drafters if r % 2 == 0 else reversed(drafters))
    return order

# ---------- SESSION STATE ----------
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

# ---------- SETUP ----------
if not st.session_state.draft_started:
    st.header("Enter Drafter Names")

    for i in range(DRAFTER_COUNT):
        name = st.text_input(f"Drafter {i+1}", value=st.session_state.drafters[i], key=f"name_{i}")
        st.session_state.drafters[i] = name

    if st.button("🎲 Randomize Draft Order"):
        random.shuffle(st.session_state.drafters)
        st.rerun()

    if st.button("🚀 Start Draft"):
        st.session_state.picks = {d: [] for d in st.session_state.drafters}
        st.session_state.draft_order = build_snake_order(st.session_state.drafters)
        st.session_state.draft_started = True
        st.rerun()

# ---------- DRAFT ----------
else:
    if st.session_state.turn < len(st.session_state.draft_order):
        current = st.session_state.draft_order[st.session_state.turn]
        st.subheader(f"🎯 Current Turn: **{current}**")
        player_options = [format_player(p) for p in st.session_state.available_players]
        choice = st.selectbox("Choose a Survivor player:", player_options)

        if st.button("Draft Player"):
            idx = player_options.index(choice)
            selected = st.session_state.available_players.pop(idx)
            st.session_state.picks[current].append(selected)
            st.session_state.turn += 1
            st.rerun()

    if st.session_state.turn > 0:
        last_drafter = st.session_state.draft_order[st.session_state.turn - 1]
        last_pick = st.session_state.picks[last_drafter][-1]
        st.markdown(f"""
        <div style="
            display:flex;
            justify-content:center;
            margin: 30px 0;
        ">
            <div style="
                text-align:center;
                background: rgba(20,18,14,0.85);
                padding: 24px 28px;
                border-radius: 18px;
                box-shadow: 0 10px 35px rgba(0,0,0,0.8);
                border: 1px solid rgba(255,255,255,0.08);
                max-width: 720px;
                backdrop-filter: blur(6px);
            ">
                <img src="data:image/webp;base64,{get_base64_image(last_pick['img'])}"
                    style="
                        width: 420px;
                        border-radius: 14px;
                        border: 6px solid #3b2a10;
                        box-shadow:
                            0 0 0 3px #7a5a22,
                            0 0 35px rgba(255,140,0,0.65),
                            inset 0 0 20px rgba(0,0,0,0.8);
                    ">
                <div style="
                    margin-top:18px;
                    font-family:'Cinzel', serif;
                    color:#f5e6c8;
                ">
                    <div style="font-size:28px; font-weight:800;">
                        {last_pick['name']}
                    </div>
                    <div style="font-size:18px; margin-top:6px; opacity:0.9;">
                        Age {last_pick['age']} — {last_pick['notes']}
                    </div>
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)

    if st.button("↩️ Undo Last Pick") and st.session_state.turn > 0:
        st.session_state.turn -= 1
        last_drafter = st.session_state.draft_order[st.session_state.turn]
        last_pick = st.session_state.picks[last_drafter].pop()
        st.session_state.available_players.append(last_pick)
        st.rerun()

    st.markdown("---")
    st.header("📋 Draft Board")
    cols = st.columns(DRAFTER_COUNT)
    for i, drafter in enumerate(st.session_state.drafters):
        with cols[i]:
            st.subheader(drafter)
            for pick in st.session_state.picks[drafter]:
                st.markdown(f"""
                <div style="text-align:center; margin-bottom:10px;">
                    <img src="data:image/webp;base64,{get_base64_image(pick['img'])}" width="110">
                    <div style="margin-top:6px; font-weight:bold;">{pick['name']}</div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("---")
    st.header("🧍 Available Players")
    for p in st.session_state.available_players:
        st.write(format_player(p))