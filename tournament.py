#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    db = connect()
    c = db.cursor()

    c.execute("DELETE FROM matches")

    db.commit()
    db.close()


def deletePlayers():
    """Remove all the player records from the database."""
    db = connect()
    c = db.cursor()

    c.execute("DELETE FROM players")

    db.commit()
    db.close()


def countPlayers():
    """Return the number of players currently registered."""
    db = connect()
    c = db.cursor()

    c.execute("SELECT count(*) FROM players")
    count = c.fetchone()[0]

    db.close()

    return count


def registerPlayer(name):
    """Add a player to the tournament database.
    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)
    #### UPDATE ####
    Args:
      name: the player's full name (need not be unique).
    """
    db = connect()
    c = db.cursor()

    c.execute("INSERT INTO players (name) VALUES (%s)", (name, ))

    c.execute("SELECT id FROM players ORDER BY id DESC")
    latest_id = c.fetchone()
    c.execute("INSERT INTO matches VALUES (%s, 0, 0)", (latest_id, ))

    db.commit()
    db.close()


def playerStandings():
    """Return a list of the players and their win records, sorted by wins.
    The first entry in the list should be the player in first place, or a
    player tied for first place if there is currently a tie.
    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    db = connect()
    c = db.cursor()

    c.execute("SELECT * FROM standings")
    stand = c.fetchall()

    db.close()

    return stand


def reportMatch(winner, loser):
    """Record the outcome of a single match between two players.
    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """
    db = connect()
    c = db.cursor()

    c.execute("UPDATE matches SET matches = matches + 1 WHERE player_id = %s OR player_id = %s", (winner, loser, ))
    c.execute("UPDATE matches SET wins = wins + 1 WHERE player_id = %s", (winner, ))

    db.commit()
    db.close()


def swissPairings():
    """Return a list of pairs of players for the next round of a match.
    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.
    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    db = connect()
    c = db.cursor()

    c.execute("SELECT id, name FROM standings")
    player_list = c.fetchall()

    db.close()

    plist = []
    while player_list:
        plist.append(player_list[0]+player_list[1])
        del player_list[0:2]

    return plist
