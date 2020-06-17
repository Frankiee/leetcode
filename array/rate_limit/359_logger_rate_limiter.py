# [Classic, Rate-Limit]
# https://leetcode.com/problems/logger-rate-limiter/
# 359. Logger Rate Limiter

# History:
# Google
# 1.
# Mar 10, 2020
# 2.
# May 5, 2020

# Design a logger system that receive stream of messages along with its timestamps, each message
# should be printed if and only if it is not printed in the last 10 seconds.
#
# Given a message and a timestamp (in seconds granularity), return true if the message should be
# printed in the given timestamp, otherwise returns false.
#
# It is possible that several messages arrive roughly at the same time.
#
# Example:
#
# Logger logger = new Logger();
#
# // logging string "foo" at timestamp 1
# logger.shouldPrintMessage(1, "foo"); returns true;
#
# // logging string "bar" at timestamp 2
# logger.shouldPrintMessage(2,"bar"); returns true;
#
# // logging string "foo" at timestamp 3
# logger.shouldPrintMessage(3,"foo"); returns false;
#
# // logging string "bar" at timestamp 8
# logger.shouldPrintMessage(8,"bar"); returns false;
#
# // logging string "foo" at timestamp 10
# logger.shouldPrintMessage(10,"foo"); returns false;
#
# // logging string "foo" at timestamp 11
# logger.shouldPrintMessage(11,"foo"); returns true;


class LoggerQueueSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []
        self.printed = set()

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        while self.queue and self.queue[-1][0] + 10 <= timestamp:
            _, msg = self.queue.pop(-1)
            self.printed.remove(msg)

        if message in self.printed:
            return False
        else:
            self.queue.insert(0, (timestamp, message))
            self.printed.add(message)
            return True


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)


class LoggerCircularBuffer(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mem = [set() for _ in range(10)]
        self.curr_idx = 0
        self.curr_idx_ts = None

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns
        false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        if self.curr_idx_ts is None:
            self.curr_idx_ts = timestamp
            self.mem[self.curr_idx].add(message)
            return True

        time_stamp_diff = timestamp - self.curr_idx_ts
        indices_to_check = min(time_stamp_diff, 10)

        # forward time
        for i in range(self.curr_idx + 1, self.curr_idx + indices_to_check + 1):
            idx = i % 10
            self.mem[idx] = set()

            self.curr_idx = i

        self.curr_idx %= 10
        self.curr_idx_ts = timestamp

        for i in range(10):
            if message in self.mem[i]:
                return False

        self.mem[self.curr_idx].add(message)
        return True

# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
