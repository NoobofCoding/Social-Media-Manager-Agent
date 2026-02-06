from flask import Flask, render_template, jsonify
import json
import os

app = Flask(__name__)

INSIGHTS_PATH = "data/insights.json"
LOG_PATH = "data/scheduled_posts.json"


def safe_load_json(path, default):
    if not os.path.exists(path):
        return default

    try:
        with open(path, "r") as f:
            content = f.read().strip()
            if content == "":
                return default
            return json.loads(content)
    except json.JSONDecodeError:
        return default


@app.route("/")
def dashboard():
    insights = safe_load_json(INSIGHTS_PATH, {})
    logs = safe_load_json(LOG_PATH, [])

    total_posts = len(logs)
    last_post_time = logs[-1]["time"] if logs else "No posts yet"

    return render_template(
        "dashboard.html",
        insights=insights,
        logs=logs,
        total_posts=total_posts,
        last_post_time=last_post_time
    )


@app.route("/api/logs")
def api_logs():
    logs = safe_load_json(LOG_PATH, [])
    return jsonify(logs)


@app.route("/api/insights")
def api_insights():
    insights = safe_load_json(INSIGHTS_PATH, {})
    return jsonify(insights)


if __name__ == "__main__":
    app.run(debug=True)
