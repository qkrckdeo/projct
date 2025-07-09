# daily_pattern.py

import datetime
import statistics

class LifestyleAnalyzer:
    def __init__(self):
        # 예시 데이터: 수면 시작 시간 (datetime.time 객체 리스트)
        self.sleep_times = []
        self.wake_times = []

    def add_record(self, sleep_time: datetime.time, wake_time: datetime.time):
        self.sleep_times.append(sleep_time)
        self.wake_times.append(wake_time)

    def average_time(self, time_list):
        seconds = [t.hour * 3600 + t.minute * 60 for t in time_list]
        avg_sec = int(statistics.mean(seconds))
        return datetime.time(hour=avg_sec // 3600, minute=(avg_sec % 3600) // 60)

    def analyze(self):
        if len(self.sleep_times) < 3 or len(self.wake_times) < 3:
            return "더 많은 데이터가 필요합니다."

        avg_sleep = self.average_time(self.sleep_times)
        avg_wake = self.average_time(self.wake_times)

        return {
            "추천 수면 시간": avg_sleep.strftime("%H:%M"),
            "추천 기상 시간": avg_wake.strftime("%H:%M"),
            "메시지": "이 시간에 맞춰 생활하면 보다 규칙적인 루틴을 만들 수 있습니다!"
        }


# 예제 실행
if __name__ == "__main__":
    analyzer = LifestyleAnalyzer()
    analyzer.add_record(datetime.time(01, 30), datetime.time(09, 0))
    analyzer.add_record(datetime.time(02, 00), datetime.time(08, 30))
    analyzer.add_record(datetime.time(00, 45), datetime.time(07, 45))

    result = analyzer.analyze()
    print(result)

