from pyspark import SparkContext

sc = SparkContext("local[*]","BroadcastDemo")

country_lookup = {
    "US":"United States",
    "UK":"United Kingdom",
    "DE":"Germany",
    "FR":"France",
    "JP":"Japan"
}

#First we'll do this without a broadcast variable

#Some country codes in an RDD - but just the abbreviated codes
data_rdd = sc.parallelize(["US", "UK", "DE", "FR", "JP"])

#create a method to lookup country codes - no broadcast
def lookup_country(code):
    return country_lookup.get(code, "Unknown")

#For every single record we run through in this RDD
#the node (or nodes) have to have a copy of the lookup dictionary
# sent to them over the network. Every. Single. Time.
#If the data rdd is 100,000 records, that's 100,000 transfers
#of the same lookup dictionary for no reason.

#With a broadcast variable
#Useing a broadcast variable, we let the Driver node know to send this data
#to every executor once. And then instruct the executro to cache it locally
#until it's done with the transformation

#Let's create  a broadcast variable for our country lookup
bc_country_lookup = sc.broadcast(country_lookup)

def country_lookup_broadcast(code):
    #Now we can access the broadcast variable's value on the executors
    return bc_country_lookup.value.get(code, "Unknown")

results = data_rdd.map(country_lookup_broadcast).collect()

print(results)

#We want to get in the habit of cleaning up our broadcast variables when we're done with them
#Otherwise the executors will keep these cached on the worker node's memory

bc_country_lookup.destroy()
