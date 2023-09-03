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

def find_smallest(data):
  smallest_num=None
  if data['First_Num'] <= data['Second_Num']:
    if data['First_Num'] <= data['Third_Num']:
      smallest_num = data['First_Num']
    else:
      smallest_num = data['Third_Num']
  elif  data['Third_Num'] <= data['Second_Num']:
    smallest_num = data['Third_Num']
  else:
     smallest_num = data['Second_Num']
  return smallest_num

  
data = user_input_features()
Smallest_Num = find_smallest(data)
Largest_Num = find_largest(data)

st.subheader("Smallest Number is : " + str(Smallest_Num))
st.subheader("Largest Number is : " + str(Largest_Num))
