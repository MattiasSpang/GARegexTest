import csvHandler
import regex
import time
start_time = time.time()


csvFile = csvHandler.readCsvFile("5000csv.csv")

finishedDict =  {
    "header"    : ["repoName", "hasGA"],
    "rows"      : []
}

i = 1

print("Begin fetching repo data...")
for line in csvFile["rows"]:
    #print(i,": getting data for repo: ", line[0])
    answer = regex.checkRepo(("https://www.github.com/" + line[0]))

    row = [line[0], answer]

    finishedDict["rows"].append(row)

    if i%10 == 0:
        print(i," repos done")
        print("--- %s seconds ---" % (time.time() - start_time))
    i+= 1

csvHandler.createCsvFile(finishedDict, "HasGACsv.csv")

print("Done creating csv file!")
