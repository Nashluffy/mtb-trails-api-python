# trailsAPI
Scrapes the local mountain bike trail status page https://www.trianglemtb.com/mobiletrailstatus.php into JSON

Try it out yourself! 

On Linux and Mac, `curl https://api.nashluffman.com/trails` 
On Windows, switch to linux-based OS

Example response
'''json
{
  "metadata": {
    "query_time": "Sun Jun  7 02:57:44 2020",
    "status_code": 200
  },
  "data": [
    {
      "trail": "Beaver Dam",
      "status": "open",
      "last_updated": "06/06 8:15 am"
    },
    {
      "trail": "Briar Chapel",
      "status": "open",
      "last_updated": "05/31 4:56 pm"
    },
    {
      "trail": "Skills Area",
      "status": "open",
      "last_updated": "06/04 11:06 am"
    },
    {
      "trail": "Herndon Loop",
      "status": "open",
      "last_updated": "06/04 11:06 am"
    },
    {
      "trail": "Brumley Forest",
      "status": "open",
      "last_updated": "06/01 10:04 am"
    },
    {
      "trail": "CNF (airport)",
      "status": "open",
      "last_updated": "06/01 11:01 am"
    },
    {
      "trail": "CNF (school)",
      "status": "open",
      "last_updated": "06/01 11:01 am"
    },
    {
      "trail": "Crabtree",
      "status": "open",
      "last_updated": "06/02 3:06 pm"
    },
    {
      "trail": "Forest Ridge",
      "status": "open",
      "last_updated": "06/06 3:45 pm"
    },
    {
      "trail": "Harris",
      "status": "open",
      "last_updated": "06/05 1:10 pm"
    },
    {
      "trail": "Legend (Lower)",
      "status": "closed",
      "last_updated": "02/15 5:56 pm"
    },
    {
      "trail": "Legend (Upper)",
      "status": "open",
      "last_updated": "05/31 2:51 pm"
    },
    {
      "trail": "Little River",
      "status": "open",
      "last_updated": "06/06 9:43 am"
    },
    {
      "trail": "New Light",
      "status": "open",
      "last_updated": "05/23 1:45 pm"
    },
    {
      "trail": "RTP Trails",
      "status": "open",
      "last_updated": "06/02 9:19 am"
    },
    {
      "trail": "San Lee Gravity Park",
      "status": "open",
      "last_updated": "06/05 3:33 pm"
    },
    {
      "trail": "San Lee Singletrack",
      "status": "open",
      "last_updated": "06/05 3:33 pm"
    },
    {
      "trail": "Wendell Falls",
      "status": "open",
      "last_updated": "05/09 8:37 am"
    }
  ]
}
'''
