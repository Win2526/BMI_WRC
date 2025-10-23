import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

st.header('st.write')

# Example 1

st.write('Hello, *World!* :sunglasses:, ')

# Example 2

st.write(1234)

df = pd.DataFrame({
     'first column': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
     'second column': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100],
     'Calculation': [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
})

add_sidebar = st.sidebar.selectbox('Select a Option !', ('Table1', 'Table2','Table3 Random & Chart','Spare1','Spare2','Spare3','Spare4'))
if add_sidebar == 'Table1':
     # Example 3

     st.write('Table1 is a Manual DataFrame:',df)


# Example 4
if add_sidebar == 'Table2':
     st.write('Table2 is a DataFrame:', df)

     # Example 5
if add_sidebar == 'Table3 Random & Chart':
     df2 = pd.DataFrame(
          np.random.randn(100, 3),
          columns=['a1', 'b1', 'c1'])

     st.write('Table3 Random Data:',df2)

     c = alt.Chart(df2).mark_circle().encode(
          x='a1', y='b1', size='c1', color='c1', tooltip=['a1', 'b1', 'c1'])
     st.write('Chart Of Random:', c)

if add_sidebar == 'Spare1':
     st.markdown("*Streamlit* is **really** ***cool***.")
     st.markdown('''
         :red[Streamlit] :orange[can] :green[write] :blue[text] :violet[in]
         :gray[pretty] :rainbow[colors] and :blue-background[highlight] text.''')
     st.markdown("Here's a bouquet &mdash;\
                 :tulip::cherry_blossom::rose::hibiscus::sunflower::blossom:")

     multi = '''If you end a line with two spaces,
     a soft return is used for the next line.

     Two (or more) newline characters in a row will result in a hard return.
     '''
     st.markdown(multi)