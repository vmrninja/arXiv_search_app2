# arXiv Paper Search Web App

A clean, modern web application for searching scientific papers on arXiv.

## Problem & Solution

**The Problem:** Direct API calls from browser JavaScript to arXiv are blocked by CORS (Cross-Origin Resource Sharing) security policies.

**The Solution:** This app uses a Python Flask backend server that makes the API requests on your behalf, avoiding CORS issues.

## Quick Start

### Step 1: Start the Backend Server

Open a terminal and run:

```bash
python arxiv_server.py
```

You should see:
```
Starting arXiv Search Server...
Server running at http://localhost:5000
```

**Keep this terminal window open** - the server needs to stay running.

### Step 2: Open the Web App

Open `arxiv-search.html` in your web browser. You can:
- Double-click the file, or
- Right-click → Open with → your browser, or
- Drag and drop it into your browser

### Step 3: Search Papers

1. Enter your search term (e.g., "quantum computing", "neural networks")
2. Choose your search options:
   - **Search in**: All fields, Title, Author, or Abstract
   - **Sort by**: Relevance, Last Updated, or Submitted Date
   - **Results**: 10, 25, or 50 papers
3. Click "Search"

## Requirements

- Python 3.6 or higher
- Flask (`pip install flask`)
- flask-cors (`pip install flask-cors`)
- requests (`pip install requests`)

All requirements should already be installed. If not, run:

```bash
pip install flask flask-cors requests
```

## Features

- 🔍 Real-time search through arXiv's database
- 📊 Multiple search filters and sorting options
- 📄 Direct links to paper abstracts and PDFs
- 📱 Responsive design (works on mobile and desktop)
- ⚡ Fast and clean interface

## Troubleshooting

### "Load failed" error
- Make sure the Python server is running (Step 1)
- Check that you see "Server running at http://localhost:5000" in your terminal

### "Connection refused" error
- The backend server isn't running. Start it with `python arxiv_server.py`

### Server won't start
- Make sure port 5000 isn't already in use
- Check that all Python packages are installed

### No results found
- Try different search terms
- Change the "Search in" field to broaden your search
- Check your internet connection

## How It Works

1. **Frontend (HTML)**: The web interface where you enter searches
2. **Backend (Python)**: A Flask server that communicates with arXiv API
3. **arXiv API**: The official arXiv database

```
Browser → Flask Server → arXiv API → Flask Server → Browser
         (localhost:5000)
```

This architecture bypasses CORS restrictions while keeping the interface simple and user-friendly.

## Architecture

```
arxiv-search.html  (Frontend - runs in browser)
        ↓
    localhost:5000 (Flask Backend - runs in terminal)
        ↓
    arXiv API (external service)
```

## Stopping the Server

Press `Ctrl+C` in the terminal where the server is running.

---

Enjoy searching papers! 📚
