import asyncio
import asyncio.exceptions


class EventLoopMonitor:
    def __init__(self):
        self.prev = asyncio.get_running_loop().time()
        self.loop = asyncio.get_running_loop()
        self.count = 0
        self.max = -1
        self.min = 10 * 1000
        self.avarage = 0
        self.median = []

    async def monitor_callback(self) -> None:
        """
        Callback to measure time between event loop iterations.
        Runs asynchronously as a daemon in the event loop.
        """

        now = self.loop.time()

        if now - self.prev > 0.001:
            self.count += 1
            self.avarage += (now - self.prev)
            self.max = max(self.max, (now - self.prev))
            self.min = min(self.min, (now - self.prev))
            self.median.append(now - self.prev)
        self.prev = now

        await asyncio.sleep(0.00005)
        asyncio.create_task(self.monitor_callback())

    def get_statistics(self) -> dict:
        """
        Calculate statistics about blocking times.
        TODO: Replace with actual implementation
        """
        self.median.sort()
        if self.count == 0:
            return {
            "count": 0,
            "average": 0,
            "max": 0,
            "min": 0,
            "median": 0
        }
        return {
            "count": self.count,
            "average": self.avarage / self.count,
            "max": self.max,
            "min": self.min,
            "median": self.median[len(self.median) // 2]
        }
