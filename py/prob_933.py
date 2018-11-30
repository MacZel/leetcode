class RecentCounter:

    def __init__(self):
        self.TIME_WINDOW = 3000
        self.recent_pings_queue = []

    def ping(self, t):
        """
        :type t: int
        :rtype: int
        """
        ping_time_diff = t - self.TIME_WINDOW
        self.recent_pings_queue.insert(0, t)
        while self.recent_pings_queue[-1] < ping_time_diff:
            self.recent_pings_queue.pop(-1)
        return len(self.recent_pings_queue)