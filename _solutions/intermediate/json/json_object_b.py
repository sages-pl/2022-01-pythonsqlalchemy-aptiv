
class User:
    def __init__(self, login, id, node_id, avatar_url, gravatar_id, url,
                 html_url, followers_url, following_url, gists_url,
                 starred_url, subscriptions_url, organizations_url,
                 repos_url, events_url, received_events_url, type,
                 site_admin):

        self.login = login
        self.id = id
        self.node_id = node_id
        self.avatar_url = avatar_url
        self.gravatar_id = gravatar_id
        self.url = url
        self.html_url = html_url
        self.followers_url = followers_url
        self.following_url = following_url
        self.gists_url = gists_url
        self.starred_url = starred_url
        self.subscriptions_url = subscriptions_url
        self.organizations_url = organizations_url
        self.repos_url = repos_url
        self.events_url = events_url
        self.received_events_url = received_events_url
        self.type = type
        self.site_admin = site_admin

    def __repr__(self):
        result = []
        for attrname, attrvalue in vars(self).items():
            if type(attrvalue) is str:
                result.append(f"{attrname}='{attrvalue}'")
            else:
                result.append(f"{attrname}={attrvalue}")
        result = ', '.join(result)
        return f"User({result})"


result = [User(**data) for data in json.loads(DATA)]

# Solution 2
from dataclasses import dataclass


@dataclass
class User:
    login: str
    id: int
    node_id: str
    avatar_url: str
    gravatar_id: str
    url: str
    html_url: str
    followers_url: str
    following_url: str
    gists_url: str
    starred_url: str
    subscriptions_url: str
    organizations_url: str
    repos_url: str
    events_url: str
    received_events_url: str
    type: str
    site_admin: bool


result = [User(**user) for user in json.loads(DATA)]
