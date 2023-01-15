import csvHandler
import regex

csvFile = csvHandler.readCsvFile("5000csv.csv")

finishedDict =  {
    "header"    : ["repoName", "hasGA"],
    "rows"      : []
}

i = 0

print("Begin fetching repo data...")
for line in csvFile["rows"]:
    #print("getting data for repo: ", line[0])
    answer = regex.checkRepo(("https://www.github.com/" + line[0]))

    row = [line[0], answer]

    finishedDict["rows"].append(row)

    if i%100 == 1:
        print(i," repos done")
    i+= 1

csvHandler.createCsvFile(finishedDict, "HasGACsv.csv")

print("Done creating csv file!")
