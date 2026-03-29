# import streamlit as st
# from module.storage import fetch_all
# import pandas as pd

# st.title("Insights")

# data = fetch_all()

# df = pd.DataFrame(data, columns=[
#     "ID", "Raw Text", "Processed", "Score", "Timestamp"
# ])

# st.bar_chart(df["Score"])
import streamlit as st
from module.storage import fetch_all
import pandas as pd

st.title("📈 Insights")

data = fetch_all()

if not data:
    st.warning("No data found!")
else:
    df = pd.DataFrame(data, columns=[
        "ID", "Raw Text", "Processed", "Score", "Timestamp"
    ])

    # -------- Sentiment Label --------
    def get_sentiment(score):
        if score > 0:
            return "Positive"
        elif score < 0:
            return "Negative"
        return "Neutral"

    df["Sentiment"] = df["Score"].apply(get_sentiment)

    # -------- 1. Distribution --------
    st.subheader("Sentiment Distribution")
    st.bar_chart(df["Sentiment"].value_counts())

    # -------- 2. Average Score --------
    avg_score = df["Score"].mean()
    st.subheader("Average Sentiment Score")
    st.write(avg_score)

    # -------- 3. Overall Insight --------
    st.subheader("Overall Insight")

    if avg_score > 0:
        st.success("Overall Sentiment is Positive 😊")
    elif avg_score < 0:
        st.error("Overall Sentiment is Negative 😡")
    else:
        st.info("Overall Sentiment is Neutral 😐")