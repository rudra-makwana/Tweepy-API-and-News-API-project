from pyspark import SparkContext, SparkConf
import operator

sc = SparkContext("local","frequencyCount")

f= open("output.txt","w+")

data = sc.textFile('data.txt').flatMap(lambda line: line.split(" ")).map(lambda word: (word, 1))
countWords = data.reduceByKey(operator.add)

for word,count in countWords.toLocalIterator():
    if(word == "canada" or word == "university" or word == "education" or
        word =="dalhousie" or word =="expensive" or word =="good school" or word =="good schools" 
        or word =="bad schools" or word =="bad schools" or word == "poor school" or word == "poor schools"
        or word == "faculty" or word == "computer science" or word == "graduate"):
            f.write(u"{} --> {}".format(word, count) + "\n")
            
f.close()
sc.stop()