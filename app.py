
import streamlit as st
import pytube
from googletrans import Translator
import pyttsx3

st.title("🎬 Drama & Movies Player with Voice Translation")

url = st.text_input("Paste YouTube Video Link:")
lang = st.selectbox("Choose Translation Language:", ["ur", "hi", "en"])

translator = Translator()

if url:
    try:
        yt = pytube.YouTube(url)
        stream = yt.streams.get_highest_resolution()
        st.video(stream.url)

        if yt.captions:
            caption = yt.captions.get_by_language_code("en")
            if caption:
                text = caption.generate_srt_captions()
                st.subheader("🔤 Translated Dialogues")
                translated = translator.translate(text, dest=lang).text
                st.text(translated)

                if st.button("🔊 Listen Translation"):
                    engine = pyttsx3.init()
                    engine.say(translated)
                    engine.runAndWait()
            else:
                st.error("❌ No English captions available for this video.")
        else:
            st.error("❌ No captions found in this video.")
    except Exception as e:
        st.error(f"⚠️ Error: {e}")
