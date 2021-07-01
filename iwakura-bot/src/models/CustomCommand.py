from .Exceptions import AlreadyInUse, NotFoundCommand

class CustomCommand:

    TABLE_NAME = 'commands'

    def __init__(self, name, text, creator_id, db_client):
        self.name = name
        self.text = text
        self.creator_id = creator_id
        self.db_client = db_client

    def to_json(self):
        return {
            'name': self.name,
            'text': self.text,
            'creator_id': self.creator_id
        }

    def save(self):
        resp = self.db_client.get(self.TABLE_NAME, {'name': self.name})
        if resp:
            raise AlreadyInUse('Error, Command name already in use')
        self.db_client.insert(self.TABLE_NAME, self.to_json())

    def delete(self):
        response = self.db_client.delete(self.TABLE_NAME, {'name': self.name, 'creator_id': self.creator_id})
        try:
            if not response or response.deleted_count < 1:
                raise NotFoundCommand('Command not found with matching name and creator')
        except AttributeError:
            raise NotFoundCommand('Command not found with matching name and creator')
