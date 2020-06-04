import requests, time
from bs4 import BeautifulSoup
'''
Example JSON response of trail status
{
  "data":[
    {
      "trail":"Beaver Dam",
      "status":"open",
      "last_updated":"05/30 9:03am"
    },
    {
      "trail":"Briar Chapel",
      "status":"closed",
      "last_updated":"05/31 10:34am"
    },
    {
      "trail":"Brumley Forest",
      "status":"closed",
      "last_updated":"05/29 4:52pm"
    }
  ]
}
'''


class Trail:

    def __init__(self, trail):
        self.trail = trail
        self.name = None
    
    def getNameAndDate(self):
        nameAndDate = self.trail.find_all('td', class_ = 'trail')
        for value in nameAndDate: 
            trailName = value.find('a').text if value.find('a') else None 
            if trailName:
                self.name = trailName.encode('ascii', errors='ignore').decode().strip()
            else:
                self.date = value.text

    def getStatus(self):
        trailOpen = self.trail.find('td', class_ = 'open')
        trailPartiallyOpen = self.trail.find('td', class_='info')
        if trailOpen or trailPartiallyOpen:
            self.status = 'open'
        else:
            self.status = 'closed'

def main():
    response = requests.get('https://www.trianglemtb.com/mobiletrailstatus.php')

    soup = BeautifulSoup(response.content, 'html.parser')

    trails = soup.find_all('tr')

    allTrailData = []
    for trail in trails:
        trailData = {}
        currentTrail = Trail(trail)
        currentTrail.getNameAndDate()
        currentTrail.getStatus()
        if currentTrail.name:
            trailData['trail'] = currentTrail.name
            trailData['status'] = currentTrail.status
            trailData['last_updated'] = currentTrail.date
            allTrailData.append(trailData)
        else:
            next
    metadata = {}
    metadata['query_time'] = time.ctime()
    metadata['status_code'] = response.status_code
    result = {
            'metadata': metadata,
            'data':allTrailData
            }
    return result
