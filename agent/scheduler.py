import schedule
import time


class PostScheduler:
    def __init__(self, agent_controller):
        self.agent = agent_controller

    def schedule_daily_posts(self, times):
        for t in times:
            schedule.every().day.at(t).do(self.agent.run_post_cycle)

    def schedule_demo_posts(self, seconds=10):
        schedule.every(seconds).seconds.do(self.agent.run_post_cycle)

    def start(self):
        while True:
            schedule.run_pending()
            time.sleep(1)
