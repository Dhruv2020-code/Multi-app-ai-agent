from flask import Flask, render_template, jsonify
import agent

app = Flask(__name__)

@app.route('/')
def home():
    # Renders the UI dashboard
    return render_template('index.html')

@app.route('/sentry-webhook', methods=['POST'])
def sentry_webhook():
    print("\n🚨 [Sentry] New Crash Detected! Triggering AI Agent...")
    try:
        # Run agent lifecycle
        pr_url = agent.run_agent_loop()
        return jsonify({
            "status": "success",
            "message": "Remediation complete",
            "pr_url": pr_url or "https://github.com/Dhruv2020-code/Multi-app-ai-agent/pulls"
        }), 200
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 500

if __name__ == '__main__':
    print("🌐 Webhook & Dashboard Server running on http://127.0.0.1:5000")
    app.run(port=5000, debug=True)