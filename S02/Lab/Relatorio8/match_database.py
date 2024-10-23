class MatchDatabase:
    def __init__(self, database):
        self.db = database

    def create_match(self, match_id, player_ids, result):
        query = """
        CREATE (m:Match {id: $match_id, result: $result})
        WITH m
        UNWIND $player_ids AS player_id
        MATCH (p:Player {id: player_id})
        CREATE (p)-[:PARTICIPATED_IN]->(m)
        """

        self.db.execute_query(query, {"match_id": match_id, "player_ids": player_ids, "result": result})

    def get_match(self, match_id):
        query = """
        MATCH (m:Match {id: $match_id})<-[:PARTICIPATED_IN]-(p:Player)
        RETURN m, collect(p) AS players
        """
        result = self.db.execute_query(query, {"match_id": match_id})
        return result[0] if result else None

    def delete_match(self, match_id):
        query = """
        MATCH (m:Match {id: $match_id})
        DETACH DELETE m
        """
        self.db.execute_query(query, {"match_id": match_id})
