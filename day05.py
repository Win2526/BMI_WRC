import numpy as np
import altair as alt
import pandas as pd
import streamlit as st

{
    "first_key" : "WRC",
    "second_key" : "two",
    "third_key" : "true"
}

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

add_sidebar = st.sidebar.selectbox('Select a Option !', ('Table1', 'Table2','Table3 Random & Chart','Spare1','BMI','Spare3','Spare4'))
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


if add_sidebar == 'BMI':

    # Title of the app
    st.title("BMI Calculator")

    # Input: Weight in kilograms
    weight = st.number_input("Enter your weight (kg):", min_value=0.0, format="%.2f")

    # Input: Height format selection
    height_unit = st.radio("Select your height unit:", ['Centimeters', 'Meters', 'Feet'])

    # Input: Height value based on selected unit
    height = st.number_input(f"Enter your height ({height_unit.lower()}):", min_value=0.0,
                             format="%.2f")  # .lower เป็น method ของ string เป็น อักษรตัวเล็ก

    # Calculate BMI when button is pressed
    if st.button("Calculate BMI"):
        try:
            # Convert height to meters based on selected unit
            if height_unit == 'Centimeters':
                height_m = height / 100
            elif height_unit == 'Feet':
                height_m = height / 3.28
            else:
                height_m = height

            # Prevent division by zero
            if height_m <= 0:
                st.error("Height must be greater than zero.")
            else:
                bmi = weight / (height_m ** 2)
                st.success(f"Your BMI is {bmi:.2f}")

                # BMI interpretation
                if bmi < 16:
                    st.error("You are Extremely Underweight")
                elif 16 <= bmi < 18.5:
                    st.warning("You are Underweight")
                elif 18.5 <= bmi < 25:
                    st.success("You are Healthy")
                elif 25 <= bmi < 30:
                    st.warning("You are Overweight")
                else:
                    st.error("You are Extremely Overweight")
        except:
            st.error("Please enter valid numeric values.")

