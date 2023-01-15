import re
import urllib.request as request

def checkRepo(url: str) -> str:

    try:
        webURL = request.urlopen(url)
    except:
        return "Repo does not excist"

    #print("result for opening repository code: " + str(webURL.getcode()))

    data = webURL.read()

    #webData = open("web-data.txt", "w+")

    #webData.truncate()

    #webData.write(str(data))

    x = re.findall('data-menu-button>(.*?)<\/span>', str(data))


    #print("Result of regex: ", x)
    #print("------------------------------------", url+'/tree/'+x[0]+'/.github/workflows')
    try:
        webGAURL = request.urlopen(url+'/tree/'+x[0]+'/.github/workflows')
    except OSError as err:
        return "No"

    #print("result for GITHUB ACTIONs CHECK code: " + str(webGAURL.getcode()))

    if(str(webGAURL.getcode()) == "200"):
        print("code was ", str(webGAURL.getcode()))
        return "Yes"
    elif(str(webGAURL.getcode()) == "404"):
        print("code was ", str(webGAURL.getcode()))
        return "No"
    else: 
        return "Undefined"