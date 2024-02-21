# This code sample uses the 'requests' library:
# http://docs.python-requests.org
import requests
from requests.auth import HTTPBasicAuth
import json

url = "https://gargi12323.atlassian.net//rest/api/3/project"
API_TOKEN = "ATATT3xFfGF0OGIwc6eTwYEn5QOuhooTNBCgu07fiR1w2tqA4KJdW4JWr-g1P_4WdBdLk0u1vA8LB3DSfZ1NJre9UXTEoxABq7Rat100UVVZ47QnDNB_-0fprMGHa_qYM50wxeUqWBukq1lbvCpBwe1ZmnTNeWQqTnsKk1wEoCwxoElnYM_VKtE=8F7D404B"
auth = HTTPBasicAuth("gargi.123.23.com", API_TOKEN)

headers = {
  "Accept": "application/json"
}

response = requests.request(
   "GET",
   url,
   headers=headers,
   auth=auth
)

output = json.loads(response.text)
name = output[0]["name"]
print(name)