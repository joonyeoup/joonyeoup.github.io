#!/usr/bin/env python3
"""
Simple HTTP server to preview the academic website locally.
Run this script and open http://localhost:8000 in your browser.
"""

import http.server
import socketserver
import webbrowser
import os

PORT = 8000

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def end_headers(self):
        # Add headers to prevent caching during development
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        self.send_header('Expires', '0')
        super().end_headers()

os.chdir(os.path.dirname(os.path.abspath(__file__)))

with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
    print(f"🚀 Server running at http://localhost:{PORT}")
    print("📁 Serving files from:", os.getcwd())
    print("\nPress Ctrl+C to stop the server")
    
    # Try to open the browser automatically
    try:
        webbrowser.open(f'http://localhost:{PORT}')
        print("✅ Browser should open automatically...")
    except:
        print("⚠️  Please open your browser manually")
    
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n\n👋 Server stopped!")
