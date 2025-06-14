import streamlit as st
import pandas as pd

st.set_page_config(page_title="Start Together", page_icon="🤝", layout="centered")

st.title("🤝 Start Together")
st.subheader("Connect. Collaborate. Create.")

st.markdown("Welcome to **Start Together**, a platform designed to help like-minded people connect for meaningful collaborations.")

page = st.sidebar.selectbox("Navigate", ["Home", "Join Community", "Find Matches", "About"])

if page == "Home":
    st.image("https://cdn-icons-png.flaticon.com/512/4202/4202849.png", width=100)
    st.write("👋 Start your collaboration journey today!")
    st.markdown("""
        **Why Start Together?**
        - 🤝 Find teammates for projects
        - 🎯 Connect based on skills & interests
        - 🚀 Build something amazing, together
    """)

elif page == "Join Community":
    st.header("📝 Join the Community")
    name = st.text_input("Your Name")
    email = st.text_input("Email")
    interests = st.text_area("Your Interests (comma separated)")
    skills = st.text_area("Your Skills (comma separated)")
    
    if st.button("Join Now"):
        st.success("🎉 Welcome to the Start Together community!")
        new_data = pd.DataFrame([[name, email, interests, skills]], columns=["Name", "Email", "Interests", "Skills"])
        try:
            existing = pd.read_csv("data/users.csv")
            updated = pd.concat([existing, new_data], ignore_index=True)
        except FileNotFoundError:
            updated = new_data
        updated.to_csv("data/users.csv", index=False)

elif page == "Find Matches":
    st.header("🔍 Find Collaborators")
    try:
        df = pd.read_csv("data/users.csv")
        st.dataframe(df)
    except FileNotFoundError:
        st.warning("No user data found. Ask someone to join first!")

elif page == "About":
    st.header("📢 About Start Together")
    st.markdown("""
    **Start Together** is a student-driven platform where people with shared visions meet and build together.
    
    🔗 Developed using Python & Streamlit  
    📧 Contact: starttogether@email.com
    """)
