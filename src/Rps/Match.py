from .Types.Player import Player
from typing import Dict, Any


class Match:
    def __init__(self, core):
        self.__players = {}
        self.__core = core
        self.__all_cards = [x.Tag for x in self.__core.AllCards]

    def AddPlayer(self, player_id):
        if player_id not in self.__players:
            self.__players[player_id] = {
                'point': 0,
                'played_cards': [],
                'won_from': {},
                'lost_by': {},
                'draw_with': {},
                'most_win_in_round': 0,
                'is_done': False
            }

    def IsDone(self, player_id: Any):
        if not self.__players[player_id]['is_done']:
            isDone = len(
                self.__players[player_id]['played_cards']
            ) == len(self.__all_cards)
            self.__players[player_id]['is_done'] = isDone
            return isDone
        else:
            return True

    def AvailableCards(self, player_id: Any):
        if player_id in self.__players:
            return [
                x for x in self.__all_cards
                if x not in self.__players[player_id]['played_cards']]

    def NotAvailableCards(self, player_id: Any):
        if player_id in self.__players:
            return self.__players[player_id]['played_cards']

    @property
    def PlayerStatus(self):
        return self.__players

    @property
    def PlayerIds(self):
        return [x for x in self.__players]

    def Fight(self, players_moves: Dict[Any, str]):
        in_round_status = {}
        played_already = []
        for x in players_moves:
            if x in self.__players:
                if players_moves[x] not in self.__all_cards:
                    continue

                if players_moves[x] not in self.__players[x]['played_cards']:
                    for player in self.__players:
                        if (
                            {x, player} in played_already
                            or {player, x} in played_already
                        ):
                            continue

                        if player == x:
                            continue

                        if player in players_moves:
                            if players_moves[player] not in self.__all_cards:
                                continue

                            if players_moves[player] not in self.__players[player]['played_cards']:
                                result = self.__core.PlayerFight(
                                    Player(x, players_moves[x]),
                                    Player(player, players_moves[player])
                                )

                                played_already.append({x, player})

                                if result:
                                    loser = player if player != result.id else x

                                    self.__players[result.id]['point'] += 1
                                    if loser in self.__players[result.id]['won_from']:
                                        self.__players[result.id]['won_from'][loser] += 1
                                    else:
                                        self.__players[result.id]['won_from'][loser] = 0

                                    if result.id in self.__players[loser]['lost_by']:
                                        self.__players[loser]['lost_by'][result.id] += 1
                                    else:
                                        self.__players[loser]['lost_by'][result.id] = 0

                                    if loser not in in_round_status:
                                        in_round_status[loser] = {
                                            'lose': 1, 'win': 0
                                        }
                                    else:
                                        in_round_status[loser]['lose'] += 1


                                    if result.id not in in_round_status:
                                        in_round_status[result.id] = {
                                            'lose': 0, 'win': 1
                                        }
                                    else:
                                        in_round_status[result.id]['win'] += 1

                                else:

                                    if player in self.__players[x]['draw_with']:
                                        self.__players[x]['draw_with'][player] += 1
                                    else:
                                        self.__players[x]['draw_with'][player] = 0

                                    if x in self.__players[player]['draw_with']:
                                        self.__players[player]['draw_with'][x] += 1
                                    else:
                                        self.__players[player]['draw_with'][x] = 0

        for user in in_round_status:
            if in_round_status[user]['win'] < in_round_status[user]['lose']:
                self.__players[user]['played_cards'].append(players_moves[user])    

            if in_round_status[user]['win'] > self.__players[user]['most_win_in_round']:
                self.__players[user]['most_win_in_round'] = in_round_status[user]['win']
