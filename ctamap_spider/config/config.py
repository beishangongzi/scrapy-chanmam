import pathlib

BASEURL = "https://restapi.amap.com/"

BASEDIR = pathlib.Path(__file__).parent.parent.resolve()

CONFIGFILE = pathlib.Path(__file__).parent.resolve()

DATAFILE = BASEDIR / "dataFile"

# about cookie
COOKIEFILE = CONFIGFILE / "cookie.txt"

# about request header
HEADER = CONFIGFILE / "header.txt"

# about regin
REGIONCODE = CONFIGFILE / "regionCode.json"
