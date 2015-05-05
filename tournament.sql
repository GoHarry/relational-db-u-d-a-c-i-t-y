-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.

-- Create the table that will hold all players.
CREATE TABLE players (
	id SERIAL PRIMARY KEY,
	p_name TEXT NOT NULL
);

-- Create the table that will hold all match results.
-- Each match will have 2 results.  One for the loser and one for the winner.
CREATE TABLE results (
	id integer REFERENCES players (id),
	opponent integer REFERENCES players (id),  
	result boolean NOT NULL,
	PRIMARY KEY (id, opponent)
);

-- Create a view that will be used to return player rankings.
CREATE VIEW standings as
	SELECT players.id, players.p_name,
		Count(nullif(results.result, false)) AS wins,
        Count(results.id) AS matches
    FROM players LEFT JOIN results ON players.id = results.id
    GROUP BY players.id ORDER BY wins desc;

