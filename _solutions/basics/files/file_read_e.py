
result = {}

with open(FILE) as file:
    for line in file:
        line = line.strip()

        if len(line) == 0:
            continue
        if line.startswith('#'):
            continue

        ip, *hostnames = line.split()

        if ip in result:
            result[ip] += hostnames
        else:
            result[ip] = hostnames
