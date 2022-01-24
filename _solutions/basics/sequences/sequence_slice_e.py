
ratio = 0.6  # 60%
split = int(len(data) * ratio)
train = data[:split]
test = data[split:]
