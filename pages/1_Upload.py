# import streamlit as st
# from pipeline import run_pipeline

# st.title("Upload Text")

# text = st.text_area("Enter your text")

# if st.button("Process"):
#     if text:
#         result = run_pipeline(text)
#         st.success("Processing Complete!")
#         st.write(result)
import streamlit as st
from pipeline import run_pipeline

st.title("📤 Upload Text or File")

# -------- INPUT --------
manual_text = st.text_area("Enter text manually")

uploaded_file = st.file_uploader(
    "Upload .txt or .csv file",
    type=["txt", "csv"]
)

text_data = ""

# -------- FILE HANDLING --------
if uploaded_file is not None:
    try:
        if uploaded_file.name.endswith(".txt"):
            text_data = uploaded_file.read().decode("utf-8", errors="ignore")
            st.success("TXT loaded!")

        elif uploaded_file.name.endswith(".csv"):
            import pandas as pd
            df = pd.read_csv(uploaded_file)

            st.success("CSV loaded!")
            st.dataframe(df.head())

            # 🔥 SIMPLE: TAKE ALL TEXT
            text_data = " ".join(df.astype(str).fillna("").values.flatten())

    except Exception as e:
        st.error(f"File error: {e}")

# -------- PROCESS --------
if st.button("🚀 Process"):

    final_text = ""

    if manual_text.strip():
        final_text = manual_text
    elif text_data.strip():
        final_text = text_data

    if not final_text:
        st.warning("Please enter text or upload file!")
    else:
        run_pipeline(final_text)

        st.success("✅ Processing Done!")

        # 🔥 AUTO NAVIGATE
        st.switch_page("pages/2_Results.py")