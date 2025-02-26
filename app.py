import streamlit as st
from pint import UnitRegistry

ureg = UnitRegistry()

def load_css(file_name):
    with open(file_name, "r") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Load external CSS
load_css("style.css")


st.title("📏 Unit Converter")

# select category
category = st.selectbox('Choose conversion category:', ['Length', 'Weight', 'Temperature'])

# Unit categories
if category == 'Length':
    units = ['meters', 'kilometers', 'centimeters', 'millimeters', 'miles', 'yards', 'feet', 'inches']
elif category == 'Weight':
    units = ['grams', 'kilograms', 'pounds', 'ounces']
else:  
    units = ['Celsius', 'Fahrenheit', 'Kelvin']


amount = st.number_input(f'Enter amount in {units[0]}:', min_value=0.0, step=0.1)

# convert from
from_unit = st.selectbox('Select unit to convert from:', units)

# Convert to
to_unit = st.selectbox('Select unit to convert to:', units)


if amount > 0:
    try:
        from_quantity = amount * ureg(from_unit)
        converted_quantity = from_quantity.to(to_unit)
        st.write(f'**{amount} {from_unit} is equal to {converted_quantity.magnitude:.2f} {to_unit}**')
    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.write("Please enter a valid amount to convert.")
