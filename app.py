import streamlit as st
import pandas as pd
import pickle
import numpy as np
import matplotlib.pyplot as plt

# Load model
with open("phobia_model.pkl", "rb") as f:
    model = pickle.load(f)

st.title("Phobia Level Predictor")
phobia_type = st.selectbox("Select Phobia Type", ["Aquaphobia", "Nyctophobia", "Acrophobia"])

st.write(f"Answer the following 12 questions based on your fear of **{phobia_type}**:")

questions = [
    f"1. How anxious do you feel when thinking about {phobia_type.lower()}?",
    f"2. Do you avoid going near places where {phobia_type.lower()} might be present?",
    f"3. How much physical discomfort do you feel near {phobia_type.lower()}?",
    f"4. How likely are you to panic when exposed to {phobia_type.lower()}?",
    f"5. Do you feel safe in situations involving {phobia_type.lower()}?",  # reverse
    f"6. How often do you avoid {phobia_type.lower()}-related situations?",
    f"7. If you had to face it now, how distressed would you feel?",
    f"8. How confident are you to stay calm around {phobia_type.lower()}?",  # reverse
    f"9. Have you canceled plans to avoid {phobia_type.lower()}?",
    f"10. Do you believe something bad will happen if exposed?",
    f"11. How much control do you feel over reactions?",  # reverse
    f"12. How much does it affect your daily life?"
]

scores = []

# Initialize percentage outside the button logic to prevent NameError
percentage = None

for i, q in enumerate(questions):
    score = st.slider(q, 0, 4, 2)
    scores.append(score)

if st.button("Predict Phobia Level"):
    input_data = np.array(scores).reshape(1, -1)
    prediction = model.predict(input_data)[0]
    percentage = int((sum(scores) / 48) * 100)  # Calculate percentage
    # Save result (append to CSV)
    result_data = {
        "Phobia": [phobia_type],
        "Score": [percentage],
        "Phase": ["Pre" if "pre_score" not in st.session_state else "Post"]
    }
    result_df = pd.DataFrame(result_data)
    result_df.to_csv("user_results.csv", mode="a", index=False, header=False)

    st.metric("Phobia Level", prediction)
    st.metric("Phobia Percentage", f"{percentage}%")

    if "pre_score" not in st.session_state:
        st.session_state["pre_score"] = percentage
        st.success("✅ Pre-Assessment Saved! Now take VR therapy.")
        # Don't show graph here yet
    else:
        # After the post-assessment
        pre = st.session_state["pre_score"]
        post = percentage
        st.markdown(f"**🆚 Pre: {pre}% | Post: {post}%**")

        if post < pre:
            st.success("🎉 Therapy was successful! Fear level decreased.")
        else:
            st.warning("⚠️ Therapy not effective. Please try again.")

        # Now show the comparison graph after both pre and post assessments
        st.subheader("📈 Phobia Score Comparison")
        fig, ax = plt.subplots()
        ax.bar(["Pre-Assessment", "Post-Assessment"], [pre, post], color=["blue", "green"])
        ax.set_ylabel("Phobia Level (%)")
        st.pyplot(fig)
