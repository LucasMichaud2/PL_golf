import pandas as pd  
import streamlit as st
 
data = [
  ['Lucas', 2, 0, 3, 2, 0, 3, 1, 1, 0, 1, 1, 0, 2, 2, 3, 2, 1, 2],
  ['Mercedes', 2, 2, 0, 3, 1, 2, 0, 2, 0, 3, 2, 2, 1, 1, 1, 1, 2, 1],
  ['Charlotte', 2, 3, 3, 1, 1, 3, 3, 3, 3, 2, 2, 2, 1, 2, 3, 3, 2, 2],
  ['Danielle', 2, 2, 0, 3, 2, 4, 0, 0, 3, 0, 2, 3, 0, 3, 2, 2, 4, 2],
  ['Franck', 0, 2, 1, 2, 1, 3, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2],
  ['JC', 2, 2, 2, 1, 1, 2, 0, 2, 2, 2, 2, 1, 1, 2, 2, 2, 2, 0],
  ['Alain', 2, 2, 1, 0, 3, 0, 3, 2, 2, 2, 1, 0, 2, 3, 2, 2, 2, 2],
  ['Ursula', 1, 3, 2, 1, 1, 2, 0, 2, 1, 0, 0, 3, 1, 2, 2, 0, 0, 2],
  ['Catherine', 2, 2, 2, 3, 2, 1, 0, 2, 1, 2, 2, 1, 2, 2, 1, 2, 1, 2],
  ['Adele', 2, 2, 0, 2, 1, 2, 2, 1, 1, 2, 2, 2, 2, 0, 3, 2, 1, 1],
  ['Cariane', 3, 3, 2, 2, 2, 2, 0, 1, 1, 2, 0, 1, 2, 1, 1, 0, 2, 0],
  ['Andy', 2, 2, 1, 0, 2, 2, 3, 2, 2, 2, 3, 2, 2, 2, 1, 1, 2, 2],
  ['Paul Em', 1, 2, 1, 2, 1, 0, 1, 2, 2, 2, 0, 0, 0, 3, 3, 1, 2, 0],
  ['Roland', 2, 2, 1, 1, 2, 1, 1, 2, 2, 0, 2, 1, 0, 1, 0, 1, 1, 1],
  ['Siba', 0, 1, 0, 1, 2, 2, 2, 1, 2, 1, 3, 2, 1, 1, 2, 1, 2, 2],
  ['Joe', 1, 2, 2, 3, 1, 0, 2, 2, 2, 3, 2, 0, 2, 2, 1, 2, 2, 1],
  ['Peter', 0, 2, 2, 1, 0, 0, 2, 0, 1, 3, 3, 2, 1, 3, 2, 3, 1, 0],
  ['Paul H', 0, 3, 0, 2, 0, 1, 2, 2, 3, 0, 2, 2, 2, 0, 3, 2, 1, 0],
  ['David', 1, 3, 2, 2, 0, 2, 2, 3, 3, 1, 4, 1, 0, 2, 3, 2, 0, 1]
  
]
  
columns = ['Player', 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]

score_card = pd.DataFrame(data, columns=columns)

score_board = [
  ['Lucas', 0],
  ['Mercedes', 0],
  ['Charlotte', 0],
  ['Danielle', 0],
  ['Franck', 0],
  ['JC', 0,],
  ['Alain', 0],
  ['Ursula', 0],
  ['Catherine', 0],
  ['Adele', 0], 
  ['Cariane', 0],
  ['Andy', 0],
  ['Paul Em', 0],
  ['Roland', 0],
  ['Siba', 0],
  ['Joe', 0],
  ['Peter', 0],
  ['Paul H', 0],
  ['David', 0]
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
    player_name = player_row['Player']
    player_score = player_row[hole1]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

if not hole2 == 0:
  for index, player_row in score_card.iterrows():
    player_name = player_row['Player']
    player_score = player_row[hole2]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

if not hole3 == 0:
  for index, player_row in score_card.iterrows():
    player_name = player_row['Player']
    player_score = player_row[hole3]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

if not hole4 == 0:
  for index, player_row in score_card.iterrows():
    player_name = player_row['Player']
    player_score = player_row[hole4]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

if not hole5 == 0:
  for index, player_row in score_card.iterrows():
    player_name = player_row['Player']
    player_score = player_row[hole5]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

if not hole6 == 0:
  for index, player_row in score_card.iterrows():
    player_name = player_row['Player']
    player_score = player_row[hole6]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

if not hole7 == 0:
  for index, player_row in score_card.iterrows():
    player_name = player_row['Player']
    player_score = player_row[hole7]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

if not hole8 == 0:
  for index, player_row in score_card.iterrows():
    player_name = player_row['Player']
    player_score = player_row[hole8]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

if not hole9 == 0:
  for index, player_row in score_card.iterrows():
    player_name = player_row['Player']
    player_score = player_row[hole9]
    score_board.loc[score_board['Player'] == player_name, 'Score'] = score_board.loc[score_board['Player'] == player_name, 'Score'] + player_score

score_board = score_board.sort_values(by='Score', ascending=False)
score_board = score_board.reset_index(drop=True)
score_board.index = score_board.index + 1 
score_board = score_board.style.set_table_attributes('style="font-size: 20px; width: 800px;"')


st.dataframe(score_board)
  
 
