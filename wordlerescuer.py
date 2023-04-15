import streamlit as st
import nltk
from nltk.corpus import words
import re
st.title("Wordle ResCLUEr")
st.image("https://news.ufl.edu/media/newsufledu/images/2022/01/wordle-gator.png")
@st.cache_resource
def download():
    nltk.download('words')
download()

five_letters = [word for word in words.words() if len(word)==5]
[a,b,c,d,e]= st.columns(5)
with a:
    first_letter =  st.text_input(label="1st",value = 'a')
with b:
    second_letter =  st.text_input(label="2nd",value = 'b')
with c:
    third_letter =  st.text_input(label="3rd",value = 'c')
with d:
    fourth_letter =  st.text_input(label="4th",value = 'd')
with e:
    fifth_letter =  st.text_input(label="5th",value = 'e')
clue = first_letter + second_letter + third_letter + fourth_letter + fifth_letter
st.markdown("### clue")
st.write(clue)
exclusions = st.text_input(label="exclusions")
st.markdown("# Wordle Clues")
clue_results = []
for word in five_letters:
    if all(c in word for c in clue) and not any(c in word for c in exclusions):
        clue_results.append(word)

st.write(clue_results)
