-- football_viz_ddl.sql
--
--	PURPOSE: create a database to store data from api.football-data.org
--
-- 	AUTHOR(S)
--		Sanjay Advani (SA)
--
--	NOTES:
--		1) need to be able to store year, teams, leagues match ups, home team, away team, fixtures and score
--              2) Points should be derivable
--			
--
--	HISTORY
--=====================================================================
--	2017-08-22: Created. SA
--=====================================================================
-- drop database if exists football_viz;
-- create database football_viz;

drop table if exists fixtures;
drop table if exists league;
drop table if exists league;
drop table if exists teams;
drop table if exists season;

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
     name character varying (64) not null,
     short_name character varying (24) not null
     )
;

create table season
(
 id serial primary key,
 season character varying (16)
 )
;

create table league_team
    (
     id serial primary key,
     league_id integer not null,
     team_id integer not null,
     season_id integer not null,
     constraint fk_lt_leag foreign key (league_id) references league (id),
     constraint fk_lt_team foreign key (team_id) references teams (id),
     constraint fk_lt_seas foreign key (season_id) references season (id)
     )
;

create table fixtures
    (
     id serial primary key,
     home_team_id integer not null,
     away_team_id integer not null,
     scheduled_date date,
     home_team_score integer,
     away_team_score integer,
     constraint fk_fx_ht foreign key (home_team_id) references teams (id),
     constraint fk_fx_at foreign key (away_team_id) references teams (id)
    )
;
     
    


