# import streamlit as st
# from module.storage import fetch_all
# import pandas as pd

# st.title("Results")

# data = fetch_all()

# df = pd.DataFrame(data, columns=[
#     "ID", "Raw Text", "Processed", "Score", "Timestamp"
# ])

# st.dataframe(df)

import streamlit as st
import pandas as pd
from module.storage import fetch_all

st.title("📊 Results")

data = fetch_all()

if not data:
    st.warning("No results found!")
else:
    df = pd.DataFrame(data, columns=[
        "ID", "Raw Text", "Processed", "Score", "Timestamp"
    ])

    # Sentiment logic
    def get_sentiment(score):
        if score > 0:
            return "Positive"
        elif score < 0:
            return "Negative"
        return "Neutral"

    df["Sentiment"] = df["Score"].apply(get_sentiment)

    final_df = df[["Processed", "Sentiment", "Score"]]
    final_df.columns = ["Text", "Sentiment", "Score"]

    st.dataframe(final_df, use_container_width=True)