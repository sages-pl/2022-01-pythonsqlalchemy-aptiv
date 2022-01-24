
def function(data):
    result = []
    for line in data.splitlines():
        username, _, uid, *_ = line.split(':')
        if int(uid) < 1000:
            result.append(username)
    return result


def generator(data):
    for line in data.splitlines():
        username, _, uid, *_ = line.split(':')
        if int(uid) < 1000:
            yield username


# def comprehension(data: str):
#     return [username
#             for row in data.splitlines()
#             if (values := row.strip().split(':'))
#             and (username := values[0])
#             and (uid := values[2])
#             and int(uid) < 1000]
