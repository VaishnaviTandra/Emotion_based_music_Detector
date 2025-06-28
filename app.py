import streamlit as st

# Expanded dictionary of playlists or songs by emotion
emotion_music = {
    "Happy": [
        "🎵 Happy – Pharrell Williams",
        "🎵 Can't Stop The Feeling – Justin Timberlake",
        "🎵 Uptown Funk – Bruno Mars",
        "🎵 I Gotta Feeling – Black Eyed Peas",
        "🎵 Good Time – Owl City & Carly Rae Jepsen"
    ],
    "Sad": [
        "🎵 Someone Like You – Adele",
        "🎵 Let Her Go – Passenger",
        "🎵 Fix You – Coldplay",
        "🎵 When I Was Your Man – Bruno Mars",
        "🎵 Skinny Love – Birdy"
    ],
    "Angry": [
        "🎵 In The End – Linkin Park",
        "🎵 Break Stuff – Limp Bizkit",
        "🎵 Killing In The Name – Rage Against The Machine",
        "🎵 Duality – Slipknot",
        "🎵 Smells Like Teen Spirit – Nirvana"
    ],
    "Relaxed": [
        "🎵 Weightless – Marconi Union",
        "🎵 Ocean Eyes – Billie Eilish",
        "🎵 Bloom – The Paper Kites",
        "🎵 Banana Pancakes – Jack Johnson",
        "🎵 Holocene – Bon Iver"
    ],
    "Romantic": [
        "🎵 Perfect – Ed Sheeran",
        "🎵 All of Me – John Legend",
        "🎵 Just The Way You Are – Bruno Mars",
        "🎵 Thinking Out Loud – Ed Sheeran",
        "🎵 A Thousand Years – Christina Perri"
    ],
    "Energetic": [
        "🎵 Don't Start Now – Dua Lipa",
        "🎵 Stronger – Kanye West",
        "🎵 Power – Little Mix",
        "🎵 Shake It Off – Taylor Swift",
        "🎵 Can’t Hold Us – Macklemore & Ryan Lewis"
    ],
    "Bored": [
        "🎵 Counting Stars – OneRepublic",
        "🎵 Riptide – Vance Joy",
        "🎵 Take A Walk – Passion Pit",
        "🎵 Feel It Still – Portugal. The Man",
        "🎵 Electric Feel – MGMT"
    ],
    "Hopeful": [
        "🎵 On Top of the World – Imagine Dragons",
        "🎵 Rise Up – Andra Day",
        "🎵 Brave – Sara Bareilles",
        "🎵 Fight Song – Rachel Platten",
        "🎵 Firework – Katy Perry"
    ],
    "Anxious": [
        "🎵 Breathe Me – Sia",
        "🎵 Lovely – Billie Eilish & Khalid",
        "🎵 Let It Go – James Bay",
        "🎵 The Night We Met – Lord Huron",
        "🎵 Lost in Japan – Shawn Mendes"
    ]
}

# App title
st.title("🎧 Emotion-Based Music Recommender")

# Instruction
st.write("Select your current emotion and get music that matches your mood!")

# Dropdown for emotion selection
selected_emotion = st.selectbox("How are you feeling right now?", list(emotion_music.keys()))

# Show recommendations
if selected_emotion:
    st.subheader(f"Recommended songs for a **{selected_emotion}** mood:")
    for song in emotion_music[selected_emotion]:
        st.write(song)

# Footer
st.markdown("---")
st.caption("Built with ❤️ using Streamlit by Vaishnavi")
