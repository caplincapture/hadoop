# pre-process csv for map reduce when lines are considered as new rows

csvFile = open('forum_node2.tsv','wb')
with open('forum_node.tsv','rb') as tsvin:
	tsvin = csv.reader(tsvin, delimiter='\t')
	csvout = csv.writer(csvFile, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)
	for row in tsvin:
	    row[4] = row[4].replace("\n", " ").replace("\r"," ")
	    csvout.writerow(row)
csvFile.close()