import requests
import json
def GetMyLocation(countryCode,Token):
    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {Token}"
    }
    Locations = requests.get("https://api.clashroyale.com/v1/locations",headers=headers)
    for location in json.loads(Locations.text)["items"]:
        if location['isCountry'] and location['countryCode'] == countryCode:
            return location["id"]
    return "Location Not Found"


# x = GetMyLocation("BR","eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiIsImtpZCI6IjI4YTMxOGY3LTAwMDAtYTFlYi03ZmExLTJjNzQzM2M2Y2NhNSJ9.eyJpc3MiOiJzdXBlcmNlbGwiLCJhdWQiOiJzdXBlcmNlbGw6Z2FtZWFwaSIsImp0aSI6ImNmZjg3OTg1LTBmNjEtNGU0NS04NTYyLWE5Zjg2MzRjMThjMSIsImlhdCI6MTYyNjI5MDI0OSwic3ViIjoiZGV2ZWxvcGVyLzgxMzAyN2MxLTZjMzUtYWU4Ny04ZTg5LWUwZDYzNmFhMDNkOSIsInNjb3BlcyI6WyJyb3lhbGUiXSwibGltaXRzIjpbeyJ0aWVyIjoiZGV2ZWxvcGVyL3NpbHZlciIsInR5cGUiOiJ0aHJvdHRsaW5nIn0seyJjaWRycyI6WyIxOTEuMjIwLjEwNy4yNDQiXSwidHlwZSI6ImNsaWVudCJ9XX0.uWDCGrFHrJBV2TK6crg5z5tS9tgM6v60otrMt-P5rkVIJMuIrtY3nqta0rjDUyfhsv8VvurbrMoQTib9eucAhA")
# print(x)