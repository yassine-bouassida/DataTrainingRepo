from pyspark import SparkContext
from pyspark.accumulators import AccumulatorParam

sc = SparkContext("local[*]", "AccumulatorDemo")

# Lets create some accumulators
# We will hve some intentionally bad data , and we want a count
# Of both total records processed, and how many of those are invalid

#They are created like other python pyspark objects
total_records = sc.accumulator(0)
error_count = sc.accumulator(0)

#Sample data with bad records
data = [
    "valid",
    "valid",
    "bad",
    "invalid",
    "valid",
]

rdd = sc.parallelize(data) # turn the data into an rdd

#We want to be able to to give a map some more custom logic
#All a map does is apply a fcuntion to everything in a collection (rdd)

#Since this function will be passed into a map
#And map runs on worker nodes (inside an executor)
#... we can't create Accumulators within the process_record()
#When working in PySpark we need to be mindful not just of python scripting
#But driver vs Worker Scoping

def process_record(record):
    #Whether a record is good or bad, we tried. So we increment
    #total_records by 1
    total_records.add(1)

    if(record!="valid"):
        #If the record is bad, we increment the error count by 1
        error_count.add(1)
        #If the record isn't valid, we simply return None
        return None
    
    return record #If the record is valid, we return it as is

#Now that we wrote our filtering function we can use it in a transformation

#when doing transformations , we can chain them
#each transformation runs sequentially
#we run process_record() for EVERY record in our initial RDD

results = rdd.map(process_record).filter(lambda x: x is not None)

#Now we trigger the computation with an action
print("Valid records:", results.collect())

print(total_records.value) # Output: 5
print(error_count.value) # Output: 2

#Custom Accumulator Example

#To use a custom accumulator, we need to define a class that extends AccumulatorParam
class myStringAccumulatorParam(AccumulatorParam):
    def zero(self, value):
        #This method defines the initial value of the accumulator
        return set() #return an empty set as the initial value

    def addInPlace(self, acc1, acc2):
        #logic to add a value from a worker task to the accumulator's current value
        acc1.update(acc2)
        return acc1
    
unique_words_accumulator = sc.accumulator(set(), myStringAccumulatorParam()) #initial value, and what kind of accumulator
def collect_words(word):
    unique_words_accumulator.add({word})
    return word

words_rdd = sc.parallelize(["hello", "world", "hello", "spark"])
words_rdd.map(collect_words).collect()
print("Unique words:", unique_words_accumulator.value)

