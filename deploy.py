import streamlit as st
import pandas as pd
from datetime import date, time

st.set_page_config(
    page_title="Student Performance Dashboard",
    page_icon="📊",
    layout="wide"
)

st.markdown("""
<style>
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        padding-left: 4rem;
        padding-right: 4rem;
    }

    .main-title {
        font-size: 38px;
        font-weight: 700;
        margin-bottom: 4px;
        letter-spacing: -0.5px;
    }

    .main-subtitle {
        font-size: 16px;
        color: #6b7280;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 650;
        margin-top: 35px;
        margin-bottom: 15px;
        padding-bottom: 7px;
        border-bottom: 1px solid #e5e7eb;
    }

    div[data-testid="stMetric"] {
    background-color: #1f2937;
    border: 1px solid #374151;
    border-radius: 12px;
    padding: 18px 20px;
    min-height: 105px;
}

div[data-testid="stMetricLabel"] {
    font-size: 14px;
    color: #d1d5db;
}

div[data-testid="stMetricValue"] {
    font-size: 27px;
    font-weight: 650;
    color: #ffffff;
}

    div[data-testid="stDataFrame"] {
        border-radius: 10px;
        overflow: hidden;
        border: 1px solid #e5e7eb;
    }

    div[data-baseweb="select"] > div {
        border-radius: 8px;
    }

    div[data-baseweb="input"] > div {
        border-radius: 8px;
    }

    div[data-testid="stFileUploader"] {
        border: 1px dashed #cbd5e1;
        border-radius: 10px;
        padding: 5px;
    }

    div[data-testid="stAlert"] {
        border-radius: 9px;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid #e5e7eb;
    }

    .sidebar-title {
        font-size: 23px;
        font-weight: 650;
        margin-bottom: 5px;
    }

    .sidebar-text {
        font-size: 14px;
        color: #6b7280;
        line-height: 1.5;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        padding-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">📊 Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">'
        'Explore student marks, attendance and subject performance.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Student CSV File",
        type=["csv"]
    )

    st.divider()

    st.markdown("### Available Subjects")

    st.write("• Python")
    st.write("• Java")
    st.write("• Database")

    st.divider()

    st.caption("Student Performance Dashboard")

st.markdown(
    '<div class="main-title">Student Performance Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    'Upload student marks and explore academic performance through '
    'interactive tables, filters and visualizations.'
    '</div>',
    unsafe_allow_html=True
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

st.markdown(
    '<div class="section-title">Student Data</div>',
    unsafe_allow_html=True
)

st.dataframe(
    df,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    '<div class="section-title">Class Summary</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4, col5 = st.columns(5)

subject_columns = [
    "Python",
    "Java",
    "Database"
]

total_students = len(df)

average_marks = df[subject_columns].mean().mean()

average_percentage = average_marks

highest_marks = df[subject_columns].max().max()

average_attendance = df["Attendance"].mean()

with col1:
    st.metric(
        "Total Students",
        total_students
    )

with col2:
    st.metric(
        "Average Marks",
        f"{average_marks:.1f} / 100"
    )

with col3:
    st.metric(
        "Average Percentage",
        f"{average_percentage:.1f}%"
    )

with col4:
    st.metric(
        "Highest Marks",
        highest_marks
    )

with col5:
    st.metric(
        "Average Attendance",
        f"{average_attendance:.1f}%"
    )

st.markdown(
    '<div class="section-title">Student Details</div>',
    unsafe_allow_html=True
)

selected_student = st.selectbox(
    "Choose a student",
    df["Name"].tolist()
)

student = df[
    df["Name"] == selected_student
].iloc[0]

col1, col2 = st.columns([1, 1.5])

with col1:
    st.markdown("### Marks")

    mark_col1, mark_col2 = st.columns(2)

    with mark_col1:
        st.metric(
            "Python",
            student["Python"]
        )

        st.metric(
            "Database",
            student["Database"]
        )

    with mark_col2:
        st.metric(
            "Java",
            student["Java"]
        )

        st.metric(
            "Attendance",
            f"{student['Attendance']}%"
        )

with col2:
    st.markdown("### Performance Result")

    average = (
        student["Python"]
        + student["Java"]
        + student["Database"]
    ) / 3

    if average >= 80:
        st.success(
            "Performance: Excellent"
        )
    elif average >= 60:
        st.info(
            "Performance: Good"
        )
    elif average >= 40:
        st.warning(
            "Performance: Average"
        )
    else:
        st.error(
            "Performance: Needs Improvement"
        )

    st.metric(
        "Overall Average",
        f"{average:.1f} / 100"
    )

    st.caption(
        f"Percentage: {average:.1f}%"
    )

st.markdown(
    '<div class="section-title">Subject Performance</div>',
    unsafe_allow_html=True
)

selected_subject = st.selectbox(
    "Choose a subject",
    subject_columns
)

st.bar_chart(
    df.set_index("Name")[selected_subject]
)

st.markdown(
    '<div class="section-title">Filter Students</div>',
    unsafe_allow_html=True
)

minimum_marks = st.slider(
    "Show students with marks greater than or equal to",
    min_value=0,
    max_value=100,
    value=50,
    step=5
)

filtered_df = df[
    df[subject_columns].mean(axis=1)
    >= minimum_marks
]

st.write(
    f"Students found: **{len(filtered_df)}**"
)

st.dataframe(
    filtered_df,
    use_container_width=True,
    hide_index=True
)

st.markdown(
    '<div class="section-title">View Performance</div>',
    unsafe_allow_html=True
)

view_option = st.radio(
    "Select what you want to view:",
    ["Marks", "Attendance", "Both"],
    horizontal=True
)

if view_option == "Marks":
    st.dataframe(
        df[["Name"] + subject_columns],
        use_container_width=True,
        hide_index=True
    )
elif view_option == "Attendance":
    st.dataframe(
        df[["Name", "Attendance"]],
        use_container_width=True,
        hide_index=True
    )
else:
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )

st.markdown(
    '<div class="section-title">Report Details</div>',
    unsafe_allow_html=True
)

col1, col2 = st.columns(2)

with col1:
    report_date = st.date_input(
        "Select report date",
        value=date.today()
    )

    st.write(
        f"Selected Date: **{report_date}**"
    )

with col2:
    report_time = st.time_input(
        "Select report time",
        value=time(10, 0)
    )

    st.write(
        f"Selected Time: **{report_time}**"
    )

st.markdown(
    '<div class="section-title">Subject Comparison</div>',
    unsafe_allow_html=True
)

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
    st.info(
        "Select at least one subject."
    )

st.markdown(
    '<div class="section-title">Class Topper</div>',
    unsafe_allow_html=True
)

show_topper = st.checkbox(
    "Show class topper"
)

if show_topper:
    df["Average"] = df[
        subject_columns
    ].mean(axis=1)

    topper = df.loc[
        df["Average"].idxmax()
    ]

    st.success(
        f"Topper: {topper['Name']} "
        f"with an average of "
        f"{topper['Average']:.1f} / 100 "
        f"({topper['Average']:.1f}%)"
    )

st.markdown(
    '<div class="section-title">Attendance Requirement</div>',
    unsafe_allow_html=True
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
    f"**{len(eligible_students)}**"
)

st.markdown(
    '<div class="section-title">Search Student</div>',
    unsafe_allow_html=True
)

student_search = st.text_input(
    "Search by student name"
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
        use_container_width=True,
        hide_index=True
    )

st.divider()

st.markdown(
    '<div class="footer">'
    'Student Performance Dashboard &nbsp;•&nbsp; '
    'Built using Python, Streamlit and Pandas'
    '</div>',
    unsafe_allow_html=True
)
