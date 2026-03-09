import streamlit as st
from datetime import date

# ==================================
# SESSION STATE INITIALIZATION
# ==================================
if "deadlines" not in st.session_state:
    st.session_state.deadlines = []

if "messages" not in st.session_state:
    st.session_state.messages = []

# ==================================
# SIDEBAR
# ==================================
st.sidebar.title("Navigation by Cee")

menu = st.sidebar.radio(
    "Go to",
    ["Home", "Profile", "About"]
)

st.sidebar.divider()
st.sidebar.markdown("### Settings")

study_mode = st.sidebar.toggle("Study Mode")

# ==================================
# STUDY DASHBOARD
# ==================================
if study_mode:

    st.sidebar.success("Study Mode is ON")

    st.title("📚 Study Dashboard")

    # Calendar
    st.subheader("School Calendar")
    selected_date = st.date_input(
        "Select a deadline date",
        date.today()
    )

    # Deadline Tracker
    st.subheader("📌 Deadline Tracker")

    task = st.text_input("Enter assignment / task")

    if st.button("Add Deadline"):
        if task.strip():
            st.session_state.deadlines.append({
                "task": task,
                "date": selected_date
            })

    # Show Deadlines
    if st.session_state.deadlines:

        st.write("### Upcoming Deadlines")

        for i, item in enumerate(st.session_state.deadlines):

            col1, col2, col3 = st.columns([4,2,1])

            with col1:
                st.write(item["task"])

            with col2:
                st.write(item["date"])

            with col3:
                if st.button("❌", key=f"deadline_{i}"):
                    st.session_state.deadlines.pop(i)
                    st.rerun()

    else:
        st.info("No deadlines yet.")

    # Progress
    st.subheader("Study Progress")
    st.progress(50, text="Assignments Completed")


# ==================================
# HOME PAGE
# ==================================
elif menu == "Home":

    st.write("Here are my socials, check and follow me.")

    col1, col2 = st.columns(2)

    with col1:
        st.page_link(
            "https://github.com/Ceejieeeeee",
            label="Github",
            icon="🌎"
        )

    with col2:
        st.page_link(
            "https://share.streamlit.io/user/ceejieeeeee",
            label="Streamlit",
            icon="👑"
        )

    st.title("Student Productivity Dashboard")
    st.write(
        "Hello, I'm Carl Justine. "
        "I would suggest exploring this page."
    )

    st.header("Put some messagea and notes.")

    # Message Input
    txt = st.text_area("Input a message:")

    st.write(f"You wrote {len(txt)} characters.")

    # Save Message
    if st.button("Save Message"):
        if txt.strip():
            st.session_state.messages.append(txt)
            st.success("Message saved to profile!")


# ==================================
# PROFILE PAGE
# ==================================
elif menu == "Profile":

    st.title("My Profile")

    col1, col2 = st.columns([1,3])

    with col1:
        st.image(
            "https://cdn-icons-png.flaticon.com/512/3135/3135715.png",
            width=120
        )

    with col2:
        st.subheader("Carl Justine")
        st.write(
            "Student | Learning Python | "
            "Exploring Streamlit for Projects"
        )

    st.subheader("Messages from Home")

    if st.session_state.messages:

        for i, msg in enumerate(st.session_state.messages):

            col1, col2 = st.columns([6,1])

            with col1:
                st.info(f"{i+1}. {msg}")

            with col2:
                if st.button("❌", key=f"delete_msg_{i}"):
                    st.session_state.messages.pop(i)
                    st.rerun()

        # Optional clear all button
        if st.button("Clear All Messages"):
            st.session_state.messages.clear()
            st.rerun()

    else:
        st.write("No message yet. Write one on the Home page.")


# ==================================
# ABOUT PAGE
# ==================================
elif menu == "About":

    st.title("About this app")

    st.write("""
### App Purpose
This application is a **Student Productivity Dashboard** built with Streamlit.

### Target Users
- Students
- Learners studying programming
- Anyone who wants to track tasks and deadlines

### What the App Does
The app helps students organize their academic tasks and share personal notes.

### Inputs Collected
The app collects:
- Messages from the Home page
- Assignment tasks
- Deadline dates from the calendar

### Outputs Displayed
The app shows:
- Saved messages on the Profile page
- A deadline tracker list
- A study dashboard with calendar and progress indicator
""")