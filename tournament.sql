  -- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;
\c tournament;

-- Create a table of just the players, mapping their names to a unique id

CREATE TABLE players (
    id serial,
    name text,
    PRIMARY KEY(id)
);

CREATE TABLE matches (
    player_id integer,
    wins integer,
    matches integer
);


-- View is created to help fetching records in player_standings method.

CREATE VIEW standings AS 
    SELECT players.id, players.name, matches.wins, matches.matches from players, matches 
    WHERE players.id = matches.player_id ORDER BY matches.matches, matches.wins DESC;
