from replit import db

keys = db.keys()

for key in keys:
  del db[key]
