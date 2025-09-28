import streamlit as st
import joblib
import os
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Cardio Care Analyzer", layout="wide")
st.title("🩺 Cardio Care Analyzer")
st.write("Enter your health details below for cardiovascular risk prediction.")

# ---------------- Load Models ----------------
if not os.path.exists("models"):
    os.mkdir("models")

# Make sure your models are inside 'models/' folder
model_files = {
    "logistic_regression_model.pkl": "Logistic Regression",
    "decision_tree_model.pkl": "Decision Tree",
    "neural_network_model.pkl": "Neural Network",
    "random_forest_model.pkl": "Random Forest",
    "xgboost_model.pkl": "XGBoost",
    "voting_ensemble.pkl": "Voting Ensemble"
}

models = {}
for file, name in model_files.items():
    path = os.path.join("models", file)
    models[name] = joblib.load(path)

# ---------------- Input Form ----------------
with st.form(key="health_form"):
    col1, col2 = st.columns(2)

    with col1:
        general_health = st.selectbox("General Health", ["Excellent","Very Good","Good","Fair","Poor"])
        checkup = st.selectbox("Last Routine Checkup", ["Within past year","1-2 years ago","2-5 years ago","5+ years ago"])
        exercise = st.selectbox("Exercise Regularly?", ["Yes","No"])
        heart_disease = st.selectbox("Heart Disease History", ["Yes","No"])
        skin_cancer = st.selectbox("Skin Cancer History", ["Yes","No"])
        other_cancer = st.selectbox("Other Cancer History", ["Yes","No"])
        depression = st.selectbox("Depression", ["Yes","No"])
        diabetes = st.selectbox("Diabetes", ["Yes","No"])
        arthritis = st.selectbox("Arthritis", ["Yes","No"])
        sex = st.selectbox("Sex", ["Male","Female"])
        age_cat = st.selectbox("Age Category", ["18-24","25-29","30-34","35-39","40-44",
                                                "45-49","50-54","55-59","60-64","65-69","70-74","75-79","80+"])
    with col2:
        height = st.number_input("Height (cm)", 120.0, 220.0, 170.0)
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        bmi = round(weight / ((height/100)**2),2)
        smoking = st.selectbox("Smoking History", ["Never","Former","Current"])
        alcohol = st.slider("Alcohol Consumption (drinks/week)", 0, 30, 2)
        fruit = st.slider("Fruit Servings per Day", 0, 10, 2)
        veg = st.slider("Green Vegetable Servings per Day", 0, 10, 2)
        fried = st.slider("Fried Potato Servings per Week", 0, 10, 1)

    submit_button = st.form_submit_button(label="Predict Risk")

# ---------------- Predictions ----------------
if submit_button:
    # NOTE: Replace this with your actual preprocessing for models
    input_features = np.array([[bmi, alcohol, fruit, veg, fried]])  # Placeholder

    st.subheader("🔮 Model Predictions")
    predictions = {}
    for name, model in models.items():
        try:
            pred = model.predict(input_features)[0]
            risk = "⚠️ High Risk" if pred==1 else "✅ Low Risk"
            predictions[name] = risk
            st.write(f"{name}: {risk}")
        except:
            st.warning(f"{name}: Prediction failed. Check preprocessing.")

    # Final Ensemble Decision
    high_risk_votes = list(pred for pred in predictions.values() if pred=="⚠️ High Risk")
    if len(high_risk_votes) >= 3:
        st.subheader("🏁 Final Risk Assessment: ⚠️ High Risk")
    else:
        st.subheader("🏁 Final Risk Assessment: ✅ Low Risk")

    # Health Recommendations
    st.subheader("💡 Health Recommendations")
    if bmi > 30:
        st.write("⚠️ High BMI detected. Increase physical activity and maintain a balanced diet.")
    if smoking == "Current":
        st.write("🚭 Quitting smoking will greatly reduce cardiovascular risk.")
    if alcohol > 14:
        st.write("⚠️ Reduce alcohol intake to maintain heart health.")
    if exercise == "No":
        st.write("🏃 Engage in regular exercise for cardiovascular benefits.")
    if bmi <= 30 and smoking != "Current" and alcohol <=14 and exercise=="Yes":
        st.success("✅ Your lifestyle appears healthy. Keep it up!")

    # Visualization
    st.subheader("📊 Health Metrics Overview")
    fig, ax = plt.subplots()
    ax.bar(["BMI","Alcohol","Fruit","Vegetables","Fried Potatoes"], [bmi, alcohol, fruit, veg, fried],
           color=['skyblue','orange','green','darkgreen','brown'])
    ax.set_ylabel("Values")
    ax.set_title("Your Health Metrics")
    st.pyplot(fig)
