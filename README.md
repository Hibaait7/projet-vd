# Data Analysis and Visualization Tool

A lightweight Django application for analyzing and visualizing CSV data with interactive features.

## Features
- CSV file upload and parsing
- Row/column-based data access
- Statistical analysis
- Interactive matplotlib visualizations with zoom capabilities
- Real-time data exploration
- No database required - all operations in memory

## Installation
```bash
# Create virtual environment
python -m venv venv
source venv/bin/activate  # Linux/Mac
# or
venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt

# Run server
python manage.py runserver
```

## Usage
1. Upload CSV file through web interface
2. Access specific rows/columns using the index tools
3. View statistical summaries
4. Create visualizations:
   - Scatter plots
   - Line charts
   - Bar graphs
   - Histograms
   - Box plots

## Requirements
```
django>=4.2.0
pandas>=2.0.0
matplotlib>=3.7.0
numpy>=1.24.0
```

## Project Structure
```
data_visualization/
├── data_analysis/
│   ├── views.py      # Main logic
│   └── urls.py       # URL routing
├── templates/        # HTML templates
├── static/          # CSS files
├── manage.py
└── requirements.txt
```

## Notes
- Data persists only during session
- Refresh page requires re-upload
- Supports numeric and text data
- Uses matplotlib for all visualizations