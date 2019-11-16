from bsddb3 import db
from sys import stdin
import argparse

def init_idx(db_type, prefix): #db.DB_HASH or db.DB_BTREE
    database = db.DB()
    DB_File = "{}.idx".format(prefix)
    database.open(DB_File, None, db_type, db.DB_CREATE)

    for line in stdin:
        k,v = line.split(":")
        database.put(k.encode("utf8"),v)

if __name__ == '__main__':
    typeMapper = {"btree":db.DB_BTREE, "hash":db.DB_HASH}

    parser = argparse.ArgumentParser()
    parser.add_argument("--prefix", type = str, required = True, choices=["terms", "emails", "dates","recs"])
    parser.add_argument("--db_type", type = str, required = True, choices=typeMapper.keys())
    args = parser.parse_args()
    init_idx(typeMapper[args.db_type], args.prefix)
