import requests
import datetime
import hashlib
import hmac
import base64
import json

GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'

def getSimpleSign(source, SecretId, SecretKey) :
    dateTime = datetime.datetime.utcnow().strftime(GMT_FORMAT)
    auth = "hmac id=\"" + SecretId + "\", algorithm=\"hmac-sha1\", headers=\"date source\", signature=\""
    signStr = "date: " + dateTime + "\n" + "source: " + source
    sign = hmac.new(bytes(SecretKey,'utf-8'), bytes(signStr,'utf-8'), hashlib.sha1).digest()
    sign = base64.b64encode(sign)
    # sign = base64.b64encode(bytes(json.dumps(sign).encode('utf-8')))
    sign = auth + sign.decode() + "\""
    return sign, dateTime