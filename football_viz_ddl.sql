-- football_viz_ddl.sql
--
--	PURPOSE: create a database to store data from api.football-data.org
--
-- 	AUTHOR(S)
--		Sanjay Advani (SA)
--
--	NOTES:
--		1) need to be able to store year, teams, leagues match up
--			
--
--	HISTORY
--=====================================================================
--	2017-08-22: Created. SA
--=====================================================================
create database football_viz;

create table league 
    (
     id serial primary key,
     name character varying (255) not null,
     country character varying (60),
     tier integer
    )
;

create table teams
    (
     id serial primary key,
     
    


