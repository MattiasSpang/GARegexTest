import re
import urllib.request as request
import urllib.error as urlerror
from urllib.error import URLError, HTTPError

def checkRepo(url: str) -> str:

    try:
        webURL = request.urlopen(url)
    except:
        return "could not open URL"
    else:

        #print("result for opening repository code: " + str(webURL.getcode()))

        data = webURL.read()

        #webData = open("web-data.txt", "w+")

        #webData.truncate()

        #webData.write(str(data))


        x = re.findall('data-menu-button>(.*?)<\/span>', str(data))

        if len(x) <= 0:
            print("len <= 0")
            return "Does not exist"


        #print("Result of regex: ", x)
        #print("------------------------------------", url+'/tree/'+x[0]+'/.github/workflows')
        try:
            webGAURL = request.urlopen(url+'/tree/'+x[0]+'/.github/workflows')
        except:
            return "No" # does not have GA

        return "Yes"
        #print("result for GITHUB ACTIONs CHECK code: " + str(webGAURL.getcode()))
