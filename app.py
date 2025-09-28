import streamlit as st
import joblib
import os
import numpy as np
import matplotlib.pyplot as plt

# ---------------- Page Config ----------------
st.set_page_config(page_title="Cardio Care Analyzer", layout="wide")
st.title("🩺 Cardio Care Analyzer")
st.write("Enter your health details below for cardiovascular risk prediction.")

# ---------------- Load Models ----------------
if not os.path.exists("models"):
    st.error("Models folder not found! Please upload all model files in 'models/' folder.")

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
        general_health = st.selectbox("General Health", ["Fair","Good","Poor","Very Good"])
        checkup = st.selectbox("Last Routine Checkup", ["Never","Within the past 2 years","Within the past 5 years","Within the past year"])
        exercise = st.selectbox("Exercise Regularly?", ["Yes","No"])
        heart_disease = st.selectbox("Heart Disease History", ["Yes","No"])
        skin_cancer = st.selectbox("Skin Cancer History", ["Yes","No"])
        other_cancer = st.selectbox("Other Cancer History", ["Yes","No"])
        depression = st.selectbox("Depression", ["Yes","No"])
        diabetes = st.selectbox("Diabetes", ["No, pre-diabetes or borderline diabetes","Yes","Yes, but female told only during pregnancy"])
        arthritis = st.selectbox("Arthritis", ["Yes","No"])
        sex = st.selectbox("Sex", ["Male","Female"])
        age_cat = st.selectbox("Age Category", ["25-29","30-34","35-39","40-44","45-49","50-54","55-59","60-64","65-69","70-74","75-79","80+"])
        smoking = st.selectbox("Smoking History", ["Yes","No"])

    with col2:
        height = st.number_input("Height (cm)", 120.0, 220.0, 170.0)
        weight = st.number_input("Weight (kg)", 30.0, 200.0, 70.0)
        bmi = round(weight / ((height/100)**2),2)
        alcohol = st.slider("Alcohol Consumption (drinks/week)", 0, 30, 2)
        fruit = st.slider("Fruit Servings per Day", 0, 10, 2)
        veg = st.slider("Green Vegetable Servings per Day", 0, 10, 2)
        fried = st.slider("Fried Potato Servings per Week", 0, 10, 1)

    submit_button = st.form_submit_button(label="Predict Risk")

# ---------------- Predictions ----------------
if submit_button:
    # ---------------- Preprocessing ----------------
    feature_columns = ['Sex','Height_(cm)','Weight_(kg)','BMI','Alcohol_Consumption','Fruit_Consumption','Green_Vegetables_Consumption','FriedPotato_Consumption',
                       'General_Health_Fair','General_Health_Good','General_Health_Poor','General_Health_Very Good',
                       'Checkup_Never','Checkup_Within the past 2 years','Checkup_Within the past 5 years','Checkup_Within the past year',
                       'Exercise_Yes','Heart_Disease_Yes','Skin_Cancer_Yes','Other_Cancer_Yes','Depression_Yes',
                       'Diabetes_No, pre-diabetes or borderline diabetes','Diabetes_Yes','Diabetes_Yes, but female told only during pregnancy',
                       'Arthritis_Yes','Age_Category_25-29','Age_Category_30-34','Age_Category_35-39','Age_Category_40-44','Age_Category_45-49','Age_Category_50-54',
                       'Age_Category_55-59','Age_Category_60-64','Age_Category_65-69','Age_Category_70-74','Age_Category_75-79','Age_Category_80+','Smoking_History_Yes']

    input_dict = {col:0 for col in feature_columns}

    # Numeric features
    input_dict['Height_(cm)'] = height
    input_dict['Weight_(kg)'] = weight
    input_dict['BMI'] = bmi
    input_dict['Alcohol_Consumption'] = alcohol
    input_dict['Fruit_Consumption'] = fruit
    input_dict['Green_Vegetables_Consumption'] = veg
    input_dict['FriedPotato_Consumption'] = fried

    # Sex
    input_dict['Sex'] = 1 if sex=='Male' else 0

    # One-hot for categorical
    input_dict[f'General_Health_{general_health}'] = 1
    input_dict[f'Checkup_{checkup}'] = 1
    input_dict['Exercise_Yes'] = 1 if exercise=='Yes' else 0
    input_dict['Heart_Disease_Yes'] = 1 if heart_disease=='Yes' else 0
    input_dict['Skin_Cancer_Yes'] = 1 if skin_cancer=='Yes' else 0
    input_dict['Other_Cancer_Yes'] = 1 if other_cancer=='Yes' else 0
    input_dict['Depression_Yes'] = 1 if depression=='Yes' else 0
    input_dict[f'Diabetes_{diabetes}'] = 1
    input_dict['Arthritis_Yes'] = 1 if arthritis=='Yes' else 0
    input_dict[f'Age_Category_{age_cat}'] = 1
    input_dict['Smoking_History_Yes'] = 1 if smoking=='Yes' else 0

    input_features = np.array([list(input_dict.values())])

    # ---------------- Model Predictions ----------------
    st.subheader("🔮 Model Predictions")
    predictions = {}
    for name, model in models.items():
        try:
            pred = model.predict(input_features)[0]
            risk = "⚠️ High Risk" if pred==1 else "✅ Low Risk"
            predictions[name] = risk
            st.write(f"{name}: {risk}")
        except Exception as e:
            st.warning(f"{name}: Prediction failed. Error: {e}")

    # Final Ensemble Decision
    high_risk_votes = list(pred for pred in predictions.values() if pred=="⚠️ High Risk")
    if len(high_risk_votes) >= 3:
        st.subheader("🏁 Final Risk Assessment: ⚠️ High Risk")
    else:
        st.subheader("🏁 Final Risk Assessment: ✅ Low Risk")

    # ---------------- Health Recommendations ----------------
    st.subheader("💡 Health Recommendations")
    if bmi > 30:
        st.write("⚠️ High BMI detected. Increase physical activity and maintain a balanced diet.")
    if smoking == "Yes":
        st.write("🚭 Quitting smoking will greatly reduce cardiovascular risk.")
    if alcohol > 14:
        st.write("⚠️ Reduce alcohol intake to maintain heart health.")
    if exercise == "No":
        st.write("🏃 Engage in regular exercise for cardiovascular benefits.")
    if bmi <= 30 and smoking != "Yes" and alcohol <=14 and exercise=="Yes":
        st.success("✅ Your lifestyle appears healthy. Keep it up!")

    # ---------------- Visualization ----------------
    st.subheader("📊 Health Metrics Overview")
    fig, ax = plt.subplots()
    ax.bar(["BMI","Alcohol","Fruit","Vegetables","Fried Potatoes"], [bmi, alcohol, fruit, veg, fried],
           color=['skyblue','orange','green','darkgreen','brown'])
    ax.set_ylabel("Values")
    ax.set_title("Your Health Metrics")
    st.pyplot(fig)

# ---------------- Footer ----------------
st.markdown("---")
st.markdown("Developed as part of **MCA Final Year Project** by **Siddhika Belsare**  \nSupervised by **Prof. Shubhangi Mahadik**")
