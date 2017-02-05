DROP TABLE IF EXISTS users;
CREATE TABLE users (
  id integer primary key autoincrement,
  name string not null,
  email string not null
);
