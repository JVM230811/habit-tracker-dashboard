# 📊 Habit Tracker Dashboard

A modern, interactive dashboard for tracking daily habits and visualizing progress over time using Streamlit.

## Features

- **📊 Overview Dashboard**: Get quick insights into your habit tracking stats
- **📅 Daily View**: Track individual daily habits
- **📈 Weekly Analytics**: See weekly completion patterns
- **📉 Monthly Reports**: Review monthly progress
- **🏆 Yearly Summary**: Analyze full-year performance
- **📈 Interactive Charts**: Beautiful, responsive visualizations
- **⚡ Real-time Updates**: Auto-reloading interface

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

## Installation

### Prerequisites
- Python 3.8+
- pip package manager

### Setup

1. **Clone or navigate to the project directory**
   ```bash
   cd dashboard
   ```

2. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the dashboard**
   ```bash
   streamlit run dashboard/app.py
   ```

4. **Open in browser**
   The dashboard will automatically open at `http://localhost:8501`

## Project Structure

```
.
├── dashboard/
│   └── app.py              # Main Streamlit application
├── requirements.txt        # Python dependencies
├── README.md              # This file
└── .github/
    └── copilot-instructions.md
```

## Usage

### Navigation
Use the sidebar to switch between different views:
- **Overview**: Dashboard summary with key metrics
- **Daily**: Track habits for a specific date
- **Weekly**: View weekly completion patterns
- **Monthly**: Analyze monthly progress
- **Yearly**: See full-year statistics

### Dashboard Metrics
- **Total Habits**: Number of habits being tracked
- **Days Tracked**: Total tracking days
- **Completion Rate**: Overall habit completion percentage
- **Latest Update**: Most recent tracking date
- **Avg Daily**: Average daily completions

## Customization

### Adding New Habits
Edit the `generate_sample_data()` function in `app.py` to include your habits:
```python
habits = ['Exercise', 'Reading', 'Meditation', 'Water Intake', 'Sleep', 'YOUR_HABIT']
```

### Changing Date Range
Modify the date range in `generate_sample_data()`:
```python
dates = pd.date_range(start='2025-06-01', end='2026-06-05', freq='D')
```

### Customizing Colors
Update the Plotly chart colors in each visualization section.

## Technologies Used

- **Streamlit**: Web framework for creating data apps
- **Pandas**: Data manipulation and analysis
- **Plotly**: Interactive data visualization
- **NumPy**: Numerical computations

## Requirements

See `requirements.txt` for full dependency list:
- streamlit>=1.28.0
- pandas>=2.0.0
- plotly>=5.0.0
- numpy>=1.24.0

## Development

### Adding New Pages
Create new pages by modifying the `page` variable in `app.py` and adding corresponding conditions.

### Modifying Visualizations
All charts are created using Plotly Express (px) for easy customization.

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

- [ ] Database integration for persistent storage
- [ ] User authentication
- [ ] Data export (CSV, PDF)
- [ ] Mobile responsive design
- [ ] Push notifications for reminders
- [ ] Habit recommendations based on patterns
- [ ] Dark mode theme

## License

MIT License - Feel free to use and modify!

## Support

For issues or questions, please refer to the [Streamlit documentation](https://docs.streamlit.io/).
