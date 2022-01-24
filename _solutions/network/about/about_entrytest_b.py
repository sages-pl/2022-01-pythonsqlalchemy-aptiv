
result = []

for line in DATA.splitlines():
    line = line.strip()

    if len(line) == 0:
        continue
    elif line.startswith('#'):
        continue

    ip, *hosts = line.split()

    for row in result:
        if row['ip'] == ip:
            row['hosts'] += hosts
            break
    else:
        result.append({
            'ip': ip,
            'hosts': hosts,
            'protocol': 'ipv4' if '.' in ip else 'ipv6'
        })
