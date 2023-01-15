import re
import urllib.request as request

def checkRepo(repoDict: dict):

    webURL = request.urlopen(url)

    print("result for opening repository code: " + str(webURL.getcode()))

    data = webURL.read()

    webData = open("web-data.txt", "w+")

    webData.truncate()

    webData.write(str(data))

    x = re.findall('data-menu-button>(\w+)</span>', str(data))

    print("Result of regex: ", x)

    webGAURL = request.urlopen(url+'tree/'+x[0]+'/.github/workflows')

    print("result for GITHUB ACTIONs CHECK code: " + str(webGAURL.getcode()))