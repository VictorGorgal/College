from database import Database
from player_database import PlayerDatabase
from match_database import MatchDatabase

db = Database("neo4j+s://xyz.databases.neo4j.io", "neo4j", "xyz")

player_db = PlayerDatabase(db)
match_db = MatchDatabase(db)

player_db.create_player("1", "João")
player_db.create_player("2", "Maria")

player_db.update_player("1", "João Silva")

players = player_db.list_players()
print("Lista de Jogadores:")
for player in players:
    print(player)

match_db.create_match("match_1", ["1", "2"], "João venceu")

match_info = match_db.get_match("match_1")
print("\nInformações da Partida:")
print(match_info)

history = player_db.get_match_history("1")
print("\nHistórico de partidas de João:")
for match in history:
    print(match)

db.close()
