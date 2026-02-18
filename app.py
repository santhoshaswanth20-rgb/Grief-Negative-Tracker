import streamlit as st
import pandas as pd
import time

# --- SETUP ---
st.set_page_config(page_title="Grief Negative Dashboard", page_icon="🔥", layout="wide")

# Custom CSS to make it look "Extreme Demon" style
st.markdown("""
    <style>
    .main { background-color: #0e1117; color: #ffffff; }
    stMetric { background-color: #1e2130; padding: 15px; border-radius: 10px; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔴 Project: Grief Negative (Verification)")
st.write(f"**Current Date:** {time.strftime('%Y-%m-%d')} | **Status:** Surpassing EVW")

# --- DATA ENTRY ---
with st.sidebar:
    st.header("📝 Log Today's Run")
    new_acc = st.slider("Today's Accuracy (%)", 0, 100, 88)
    new_deaths = st.number_input("Deaths this run", value=645)
    session_note = st.text_input("Session Notes", "Gaps look too wide lol")
    
    if st.button("Save Progress"):
        st.balloons()
        st.toast("Progress Saved to Local Storage!", icon="✅")

# --- DASHBOARD ---
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="Current Accuracy", value=f"{new_acc}%", delta="Keep going!")

with col2:
    # We want deaths to go DOWN, so a negative delta is GOOD
    st.metric(label="Total Deaths", value=new_deaths, delta="-52", delta_color="inverse")

with col3:
    st.metric(label="Current Rank", value="Top 100 Candidate", delta="Buffed")

# --- PROGRESS BAR ---
st.write("### 🚀 Road to 100% (The Drop)")
st.progress(new_acc / 100, text=f"Accuracy Progress: {new_acc}%")

# --- VISUALS ---
st.write("---")
st.write("### 📈 Death Count Trend")
# Just a placeholder chart to show how your skill is climbing
chart_data = pd.DataFrame({
    'Run #': [1, 2, 3, 4, 5],
    'Deaths': [1200, 1050, 890, 750, 645] 
})
st.line_chart(chart_data, x='Run #', y='Deaths', color="#ff4b4b")

# --- THE REALITY CHECK ---
st.info(f"💡 **Analysis:** Your 88% accuracy on a Mac is insane. Even with 645 deaths, you're already more consistent than most players on the lower list.")

st.warning("⚠️ **Reminder:** Tomorrow is Poppy Playtime 5 release. Plan your GD grind accordingly!")
import streamlit as st
import pandas as pd
import time

# --- SETUP ---
st.set_page_config(page_title="Grief Negative Dashboard", page_icon="🔥", layout="wide")

st.title("🔴 Project: Grief Negative (Verification)")

# --- VIDEO REVIEW SECTION ---
st.write("---")
st.header("📹 Video Review: Analyze Your Runs")
uploaded_video = st.file_uploader("Drag and drop your Mac screen recording here", type=["mp4", "mov"])

if uploaded_video is not None:
    st.video(uploaded_video)
    st.caption("Analyzing: Check the 0.7 ship gaps vs Kenos hitboxes.")

# --- DASHBOARD STATS ---
st.write("---")
col1, col2 = st.columns(2)
with col1:
    acc = st.slider("Today's Accuracy (%)", 0, 100, 88)
    st.progress(acc/100, text=f"Climbing to 100%: {acc}%")
with col2:
    deaths = st.number_input("Total Deaths", value=645)
    st.metric("Session Difficulty", "Very Harder", delta="Surpassing EVW")

# --- COMPARISON TABLE ---
st.write("### 🧱 Why Kenos looks 'Wide'")
data = {
    "Level": ["Kenos Showcase", "Your Level", "Thinking Space II"],
    "Hitbox Reality": ["Wide (Bot play)", "0.7 Block (Extreme)", "Pixel Perfect"],
    "Reaction": ["'Alright'", "Buffing...", "Warm-up"]
}
st.table(pd.DataFrame(data))

st.success("💡 Tip: Use your warm-up skill from TS2 to tackle the 10 frame-perfects today!")
import streamlit as st
import pandas as pd
import time
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Grief Negative HQ", page_icon="🔴", layout="wide")

# Custom CSS for the "Dark Demon" vibe
st.markdown("""
    <style>
    .stApp { background-color: #0b0c10; color: #66fcf1; }
    h1, h2, h3 { color: #45a29e; }
    .stButton>button { background-color: #1f2833; color: #66fcf1; border: 1px solid #45a29e; }
    </style>
    """, unsafe_allow_html=True)

st.title("🔴 Grief Negative: Verification Dashboard")

# --- 1. SIDEBAR (LOGGING & CUSTOM MUSIC) ---
with st.sidebar:
    st.header("📝 Log Today's Run")
    side_acc = st.slider("Today's Accuracy (%)", 0, 100, 88, key="unique_slider_1")
    side_deaths = st.number_input("Deaths this run", value=645, key="unique_deaths_1")
    session_note = st.text_input("Session Notes", "Gaps look too wide lol", key="unique_notes_1")
    
    if st.button("Save Progress", key="save_btn_1"):
        st.balloons()
        st.success("Progress Saved!")

    st.write("---")
    st.header("🎶 Custom Level Music")
    # NEW FEATURE: Drop your song file here!
    uploaded_song = st.file_uploader("Drop your song file (.mp3, .wav)", type=['mp3', 'wav'], key="song_uploader")
    
    if uploaded_song is not None:
        st.audio(uploaded_song)
        st.caption(f"Now Playing: {uploaded_song.name}")
    else:
        st.info("Drop a file to play your custom track!")

# --- 2. TS2 WARM-UP TIMER ---
st.header("⏱️ TS2 Warm-up Timer")
if 'start_time' not in st.session_state:
    st.session_state.start_time = None

t_col1, t_col2 = st.columns(2)
if t_col1.button("Start Warm-up", key="timer_start"):
    st.session_state.start_time = time.time()
    st.toast("Timer Started! Go play Thinking Space II.")

if t_col2.button("Stop & Log", key="timer_stop"):
    if st.session_state.start_time:
        elapsed = time.time() - st.session_state.start_time
        st.success(f"Warm-up complete: {elapsed:.2f} seconds.")
        st.session_state.start_time = None
    else:
        st.error("Start the timer first!")

# --- 3. MAIN DASHBOARD ---
st.write("---")
st.header("📊 Live Stats")
col1, col2, col3 = st.columns(3)

with col1:
    main_acc = st.number_input("Final Accuracy Check %", value=side_acc, key="unique_acc_2")
    st.progress(main_acc/100)

with col2:
    st.metric("Total Deaths", value=side_deaths, delta="-52", delta_color="inverse")

with col3:
    if 'clicks' not in st.session_state: st.session_state.clicks = 0
    if st.button("Log Training Click", key="click_counter_btn"):
        st.session_state.clicks += 1
    st.metric("Session Clicks", st.session_state.clicks)

# --- 4. VIDEO & HORROR MODE ---
st.write("---")
v_col, h_col = st.columns(2)

with v_col:
    st.header("📹 Video Review")
    video_file = st.file_uploader("Analyze your 88% run", type=['mp4', 'mov'], key="video_up_1")
    if video_file:
        st.video(video_file)

with h_col:
    st.header("🧸 PP5 Tracker")
    if st.checkbox("⚠️ ENABLE HORROR MODE", key="horror_mode_toggle"):
        st.warning("THE PROTOTYPE IS WATCHING...")
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJqZ3RreXBrZXR3Z3RreXBrZXR3Z3RreXBrZXR3Z3RreXBrZSZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/3o7TKv6MgQxcfPzEV2/giphy.gif")
        st.snow()

if main_acc >= 100:
    st.balloons()
    st.write("# BRO I BEAT IT!")
    import streamlit as st
import time

st.set_page_config(page_title="Grief Negative HQ", layout="wide")

# --- SIDEBAR: THE SOUNDTRACK ---
with st.sidebar:
    st.header("🎶 Level OST")
    # This is where you drop your 'Greif_Negative' file!
    custom_track = st.file_uploader("Upload your MP3", type=['mp3'])
    if custom_track:
        st.audio(custom_track)
        st.success(f"Now Playing: {custom_track.name}")
    
    st.write("---")
    st.write("**Artist Notes:**")
    st.info("Created for the 'Drop to 100' run. Syncs with the 10 frame-perfects.")

# --- MAIN DASHBOARD ---
st.title("🔴 Grief Negative Verification")
st.subheader("Mac Performance Mode: ON")

col1, col2 = st.columns(2)
with col1:
    acc = st.slider("Accuracy (%)", 0, 100, 88, key="final_acc")
    st.metric("Status", "Very Harder", delta="Surpassing EVW")
with col2:
    deaths = st.number_input("Death Count", value=645, key="final_deaths")
    if st.checkbox("Show Progress Bar"):
        st.progress(acc/100)

# --- THE PP5 COUNTDOWN ---
st.write("---")
if st.checkbox("Check Poppy Playtime 5 Release"):
    st.warning("RELEASE DAY: TOMORROW (Feb 18, 2026)")
    st.write("Don't let the Prototype distract you from the 0.7-block gaps!")
import streamlit as st
import time

st.set_page_config(page_title="Grief Negative HQ", layout="wide")

# --- SIDEBAR ---
with st.sidebar:
    st.header("📝 Log Today's Run")
    # Added 'key' to make these unique from the main page
    side_acc = st.slider("Accuracy %", 0, 100, 88, key="sb_accuracy")
    side_deaths = st.number_input("Deaths", value=645, key="sb_deaths")
    
    st.write("---")
    st.header("🎶 Level Music")
    uploaded_song = st.file_uploader("Drop Greif_Negative.mp3 here", type=['mp3'], key="sb_music")
    if uploaded_song:
        st.audio(uploaded_song)

# --- MAIN DASHBOARD ---
st.title("🔴 Grief Negative: Taco Buff Edition")
st.subheader("Current Difficulty: Top 1 (?)")

col1, col2 = st.columns(2)
with col1:
    # Use a different key here!
    main_acc = st.number_input("Live Accuracy Check", value=side_acc, key="main_acc_input")
    st.progress(main_acc/100)

with col2:
    st.metric("Total Deaths", value=side_deaths, delta="-52", delta_color="inverse")

# --- TACO BUFF ANALYSIS ---
st.write("---")
st.header("🌮 Taco Part Analysis")
st.error("⚠️ FRAME PERFECT DETECTED: 0.5 gap at 4x Speed.")
st.write("Those hitboxes in your screenshot are crazy. At 4x speed, that's a sub-10ms window.")

if st.checkbox("Check Poppy Playtime 5 Release Status", key="sb_pp5"):
    st.info("Release Day is TODAY! (Feb 18, 2026). Don't let the Prototype see your 4x speed gaps.")

if main_acc >= 100:
    st.balloons()
    st.write("# VERIFIED!!")