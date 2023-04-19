import streamlit as st

st.write(""" # Find Largest Number """)

st.header('Input Three Numbers')

def user_input_features():
  first_num = st.number_input("First Number")
  second_num = st.number_input("Second Number")
  third_num = st.number_input("Third Number")
  
  data = {'First_Num': first_num,
          'Second_Num': second_num,
          'Third_Num': third_num,
          }
  return data

def find_largest(data):
  largest_num=None
  if data['First_Num'] >= data['Second_Num']:
    if data['First_Num'] >= data['Third_Num']:
      largest_num = data['First_Num']
    else:
      largest_num = data['Third_Num']
  elif  data['Third_Num'] >= data['Second_Num']:
    largest_num = data['Third_Num']
  else:
     largest_num = data['Second_Num']
  return largest_num

data = user_input_features()
Largest_Num = find_largest(data)

st.subheader("Largest Number is : " + str(Largest_Num))