from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import xml.etree.ElementTree as ET

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

@app.route('/api/search', methods=['GET'])
def search_arxiv():
    try:
        # Get query parameters
        query = request.args.get('query', '')
        field = request.args.get('field', 'all')
        sort_by = request.args.get('sortBy', 'relevance')
        max_results = request.args.get('maxResults', '25')
        
        # Construct arXiv API URL
        search_query = f"{field}:{query}"
        api_url = f"https://export.arxiv.org/api/query?search_query={search_query}&start=0&max_results={max_results}&sortBy={sort_by}&sortOrder=descending"
        
        # Make request to arXiv API
        response = requests.get(api_url, timeout=10)
        response.raise_for_status()
        
        # Parse XML response
        root = ET.fromstring(response.content)
        
        # Define namespaces
        ns = {
            'atom': 'http://www.w3.org/2005/Atom',
            'arxiv': 'http://arxiv.org/schemas/atom'
        }
        
        # Extract papers
        papers = []
        for entry in root.findall('atom:entry', ns):
            paper = {
                'id': entry.find('atom:id', ns).text if entry.find('atom:id', ns) is not None else '',
                'title': entry.find('atom:title', ns).text.strip() if entry.find('atom:title', ns) is not None else 'No title',
                'summary': entry.find('atom:summary', ns).text.strip() if entry.find('atom:summary', ns) is not None else 'No abstract',
                'published': entry.find('atom:published', ns).text if entry.find('atom:published', ns) is not None else '',
                'updated': entry.find('atom:updated', ns).text if entry.find('atom:updated', ns) is not None else '',
                'authors': [author.find('atom:name', ns).text for author in entry.findall('atom:author', ns)]
            }
            papers.append(paper)
        
        return jsonify({
            'success': True,
            'papers': papers,
            'count': len(papers)
        })
        
    except requests.exceptions.RequestException as e:
        return jsonify({
            'success': False,
            'error': f'Failed to fetch from arXiv: {str(e)}'
        }), 500
    except Exception as e:
        return jsonify({
            'success': False,
            'error': str(e)
        }), 500

@app.route('/')
def index():
    return 'arXiv Search API is running. Use /api/search endpoint.'

if __name__ == '__main__':
    print("Starting arXiv Search Server...")
    print("Server running at http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    app.run(debug=True, host='0.0.0.0', port=5000)
