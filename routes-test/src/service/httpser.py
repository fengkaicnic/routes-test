import httplib

httpclient = None

try:
    httpclient = httplib.HTTPConnection('localhost', 9999, timeout=10)
    httpclient.request('GET', '/test')
    
    response = httpclient.getresponse()
    print response.status()
    print response.reason
    print response.read()

except Exception, e:
    print e
    
finally:
    if httpclient:
        httpclient.close()