from flask import Flask, jsonify
import threading
from agent import start_agent_loop

app = Flask(__name__)

@app.route('/sentry-webhook', methods=['POST'])
def sentry_trigger():
    print("🚨 [Sentry] New Crash Detected! Triggering AI Agent...")
    
    # Run agent in the background
    thread = threading.Thread(target=start_agent_loop)
    thread.start()
    
    return jsonify({"status": "received", "message": "AI Agent deployed to fix the bug"}), 200

if __name__ == '__main__':
    print("🌐 Webhook server running on port 5000. Listening for Sentry alerts...")
    app.run(port=5000)