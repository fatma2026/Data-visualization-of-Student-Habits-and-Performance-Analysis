import streamlit as st
import pandas as pd
import plotly.express as px

# 📥 Load Data
df = pd.read_csv("D:\project Analysis\student_habits_performance.csv")

# 🧼 Data Cleaning (optional preview)
df.dropna(inplace=True)

# 🖥️ Dashboard Title
st.title("🎓 Student Habits and Performance Dashboard")
st.markdown("Analyze how student habits (like study hours, sleep, part-time jobs) impact academic and mental health performance.")

# 🎚️ Sidebar Filters
st.sidebar.header("Filter the Data")

# Filter by Study Hours per Day
study_hours_filter = st.sidebar.slider("Select Study Hours per Day:", min_value=int(df['study_hours_per_day'].min()), max_value=int(df['study_hours_per_day'].max()), value=(int(df['study_hours_per_day'].min()), int(df['study_hours_per_day'].max())))
df_filtered = df[df['study_hours_per_day'].between(study_hours_filter[0], study_hours_filter[1])]

# Filter by Diet Quality
diet_quality_filter = st.sidebar.selectbox("Select Diet Quality:", options=["All"] + list(df['diet_quality'].unique()))
if diet_quality_filter != "All":
    df_filtered = df_filtered[df_filtered['diet_quality'] == diet_quality_filter]

# Filter by Internet Quality
internet_quality_filter = st.sidebar.selectbox("Select Internet Quality:", options=["All"] + list(df['internet_quality'].unique()))
if internet_quality_filter != "All":
    df_filtered = df_filtered[df_filtered['internet_quality'] == internet_quality_filter]

# Filter by Part-Time Job
job_filter = st.sidebar.selectbox("Part-Time Job?", options=["All", "Yes", "No"])
if job_filter != "All":
    df_filtered = df_filtered[df_filtered['part_time_job'] == job_filter]

# 📈 1. Study Hours vs Exam Score
st.subheader("📘 Study Hours vs Exam Score")
fig1 = px.scatter(
    df_filtered,
    x="study_hours_per_day",
    y="exam_score",
    color="gender",
    hover_data=["student_id", "mental_health_rating"],
    labels={"study_hours_per_day": "Study Hours Per Day", "exam_score": "Exam Score"}
)
st.plotly_chart(fig1, use_container_width=True)

# 😴 2. Sleep vs Mental Health
st.subheader("💤 Sleep Duration vs Mental Health Rating")
fig2 = px.scatter(
    df_filtered,
    x="sleep_hours",
    y="mental_health_rating",
    size="exam_score",
    color="gender",
    hover_name="student_id",
    labels={"sleep_hours": "Sleep Hours", "mental_health_rating": "Mental Health Rating"}
)
st.plotly_chart(fig2, use_container_width=True)

# 💼 3. Exam Scores by Part-Time Job
st.subheader("💼 Exam Scores by Part-Time Job Status")
fig3 = px.box(
    df_filtered,
    x="part_time_job",
    y="exam_score",
    color="part_time_job",
    labels={"part_time_job": "Has Part-Time Job", "exam_score": "Exam Score"}
)
st.plotly_chart(fig3, use_container_width=True)

# 📊 4. Average Exam Score by Internet Quality
st.subheader("🌐 Average Exam Score by Internet Quality")
fig4 = px.bar(
    df_filtered.groupby('internet_quality')['exam_score'].mean().reset_index(),
    x='internet_quality',
    y='exam_score',
    title='Average Exam Score by Internet Quality',
    labels={'internet_quality': 'Internet Quality', 'exam_score': 'Average Exam Score'}
)
st.plotly_chart(fig4, use_container_width=True)

# 🍏 5. Average Exam Score by Diet Quality
st.subheader("🍏 Average Exam Score by Diet Quality")
fig5 = px.bar(
    df_filtered.groupby('diet_quality')['exam_score'].mean().reset_index(),
    x='diet_quality',
    y='exam_score',
    title='Average Exam Score by Diet Quality',
    labels={'diet_quality': 'Diet Quality', 'exam_score': 'Average Exam Score'}
)
st.plotly_chart(fig5, use_container_width=True)

# 📌 Footer
st.markdown("---")
st.markdown("Created by: **Fatmah**")
