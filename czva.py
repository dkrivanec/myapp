import streamlit as st

# Title for the app
st.title("Simple Calculator")

# Input fields for numbers x and y
x = st.number_input("Enter number x", value=0.0)
y = st.number_input("Enter number y", value=0.0)

# Dropdown to select the operation
operation = st.selectbox("Select operation", ["Addition", "Subtraction", "Multiplication", "Division"])

# Perform the calculation when the button is pressed
if st.button("Calculate"):
    if operation == "Addition":
        result = x + y
    elif operation == "Subtraction":
        result = x - y
    elif operation == "Multiplication":
        result = x * y
    elif operation == "Division":
        result = "Error: Division by zero!" if y == 0 else x / y

    # Display the result
    st.write(f"Result: {result}")
