class Quote:

    TABLE_NAME = 'quotes'
    
    def __init__(self, author_id, creator_id, quote, creation, db_client):
        self.author_id = author_id
        self.creator_id = creator_id
        self.quote = quote
        self.db_client = db_client
        self.creation = creation

    def to_json(self):
        return {
            'author_id': self.author_id,
            'creator_id': self.creator_id,
            'quote': self.quote,
            'creation': self.creation
        }

    def load_quote(self, quote):
        quote = [q for q in quote]
        quote = quote[0]
        
        self.quote = quote["quote"]
        self.author_id = quote["author_id"]
        self.creator_id = quote["creator_id"]
        self.creation = quote["creation"]

    def save(self):
        self.db_client.insert(self.TABLE_NAME, self.to_json())

