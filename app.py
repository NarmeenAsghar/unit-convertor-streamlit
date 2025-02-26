import streamlit as st

# main title
st.title("🌍 Advanced Unit Convertor 🔄")
st.write("This app is used to covert the units of differnet physical quantities 💡")

# categories
categories = ["Length", "Weight", "Temperature", "Time"]

# user input from categories
select_category = st.selectbox("Select the unit from this to convert", categories)

# if user selects length
if select_category == "Length":
    length_units = ["Meter", "Kilometer", "Centimeter", "Foot", "Milimeter", "Micrometer", "Nanometer", "Mile", "Yard", "Inch"]
    col1, col2 = st.columns(2)
    with col1:
        select_unit_from = st.selectbox("Select the unit you want to convert from", length_units)
    with col2:
        select_unit_to = st.selectbox("Select the unit you want to convert to", length_units)

    value = st.number_input("Enter the value")

    if st.button("Convert 🔄"):
# From units
        if select_unit_from == "Meter":
            meters = value * 1
        elif select_unit_from == "Kilometer":
            meters = value * 1000
        elif select_unit_from == "Centimeter":
            meters = value * 0.01
        elif select_unit_from == "Foot":
            meters = value * 0.3048
        elif select_unit_from == "Milimeter":
            meters = value * 0.001
        elif select_unit_from == "Micrometer":
            meters = value * 0.000001
        elif select_unit_from == "Nanometer":
            meters = value * 1e-9
        elif select_unit_from == "Mile":
            meters = value * 1609.34
        elif select_unit_from == "Yard":
            meters = value * 0.9144
        elif select_unit_from == "Inch":
            meters = value * 0.0254

# To units
        if select_unit_to == "Meter":
            result = meters
        elif select_unit_to == "Kilometer":
            result = meters / 1000
        elif select_unit_to == "Centimeter":
            result = meters * 100
        elif select_unit_to == "Foot":
            result = meters / 0.3048
        elif select_unit_to == "Milimeter":
            result = meters * 1000
        elif select_unit_to == "Micrometer":
            result = meters * 1000000
        elif select_unit_to == "Nanometer":
            result = meters * 1e9
        elif select_unit_to == "Mile":
            result = meters / 1609.34
        elif select_unit_to == "Yard":
            result = meters / 0.9144
        elif select_unit_to == "Inch":
            result = meters / 0.0254
# result        
        st.success(f"{value} {select_unit_from} = {result} {select_unit_to}")

# if user select weight
elif select_category == "Weight":
    weight_units = ["Kilogram", "Gram", "Milligram", "Pound", "Ounce", "Metric Ton"]
    col1, col2 = st.columns(2)
    with col1:
        select_unit_from = st.selectbox("Select the unit you want to convert from", weight_units)
    with col2:
        select_unit_to = st.selectbox("Select the unit you want to convert to", weight_units)
    
    value = st.number_input("Enter the value")
    
    if st.button("Convert 🔄"):
# From unit
        if select_unit_from == "Kilogram":
            kg = value * 1
        elif select_unit_from == "Gram":
            kg = value * 0.001
        elif select_unit_from == "Milligram":
            kg = value * 0.000001
        elif select_unit_from == "Pound":
            kg = value * 0.453592
        elif select_unit_from == "Ounce":
            kg = value * 0.0283495
        elif select_unit_from == "Metric Ton":
            kg = value * 1000

# To units
        if select_unit_to == "Kilogram":
            result = kg
        elif select_unit_to == "Gram":
            result = kg * 1000
        elif select_unit_to == "Milligram":
            result = kg * 1000000
        elif select_unit_to == "Pound":
            result = kg / 0.453592
        elif select_unit_to == "Ounce":
            result = kg / 0.0283495
        elif select_unit_to == "Metric Ton":
            result = kg / 1000
# result           
        st.success(f"{value} {select_unit_from} = {result} {select_unit_to}")

# if user select temperature
elif select_category == "Temperature":
    temp_units = ["Celsius", "Fahrenheit", "Kelvin"]
    col1, col2 = st.columns(2)
    with col1:
        select_unit_from = st.selectbox("Select the unit you want to convert from", temp_units)
    with col2:
        select_unit_to = st.selectbox("Select the unit you want to convert to", temp_units)
    
    value = st.number_input("Enter the value")
    
    if st.button("Convert 🔄"):
# From units
        if select_unit_from == "Celsius":
            celsius = value
        elif select_unit_from == "Fahrenheit":
            celsius = (value - 32) * 5/9
        elif select_unit_from == "Kelvin":
            celsius = value - 273.15

# To units
        if select_unit_to == "Celsius":
            result = celsius
        elif select_unit_to == "Fahrenheit":
            result = (celsius * 9/5) + 32
        elif select_unit_to == "Kelvin":
            result = celsius + 273.15
# result          
        st.success(f"{value} {select_unit_from} = {result} {select_unit_to}")

# if user select time
elif select_category == "Time":
    time_units = ["Second", "Minute", "Hour", "Day", "Week", "Month", "Year"]
    col1, col2 = st.columns(2)
    with col1:
        select_unit_from = st.selectbox("Select the unit you want to convert from", time_units)
    with col2:
        select_unit_to = st.selectbox("Select the unit you want to convert to", time_units)
    
    value = st.number_input("Enter the value")
    
    if st.button("Convert 🔄"):
# From units
        if select_unit_from == "Second":
            seconds = value
        elif select_unit_from == "Minute":
            seconds = value * 60
        elif select_unit_from == "Hour":
            seconds = value * 3600
        elif select_unit_from == "Day":
            seconds = value * 86400
        elif select_unit_from == "Week":
            seconds = value * 604800

# To units
        if select_unit_to == "Second":
            result = seconds
        elif select_unit_to == "Minute":
            result = seconds / 60
        elif select_unit_to == "Hour":
            result = seconds / 3600
        elif select_unit_to == "Day":
            result = seconds / 86400
        elif select_unit_to == "Week":
            result = seconds / 604800
# result       
        st.success(f"{value} {select_unit_from} = {result} {select_unit_to}")

# separator for questions section
st.markdown("---")

# questions
st.subheader("🤔 Frequently Asked Questions ❓")
questions_categories = [
    "What is the main purpose of this app?",
    "What is the unit of length?",
    "What is the unit of weight?",
    "What is the unit of temperature?",
    "What is the unit of time?",
    "How do I convert between units?",
    "Which categories are available for conversion?",
    "What are the common length units used?",
    "What are the common weight units used?",
    "What are the temperature scales available?",
    "What are the time units available for conversion?"
]

select_question = st.selectbox("Select a Question", questions_categories)

# answers
if select_question == "What is the main purpose of this app?":
    st.write("This app is designed to convert units between different measurement systems easily and accurately. It supports conversions for length, weight, temperature, and time.")

elif select_question == "What is the unit of length?":
    st.write("A unit of length is a standardized way to measure distance. The base unit in the metric system is the meter (m).")

elif select_question == "What is the unit of weight?":
    st.write("A unit of weight measures the mass of an object. The base unit in the metric system is the kilogram (kg).")

elif select_question == "What is the unit of temperature?":
    st.write("Temperature units measure how hot or cold something is. The most common scales are Celsius (°C), Fahrenheit (°F), and Kelvin (K).")

elif select_question == "What is the unit of time?":
    st.write("Time units measure duration. The base unit is the second (s), with larger units including minutes, hours, days, weeks.")

elif select_question == "How do I convert between units?":
    st.write("To convert between units:\n"
             "1. Select a category (Length, Weight, Temperature, or Time)\n"
             "2. Choose the unit you want to convert from\n"
             "3. Choose the unit you want to convert to\n"
             "4. Enter the value you want to convert\n"
             "5. Click the 'Convert' button to see the result")

elif select_question == "Which categories are available for conversion?":
    st.write("This app supports four main categories of conversion:\n"
             "• Length\n"
             "• Weight\n"
             "• Temperature\n"
             "• Time")

elif select_question == "What are the common length units used?":
    st.write("The available length units are:\n"
             "• Meter (m)\n"
             "• Kilometer (km)\n"
             "• Centimeter (cm)\n"
             "• Foot (ft)\n"
             "• Millimeter (mm)\n"
             "• Micrometer (μm)\n"
             "• Nanometer (nm)\n"
             "• Mile (mi)\n"
             "• Yard (yd)\n"
             "• Inch (in)")

elif select_question == "What are the common weight units used?":
    st.write("The available weight units are:\n"
             "• Kilogram (kg)\n"
             "• Gram (g)\n"
             "• Milligram (mg)\n"
             "• Pound (lb)\n"
             "• Ounce (oz)\n"
             "• Metric Ton (t)")

elif select_question == "What are the temperature scales available?":
    st.write("The available temperature scales are:\n"
             "• Celsius (°C) - Used in most countries\n"
             "• Fahrenheit (°F) - Commonly used in the United States\n"
             "• Kelvin (K) - Used in scientific measurements")

elif select_question == "What are the time units available for conversion?":
    st.write("The available time units are:\n"
             "• Second (s)\n"
             "• Minute (min)\n"
             "• Hour (h)\n"
             "• Day (d)\n"
             "• Week (w)")
