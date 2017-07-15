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
