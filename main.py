import base64
import numpy as np
import streamlit as st
from gtts import gTTS

st.balloons()
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
        f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"jpg"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
        unsafe_allow_html=True
    )


add_bg_from_local('lll.jpg')


option = st.selectbox(
    'Выберите язык вашего текста',
    ('ru', 'en'))


# st.write('Вы выбрали:', option)



txt = st.text_input('Введите текст для перевода')
# title = st.text_input('Введите текст для перевода', disabled=False, max_chars=500)


st.write('Введённый текст будет переведён из нечитаемого формата в приемлемый, согласно раскладке клавиатуры QWERTY и озвучен')



dict_alpha = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н',
              'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
              'a': 'ф', 's': 'ы', 'd': 'в', 'f': 'а', 'g': 'п', 'h': 'р',
              'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', "'": 'э',
              'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т',
              'm': 'ь', ',': 'б', '.': 'ю', '/': '.', ' ': ' ',

              'Q': 'Й', 'W': 'Ц', 'E': 'У', 'R': 'К', 'T': 'Е', 'Y': 'Н',
              'U': 'Г', 'I': 'Ш', 'O': 'Щ', 'P': 'З', '{': 'Х', '}': 'Ъ',
              'A': 'Ф', 'S': 'Ы', 'D': 'В', 'F': 'А', 'G': 'П', 'H': 'Р',
              'J': 'О', 'K': 'Л', 'L': 'Д', ':': 'Ж', '"': 'Э', '|': '/',
              'Z': 'Я', 'X': 'Ч', 'C': 'С', 'V': 'М', 'B': 'И', 'N': 'Т',
              'M': 'Ь', '<': 'Б', '>': 'Ю', '?': ',',

              '1': '1', '2': '2', '3': '3', '4': '4', '5': '5',
              '6': '6', '7': '7', '8': '8', '9': '9', '0': '0',

              'й': 'q', 'ц': 'w', 'у': 'e', 'к': 'r', 'е': 't', 'н': 'y',
              'г': 'u', 'ш': 'i', 'щ': 'o', 'з': 'p', 'х': '[', 'ъ': ']',
              'ф': 'a', 'ы': 's', 'в': 'd', 'а': 'f', 'п': 'g', 'р': 'h',
              'о': 'j', 'л': 'k', 'д': 'l', 'ж': ';', 'э': "'", '\\': '\\',
              'я': 'z', 'ч': 'x', 'с': 'c', 'м': 'v', 'и': 'b', 'т': 'n',
              'ь': 'm', 'б': ',', 'ю': '.',

              'Й': 'Q', 'Ц': 'W', 'У': 'E', 'К': 'R', 'Е': 'T', 'Н': 'Y',
              'Г': 'U', 'Ш': 'I', 'Щ': 'O', 'З': 'P', 'Х': '{', 'Ъ': '}',
              'Ф': 'A', 'Ы': 'S', 'В': 'D', 'А': 'F', 'П': 'G', 'Р': 'H',
              'О': 'J', 'Л': 'K', 'Д': 'L', 'Ж': ':', 'Э': '"',
              'Я': 'Z', 'Ч': 'X', 'С': 'C', 'М': 'V', 'И': 'B', 'Т': 'N',
              'Ь': 'M', 'Б': '<', 'Ю': '>',

              '!': '!', '@': '@', '#': '#', '№': '№', '$': '$',
              '%': '%', '^': '^', '*': '*', '(': '(', ')': ')', '-': '-',
              '_': '_', '+': '+', '=': '=', '    ': '    ', '`': 'ё', '~': 'Ё',
              '\n': '\n', '&': '?'
              }




new_text = []
for i in txt:
    for key, value in dict_alpha.items():
        if i == key:
            new_text.append(value)
string1 = ''.join(new_text)
st.text(string1)



if option and string1:
    tts = gTTS(text=string1, lang=option)
    tts.save("good.mp3")


    audio_file = open('good.mp3', 'rb')
    audio_bytes = audio_file.read()

    st.audio(audio_bytes, format='audio/mp3')