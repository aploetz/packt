CREATE KEYSPACE packt WITH replication = {'class': 'NetworkTopologyStrategy', 'dc1': '1'}  AND durable_writes = true;

CREATE TABLE packt.logins_by_user (
    user_id text,
    login_datetime timestamp,
    origin_ip text,
    PRIMARY KEY (user_id, login_datetime)
) WITH CLUSTERING ORDER BY (login_datetime DESC);

INSERT INTO logins_by_user (user_id, login_datetime, origin_ip) VALUES ('aploetz','2017-06-01 12:36:01','192.168.0.101');
INSERT INTO logins_by_user (user_id, login_datetime, origin_ip) VALUES ('aploetz','2017-06-01 12:53:28','192.168.0.101');
INSERT INTO logins_by_user (user_id, login_datetime, origin_ip) VALUES ('aploetz','2017-06-02 13:23:11','192.168.0.105');
INSERT INTO logins_by_user (user_id, login_datetime, origin_ip) VALUES ('aploetz','2017-06-03 09:04:55','192.168.0.101');

CREATE TABLE packt.astronauts (
name text,
year int,
group int,
status text,
dob text,
birthplace text,
gender text,
alma_mater text,
spaceflights int,
spaceflight_hours int,
spacewalks int,
spacewalk_hours int,
missions text,
PRIMARY KEY (name));

CREATE TABLE packt.astronauts_by_group (
name text,
year int,
group int,
status text,
dob text,
birthplace text,
gender text,
alma_mater text,
spaceflights int,
spaceflight_hours int,
spacewalks int,
spacewalk_hours int,
missions text,
PRIMARY KEY (group,name))
WITH CLUSTERING ORDER BY (name asc);

COPY packt.astronauts (name,year,group,status,dob,birthplace,gender,alma_mater,spaceflights,spaceflight_hours,spacewalks,spacewalk_hours,missions) FROM '~/Documents/Packt/astronauts.csv' WITH HEADER=true;

COPY packt.astronauts_by_group (name,year,group,status,dob,birthplace,gender,alma_mater,spaceflights,spaceflight_hours,spacewalks,spacewalk_hours,missions) FROM '~/Documents/Packt/astronauts.csv' WITH HEADER=true;

