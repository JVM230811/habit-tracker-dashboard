# Habit Tracker Dashboard - Streamlit App

A fully customizable habit tracking dashboard built with Streamlit. Track daily habits, visualize progress, and manage everything from a web interface.

## ✨ Features

- 📊 **Dashboard Overview** - Key metrics and visualizations
- 📅 **Daily Tracking** - Mark habits complete/incomplete
- 📈 **Weekly & Monthly Analytics** - See your progress patterns
- ⚙️ **Manage Habits** - Add, edit, delete habits with custom colors
- 💾 **Auto-Save** - All data persists locally in CSV format
- 📱 **Responsive UI** - Works on any device
- 🎨 **Customizable** - Full control over habit names and colors

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/habit-tracker-dashboard.git
   cd habit-tracker-dashboard
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the dashboard**
   ```bash
   streamlit run dashboard/app.py
   ```

5. **Open in browser**
   ```
   http://localhost:8501
   ```

### On Windows (Easiest)
Just double-click `start.bat` in the project folder!

## 📁 Project Structure

```
.
├── dashboard/
│   ├── app.py                 # Main Streamlit app
│   ├── utils/
│   │   └── data_handler.py   # Data persistence layer
│   └── data/
│       ├── habits.csv        # Your habits
│       └── entries.csv       # Daily entries
├── requirements.txt           # Dependencies
├── start.bat                  # Windows launcher
├── run_dashboard.bat          # Alternative launcher
├── run_dashboard.ps1          # PowerShell launcher
└── README.md                  # Documentation
```

## 📋 How to Use

### Add Habits
1. Go to **"Manage Habits"** tab
2. Enter habit name and pick a color
3. Click "Add Habit"

### Track Daily
1. Go to **"Daily"** tab
2. Select a date
3. Click "Mark Done" to toggle completion

### View Analytics
- **Overview**: Summary and overall stats
- **Weekly**: Weekly completion patterns
- **Monthly**: Monthly trends
- **Yearly**: Annual statistics

## 🌐 Deploy to Streamlit Cloud

### Free Hosting with Streamlit Cloud

1. **Push to GitHub** (see below)

2. **Go to [Streamlit Cloud](https://share.streamlit.io/)**

3. **Click "New app"**
   - Repository: `your-username/habit-tracker-dashboard`
   - Branch: `main`
   - Main file path: `dashboard/app.py`

4. **Deploy!** Your app is live in seconds

### Deploy to Heroku (Paid)

1. **Install Heroku CLI**
2. **Add Procfile:**
   ```
   web: streamlit run dashboard/app.py
   ```
3. **Deploy:**
   ```bash
   heroku create your-app-name
   git push heroku main
   ```

### Deploy to Railway, Render, or Other Platforms

All support Python/Streamlit apps. Just set:
- **Command:** `streamlit run dashboard/app.py`
- **Port:** `8501`

## 💾 Data Storage

Data is stored locally in CSV files:
- `dashboard/data/habits.csv` - Habit definitions
- `dashboard/data/entries.csv` - Daily records

**Note:** When deploying to cloud, data is stored in the container (temporary). For persistent storage, consider:
- Adding a database (PostgreSQL, MongoDB)
- Using cloud storage (AWS S3, Google Cloud Storage)
- Using a backend API

## 🛠️ Customization

### Change Port
```bash
streamlit run dashboard/app.py --server.port 8502
```

### Disable Telemetry (Streamlit)
Create `.streamlit/config.toml`:
```toml
[browser]
gatherUsageStats = false
```

## 📦 Dependencies

- streamlit>=1.28.0
- pandas>=2.0.0
- plotly>=5.0.0
- numpy>=1.24.0

## 🔄 GitHub Setup

### First Time Setup

```bash
# Initialize git (if not already done)
git init
git add .
git commit -m "Initial commit: Habit Tracker Dashboard"

# Add your GitHub repository
git remote add origin https://github.com/yourusername/habit-tracker-dashboard.git
git branch -M main
git push -u origin main
```

### Push Updates
```bash
git add .
git commit -m "Your message"
git push origin main
```

## 📝 License

MIT License - Feel free to use and modify!

## 🤝 Contributing

Feel free to fork, modify, and submit PRs!

## 📧 Support

For issues or questions, check the [Streamlit docs](https://docs.streamlit.io/).
