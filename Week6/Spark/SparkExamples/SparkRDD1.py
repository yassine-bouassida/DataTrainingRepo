from operator import add

from pyspark.sql import SparkSession

spark:SparkSession = SparkSession.builder \
    .master("local")\
    .appName("spark_rdd_1")\
    .getOrCreate()

sc = spark.sparkContext

rdd1 = sc.parallelize(range(10))
print(rdd1.collect())


rdd2 = rdd1.map(lambda x: {x:x*10})

#now I have a dictionary
dict_list = rdd2.collect()
print(dict_list)
dict1={}
for row in dict_list:
    dict1.update(row)

print(dict1)

dict2 = {k: v for row in dict_list for k, v in row.items()}

print(dict2)

print(dict1[5])

#######################################
#Zip
a = sc.parallelize(["dog","almon"])
b= a.map(lambda x: len(x))

c=a.zip(b)

#Filter
a = sc.parallelize(range(1,10))
b=a.filter(lambda x:x%2 ==0)

b.collect()

#Group By (gives key value pairs)
a = sc.parallelize(range(1,10))
b=a.groupBy(lambda x:"even" if x%2 == 0 else "odd")
b.collect() 

#this looks a little neater but still missing the even and odd
print(list(b.collect()[0][1])) 

#instead, thank you Eric, we should use mapValues

bconverted = b.mapValues(list).collect()

print(bconverted)

##KeyBy / Join / ToDebugString
a = sc.parallelize(["hi","hello","world","are"])
#to make a key value pair just use keyBy
b = a.keyBy(lambda x: len(x))
print(b.collect())
c= sc.parallelize(["hi","hello","koi","two"])

d= c.keyBy(lambda x: len(x))

k=b.join(d)

print(k.toDebugString()) #to show lineage

##reading from a file
filename = "file:///home/will/pysparkFun2/pokemon.csv" 
a = sc.textFile(filename)
b= a.map(lambda line:line.split(" "))

#map vs flatmap
data = ["spark is fast",
        "spark is powerful",
        "spark is the best fast framework for data"]

rdd=sc.parallelize(data)
mapped = rdd.map(lambda line: line.split(" "))
print(mapped.collect())

flatmapped = rdd.flatMap(lambda line: line.split(" "))
print(flatmapped.collect())

#example wordcount
words = rdd.flatMap(lambda line: line.split(" "))
pairs = words.map(lambda word: (word,1))
print(pairs.collect())

word_counts = pairs.reduceByKey(lambda a,b:a+b)

print(word_counts.collect())

#could do the word count in one line 
print("word count in one line from above")
print(rdd.flatMap(lambda line: line.split(" ")).map(lambda word: (word,1)).reduceByKey(lambda a,b:a+b).collect())

#Actions other than just collect
a = sc.parallelize(range(1,10))
a1=a.reduce(add)
print(a.reduce(lambda a,b:a+b))

#take and take ordered ar actions
print(a1)
print(a.takeOrdered(2))
print(a.take(5))
print(a.first())

#countByKey and countByValue are actions
c = sc.parallelize([(3,6),(5,8),(5,8),(3,"Dog")])
print(c.countByKey())
print(c.countByValue())

## the following are more transformations not actions
y = sc.parallelize([(3,6),(3,8),(5,8)])

z=y.groupByKey().mapValues(list).collect()
print(z)

#flatMapValues similar to flatMap but for mapValues
z=y.groupByKey().flatMapValues(list).collect()
#TODO find a better example for flatMapValues

print(y.keys().collect())
print(y.values().collect())                                                                  
print(y.sortByKey().collect())


spark.stop()