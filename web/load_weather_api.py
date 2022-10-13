import http.client
import json

if __name__ == '__main__':
    conn = http.client.HTTPSConnection("api.openweathermap.org")
    payload = ''
    headers = {}
    conn.request("GET", "/data/2.5/forecast?q=Tashkent&appid=674e6f32954b4d369068e0edbf6137a4&units=metric", payload,
                 headers)
    res = conn.getresponse()
    data = res.read()
    print(data.decode("utf-8"))
    json.dumps(data.decode("utf-8"))
    print(data)
