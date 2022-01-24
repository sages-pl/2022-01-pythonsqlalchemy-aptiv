
result = []

with open(FILE) as file:
    for line in file:
        line = line.strip()

        if len(line) == 0:
            continue
        if line.startswith('#'):
            continue

        ip, *hostnames = line.split()
        found = False

        for host in result:
            if host['ip'] == ip:
                host['hostnames'] += hostnames
                found = True
                break

        if not found:
            result.append({
                'ip': ip,
                'hostnames': list(hostnames),
                'protocol': 'IPv4' if '.' in ip else 'IPv6'
            })

## Alternative solution
# for record in result:
#     if record['ip'] == ip:
#         record['hostnames'].update(hostnames)
#         break
# else:
#     result.append({
#         'hostnames': set(hostnames),
#         'protocol': 'IPv4' if '.' in ip else 'IPv6',
#         'ip': ip,
#     })
