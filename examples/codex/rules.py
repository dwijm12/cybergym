from mitmproxy import http

#allow connecting to codex and also intalling packages
whitelist = ['openai', 'chatgpt', 'codex', 'debian', 'pypi', 'python', 'npm', 'yarn', 'node']

def request(flow):
    if not any(x in flow.request.pretty_url for x in whitelist):
        flow.response = http.Response.make(404, "You are not permitted to search the Internet.")
    else:
        print(flow.request.pretty_url)
