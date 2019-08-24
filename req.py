logout_url = "https://auth.geeksforgeeks.org/logout.php"
login_url = "https://auth.geeksforgeeks.org/auth.php"

import requests

session = requests.Session()
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36', "host": "auth.geeksforgeeks.org"}
resp = session.post(login_url, data={
                                      "reqType":"Login",
                                      "user":"EMAIL",
                                      "pass":"PASSWORD",
                                      "rem":False,
                                      "to": "https%3A%2F%2Fauth.geeksforgeeks.org%2F%3Fto%3Dhttps%253A%252F%252Fpractice.geeksforgeeks.org%252Ftransactions",
                                      "rem":"on",
                                      "g-recaptcha-response":""
                                }, headers=headers)

def logout():
  resp = session.get(logout_url)
  return resp.status_code == 200


url = "https://s3.ap-south-1.amazonaws.com/videoin.gfg.org/courses/7d8358e7e9f29b15140f094721e55e55gfg-arrayscorrected.m3u8"

headers = {
  "Origin":"https://practice.geeksforgeeks.org",
  "Referer":"https://practice.geeksforgeeks.org/tracks/SPC-Arrays/?batchId=140",
  "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36"
}

resp = session.get(url, headers=headers)
print(resp.text)

#logout()
