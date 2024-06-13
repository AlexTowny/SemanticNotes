db = db.getSiblingDB('storage');

db.createCollection('notes');

db.createUser({
    user: 'user',
    pwd: 'semantic',
    roles: [{ role: 'readWrite', db: 'storage' }]
  });