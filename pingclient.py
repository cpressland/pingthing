import requests

from settings import pingproxy_url, results

while True:
    try:
        r = requests.get(pingproxy_url)
        r.raise_for_status()
    except Exception as e:
        print(e)
        results["loses"] += 1
    else:
        results["wins"] += 1
    print(results)
