import gradio as gr
import joblib
import numpy as np

save_file_name = "xgboost-model.pkl"

xgb_clf = joblib.load(save_file_name)

def predict_death_event(age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
            high_blood_pressure, platelets, serum_creatinine, serum_sodium,
            sex, smoking, time):
    
    # Create the input as a list (single sample)
    features = [
        age, anaemia, creatinine_phosphokinase, diabetes, ejection_fraction,
        high_blood_pressure, platelets, serum_creatinine, serum_sodium,
        sex, smoking, time
    ]
    
    prediction = xgb_clf.predict([features])[0]  # Get the prediction
    return "Death Event: Yes" if prediction == 1 else "Death Event: No"
    


inputs = [
    gr.Slider(minimum=0, maximum=120, label="Age"),
    gr.Radio(choices=[0, 1], label="Anaemia (0 = No, 1 = Yes)"),
    gr.Slider(minimum=0, maximum=10, label="Creatinine Phosphokinase"),
    gr.Radio(choices=[0, 1], label="Diabetes (0 = No, 1 = Yes)"),
    gr.Slider(minimum=10, maximum=80, label="Ejection Fraction"),
    gr.Radio(choices=[0, 1], label="High Blood Pressure (0 = No, 1 = Yes)"),
    gr.Slider(minimum=0, maximum=850000, label="Platelets"),
    gr.Slider(minimum=0.0, maximum=10.0, step=0.1, label="Serum Creatinine"),
    gr.Slider(minimum=100, maximum=150, label="Serum Sodium"),
    gr.Radio(choices=[0, 1], label="Sex (0 = Female, 1 = Male)"),
    gr.Radio(choices=[0, 1], label="Smoking (0 = No, 1 = Yes)"),
    gr.Slider(minimum=0, maximum=300, label="Time (Follow-up days)")
]
outputs = gr.Textbox(label="Prediction")

# Gradio interface to generate UI link
title = "Patient Survival Prediction"
description = "Predict survival of patient with heart failure, given their clinical record"

iface = gr.Interface(fn = predict_death_event,
                         inputs =inputs,
                         outputs = outputs,
                         title = title,
                         description = description,
                         allow_flagging='never')

iface.launch(share = True) 

