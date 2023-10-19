import pandas as pd 
import streamlit as st

data = [
  ['Franck', 4, 3, 4, 3, 5, 4, 4, 5, 4, 4, 3, 4, 5, 4, 4, 4, 3, 5],
  ['Lucas', 4, 3, 4, 3, 5, 4, 4, 5, 4, 4, 3, 4, 5, 4, 4, 4, 3, 5],
  ['Charlotte', 4, 3, 4, 3, 5, 4, 4, 5, 4, 4, 3, 4, 5, 4, 4, 4, 3, 5]
]
  
columns = ['Player', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

score_card = pd.DataFrame(data, columns=columns)

st.dataframe(score_card)


