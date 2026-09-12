import streamlit as st
from datetime import date

st.set_page_config(
    page_title="Student Information Form",
    page_icon="🎓",
    layout="centered"
)

st.markdown("""
<style>
    .main-title {
        text-align: center;
        margin-bottom: 5px;
    }

    .subtitle {
        text-align: center;
        color: #666;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 20px;
        font-weight: 600;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    .info-box {
        padding: 15px;
        border-radius: 10px;
        background-color: #f5f5f5;
        margin-bottom: 20px;
    }

    .result-box {
        padding: 20px;
        border-radius: 12px;
        background-color: #f0f7ff;
        margin-top: 20px;
    }
</style>
""", unsafe_allow_html=True)


# Header
st.markdown(
    '<h1 class="main-title">CHRIST UNIVERSITY</h1>',
    unsafe_allow_html=True
)

st.markdown(
    '<p class="subtitle">Student Information Form</p>',
    unsafe_allow_html=True
)

st.progress(0.25)
st.caption("Please complete the form below")


# Personal Details
st.markdown(
    '<div class="section-title">Personal Details</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name", placeholder="Enter your name")

    with col2:
        email = st.text_input(
            "Email Address",
            placeholder="example@email.com"
        )

    col3, col4 = st.columns(2)

    with col3:
        phone = st.text_input(
            "Phone Number",
            placeholder="10-digit number"
        )

    with col4:
        dob = st.date_input(
            "Date of Birth",
            value=date(2005, 1, 1)
        )

    gender = st.radio(
        "Gender",
        ["Male", "Female", "Other"],
        horizontal=True
    )


# Academic Details
st.markdown(
    '<div class="section-title">Academic Details</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    course = st.selectbox(
        "Select Course",
        ["BCA", "BBA", "B.Com", "B.Sc", "BA"]
    )

    year = st.selectbox(
        "Current Year",
        ["1st Year", "2nd Year", "3rd Year", "4th Year"]
    )

    subjects = st.multiselect(
        "Favourite Subjects",
        [
            "Python",
            "Java",
            "Web Development",
            "Database",
            "Artificial Intelligence",
            "Computer Networks"
        ],
        placeholder="Choose subjects"
    )

    percentage = st.slider(
        "Previous Semester Percentage",
        0,
        100,
        70
    )

    st.caption(f"Selected Percentage: {percentage}%")


# Additional Details
st.markdown(
    '<div class="section-title">Additional Details</div>',
    unsafe_allow_html=True
)

with st.container(border=True):

    city = st.selectbox(
        "City",
        ["Delhi", "Mumbai", "Pune", "Bangalore", "Hyderabad", "Other"]
    )

    interests = st.multiselect(
        "Interests",
        [
            "Coding",
            "Sports",
            "Dance",
            "Music",
            "Acting",
            "Photography",
            "Writing"
        ],
        placeholder="Select your interests"
    )

    about = st.text_area(
        "About Yourself",
        placeholder="Write a few lines about yourself..."
    )

    col1, col2 = st.columns(2)

    with col1:
        hostel = st.checkbox("Hostel Accommodation")

    with col2:
        updates = st.checkbox("Receive University Updates")


st.divider()


# Submit
col1, col2, col3 = st.columns([1, 2, 1])

with col2:
    submit = st.button(
        "Submit Form",
        use_container_width=True
    )


if submit:

    if name == "" or email == "" or phone == "":
        st.error("Please fill in all required fields.")

    elif len(phone) != 10 or not phone.isdigit():
        st.error("Please enter a valid 10-digit phone number.")

    else:

        st.progress(1.0)

        st.success("Registration submitted successfully!")

        st.markdown(
            '<div class="result-box">',
            unsafe_allow_html=True
        )

        st.subheader("Submitted Details")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Name:**", name)
            st.write("**Email:**", email)
            st.write("**Phone:**", phone)
            st.write("**Date of Birth:**", dob)
            st.write("**Gender:**", gender)

        with col2:
            st.write("**Course:**", course)
            st.write("**Year:**", year)
            st.write("**Percentage:**", f"{percentage}%")
            st.write("**City:**", city)
            st.write(
                "**Hostel:**",
                "Yes" if hostel else "No"
            )

        st.write(
            "**Favourite Subjects:**",
            ", ".join(subjects) if subjects else "None selected"
        )

        st.write(
            "**Interests:**",
            ", ".join(interests) if interests else "None selected"
        )

        st.write("**About:**", about if about else "Not provided")

        st.markdown("</div>", unsafe_allow_html=True)
