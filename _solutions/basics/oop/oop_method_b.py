
class Stats:
    def mean(self, data):
        mean = sum(data) / len(data)
        return round(mean, 1)
