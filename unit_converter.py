import streamlit as st

def main():
    st.title("Unit Converter App")
    st.write("Easily convert between different units")
    
    # Sidebar for conversion type selection
    conversion_type = st.sidebar.selectbox(
        "Select Conversion Type",
        ["Length", "Weight", "Temperature", "Time"]
    )
    
    if conversion_type == "Length":
        length_converter()
    elif conversion_type == "Weight":
        weight_converter()
    elif conversion_type == "Temperature":
        temperature_converter()
    elif conversion_type == "Time":
        time_converter()
    
    # Footer
    st.sidebar.markdown("---")
    st.sidebar.info("This app is built using Streamlit and Python")

def length_converter():
    st.header("Length Converter")
    
    # List of units
    units = {
        "Millimeter": 0.001,
        "Centimeter": 0.01,
        "Meter": 1.0,
        "Kilometer": 1000.0,
        "Inch": 0.0254,
        "Foot": 0.3048,
        "Yard": 0.9144,
        "Mile": 1609.34
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=0.0)
        input_unit = st.selectbox("From", list(units.keys()), key="input_length")
    
    with col2:
        output_unit = st.selectbox("To", list(units.keys()), key="output_length")
        # Calculate conversion
        result = input_value * units[input_unit] / units[output_unit]
        st.success(f"{input_value} {input_unit} = {result:.6f} {output_unit}")

def weight_converter():
    st.header("Weight Converter")
    
    # List of units
    units = {
        "Milligram": 0.001,
        "Gram": 1.0,
        "Kilogram": 1000.0,
        "Metric Ton": 1000000.0,
        "Ounce": 28.3495,
        "Pound": 453.592,
        "Stone": 6350.29
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=0.0)
        input_unit = st.selectbox("From", list(units.keys()), key="input_weight")
    
    with col2:
        output_unit = st.selectbox("To", list(units.keys()), key="output_weight")
        # Calculate conversion
        result = input_value * units[input_unit] / units[output_unit]
        st.success(f"{input_value} {input_unit} = {result:.6f} {output_unit}")

def temperature_converter():
    st.header("Temperature Converter")
    
    units = ["Celsius", "Fahrenheit", "Kelvin"]
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=0.0)
        input_unit = st.selectbox("From", units, key="input_temp")
    
    with col2:
        output_unit = st.selectbox("To", units, key="output_temp")
        
        # Calculate conversion
        if input_unit == output_unit:
            result = input_value
        elif input_unit == "Celsius" and output_unit == "Fahrenheit":
            result = (input_value * 9/5) + 32
        elif input_unit == "Celsius" and output_unit == "Kelvin":
            result = input_value + 273.15
        elif input_unit == "Fahrenheit" and output_unit == "Celsius":
            result = (input_value - 32) * 5/9
        elif input_unit == "Fahrenheit" and output_unit == "Kelvin":
            result = ((input_value - 32) * 5/9) + 273.15
        elif input_unit == "Kelvin" and output_unit == "Celsius":
            result = input_value - 273.15
        elif input_unit == "Kelvin" and output_unit == "Fahrenheit":
            result = ((input_value - 273.15) * 9/5) + 32
        
        st.success(f"{input_value} {input_unit} = {result:.2f} {output_unit}")

def time_converter():
    st.header("Time Converter")
    
    # List of units
    units = {
        "Second": 1.0,
        "Minute": 60.0,
        "Hour": 3600.0,
        "Day": 86400.0,
        "Week": 604800.0,
        "Month (30 days)": 2592000.0,
        "Year": 31536000.0
    }
    
    col1, col2 = st.columns(2)
    
    with col1:
        input_value = st.number_input("Enter value", value=0.0)
        input_unit = st.selectbox("From", list(units.keys()), key="input_time")
    
    with col2:
        output_unit = st.selectbox("To", list(units.keys()), key="output_time")
        # Calculate conversion
        result = input_value * units[input_unit] / units[output_unit]
        st.success(f"{input_value} {input_unit} = {result:.6f} {output_unit}")

if __name__ == "__main__":
    main()