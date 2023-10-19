import pandas as pd 
import streamlit as st

data = [
  ['Franck', 4, 3, 4, 3, 5, 4, 4, 5, 4, 4, 3, 4, 5, 4, 4, 4, 3, 5],
  ['Lucas', 4, 3, 4, 3, 5, 4, 4, 5, 4, 4, 3, 4, 5, 4, 4, 4, 3, 5],
  ['Charlotte', 4, 3, 4, 3, 5, 4, 4, 5, 4, 4, 3, 4, 5, 4, 4, 4, 3, 5]
]
  
columns = ['Player', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

score_card = pd.DataFrame(data, columns=columns)

score_board = [
  ['Franck', 0],
  ['Lucas', 0],
  ['Charlotte', 0]
]

col = ['Player', 'Score']

score_board = pd.DataFrame(score_board, columns=col)

st.dataframe(score_card)

col1, col2, col3, col4, col5, col6, col7, col8, col9 = st.columns(9)

hole1 = col1.number_input('Hole 1', value=0)
hole2 = col2.number_input('Hole 2', value=0)
hole3 = col3.number_input('Hole 3', value=0)
hole4 = col4.number_input('Hole 4', value=0)
hole5 = col5.number_input('Hole 5', value=0)
hole6 = col6.number_input('Hole 6', value=0)
hole7 = col7.number_input('Hole 7', value=0)
hole8 = col8.number_input('Hole 8', value=0)
hole9 = col9.number_input('Hole 9', value=0)

if not hole1 == 0:
  for index, player_row in score_card.iterrows():
    st.dataframe(player_row)
  
 
