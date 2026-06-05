import pandas as pd
import os
from datetime import datetime
import json

# Data file paths
DATA_DIR = "dashboard/data"
HABITS_FILE = os.path.join(DATA_DIR, "habits.csv")
ENTRIES_FILE = os.path.join(DATA_DIR, "entries.csv")
CONFIG_FILE = os.path.join(DATA_DIR, "config.json")

# Ensure data directory exists
os.makedirs(DATA_DIR, exist_ok=True)


def initialize_data():
    """Initialize default data if files don't exist"""
    # Create habits if not exists
    if not os.path.exists(HABITS_FILE):
        default_habits = pd.DataFrame({
            'habit_id': [1, 2, 3, 4, 5],
            'name': ['Exercise', 'Reading', 'Meditation', 'Water Intake', 'Sleep'],
            'color': ['#FF6B6B', '#4ECDC4', '#45B7D1', '#FFA07A', '#98D8C8'],
            'created_date': [datetime.now()] * 5
        })
        default_habits.to_csv(HABITS_FILE, index=False)
    
    # Create entries if not exists
    if not os.path.exists(ENTRIES_FILE):
        entries = []
        habits = get_all_habits()
        dates = pd.date_range(start='2025-06-01', end=datetime.now(), freq='D')
        
        for date in dates:
            for _, habit in habits.iterrows():
                completed = (hash(f"{date}{habit['name']}") % 3) != 0
                entries.append({
                    'date': date.date(),
                    'habit_id': habit['habit_id'],
                    'completed': completed
                })
        
        entries_df = pd.DataFrame(entries)
        entries_df.to_csv(ENTRIES_FILE, index=False)


def get_all_habits():
    """Get all habits"""
    if not os.path.exists(HABITS_FILE):
        initialize_data()
    return pd.read_csv(HABITS_FILE)


def add_habit(name, color='#45B7D1'):
    """Add a new habit"""
    habits = get_all_habits()
    new_id = habits['habit_id'].max() + 1 if len(habits) > 0 else 1
    
    new_habit = pd.DataFrame({
        'habit_id': [new_id],
        'name': [name],
        'color': [color],
        'created_date': [datetime.now()]
    })
    
    habits = pd.concat([habits, new_habit], ignore_index=True)
    habits.to_csv(HABITS_FILE, index=False)
    return new_id


def delete_habit(habit_id):
    """Delete a habit"""
    habits = get_all_habits()
    habits = habits[habits['habit_id'] != habit_id]
    habits.to_csv(HABITS_FILE, index=False)
    
    # Also delete entries for this habit
    if os.path.exists(ENTRIES_FILE):
        entries = pd.read_csv(ENTRIES_FILE)
        entries = entries[entries['habit_id'] != habit_id]
        entries.to_csv(ENTRIES_FILE, index=False)


def update_habit_name(habit_id, new_name):
    """Update habit name"""
    habits = get_all_habits()
    habits.loc[habits['habit_id'] == habit_id, 'name'] = new_name
    habits.to_csv(HABITS_FILE, index=False)


def update_habit_color(habit_id, new_color):
    """Update habit color"""
    habits = get_all_habits()
    habits.loc[habits['habit_id'] == habit_id, 'color'] = new_color
    habits.to_csv(HABITS_FILE, index=False)


def get_entries_for_date(date):
    """Get habit entries for a specific date"""
    initialize_data()
    entries = pd.read_csv(ENTRIES_FILE)
    entries['date'] = pd.to_datetime(entries['date'])
    day_entries = entries[entries['date'].dt.date == date]
    
    habits = get_all_habits()
    result = day_entries.merge(habits, on='habit_id', how='left')
    return result


def toggle_habit_completion(habit_id, date):
    """Toggle habit completion for a specific date"""
    entries = pd.read_csv(ENTRIES_FILE)
    entries['date'] = pd.to_datetime(entries['date'])
    
    mask = (entries['habit_id'] == habit_id) & (entries['date'].dt.date == date)
    
    if mask.any():
        entries.loc[mask, 'completed'] = ~entries.loc[mask, 'completed']
    else:
        # If entry doesn't exist, create it
        new_entry = pd.DataFrame({
            'date': [pd.Timestamp(date)],
            'habit_id': [habit_id],
            'completed': [True]
        })
        entries = pd.concat([entries, new_entry], ignore_index=True)
    
    entries.to_csv(ENTRIES_FILE, index=False)


def get_all_data():
    """Get all data for dashboard"""
    initialize_data()
    entries = pd.read_csv(ENTRIES_FILE)
    entries['date'] = pd.to_datetime(entries['date'])
    
    habits = get_all_habits()
    data = entries.merge(habits, on='habit_id', how='left')
    return data


def add_entry(habit_id, date, completed=True):
    """Add a new entry"""
    entries = pd.read_csv(ENTRIES_FILE)
    
    new_entry = pd.DataFrame({
        'date': [pd.Timestamp(date)],
        'habit_id': [habit_id],
        'completed': [completed]
    })
    
    entries = pd.concat([entries, new_entry], ignore_index=True)
    entries.to_csv(ENTRIES_FILE, index=False)
