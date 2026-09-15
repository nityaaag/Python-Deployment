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
        color: #9ca3af;
        margin-bottom: 25px;
    }

    .section-title {
        font-size: 23px;
        font-weight: 650;
        margin-top: 25px;
        margin-bottom: 15px;
        padding-bottom: 7px;
        border-bottom: 1px solid #374151;
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
        border: 1px solid #374151;
    }

    div[data-baseweb="select"] > div {
        border-radius: 8px;
    }

    div[data-baseweb="input"] > div {
        border-radius: 8px;
    }

    div[data-testid="stFileUploader"] {
        border: 1px dashed #6b7280;
        border-radius: 10px;
        padding: 5px;
    }

    div[data-testid="stAlert"] {
        border-radius: 9px;
    }

    section[data-testid="stSidebar"] {
        border-right: 1px solid #374151;
    }

    .sidebar-title {
        font-size: 23px;
        font-weight: 650;
        margin-bottom: 5px;
    }

    .sidebar-text {
        font-size: 14px;
        color: #9ca3af;
        line-height: 1.5;
    }

    .top-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 20px;
        text-align: center;
        min-height: 125px;
    }

    .top-position {
        font-size: 25px;
        margin-bottom: 8px;
    }

    .top-name {
        font-size: 18px;
        font-weight: 650;
    }

    .top-score {
        font-size: 15px;
        color: #9ca3af;
        margin-top: 6px;
    }

    .info-card {
        background-color: #1f2937;
        border: 1px solid #374151;
        border-radius: 12px;
        padding: 18px;
        margin-bottom: 15px;
    }

    .footer {
        text-align: center;
        color: #6b7280;
        font-size: 13px;
        padding-top: 8px;
    }
</style>
""", unsafe_allow_html=True)

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
    "Python": [95, 82, 91, 68, 78, 95, 64, 88],
    "Java": [88, 81, 89, 70, 75, 92, 60, 86],
    "Database": [92, 86, 94, 65, 80, 90, 79, 84],
    "Attendance": [98, 88, 95, 76, 84, 97, 82, 91]
}

with st.sidebar:
    st.markdown(
        '<div class="sidebar-title">📊 Dashboard</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="sidebar-text">'
        'Explore student marks, attendance and academic performance.'
        '</div>',
        unsafe_allow_html=True
    )

    st.divider()

    uploaded_file = st.file_uploader(
        "Upload Student CSV File",
        type=["csv"]
    )

    st.divider()

    st.markdown("### Class")

    class_name = st.selectbox(
        "Select class",
        ["4 BCA"]
    )

    st.divider()

    st.markdown("### Available Subjects")

    st.write("• Python")
    st.write("• Java")
    st.write("• Database")

    st.divider()

    st.caption("Student Performance Dashboard")

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.DataFrame(sample_data)

subject_columns = [
    "Python",
    "Java",
    "Database"
]

required_columns = [
    "Name",
    "Python",
    "Java",
    "Database",
    "Attendance"
]

missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

st.markdown(
    '<div class="main-title">Student Performance Dashboard</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="main-subtitle">'
    f'{class_name} &nbsp;•&nbsp; '
    'Academic performance, attendance and student analytics'
    '</div>',
    unsafe_allow_html=True
)

if missing_columns:
    st.error(
        "The uploaded CSV is missing these columns: "
        + ", ".join(missing_columns)
    )
    st.stop()

df["Average"] = df[subject_columns].mean(axis=1)

def get_grade(average):
    if average >= 80:
        return "A"
    elif average >= 70:
        return "B"
    elif average >= 60:
        return "C"
    elif average >= 40:
        return "D"
    else:
        return "F"

def get_result(average):
    if average >= 80:
        return "Excellent"
    elif average >= 60:
        return "Good"
    elif average >= 40:
        return "Average"
    else:
        return "Needs Improvement"

df["Grade"] = df["Average"].apply(get_grade)
df["Result"] = df["Average"].apply(get_result)

ranking_df = df.sort_values(
    "Average",
    ascending=False
).reset_index(drop=True)

ranking_df["Rank"] = range(
    1,
    len(ranking_df) + 1
)

total_students = len(df)
average_marks = df[subject_columns].mean().mean()
average_percentage = average_marks
highest_marks = df[subject_columns].max().max()
average_attendance = df["Attendance"].mean()

tab1, tab2, tab3, tab4 = st.tabs([
    "📊 Overview",
    "👤 Students",
    "📚 Subjects",
    "📋 Reports"
])

with tab1:

    st.markdown(
        '<div class="section-title">Class Summary</div>',
        unsafe_allow_html=True
    )

    col1, col2, col3, col4, col5 = st.columns(5)

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
        '<div class="section-title">Top 3 Students</div>',
        unsafe_allow_html=True
    )

    top_students = ranking_df.head(3)

    top_col1, top_col2, top_col3 = st.columns(3)

    if len(top_students) >= 1:
        with top_col1:
            st.markdown(
                f"""
                <div class="top-card">
                    <div class="top-position">🥇</div>
                    <div class="top-name">{top_students.iloc[0]["Name"]}</div>
                    <div class="top-score">
                        {top_students.iloc[0]["Average"]:.1f}% Average
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    if len(top_students) >= 2:
        with top_col2:
            st.markdown(
                f"""
                <div class="top-card">
                    <div class="top-position">🥈</div>
                    <div class="top-name">{top_students.iloc[1]["Name"]}</div>
                    <div class="top-score">
                        {top_students.iloc[1]["Average"]:.1f}% Average
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    if len(top_students) >= 3:
        with top_col3:
            st.markdown(
                f"""
                <div class="top-card">
                    <div class="top-position">🥉</div>
                    <div class="top-name">{top_students.iloc[2]["Name"]}</div>
                    <div class="top-score">
                        {top_students.iloc[2]["Average"]:.1f}% Average
                    </div>
                </div>
                """,
                unsafe_allow_html=True
            )

    st.markdown(
        '<div class="section-title">Student Ranking</div>',
        unsafe_allow_html=True
    )

    ranking_display = ranking_df[
        [
            "Rank",
            "Name",
            "Python",
            "Java",
            "Database",
            "Average",
            "Grade",
            "Attendance"
        ]
    ].copy()

    ranking_display["Average"] = ranking_display[
        "Average"
    ].round(1)

    st.dataframe(
        ranking_display,
        use_container_width=True,
        hide_index=True
    )

    st.markdown(
        '<div class="section-title">Class Performance</div>',
        unsafe_allow_html=True
    )

    class_chart = df.set_index("Name")[
        subject_columns
    ]

    st.bar_chart(class_chart)

with tab2:

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

    student_average = student["Average"]
    student_grade = student["Grade"]
    student_result = student["Result"]

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
                "Overall Average",
                f"{student_average:.1f} / 100"
            )

    with col2:
        st.markdown("### Performance Result")

        if student_result == "Excellent":
            st.success(
                f"Performance: {student_result}"
            )
        elif student_result == "Good":
            st.info(
                f"Performance: {student_result}"
            )
        elif student_result == "Average":
            st.warning(
                f"Performance: {student_result}"
            )
        else:
            st.error(
                f"Performance: {student_result}"
            )

        result_col1, result_col2 = st.columns(2)

        with result_col1:
            st.metric(
                "Percentage",
                f"{student_average:.1f}%"
            )

        with result_col2:
            st.metric(
                "Grade",
                student_grade
            )

        st.markdown("**Overall Performance**")

        st.progress(
            min(max(int(student_average), 0), 100)
        )

        st.caption(
            f"{student_average:.1f}% overall performance"
        )

        st.markdown("**Attendance**")

        st.progress(
            min(max(int(student["Attendance"]), 0), 100)
        )

        st.caption(
            f"{student['Attendance']}% attendance"
        )

        if student["Attendance"] >= 75:
            st.success("Attendance Status: Eligible")
        else:
            st.warning("Attendance Status: Short Attendance")

    st.markdown(
        '<div class="section-title">Student Subject Performance</div>',
        unsafe_allow_html=True
    )

    student_chart = pd.DataFrame({
        "Marks": [
            student["Python"],
            student["Java"],
            student["Database"]
        ]
    }, index=subject_columns)

    st.bar_chart(student_chart)

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

        if len(search_result) > 0:
            st.dataframe(
                search_result[
                    [
                        "Name",
                        "Python",
                        "Java",
                        "Database",
                        "Average",
                        "Grade",
                        "Attendance"
                    ]
                ],
                use_container_width=True,
                hide_index=True
            )
        else:
            st.info("No student found.")

with tab3:

    st.markdown(
        '<div class="section-title">Subject Performance</div>',
        unsafe_allow_html=True
    )

    selected_subject = st.selectbox(
        "Choose a subject",
        subject_columns
    )

    subject_average = df[selected_subject].mean()
    subject_highest = df[selected_subject].max()
    subject_lowest = df[selected_subject].min()

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(
            "Subject Average",
            f"{subject_average:.1f}"
        )

    with col2:
        st.metric(
            "Highest Score",
            subject_highest
        )

    with col3:
        st.metric(
            "Lowest Score",
            subject_lowest
        )

    st.bar_chart(
        df.set_index("Name")[selected_subject]
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

        subject_summary = pd.DataFrame({
            "Subject": selected_subjects,
            "Average Marks": [
                df[subject].mean()
                for subject in selected_subjects
            ]
        })

        subject_summary["Average Marks"] = subject_summary[
            "Average Marks"
        ].round(1)

        st.dataframe(
            subject_summary,
            use_container_width=True,
            hide_index=True
        )
    else:
        st.info(
            "Select at least one subject."
        )

    st.markdown(
        '<div class="section-title">Subject Averages</div>',
        unsafe_allow_html=True
    )

    subject_averages = pd.DataFrame({
        "Average Marks": df[subject_columns].mean()
    })

    st.bar_chart(subject_averages)

with tab4:

    st.markdown(
        '<div class="section-title">Performance Filters</div>',
        unsafe_allow_html=True
    )

    filter_col1, filter_col2 = st.columns(2)

    with filter_col1:
        minimum_marks = st.slider(
            "Minimum average marks",
            min_value=0,
            max_value=100,
            value=50,
            step=5
        )

    with filter_col2:
        attendance_limit = st.number_input(
            "Minimum attendance requirement (%)",
            min_value=0,
            max_value=100,
            value=75,
            step=5
        )

    result_filter = st.radio(
        "Filter by result",
        ["All", "Passed", "Needs Improvement"],
        horizontal=True
    )

    filtered_df = df[
        (df["Average"] >= minimum_marks)
        & (df["Attendance"] >= attendance_limit)
    ]

    if result_filter == "Passed":
        filtered_df = filtered_df[
            filtered_df["Average"] >= 40
        ]

    elif result_filter == "Needs Improvement":
        filtered_df = filtered_df[
            filtered_df["Average"] < 40
        ]

    st.markdown(
        f"**Students found: {len(filtered_df)}**"
    )

    filtered_display = filtered_df[
        [
            "Name",
            "Python",
            "Java",
            "Database",
            "Average",
            "Grade",
            "Attendance"
        ]
    ].copy()

    filtered_display["Average"] = filtered_display[
        "Average"
    ].round(1)

    st.dataframe(
        filtered_display,
        use_container_width=True,
        hide_index=True
    )

    csv_data = filtered_display.to_csv(
        index=False
    ).encode("utf-8")

    st.download_button(
        "Download Filtered Data",
        csv_data,
        "filtered_students.csv",
        "text/csv"
    )

    st.markdown(
        '<div class="section-title">Report Details</div>',
        unsafe_allow_html=True
    )

    report_col1, report_col2 = st.columns(2)

    with report_col1:
        report_date = st.date_input(
            "Select report date",
            value=date.today()
        )

        st.write(
            f"Selected Date: **{report_date}**"
        )

    with report_col2:
        report_time = st.time_input(
            "Select report time",
            value=time(10, 0)
        )

        st.write(
            f"Selected Time: **{report_time}**"
        )

    st.markdown(
        '<div class="section-title">Attendance Analysis</div>',
        unsafe_allow_html=True
    )

    eligible_students = df[
        df["Attendance"] >= attendance_limit
    ]

    attendance_col1, attendance_col2 = st.columns(2)

    with attendance_col1:
        st.metric(
            "Meeting Requirement",
            len(eligible_students)
        )

    with attendance_col2:
        st.metric(
            "Below Requirement",
            total_students - len(eligible_students)
        )

    attendance_chart = df.set_index("Name")[
        ["Attendance"]
    ]

    st.bar_chart(attendance_chart)

    st.markdown(
        '<div class="section-title">Class Topper</div>',
        unsafe_allow_html=True
    )

    show_topper = st.checkbox(
        "Show class topper"
    )

    if show_topper:
        topper = ranking_df.iloc[0]

        st.success(
            f"Topper: {topper['Name']} | "
            f"Average: {topper['Average']:.1f} / 100 | "
            f"Percentage: {topper['Average']:.1f}% | "
            f"Grade: {topper['Grade']}"
        )

st.divider()

st.markdown(
    '<div class="footer">'
    'Student Performance Dashboard &nbsp;•&nbsp; '
    'Built using Python, Streamlit and Pandas'
    '</div>',
    unsafe_allow_html=True
)