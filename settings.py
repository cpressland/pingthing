from os import getenv

results = {
    "wins": 0,
    "loses": 0,
}

pingapi_url = getenv("PINGAPI_URL", "https://api.gb.bink.com/ping")
pingproxy_url = getenv("PINGPROXY_URL", "https://ping.cpressland.io/ping")
