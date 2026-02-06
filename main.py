from agent.agent_controller import SocialMediaAgent
from agent.scheduler import PostScheduler


def main():
    agent = SocialMediaAgent()
    scheduler = PostScheduler(agent)

    insights = agent.load_insights()

    # If Person A generated best_time
    best_time = insights.get("best_time", None)

    print("===================================")
    print("🚀 SOCIAL MEDIA AGENT STARTED")
    print("===================================")

    if best_time:
        print(f"📌 Scheduling daily post at: {best_time}")
        scheduler.schedule_daily_posts([best_time])
    else:
        print("⚠️ insights.json missing best_time, running demo mode.")

    # Always run demo mode too (good for hackathon)
    print("🔥 DEMO MODE: Posting every 10 seconds")
    scheduler.schedule_demo_posts(seconds=10)

    print("🤖 Agent running... (CTRL+C to stop)")
    scheduler.start()


if __name__ == "__main__":
    main()
