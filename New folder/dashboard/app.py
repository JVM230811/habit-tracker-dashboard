import streamlit as st
import pandas as pd
from datetime import datetime, timedelta
import plotly.graph_objects as go
import plotly.express as px
import sys
import os

# Add utils to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'utils'))
from data_handler import (
    initialize_data, get_all_habits, get_all_data, add_habit, 
    delete_habit, update_habit_name, update_habit_color, 
    get_entries_for_date, toggle_habit_completion
)

# Configure page
st.set_page_config(
    page_title="Habit Tracker Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Initialize data
initialize_data()

# Add custom styling
st.markdown("""
    <style>
    .metric-card {
        background-color: #f0f2f6;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
    }
    .habit-item {
        padding: 10px;
        border-radius: 5px;
        margin: 5px 0;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.title("📊 Habit Tracker Dashboard")
st.markdown("---")

# Sidebar navigation
st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Select View:",
    ["Overview", "Daily", "Weekly", "Monthly", "Yearly", "Manage Habits"],
    index=0
)

# Get data
df = get_all_data()
habits = get_all_habits()

# Overview Page
if page == "Overview":
    col1, col2, col3, col4, col5 = st.columns(5)
    
    with col1:
        total_habits = len(habits)
        st.metric("Total Habits", total_habits)
    
    with col2:
        total_days = df['date'].nunique()
        st.metric("Days Tracked", total_days)
    
    with col3:
        completion_rate = (df['completed'].sum() / len(df)) * 100
        st.metric("Completion Rate", f"{completion_rate:.1f}%")
    
    with col4:
        current_date = df['date'].max()
        st.metric("Latest Update", current_date.strftime("%b %d"))
    
    with col5:
        avg_daily = df.groupby('date')['completed'].sum().mean()
        st.metric("Avg Daily", f"{avg_daily:.1f}")
    
    st.markdown("---")
    
    # Overall completion chart
    st.subheader("📈 Overall Habit Completion")
    daily_completion = df.groupby('date').apply(
        lambda x: (x['completed'].sum() / len(x)) * 100
    ).reset_index()
    daily_completion.columns = ['date', 'completion_rate']
    
    fig = px.line(daily_completion, x='date', y='completion_rate',
                  title='Daily Completion Rate',
                  labels={'completion_rate': 'Completion %', 'date': 'Date'},
                  markers=True)
    fig.update_layout(height=400)
    st.plotly_chart(fig, width='stretch')
    
    # Habit breakdown
    st.subheader("🎯 Habit Breakdown")
    col1, col2 = st.columns(2)
    
    with col1:
        habit_completion = df.groupby('name')['completed'].apply(
            lambda x: (x.sum() / len(x)) * 100
        ).sort_values(ascending=True)
        
        fig = px.bar(habit_completion,
                     title='Completion Rate by Habit',
                     labels={'value': 'Completion %'},
                     orientation='h')
        fig.update_layout(height=400)
        st.plotly_chart(fig, width='stretch')
    
    with col2:
        habit_counts = df[df['completed']].groupby('name').size().sort_values(ascending=False)
        fig = px.pie(values=habit_counts.values, names=habit_counts.index,
                    title='Times Completed by Habit')
        fig.update_layout(height=400)
        st.plotly_chart(fig, width='stretch')

# Daily Page with Edit Capabilities
elif page == "Daily":
    st.subheader("📅 Daily Tracking & Edit")
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_date = st.date_input("Select Date:", datetime.now().date())
    
    with col2:
        if st.button("Today", use_container_width=True):
            selected_date = datetime.now().date()
    
    # Get entries for selected date
    daily_data = get_entries_for_date(selected_date)
    
    if len(daily_data) == 0:
        st.info("No habits tracked yet. Go to 'Manage Habits' to add some!")
    else:
        st.write(f"**Date:** {selected_date.strftime('%A, %B %d, %Y')}")
        
        # Display habits with toggle buttons
        cols = st.columns([2, 1, 1])
        with cols[0]:
            st.write("**Habit**")
        with cols[1]:
            st.write("**Status**")
        with cols[2]:
            st.write("**Action**")
        
        st.divider()
        
        for idx, (_, row) in enumerate(daily_data.iterrows()):
            cols = st.columns([2, 1, 1])
            
            with cols[0]:
                st.write(row['name'])
            
            with cols[1]:
                status = "✅ Done" if row['completed'] else "⏳ Pending"
                st.write(status)
            
            with cols[2]:
                if st.button(
                    "Toggle" if row['completed'] else "Mark Done",
                    key=f"toggle_{row['habit_id']}_{selected_date}",
                    use_container_width=True
                ):
                    toggle_habit_completion(row['habit_id'], selected_date)
                    st.rerun()
        
        # Summary
        st.divider()
        completed = daily_data['completed'].sum()
        total = len(daily_data)
        st.metric("Today's Completion", f"{completed}/{total} ({int(completed/total*100)}%)")

# Weekly Page
elif page == "Weekly":
    st.subheader("📊 Weekly Statistics")
    
    df['week'] = df['date'].dt.isocalendar().week
    df['year'] = df['date'].dt.year
    
    weekly_data = df.groupby(['year', 'week', 'name'])['completed'].sum().reset_index()
    
    fig = px.bar(weekly_data, x='week', y='completed', color='name',
                title='Weekly Completion by Habit',
                labels={'completed': 'Completed Days', 'week': 'Week Number'})
    fig.update_layout(height=500)
    st.plotly_chart(fig, width='stretch')

# Monthly Page
elif page == "Monthly":
    st.subheader("📈 Monthly Overview")
    
    df['month'] = df['date'].dt.to_period('M')
    
    monthly_data = df.groupby(['month', 'name'])['completed'].sum().reset_index()
    monthly_data['month'] = monthly_data['month'].astype(str)
    
    fig = px.bar(monthly_data, x='month', y='completed', color='name',
                title='Monthly Completion by Habit',
                labels={'completed': 'Completed Days', 'month': 'Month'})
    fig.update_layout(height=500)
    st.plotly_chart(fig, width='stretch')

# Yearly Page
elif page == "Yearly":
    st.subheader("🏆 Yearly Summary")
    
    yearly_data = df.groupby('name')['completed'].sum().sort_values(ascending=False)
    
    fig = px.bar(yearly_data, title='Total Completions by Habit',
                labels={'value': 'Times Completed', 'index': 'Habit'},
                orientation='v')
    fig.update_layout(height=500)
    st.plotly_chart(fig, width='stretch')
    
    # Stats
    st.subheader("📊 Annual Statistics")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        total_completed = df['completed'].sum()
        st.metric("Total Completed", int(total_completed))
    
    with col2:
        total_possible = len(df)
        st.metric("Total Possible", int(total_possible))
    
    with col3:
        annual_rate = (total_completed / total_possible) * 100
        st.metric("Annual Rate", f"{annual_rate:.1f}%")

# Manage Habits Page
elif page == "Manage Habits":
    st.subheader("⚙️ Manage Your Habits")
    
    # Add new habit section
    st.markdown("### ➕ Add New Habit")
    col1, col2, col3 = st.columns([2, 1, 1])
    
    with col1:
        new_habit_name = st.text_input("Habit name:", key="new_habit_input")
    
    with col2:
        new_habit_color = st.color_picker("Color:", value="#45B7D1", key="new_habit_color")
    
    with col3:
        if st.button("Add Habit", use_container_width=True):
            if new_habit_name.strip():
                add_habit(new_habit_name, new_habit_color)
                st.success(f"✅ Added '{new_habit_name}'!")
                st.rerun()
            else:
                st.error("Please enter a habit name")
    
    st.divider()
    
    # Edit existing habits
    st.markdown("### 📝 Edit Habits")
    
    if len(habits) == 0:
        st.info("No habits yet. Add one above!")
    else:
        for idx, (_, habit) in enumerate(habits.iterrows()):
            col1, col2, col3, col4 = st.columns([2, 1, 1, 0.8])
            
            with col1:
                new_name = st.text_input(
                    "Habit name:",
                    value=habit['name'],
                    key=f"habit_name_{habit['habit_id']}"
                )
                if new_name != habit['name']:
                    update_habit_name(habit['habit_id'], new_name)
                    st.rerun()
            
            with col2:
                new_color = st.color_picker(
                    "Color:",
                    value=habit['color'],
                    key=f"habit_color_{habit['habit_id']}"
                )
                if new_color != habit['color']:
                    update_habit_color(habit['habit_id'], new_color)
                    st.rerun()
            
            with col3:
                completed_count = len(df[df['habit_id'] == habit['habit_id']])
                st.metric("Entries", completed_count)
            
            with col4:
                if st.button(
                    "❌ Delete",
                    key=f"delete_{habit['habit_id']}",
                    use_container_width=True
                ):
                    delete_habit(habit['habit_id'])
                    st.success("✅ Deleted!")
                    st.rerun()

st.markdown("---")
st.caption("📊 Habit Tracker Dashboard • Fully customizable • Data auto-saved")
