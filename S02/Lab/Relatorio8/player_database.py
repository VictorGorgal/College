class PlayerDatabase:
    def __init__(self, database):
        self.db = database

    def create_player(self, player_id, name):
        query = "CREATE (p:Player {id: $player_id, name: $name})"
        self.db.execute_query(query, {"player_id": player_id, "name": name})

    def update_player(self, player_id, name):
        query = "MATCH (p:Player {id: $player_id}) SET p.name = $name"
        self.db.execute_query(query, {"player_id": player_id, "name": name})

    def delete_player(self, player_id):
        query = "MATCH (p:Player {id: $player_id}) DETACH DELETE p"
        self.db.execute_query(query, {"player_id": player_id})

    def get_player(self, player_id):
        query = "MATCH (p:Player {id: $player_id}) RETURN p"
        result = self.db.execute_query(query, {"player_id": player_id})
        return result[0] if result else None

    def list_players(self):
        query = "MATCH (p:Player) RETURN p"
        return self.db.execute_query(query)

    def get_match_history(self, player_id):
        query = """
        MATCH (p:Player {id: $player_id})-[:PARTICIPATED_IN]->(m:Match)
        RETURN m
        """
        return self.db.execute_query(query, {"player_id": player_id})
