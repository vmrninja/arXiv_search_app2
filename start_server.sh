#!/bin/bash

echo "================================================"
echo "  arXiv Paper Search - Starting Backend Server"
echo "================================================"
echo ""
echo "Checking Python installation..."

if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is not installed. Please install Python 3 first."
    exit 1
fi

echo "✓ Python 3 found"
echo ""
echo "Installing/checking required packages..."
python3 -m pip install flask flask-cors requests --quiet

echo "✓ All packages ready"
echo ""
echo "================================================"
echo "  🚀 Starting Server..."
echo "================================================"
echo ""
echo "The server will run at: http://localhost:5000"
echo "Now open arxiv-search.html in your browser!"
echo ""
echo "Press Ctrl+C to stop the server"
echo ""

python3 arxiv_server.py
