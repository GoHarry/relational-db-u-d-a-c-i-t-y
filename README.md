# Swiss Tournament schema and python api
## Description
This is a project submission for the Udacity full stack web dev nanodegree.  Project 2: Swiss Tournament database schema and python api.

##Steps to run
###Launch the Vagrant VM

vagrant up

vagrant ssh

###Create the database and create the tables:

vagrant=>cd /vagrant/tournament

psql

CREATE DATABASE tournament;

\c tournament

\i tournament.sql

\q

###Run the test application to check that everything is fine:

cd /vagrant/tournament

python tournament_test.py

##The expected result should be:

cd /vagrant/tournament
vagrant@vagrant-ubuntu-trusty-32:/vagrant/tournament$ python tournament_test.py 
1. Old matches can be deleted.

2. Player records can be deleted.

3. After deleting, countPlayers() returns zero.

4. After registering a player, countPlayers() returns 1.

5. Players can be registered and deleted.

6. Newly registered players appear in the standings with no matches.

7. After a match, players have updated standings.

8. After one match, players with one win are paired.

Success!  All tests pass!