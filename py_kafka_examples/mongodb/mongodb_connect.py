from pymongo import MongoClient

def get_db():

    # the standard URI connection scheme
    # mongodb: // [username: password @]host1[:port1][, host2[:port2], ...[, hostN[:portN]]][ / [database][?options]]

    client = MongoClient("mongodb://localhost:27017")
    return client