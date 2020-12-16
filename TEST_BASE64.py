import urllib2
import urllib
import json
import base64
import wave


def encode_wav(path):
    file = wave.open(path, 'rb')
    params = base64.b64encode(str(file.getparams()))
    print(params)
    data = base64.b64encode(file.readframes(file.getnframes()))

    return data, params


def send_request(speech_data, params):
    url = "http://172.17.0.1:3211/wav"
    json_data = {
        "wav": speech_data,
        "param": params,
    }

    method = "POST"
    handler = urllib2.HTTPHandler()
    opener = urllib2.build_opener(handler)
    data = urllib.urlencode(json_data)
    request = urllib2.Request(url, data=data)

    request.get_method = lambda: method
    try:
        connection = opener.open(request)
    except urllib2.HTTPError, e:
        connection = e

    # check. Substitute with appropriate HTTP code.
    if connection.code == 200:
        response = connection.read()
    else:
        pass
    # handle the error case. connection.read() will still contain data
    # if any was returned, but it probably won't be of any use

    return response


d, p = encode_wav("test.wav")
print(send_request(d,p))
