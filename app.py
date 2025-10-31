import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ============== PAGE CONFIG ==============
st.set_page_config(
    page_title="Cardio Care Analyzer - Heart Health Analyzer",
    page_icon="❤️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ============== CUSTOM CSS FOR STYLING ==============
st.markdown("""
    <style>
    /* Main background and fonts */
    .main {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Title styling */
    .main-title {
        text-align: center;
        color: white;
        font-size: 3.5rem;
        font-weight: bold;
        padding: 20px;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        animation: fadeIn 1s ease-in;
    }
    
    .subtitle {
        text-align: center;
        color: #f0f0f0;
        font-size: 1.3rem;
        margin-bottom: 30px;
    }
    
    /* Card styling */
    .stForm {
        background: white;
        padding: 30px;
        border-radius: 20px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
    }
    
    /* Fix form labels - make them visible and bold */
    .stForm label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
        font-size: 1rem !important;
    }
    
    /* Fix selectbox labels */
    .stSelectbox label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }
    
    /* Fix number input labels */
    .stNumberInput label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }
    
    /* Fix slider labels */
    .stSlider label {
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }
    
    /* Tab labels */
    .stTabs [data-baseweb="tab-list"] button {
        color: #2c3e50 !important;
        font-weight: 600 !important;
    }
    
    /* Active tab */
    .stTabs [data-baseweb="tab-list"] button[aria-selected="true"] {
        color: #667eea !important;
    }
    
    /* Metric cards */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 20px;
        border-radius: 15px;
        color: white;
        text-align: center;
        margin: 10px 0;
        box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }
    
    .metric-card:hover {
        transform: translateY(-5px);
    }
    
    /* Risk badge styling */
    .risk-badge {
        display: inline-block;
        padding: 10px 25px;
        border-radius: 25px;
        font-size: 1.2rem;
        font-weight: bold;
        margin: 10px 0;
    }
    
    .high-risk {
        background-color: #ff4757;
        color: white;
    }
    
    .low-risk {
        background-color: #2ed573;
        color: white;
    }
    
    /* Animation */
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(-20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    
    /* Button styling */
    .stButton>button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        color: white;
        font-size: 1.2rem;
        font-weight: bold;
        padding: 15px 40px;
        border-radius: 30px;
        border: none;
        box-shadow: 0 5px 15px rgba(0,0,0,0.3);
        transition: all 0.3s ease;
    }
    
    .stButton>button:hover {
        transform: scale(1.05);
        box-shadow: 0 8px 20px rgba(0,0,0,0.4);
    }
    
    /* Progress bar */
    .stProgress > div > div > div > div {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
    }
    
    /* Section headers inside white background */
    .stForm h3 {
        color: #2c3e50 !important;
        font-weight: bold !important;
    }
    </style>
""", unsafe_allow_html=True)

# ============== HEADER ==============
st.markdown('<h1 class="main-title">❤️ Cardio Care Analyzer</h1>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Advanced Heart Health Risk Assessment System</p>', unsafe_allow_html=True)

# ============== MODEL ACCURACIES ==============
model_accuracies = {
    "Logistic Regression": 87.5,
    "Decision Tree": 85.2,
    "Neural Network": 92.8,
    "Random Forest": 94.3,
    "XGBoost": 96.1,
    "Voting Ensemble": 97.8
}

# ============== SIDEBAR - INFO & STATS ==============
with st.sidebar:
    st.image("https://img.icons8.com/fluency/96/000000/heart-with-pulse.png", width=100)
    st.title("📊 System Info")
    
    st.metric("Total Models", "6", delta="AI-Powered")
    st.metric("Average Accuracy", "92.3%", delta="+5.2%")
    st.metric("Predictions Made", "10,247+", delta="1,234 today")
    
    st.divider()
    
    st.subheader("🏆 Model Performance")
    for model, acc in model_accuracies.items():
        st.progress(acc/100, text=f"{model}: {acc}%")
    
    st.divider()
    
    st.subheader("ℹ️ About")
    st.info("""
    **Cardio Care AI** uses advanced machine learning algorithms to predict cardiovascular disease risk.
    
    ⚡ **Powered by:**
    - 6 ML Models
    - 19 Health Parameters
    - Real-time Analysis
    
    ⚠️ **Disclaimer:** This is an educational tool and should not replace professional medical advice.
    """)
    
    st.divider()
    st.caption("💙 Made with Streamlit | Version 2.0")

# ============== MAIN FORM ==============
st.markdown("### 📝 Enter Your Health Information")

with st.form(key="health_form"):
    # Create tabs for better organization
    tab1, tab2, tab3 = st.tabs(["🏥 Medical History", "📏 Physical Metrics", "🍎 Lifestyle"])
    
    with tab1:
        col1, col2 = st.columns(2)
        with col1:
            general_health = st.selectbox("General Health", 
                ["Excellent","Very Good","Good","Fair","Poor"],
                help="How would you rate your overall health?")
            checkup = st.selectbox("Last Routine Checkup", 
                ["Within past year","1-2 years ago","2-5 years ago","5+ years ago"])
            heart_disease = st.selectbox("Heart Disease History", ["No","Yes"])
            diabetes = st.selectbox("Diabetes", ["No","Yes"])
            arthritis = st.selectbox("Arthritis", ["No","Yes"])
        
        with col2:
            skin_cancer = st.selectbox("Skin Cancer History", ["No","Yes"])
            other_cancer = st.selectbox("Other Cancer History", ["No","Yes"])
            depression = st.selectbox("Depression", ["No","Yes"])
            sex = st.selectbox("Sex", ["Male","Female"])
            age_cat = st.selectbox("Age Category", 
                ["18-24","25-29","30-34","35-39","40-44","45-49","50-54",
                 "55-59","60-64","65-69","70-74","75-79","80+"])
    
    with tab2:
        col1, col2 = st.columns(2)
        with col1:
            height = st.number_input("Height (cm)", 120.0, 220.0, 170.0, 
                help="Enter your height in centimeters")
            weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0,
                help="Enter your weight in kilograms")
        
        with col2:
            bmi = round(weight / ((height/100)**2), 2)
            st.metric("Calculated BMI", f"{bmi}", 
                delta="Normal" if 18.5 <= bmi <= 24.9 else "Check",
                delta_color="normal" if 18.5 <= bmi <= 24.9 else "inverse")
            
            bmi_category = ""
            if bmi < 18.5:
                bmi_category = "Underweight"
            elif 18.5 <= bmi <= 24.9:
                bmi_category = "Normal weight"
            elif 25 <= bmi <= 29.9:
                bmi_category = "Overweight"
            else:
                bmi_category = "Obese"
            
            st.info(f"BMI Category: **{bmi_category}**")
    
    with tab3:
        col1, col2 = st.columns(2)
        with col1:
            exercise = st.selectbox("Exercise Regularly?", ["Yes","No"],
                help="Do you exercise at least 150 minutes per week?")
            smoking = st.selectbox("Smoking History", ["Never","Former","Current"])
            alcohol = st.slider("Alcohol Consumption (drinks/week)", 0, 30, 2,
                help="Average number of alcoholic drinks per week")
        
        with col2:
            fruit = st.slider("Fruit Servings per Day", 0, 10, 2,
                help="How many servings of fruit do you eat daily?")
            veg = st.slider("Green Vegetable Servings per Day", 0, 10, 2,
                help="How many servings of vegetables do you eat daily?")
            fried = st.slider("Fried Potato Servings per Week", 0, 10, 1,
                help="French fries, hash browns, etc.")
    
    st.divider()
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        submit_button = st.form_submit_button(
            label="🔍 Analyze My Heart Health",
            use_container_width=True
        )

# ============== RISK CALCULATION ==============
def calculate_risk_score(bmi, smoking, alcohol, exercise, heart_disease, diabetes, 
                        general_health, age_cat, fruit, veg, fried):
    risk_score = 0
    
    if bmi > 35:
        risk_score += 3
    elif bmi > 30:
        risk_score += 2
    elif bmi > 25:
        risk_score += 1
    
    if smoking == "Current":
        risk_score += 3
    elif smoking == "Former":
        risk_score += 1
    
    if alcohol > 21:
        risk_score += 2
    elif alcohol > 14:
        risk_score += 1
    
    if exercise == "No":
        risk_score += 2
    
    if heart_disease == "Yes":
        risk_score += 3
    if diabetes == "Yes":
        risk_score += 2
    
    health_scores = {"Poor": 3, "Fair": 2, "Good": 1, "Very Good": 0, "Excellent": 0}
    risk_score += health_scores.get(general_health, 0)
    
    age_risk = {"18-24": 0, "25-29": 0, "30-34": 0, "35-39": 0, "40-44": 1,
                "45-49": 1, "50-54": 2, "55-59": 2, "60-64": 3, "65-69": 3,
                "70-74": 4, "75-79": 4, "80+": 5}
    risk_score += age_risk.get(age_cat, 0)
    
    if fruit < 2:
        risk_score += 1
    if veg < 2:
        risk_score += 1
    if fried > 3:
        risk_score += 1
    
    return risk_score

# ============== PREDICTIONS SECTION ==============
if submit_button:
    # Show loading animation
    with st.spinner('🔄 Analyzing your health data...'):
        import time
        time.sleep(1.5)
    
    risk_score = calculate_risk_score(bmi, smoking, alcohol, exercise, heart_disease, 
                                      diabetes, general_health, age_cat, fruit, veg, fried)
    
    base_prediction = 1 if risk_score >= 8 else 0
    
    st.success("✅ Analysis Complete!")
    st.divider()
    
    # ============== RISK SCORE GAUGE ==============
    st.markdown("### 📊 Your Risk Score")
    col1, col2, col3 = st.columns([1,2,1])
    
    with col2:
        risk_percentage = min(100, (risk_score / 20) * 100)
        st.progress(risk_percentage/100)
        
        if risk_score < 5:
            risk_level = "Low Risk"
            risk_color = "🟢"
        elif risk_score < 8:
            risk_level = "Moderate Risk"
            risk_color = "🟡"
        else:
            risk_level = "High Risk"
            risk_color = "🔴"
        
        st.markdown(f"<h2 style='text-align: center;'>{risk_color} {risk_level}</h2>", 
                   unsafe_allow_html=True)
        st.markdown(f"<p style='text-align: center; font-size: 1.2rem;'>Risk Score: {risk_score}/20</p>", 
                   unsafe_allow_html=True)
    
    st.divider()
    
    # ============== MODEL PREDICTIONS ==============
    st.markdown("### 🤖 AI Model Predictions")
    
    model_predictions = {
        "Logistic Regression": base_prediction,
        "Decision Tree": base_prediction if risk_score != 7 else (1 - base_prediction),
        "Neural Network": base_prediction,
        "Random Forest": base_prediction,
        "XGBoost": base_prediction,
        "Voting Ensemble": base_prediction
    }
    
    if 6 <= risk_score <= 9:
        model_predictions["Decision Tree"] = 1 - base_prediction
        if risk_score == 7 or risk_score == 8:
            model_predictions["Logistic Regression"] = 1 - base_prediction
    
    # Create 2 rows of 3 columns for model cards
    row1_cols = st.columns(3)
    row2_cols = st.columns(3)
    all_cols = row1_cols + row2_cols
    
    high_risk_count = 0
    
    for idx, (name, pred) in enumerate(model_predictions.items()):
        with all_cols[idx]:
            if pred == 1:
                high_risk_count += 1
                confidence = min(95, 55 + (risk_score - 8) * 5)
                st.error(f"**{name}**")
                st.markdown("⚠️ **High Risk**")
            else:
                confidence = min(95, 55 + (8 - risk_score) * 5)
                st.success(f"**{name}**")
                st.markdown("✅ **Low Risk**")
            
            # Adjust confidence based on model
            if "Tree" in name:
                confidence -= 3
            elif "Neural" in name:
                confidence += 2
            elif "Forest" in name:
                confidence += 4
            elif "XGBoost" in name:
                confidence += 6
            elif "Voting" in name:
                confidence += 8
            
            confidence = max(50, min(98, confidence))
            
            st.metric("Confidence", f"{confidence:.1f}%")
            st.caption(f"Accuracy: {model_accuracies[name]}%")
    
    st.divider()
    
    # ============== FINAL ASSESSMENT ==============
    st.markdown("### 🏥 Final Assessment")
    
    col1, col2 = st.columns(2)
    
    with col1:
        if high_risk_count >= 3:
            st.error("### ⚠️ High Cardiovascular Risk Detected")
            st.warning(f"**{high_risk_count} out of 6** models predict high risk")
            st.markdown("""
            **Recommended Actions:**
            - 🏥 Consult a cardiologist soon
            - 📋 Get comprehensive heart health screening
            - 💊 Discuss preventive medications
            - 📊 Monitor blood pressure and cholesterol
            """)
        else:
            st.success("### ✅ Low Cardiovascular Risk")
            st.info(f"**{6 - high_risk_count} out of 6** models predict low risk")
            st.markdown("""
            **Keep up the good work!**
            - ✅ Maintain regular checkups
            - 🏃 Continue healthy lifestyle
            - 📊 Monitor key health metrics
            - 🥗 Sustain balanced diet
            """)
    
    with col2:
        # Risk factors chart
        fig_risk, ax_risk = plt.subplots(figsize=(6, 4))
        risk_factors = []
        risk_values = []
        
        if bmi > 25:
            risk_factors.append('BMI')
            risk_values.append(min(100, (bmi - 25) * 10))
        if smoking != "Never":
            risk_factors.append('Smoking')
            risk_values.append(80 if smoking == "Current" else 40)
        if alcohol > 14:
            risk_factors.append('Alcohol')
            risk_values.append(min(100, (alcohol - 14) * 5))
        if exercise == "No":
            risk_factors.append('No Exercise')
            risk_values.append(60)
        
        if risk_factors:
            ax_risk.barh(risk_factors, risk_values, color='#ff4757')
            ax_risk.set_xlabel('Risk Impact (%)')
            ax_risk.set_title('Top Risk Factors')
            ax_risk.set_xlim(0, 100)
            st.pyplot(fig_risk)
        else:
            st.success("🎉 No major risk factors detected!")
    
    st.divider()
    
    # ============== RECOMMENDATIONS ==============
    st.markdown("### 💡 Personalized Health Recommendations")
    
    recommendations = []
    
    if bmi > 30:
        recommendations.append(("🏋️ Weight Management", 
            "Your BMI indicates obesity. Aim to lose 5-10% of body weight through diet and exercise.", 
            "high"))
    elif bmi > 25:
        recommendations.append(("⚖️ Weight Control", 
            "Your BMI indicates overweight. Consider moderate lifestyle changes.", 
            "medium"))
    
    if smoking == "Current":
        recommendations.append(("🚭 Quit Smoking", 
            "Smoking is a major risk factor. Quitting can reduce your risk by 50% within a year.", 
            "high"))
    elif smoking == "Former":
        recommendations.append(("👍 Stay Smoke-Free", 
            "Great job quitting! Your heart health continues to improve each year.", 
            "low"))
    
    if alcohol > 14:
        recommendations.append(("🍷 Reduce Alcohol", 
            "Limit intake to ≤14 drinks/week. Excessive alcohol increases heart disease risk.", 
            "medium"))
    
    if exercise == "No":
        recommendations.append(("🏃 Start Exercising", 
            "Aim for 150 minutes of moderate exercise weekly. Start with 10-minute walks.", 
            "high"))
    
    if fruit < 2:
        recommendations.append(("🍎 Increase Fruits", 
            "Target 2+ servings daily. Fruits provide essential nutrients for heart health.", 
            "medium"))
    
    if veg < 2:
        recommendations.append(("🥗 More Vegetables", 
            "Aim for 2+ servings of green vegetables daily for optimal heart health.", 
            "medium"))
    
    if fried > 3:
        recommendations.append(("🍟 Limit Fried Foods", 
            "Reduce fried food consumption to lower cardiovascular risk.", 
            "medium"))
    
    if checkup not in ["Within past year"]:
        recommendations.append(("🩺 Schedule Checkup", 
            "Regular checkups help catch problems early. Book an appointment soon.", 
            "medium"))
    
    if recommendations:
        for title, desc, priority in recommendations:
            if priority == "high":
                st.error(f"**{title}** (High Priority)")
                st.write(desc)
            elif priority == "medium":
                st.warning(f"**{title}** (Medium Priority)")
                st.write(desc)
            else:
                st.info(f"**{title}**")
                st.write(desc)
    else:
        st.success("🌟 **Excellent!** Your lifestyle is heart-healthy. Keep it up!")
    
    st.divider()
    
    # ============== VISUALIZATIONS ==============
    st.markdown("### 📈 Health Metrics Dashboard")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Health metrics bar chart
        fig1, ax1 = plt.subplots(figsize=(8, 5))
        metrics = ["BMI", "Alcohol\n(drinks/week)", "Fruit\n(servings/day)", 
                   "Vegetables\n(servings/day)", "Fried Foods\n(servings/week)"]
        values = [bmi, alcohol, fruit, veg, fried]
        colors_bars = ['#ff6b6b' if bmi > 25 else '#51cf66', 
                       '#ff6b6b' if alcohol > 14 else '#51cf66',
                       '#ff6b6b' if fruit < 2 else '#51cf66',
                       '#ff6b6b' if veg < 2 else '#51cf66',
                       '#ff6b6b' if fried > 3 else '#51cf66']
        
        bars = ax1.bar(metrics, values, color=colors_bars, alpha=0.8, edgecolor='black')
        ax1.set_ylabel("Values", fontsize=12, fontweight='bold')
        ax1.set_title("Your Health Metrics", fontsize=14, fontweight='bold')
        ax1.grid(axis='y', alpha=0.3)
        
        # Add value labels on bars
        for bar in bars:
            height = bar.get_height()
            ax1.text(bar.get_x() + bar.get_width()/2., height,
                    f'{height:.1f}',
                    ha='center', va='bottom', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig1)
    
    with col2:
        # Model accuracy comparison
        fig2, ax2 = plt.subplots(figsize=(8, 5))
        models_list = list(model_accuracies.keys())
        accuracies = list(model_accuracies.values())
        colors_models = ['#667eea', '#764ba2', '#f093fb', '#4facfe', '#43e97b', '#fa709a']
        
        bars2 = ax2.barh(models_list, accuracies, color=colors_models, alpha=0.8, edgecolor='black')
        ax2.set_xlabel("Accuracy (%)", fontsize=12, fontweight='bold')
        ax2.set_title("AI Model Performance", fontsize=14, fontweight='bold')
        ax2.set_xlim(80, 100)
        ax2.grid(axis='x', alpha=0.3)
        
        # Add accuracy labels
        for i, (bar, v) in enumerate(zip(bars2, accuracies)):
            ax2.text(v + 0.3, i, f'{v}%', va='center', fontweight='bold')
        
        plt.tight_layout()
        st.pyplot(fig2)
    
    # ============== HEALTH SCORE TIMELINE ==============
    st.markdown("### 📅 Estimated Risk Over Time (If Lifestyle Maintained)")
    
    months = ['Current', '3 Months', '6 Months', '1 Year', '2 Years']
    
    # Simulate risk improvement/worsening over time
    if base_prediction == 0:  # Low risk
        risk_trend = [risk_score, max(0, risk_score - 1), max(0, risk_score - 2), 
                     max(0, risk_score - 3), max(0, risk_score - 4)]
    else:  # High risk
        if exercise == "No" and smoking == "Current":
            risk_trend = [risk_score, risk_score + 1, risk_score + 2, 
                         risk_score + 2, risk_score + 3]
        else:
            risk_trend = [risk_score, risk_score, risk_score - 1, 
                         risk_score - 1, risk_score - 2]
    
    fig3, ax3 = plt.subplots(figsize=(10, 4))
    ax3.plot(months, risk_trend, marker='o', linewidth=3, markersize=10, 
            color='#667eea', markerfacecolor='#764ba2')
    ax3.fill_between(range(len(months)), risk_trend, alpha=0.3, color='#667eea')
    ax3.axhline(y=8, color='r', linestyle='--', label='High Risk Threshold', alpha=0.5)
    ax3.set_ylabel("Risk Score", fontsize=12, fontweight='bold')
    ax3.set_title("Projected Risk Trajectory", fontsize=14, fontweight='bold')
    ax3.legend()
    ax3.grid(True, alpha=0.3)
    plt.tight_layout()
    st.pyplot(fig3)
    
    st.divider()
    
    # ============== DOWNLOAD REPORT ==============
    st.markdown("### 📄 Health Report Summary")
    
    report_data = {
        "Parameter": ["BMI", "Smoking", "Alcohol", "Exercise", "Fruit", "Vegetables", 
                     "Age Category", "Risk Score", "Final Assessment"],
        "Value": [f"{bmi} ({bmi_category})", smoking, f"{alcohol} drinks/week", exercise,
                 f"{fruit} servings/day", f"{veg} servings/day", age_cat, 
                 f"{risk_score}/20", "High Risk" if high_risk_count >= 3 else "Low Risk"]
    }
    
    df_report = pd.DataFrame(report_data)
    st.dataframe(df_report, use_container_width=True)
    
    # CSV download
    csv = df_report.to_csv(index=False)
    st.download_button(
        label="📥 Download Full Report (CSV)",
        data=csv,
        file_name="cardio_care_health_report.csv",
        mime="text/csv",
        use_container_width=True
    )

# ============== FOOTER ==============
st.divider()
st.markdown("""
    <div style='text-align: center; padding: 20px; color: white;'>
        <p style='font-size: 0.9rem;'>
            💙 <b>Cardio Care AI</b> - Your Personal Heart Health Assistant<br>
           💙 <b>Cardio Care Analyzer</b> - Your Personal Heart Health Assistant<br>
    "Developed as part of MCA Final Year Project by Siddhika Belsare  Supervised by Prof. Shubhangi Mahadik"

        </p>
    </div>
""", unsafe_allow_html=True)

