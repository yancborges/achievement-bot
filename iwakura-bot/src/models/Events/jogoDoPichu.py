from datetime import datetime, timedelta

class JogoDoPichu:

    def __init__(self, db_client, discord_client):
        self.db_client = db_client


    def load_active_game(self):
        event = self.db_client.get('pichu', {'active': True})
        amount_bet = 0
        if event:
            bets = self.db_client.get('bets', {'event': event[0]['_id']})
            if bets:
                for b in bets:
                    amount_bet += b['amount']
                event[0]['total_bet'] = amount_bet
            return event[0]
        return None


    def start_event(self):
        event = {
            'started': datetime.today().utcnow().strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'active': True,
            'planned_end_date': (datetime.today().utcnow() + timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%S.%fZ'),
            'finished': None,
            'pokemons': []
        }

        self.db_client.insert('pichu', event)


    def generate_result():
        return


    def __make_bet(self, user_id, amount):
        event = self.load_active_game()
        bet = {
            'user_id': user_id,
            'amount': amount,
            'event': event['_id']

        }
        self.db_client.insert('bets', bet)


    def bet(self, user_id, amount):
        user = self.db_client.get('money', {'user_id': user_id})
        status = ''
        if not user:
            user = {
                'user_id': user_id,
                'coins': 50
            }
            new_coins = 'free'
        else:
            user = user[0]
            new_coins = user['coins'] - amount
        if new_coins == 'free' or new_coins >= 0:
            if new_coins == 'free':
                user['coins'] = 50
            else:
                user['coins'] = new_coins
            self.db_client.update('money', {'user_id': user_id}, user, upsert=True)
            self.__make_bet(user_id, amount)
        return new_coins
        

    def finish_event():
        return