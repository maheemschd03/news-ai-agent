from flask import Flask, render_template, jsonify, send_from_directory
from test import Reporter, Organizer
import threading
import time
import os

app = Flask(__name__)

# Global variables to track progress
progress_status = {
    "status": "idle",
    "message": "",
    "completion": 0
}

def update_progress(status, message, completion):
    global progress_status
    progress_status = {
        "status": status,
        "message": message,
        "completion": completion
    }

def fetch_news():
    try:
        update_progress("running", "Starting news collection...", 10)
        
        # Create instances
        reporter = Reporter()
        organizer = Organizer()
        
        update_progress("running", "Fetching news from sources...", 30)
        content = reporter.research()
        
        update_progress("running", "Organizing and creating website...", 60)
        organizer.Work(content)
        
        update_progress("complete", "News website generated successfully!", 100)
        
    except Exception as e:
        update_progress("error", f"Error occurred: {str(e)}", 0)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start')
def start_process():
    if progress_status["status"] != "running":
        threading.Thread(target=fetch_news).start()
    return jsonify({"message": "Process started"})

@app.route('/status')
def get_status():
    return jsonify(progress_status)

@app.route('/Final.html')
def serve_news():
    return send_from_directory('static', 'Final.html')

if __name__ == '__main__':
    # Create required directories if they don't exist
    os.makedirs('templates', exist_ok=True)
    os.makedirs('static', exist_ok=True)
    app.run(debug=True) 