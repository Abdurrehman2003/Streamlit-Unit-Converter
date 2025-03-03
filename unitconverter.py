import streamlit as st
import time
import random

# Set Streamlit page configuration
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Define conversion factors
conversion_factors = {
    'Length': {
        'Meters': 1, 'Kilometers': 0.001, 'Miles': 0.000621371, 'Feet': 3.28084, 'Inches': 39.3701,
        'Centimeters': 100, 'Millimeters': 1000, 'Yards': 1.09361, 'Nautical Miles': 0.000539957
    },
    'Weight': {
        'Grams': 1, 'Kilograms': 0.001, 'Pounds': 0.00220462, 'Ounces': 0.035274, 'Stones': 0.000157473, 'Tons': 0.000001
    },
    'Temperature': {
        'Celsius': lambda x: x,
        'Fahrenheit': lambda x: (x * 9/5) + 32,
        'Kelvin': lambda x: x + 273.15
    },
    'Time': {
        'Seconds': 1, 'Minutes': 1/60, 'Hours': 1/3600, 'Days': 1/86400, 'Weeks': 1/604800, 'Months': 1/2628000, 'Years': 1/31536000
    },
    'Speed': {
        'Meters per Second': 1, 'Kilometers per Hour': 3.6, 'Miles per Hour': 2.23694, 'Feet per Second': 3.28084, 'Knots': 1.94384
    }
}

# Function to convert units
def convert_units(value, from_unit, to_unit, conversion_type):
    if conversion_type == 'Temperature':
        if from_unit == 'Celsius':
            return conversion_factors['Temperature'][to_unit](value)
        elif from_unit == 'Fahrenheit':
            celsius = (value - 32) * 5/9
            return conversion_factors['Temperature'][to_unit](celsius)
        elif from_unit == 'Kelvin':
            celsius = value - 273.15
            return conversion_factors['Temperature'][to_unit](celsius)
    else:
        return value * conversion_factors[conversion_type][to_unit] / conversion_factors[conversion_type][from_unit]

# Apply custom CSS for modern design
st.markdown("""
    <style>
        .stApp {
            background-color: #f8f9fa;
            font-family: 'Arial', sans-serif;
        }
        .stButton>button {
            background-color: #007bff;
            color: white;
            border-radius: 8px;
            padding: 12px 24px;
            font-size: 16px;
            transition: background-color 0.3s ease;
        }
        .stButton>button:hover {
            background-color: #0056b3;
        }
        .stTextInput>div>div>input {
            border-radius: 8px;
            padding: 12px;
            border: 1px solid #ced4da;
        }
        .stSelectbox>div>div>select {
            border-radius: 8px;
            padding: 12px;
            border: 1px solid #ced4da;
        }
        .stSuccess {
            background-color: #d4edda;
            color: #155724;
            border-radius: 8px;
            padding: 16px;
            margin-top: 16px;
        }
        .stError {
            background-color: #f8d7da;
            color: #721c24;
            border-radius: 8px;
            padding: 16px;
            margin-top: 16px;
        }
        .stSpinner>div {
            text-align: center;
            margin-top: 16px;
        }
        .stMarkdown h1 {
            color: #007bff;
            text-align: center;
            margin-bottom: 24px;
        }
        .stMarkdown h2 {
            color: #343a40;
            text-align: center;
            margin-bottom: 16px;
        }
    </style>
""", unsafe_allow_html=True)

# Streamlit UI
st.title("🔄 Unit Converter")
st.markdown("### Easily convert between different units of measurement")

# Select conversion type
conversion_type = st.selectbox(
    "**Choose a category**",
    list(conversion_factors.keys()),
    key="conversion_type"
)

# Input value
value = st.number_input(
    "**Enter value to convert**",
    min_value=0.0,
    format="%.2f",
    key="value_input"
)

# Select units
col1, col2 = st.columns(2)
with col1:
    from_unit = st.selectbox(
        "**From unit**",
        list(conversion_factors[conversion_type].keys()),
        key="from_unit"
    )
with col2:
    to_unit = st.selectbox(
        "**To unit**",
        list(conversion_factors[conversion_type].keys()),
        key="to_unit"
    )

# Convert and display result
if st.button("**Convert**", key="convert_button"):
    with st.spinner("Processing..."):
        time.sleep(random.uniform(0.5, 1.5))
    try:
        if value < 0 and conversion_type != 'Temperature':
            st.error("Please enter a non-negative value for this conversion type.")
        else:
            result = convert_units(value, from_unit, to_unit, conversion_type)
            st.success(f"**{value} {from_unit} is equal to {result:.4f} {to_unit}**")
    except Exception as e:
        st.error("An error occurred. Please check your input values.")

# Footer
st.markdown("---")
st.markdown("Built with ❤️ using [Streamlit](https://streamlit.io)")