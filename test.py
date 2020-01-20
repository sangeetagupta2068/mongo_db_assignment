#!usr/bin/python3

import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
mydb = myclient["mydatabase"]
mycol = mydb["book"]

book_name = input("Enter book name: ")
mydoc = mycol.find({"book_name" : book_name})
for book_item in mydoc:
    print(book_item)

book_id = int(input("Enter book_id of book to be deleted"))

mycol.delete_one({ "address" : book_id })
