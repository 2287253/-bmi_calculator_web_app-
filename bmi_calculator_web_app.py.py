import streamlit as st

def calculate_bmi(weight, height):
    """Calculate BMI and return the value and category"""
    height_in_meters = height / 100  # Convert cm to meters
    bmi = weight / (height_in_meters ** 2)
    
    if bmi < 18.5:
        category = "Underweight"
    elif 18.5 <= bmi < 25:
        category = "Normal weight"
    elif 25 <= bmi < 30:
        category = "Overweight"
    else:
        category = "Obese"
    
    return round(bmi, 2), category

def main():
    st.set_page_config(
        page_title="BMI Calculator",
        page_icon="⚖️",
        layout="centered"
    )
    
    st.title("BMI Calculator")
    st.write("Calculate your Body Mass Index (BMI) and check your health category.")
    
    # Create two columns for input fields
    col1, col2 = st.columns(2)
    
    with col1:
        weight = st.number_input(
            "Enter your weight (kg)",
            min_value=30.0,
            max_value=300.0,
            value=70.0,
            step=0.1
        )
    
    with col2:
        height = st.number_input(
            "Enter your height (cm)",
            min_value=100.0,
            max_value=250.0,
            value=170.0,
            step=0.1
        )
    
    if st.button("Calculate BMI"):
        bmi, category = calculate_bmi(weight, height)
        
        st.markdown("---")
        st.markdown(f"### Your BMI: **{bmi}**")
        st.markdown(f"### Category: **{category}**")
        
        # Display BMI chart
        st.markdown("### BMI Categories:")
        st.markdown("""
        - Underweight: < 18.5
        - Normal weight: 18.5 - 24.9
        - Overweight: 25 - 29.9
        - Obese: ≥ 30
        """)
        
        # Add some styling
        st.markdown("""
        <style>
        .stApp {
            background-color: #f0f2f6;
        }
        </style>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    main() 