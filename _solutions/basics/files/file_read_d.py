
result = {}

with open(FILE) as file:
    for line in file:
        ip, *hostnames = line.strip().split()

        if ip in result:
            result[ip] += hostnames
        else:
            result[ip] = hostnames
