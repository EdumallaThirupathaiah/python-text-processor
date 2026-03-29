# import streamlit as st
# from module.storage import fetch_all
# import pandas as pd

# st.title("Export Data")

# data = fetch_all()

# df = pd.DataFrame(data, columns=[
#     "ID", "Raw Text", "Processed", "Score", "Timestamp"
# ])

# csv = df.to_csv(index=False)

# st.download_button(
#     label="Download CSV",
#     data=csv,
#     file_name="processed_data.csv",
#     mime="text/csv"
# )
import streamlit as st
from module.storage import fetch_all
import pandas as pd
import smtplib
from email.message import EmailMessage

st.title("📧 Send Processed Results")

# -------- FETCH DATA --------
data = fetch_all()

if not data:
    st.warning("⚠️ No processed data found! Please process data first.")
else:
    df = pd.DataFrame(data, columns=[
        "ID", "Raw Text", "Processed", "Score", "Timestamp"
    ])

    st.subheader("Preview of Data")
    st.dataframe(df.head())

    receiver_email = st.text_input("Enter receiver email")

    if st.button("📧 Send Email"):

        if not receiver_email:
            st.warning("Please enter receiver email!")
        else:
            try:
                # Convert to CSV
                csv_data = df.to_csv(index=False)

                # 🔐 YOUR EMAIL CONFIG
                sender_email = "your_email@gmail.com"
                app_password = "your_app_password"

                msg = EmailMessage()
                msg["Subject"] = "Processed Text Report"
                msg["From"] = sender_email
                msg["To"] = receiver_email

                msg.set_content("Attached is your processed text report.")

                msg.add_attachment(
                    csv_data.encode(),
                    maintype="application",
                    subtype="octet-stream",
                    filename="processed_data.csv"
                )

                # Send email
                with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
                    smtp.login(sender_email, app_password)
                    smtp.send_message(msg)

                st.success("✅ Email sent successfully!")

            except Exception as e:
                st.error(f"Error: {e}")