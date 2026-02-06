import json
import os
from datetime import datetime

from ai.content_generator import generate_post


class SocialMediaAgent:
    def __init__(self,
                 insights_path="data/insights.json",
                 schedule_log_path="data/scheduled_posts.json"):
        self.insights_path = insights_path
        self.schedule_log_path = schedule_log_path

        # Ensure scheduled_posts.json exists
        if not os.path.exists(self.schedule_log_path):
            with open(self.schedule_log_path, "w") as f:
                json.dump([], f, indent=4)

    def load_insights(self):
        if not os.path.exists(self.insights_path):
            return {}

        with open(self.insights_path, "r") as f:
            content = f.read().strip()
            if content == "":
                return {}
            return json.loads(content)

    def log_post(self, post_text, platform="Unknown"):
        entry = {
            "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "post": post_text,
            "platform": platform,
            "status": "POSTED"
        }

        with open(self.schedule_log_path, "r") as f:
            data = json.load(f)

        data.append(entry)

        with open(self.schedule_log_path, "w") as f:
            json.dump(data, f, indent=4)

    def run_post_cycle(self):
        print("\n===============================")
        print("🤖 AGENT RUNNING POST CYCLE")
        print("🕒 Time:", datetime.now())
        print("===============================\n")

        # Call Person A generator
        result = generate_post()

        post_text = result["generated_post"]
        platform = result.get("recommended_platform", "Unknown")

        print("📌 Platform:", platform)
        print("📝 Generated Post:\n", post_text)

        self.log_post(post_text, platform)

        print("\n✅ Post saved into scheduled_posts.json")
