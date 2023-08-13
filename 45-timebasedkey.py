class TimeMap:

    def __init__(self):
        self.time_map = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.time_map:
            self.time_map[key] = []
        self.time_map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.time_map: 
            return ""

        most_recent_val = ""
        start = 0
        end = len(self.time_map[key])

        while start <= end: 
            cur = (start + end) // 2;
            if self.time_map[key][cur][0] <= timestamp and (cur == len(self.time_map[key]) - 1 or self.time_map[key][cur + 1][0] > timestamp):
                most_recent_val = self.time_map[key][cur][1]
                break
            elif self.time_map[key][cur][0] < timestamp: 
                start = cur + 1
            else: 
                end = cur - 1

        # for timestamp_prev, value in self.time_map[key]:
        #     if timestamp_prev <= timestamp: 
        #         most_recent_val = value
        return most_recent_val