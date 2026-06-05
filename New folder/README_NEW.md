# 📊 Habit Tracker Dashboard

A modern, interactive dashboard for tracking daily habits and visualizing progress over time using Streamlit. **Now with full customization** - edit habits, names, colors, and completion status directly on the site!

## ✨ Features

- **⚙️ Manage Habits**: Add, edit, delete habits directly from the interface
- **✏️ Edit Everything**: Change habit names and colors anytime
- **✅ Daily Tracking**: Click to mark habits complete/incomplete
- **📊 Overview Dashboard**: Get quick insights into your habit tracking stats
- **📅 Daily View**: Track individual daily habits with real-time editing
- **📈 Weekly Analytics**: See weekly completion patterns
- **📉 Monthly Reports**: Review monthly progress
- **🏆 Yearly Summary**: Analyze full-year performance
- **💾 Auto-Save**: All changes are automatically saved to persistent storage
- **📈 Interactive Charts**: Beautiful, responsive visualizations
- **🎨 Custom Colors**: Choose colors for each habit

## 🚀 Quick Start

### **Easiest - Just Run This:**
1. Double-click **`start.bat`** in your project folder
2. Dashboard opens automatically at `http://localhost:8501`

That's it! The script handles everything:
- ✅ Checks if Python is installed
- ✅ Creates virtual environment (first time only)
- ✅ Installs dependencies (first time only)
- ✅ Starts the dashboard
- ✅ Opens in browser

### Alternative Methods

**Option 2: PowerShell**
```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\run_dashboard.ps1
```

**Option 3: Manual Command Line**
```bash
cd "C:\Users\JMist\OneDrive\Desktop\Python\New folder"
.venv\Scripts\activate
streamlit run dashboard/app.py
```

## 📋 How to Use

### Adding New Habits
1. Go to **"Manage Habits"** tab
2. Enter habit name and pick a color
3. Click "Add Habit"
4. Habit appears in all views immediately

### Editing Habits
1. Go to **"Manage Habits"** tab
2. Edit the name directly in the text field
3. Change color with the color picker
4. Changes save automatically

### Daily Tracking
1. Go to **"Daily"** tab
2. Select a date
3. Click "Mark Done" or "Toggle" to update status
4. Status updates instantly

### Deleting Habits
1. Go to **"Manage Habits"** tab
2. Click "❌ Delete" next to any habit
3. Habit and all its data removed

## 📁 Project Structure

```
.
├── dashboard/
│   ├── app.py                 # Main Streamlit application
│   ├── utils/
│   │   └── data_handler.py   # Data management & persistence
│   └── data/
│       ├── habits.csv        # Stored habits
│       └── entries.csv       # Stored entries
├── start.bat                  # One-click launcher
├── run_dashboard.bat          # Alternative launcher
├── run_dashboard.ps1          # PowerShell launcher
├── requirements.txt           # Python dependencies
├── README.md                  # This file
└── .github/
    └── copilot-instructions.md
```

## 💾 Data Storage

All your data is stored locally in CSV files:
- **`dashboard/data/habits.csv`** - Your habit definitions and colors
- **`dashboard/data/entries.csv`** - Daily completion records

You can also edit these files directly in Excel or any text editor!

## 🛠️ Customization

### Changing Default Habits
Delete `dashboard/data/habits.csv` and restart - it will create new defaults.

### Exporting Data
- Download the CSV files from `dashboard/data/` folder
- Open in Excel for reports and analysis

## Technologies Used

- **Streamlit**: Web framework for creating data apps
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualization
- **NumPy**: Numerical computations
- **CSV**: Simple local data storage

## Requirements

See `requirements.txt` for full dependency list:
- streamlit>=1.28.0
- pandas>=2.0.0
- plotly>=5.0.0
- numpy>=1.24.0

## Development

### Adding New Features
1. Edit habit display in the Daily tab
2. Modify visualizations in Weekly/Monthly/Yearly tabs
3. Add new pages by updating the sidebar radio buttons

### Modifying Data Storage
Edit `dashboard/utils/data_handler.py` to change how data is stored.

## Troubleshooting

### Port Already in Use
If port 8501 is already in use:
```bash
streamlit run dashboard/app.py --server.port 8502
```

### Missing Dependencies
Ensure all packages are installed:
```bash
pip install -r requirements.txt --upgrade
```

### Dashboard Not Loading
Verify Streamlit is properly installed:
```bash
streamlit --version
```

## Future Enhancements

- [ ] Export to PDF reports
- [ ] Dark mode theme
- [ ] Habit reminders
- [ ] Streak tracking
- [ ] Mobile app
- [ ] Cloud sync
- [ ] Multiple users
- [ ] Statistics and insights

## License

MIT License - Feel free to use and modify!

## Support

For issues or questions, please refer to the [Streamlit documentation](https://docs.streamlit.io/).
