#!/usr/bin/env python3
"""
Simple HTTP server for previewing landing pages.
Usage: python3 serve.py
Access at: http://localhost:8091
"""

import http.server
import socketserver
import os

PORT = 8091
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class MyHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Add CORS headers for local development
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Cache-Control', 'no-store, no-cache, must-revalidate')
        super().end_headers()

if __name__ == "__main__":
    os.chdir(DIRECTORY)
    
    with socketserver.TCPServer(("", PORT), MyHTTPRequestHandler) as httpd:
        print(f"🚀 Server running at http://localhost:{PORT}")
        print(f"📂 Serving files from: {DIRECTORY}")
        print(f"\n📄 Available pages:")
        print(f"   • http://localhost:{PORT}/index.html (Hub)")
        print(f"   • http://localhost:{PORT}/pdf-scanner.html (ScanSnap Pro)")
        print(f"   • http://localhost:{PORT}/freelancer-tool.html (InvoiceCraft)")
        print(f"   • http://localhost:{PORT}/voice-journal.html (MindVault)")
        print(f"\n💡 Press Ctrl+C to stop the server\n")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n\n👋 Server stopped")
