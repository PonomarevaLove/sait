
import streamlit as st
import numpy as np
from gtts import gTTS

option = st.selectbox(
    'Выберите язык вашего текста',
    ('ru', 'en'))

st.write('Вы выбрали:', option)

title = st.text_input('Введите текст для озвучивания')
# st.write('The current movie title is', title)

if option and title:
    tts = gTTS(text=title, lang=option)
    tts.save("good.mp3")

    audio_file = open('good.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')

