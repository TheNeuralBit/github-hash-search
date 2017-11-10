import sys
import time
import requests

query = sys.argv[1]

url = "https://api.github.com/search/repositories?q={}".format(query)

sys.stderr.write("Searching for %s...\n" % query)
sys.stderr.flush()

while True:
    result = requests.get(url)


    if 'items' not in result.json():
        timeout = int(result.headers['X-RateLimit-Reset']) - time.time() + 1
        sys.stderr.write("Sleeping for %.3f seconds...\n" % timeout)
        sys.stderr.flush()
        time.sleep(timeout)
        continue

    for item in result.json()['items']:
        print(item['ssh_url'])
    if 'next' in result.links:
        url = result.links['next']['url']
    else:
        break

    #X-RateLimit-Limit: 10
    #X-RateLimit-Remaining: 9
    #X-RateLimit-Reset: 1510279322
    if int(result.headers['X-RateLimit-Remaining']) == 0:
        timeout = int(result.headers['X-RateLimit-Reset']) - time.time() + 1
        sys.stderr.write("Sleeping for %.3f seconds...\n" % timeout)
        sys.stderr.flush()
        time.sleep(timeout)
