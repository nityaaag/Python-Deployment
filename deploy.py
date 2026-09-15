import streamlit as st
import pandas as pd
from datetime import date, time

st.set_page_config(
    page_title="Student Performance Dashboard",
    layout="wide"
)

st.title("Student Performance Dashboard")
st.write("Upload student marks and explore the performance data.")


uploaded_file = st.file_uploader(
    "Upload Student CSV File",
    type=["csv"]
)

sample_data = {
    "Name": [
        "Nitya",
        "Mayank",
        "Ashish",
        "Suryansh",
        "Sneha",
        "Shubha",
        "Harshil",
        "Arghya"
    ],
    "Python": [85, 72, 91, 68, 78, 95, 64, 88],
    "Java": [78, 81, 89, 70, 75, 92, 60, 86],
    "Database": [82, 76, 94, 65, 80, 90, 69, 84],
    "Attendance": [92, 88, 95, 76, 84, 97, 72, 91]
}

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(sample_data)


st.subheader("Student Data")

st.dataframe(
    df,
    use_container_width=True
)


st.subheader("Class Summary")

col1, col2, col3, col4 = st.columns(4)

subject_columns = ["Python", "Java", "Database"]

total_students = len(df)
average_marks = df[subject_columns].mean().mean()
highest_marks = df[subject_columns].max().max()
average_attendance = df["Attendance"].mean()

with col1:
    st.metric("Total Students", total_students)

with col2:
    st.metric("Average Marks", f"{average_marks:.1f}")

with col3:
    st.metric("Highest Marks", highest_marks)

with col4:
    st.metric("Average Attendance", f"{average_attendance:.1f}%")


st.subheader("Student Details")

selected_student = st.selectbox(
    "Choose a student",
    df["Name"].tolist()
)

student = df[df["Name"] == selected_student].iloc[0]

col1, col2 = st.columns(2)

with col1:
    st.write("### Marks")

    st.write("Python:", student["Python"])
    st.write("Java:", student["Java"])
    st.write("Database:", student["Database"])

with col2:
    st.write("### Attendance")

    st.write(f"Attendance: {student['Attendance']}%")

    # if/else result
    average = (
        student["Python"]
        + student["Java"]
        + student["Database"]
    ) / 3

    if average >= 80:
        st.success("Performance: Excellent")
    elif average >= 60:
        st.info("Performance: Good")
    elif average >= 40:
        st.warning("Performance: Average")
    else:
        st.error("Performance: Needs Improvement")


st.subheader("Subject Performance")

selected_subject = st.selectbox(
    "Choose a subject",
    subject_columns
)

st.bar_chart(
    df.set_index("Name")[selected_subject]
)

st.subheader("Filter Students")

minimum_marks = st.slider(
    "Show students with marks greater than or equal to",
    min_value=0,
    max_value=100,
    value=50,
    step=5
)

filtered_df = df[
    df[subject_columns].mean(axis=1) >= minimum_marks
]

st.write(
    f"Students found: {len(filtered_df)}"
)

st.dataframe(
    filtered_df,
    use_container_width=True
)

st.subheader("View Performance")

view_option = st.radio(
    "Select what you want to view:",
    ["Marks", "Attendance", "Both"],
    horizontal=True
)

if view_option == "Marks":
    st.dataframe(
        df[["Name"] + subject_columns],
        use_container_width=True
    )

elif view_option == "Attendance":
    st.dataframe(
        df[["Name", "Attendance"]],
        use_container_width=True
    )

else:
    st.dataframe(
        df,
        use_container_width=True
    )


st.subheader("Report Details")

report_date = st.date_input(
    "Select report date",
    value=date.today()
)

st.write("Selected Date:", report_date)


report_time = st.time_input(
    "Select report time",
    value=time(10, 0)
)

st.write("Selected Time:", report_time)


selected_subjects = st.multiselect(
    "Select subjects for comparison",
    subject_columns,
    default=subject_columns
)

if selected_subjects:
    st.bar_chart(
        df.set_index("Name")[selected_subjects]
    )
else:
    st.info("Select at least one subject.")


show_topper = st.checkbox(
    "Show class topper"
)

if show_topper:
    df["Average"] = df[subject_columns].mean(axis=1)

    topper = df.loc[df["Average"].idxmax()]

    st.success(
        f"Topper: {topper['Name']} "
        f"with an average of {topper['Average']:.1f}"
    )


attendance_limit = st.number_input(
    "Minimum attendance requirement (%)",
    min_value=0,
    max_value=100,
    value=75,
    step=5
)

eligible_students = df[
    df["Attendance"] >= attendance_limit
]

st.write(
    f"Students meeting attendance requirement: "
    f"{len(eligible_students)}"
)


student_search = st.text_input(
    "Search student by name"
)

if student_search:
    search_result = df[
        df["Name"].str.contains(
            student_search,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        search_result,
        use_container_width=True
    )

st.divider()

st.caption(
    "Student Performance Dashboard | Built using Python, "
    "Streamlit and Pandas"
)