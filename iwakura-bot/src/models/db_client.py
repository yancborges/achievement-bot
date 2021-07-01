class DbClient:

    def __init__(self, client, db, environment):
        self.__mongo = client[db]
        self.environment = environment

    def insert(self, table, document):
        return self.__mongo[self.get_table(table)].insert(document)
    
    def get(self, table, query):
        return [doc for doc in self.__mongo[self.get_table(table)].find(query)]

    def update(self, table, match, query, upsert=False):
        return self.__mongo[self.get_table(table)].update(match, query, upsert=upsert)

    def delete(self, table, match):
        return self.__mongo[self.get_table(table)].delete_one(match)

    def get_table(self, table):
        return table + '-' + self.environment

    