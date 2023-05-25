import streamlit as st

title = st.text_input('Введите текст для перевода')
st.write('Данный текст будет переведён из нечитаемого формата в приемлемый, согласно раскладке клавиатуры QWE')

dict_alpha = {'q': 'й', 'w': 'ц', 'e': 'у', 'r': 'к', 't': 'е', 'y': 'н',
              'u': 'г', 'i': 'ш', 'o': 'щ', 'p': 'з', '[': 'х', ']': 'ъ',
              'a': 'ф', 's': 'ы', 'd': 'в',  'f': 'а', 'g': 'п', 'h': 'р',
              'j': 'о', 'k': 'л', 'l': 'д', ';': 'ж', '"': 'э',
              'z': 'я', 'x': 'ч', 'c': 'с', 'v': 'м', 'b': 'и', 'n': 'т',
              'm': 'ь', ',': 'б', '.': 'ю', '/': '.', }
              # '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
              # '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
              # '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
              # '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
              # '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
              # '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
              # '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''
              # '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' '' ''}

new_text = []
for i in title:
    for key, value in dict_alpha.items():
        if i == key:
            new_text.append(value)
string1 =''.join(new_text)
st.text(string1)
#