"""
Read the csv data downloaded from S3 and then dump it to the database.
"""


import numpy as np
import pymongo as pm
from pymongo import MongoClient
from pprint import pprint
from bson.binary import  Binary
import pickle

TOTAL_SAMPLES_IN_FIELD_DATA=198
NUMBER_OF_SAMPLES=1126
NUMBER_OF_CHANNELS=648

client=MongoClient()
db=client.data_db

data=db.data_test
data.remove()

print('reading the shot data for seq 80')

#field_data=np.loadtxt('/home/sharath/programming/python/pycharmProjects/proto-14/data/csv_for_proto-14/data.csv')
#field_labels=np.loadtxt('/home/sharath/programming/python/pycharmProjects/proto-14/data/csv_for_proto-14/labels.csv')


#field_data=field_data.reshape(TOTAL_SAMPLES_IN_FIELD_DATA,NUMBER_OF_SAMPLES,NUMBER_OF_CHANNELS)
#field_labels=field_labels.reshape(TOTAL_SAMPLES_IN_FIELD_DATA,1)

field_data=np.random.rand(10,2,3)
field_labels=np.array([np.random.randint(0,2) for x in range(10)]).reshape(10,1)

print('shape of field_data ',field_data.shape)
print('shape of field_label ',field_labels.shape)

#assert field_data.shape==(TOTAL_SAMPLES_IN_FIELD_DATA,NUMBER_OF_SAMPLES,NUMBER_OF_CHANNELS)
#assert field_labels.shape==(TOTAL_SAMPLES_IN_FIELD_DATA,1)

shots=[]

def get_random_shot(rn):
    xr=data.find({'shot_no':rn})
    traces=[]
    for c in xr:
        traces=[pickle.loads(c['trace'])]
    return np.array(traces)

def get_label_for_shot(rn):
    xr=data.find({'shot_no':rn})
    traces=[]
    for c in xr:
        traces=[pickle.loads(c['label'])]
    return traces

for i in range(field_data.shape[0]):
    shot={
        "shot_no":i,
        "trace":Binary(pickle.dumps(field_data[i],protocol=2)),
        'label':Binary(pickle.dumps(field_labels[i],protocol=2))
    }
    print("shot: ",i)
    if i==1:
        pprint(field_data[i])
    shots.append(shot)
    pprint(shot)


print("inserting into the db")
result=data.insert_many(shots)

rand_traces=get_random_shot(5)
print('returned traces of shape ',rand_traces.shape)



print('fetching from the db')
traces=get_random_shot(1)
print("result from function")
pprint(traces)