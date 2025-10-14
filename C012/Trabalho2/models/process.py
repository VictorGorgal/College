import time


class Process:
    def __init__(self, pid, text, priority=1, charsPerSecond=10):
        self.pid = pid
        self.text = text
        self.length = len(text)
        self.priority = priority
        self.charsPerSecond = charsPerSecond

    def __repr__(self):
        return self.text

    def execute(self, output_buffer):
        for ch in self.text:
            output_buffer.append(ch)
            time.sleep(1 / self.charsPerSecond)
        output_buffer.append('\n')
