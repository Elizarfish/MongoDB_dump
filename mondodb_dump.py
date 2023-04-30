import argparse
from pymongo import MongoClient

def main():
    parser = argparse.ArgumentParser(description="MongoDB Information Viewer")
    parser.add_argument("-host", default="localhost", help="MongoDB server hostname (default: localhost)")
    parser.add_argument("-port", type=int, default=27017, help="MongoDB server port (default: 27017)")
    parser.add_argument("-db", help="Database name")
    parser.add_argument("-collection", help="Collection name")

    args = parser.parse_args()

    client = MongoClient(args.host, args.port)

    if not args.db:
        print_databases(client)
    else:
        db = client[args.db]
        if not args.collection:
            print_collections(db)
        else:
            print_documents(db[args.collection])

def print_databases(client):
    databases = client.list_database_names()
    print("Databases:")
    for db_name in databases:
        print(f" - {db_name}")

def print_collections(db):
    collections = db.list_collection_names()
    print(f"Collections in database '{db.name}':")
    for collection_name in collections:
        print(f" - {collection_name}")

def print_documents(collection):
    documents = collection.find()
    print(f"Documents in collection '{collection.name}':")
    for document in documents:
        print(document)

if __name__ == "__main__":
    main()
