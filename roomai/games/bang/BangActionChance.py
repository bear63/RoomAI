#!/bin/python

from roomai.games.common import AbstractActionChance
from roomai.games.bang import PlayingCard
from roomai.games.bang import CharacterCard
from roomai.games.bang import RoleCard
from roomai.games.bang import PlayingCardsDict
from roomai.games.bang import CharacterCardsDict
from roomai.games.bang import RoleCardsDict

import roomai

class BangActionChanceType:
    rolecard = "rolecard"
    Charactercard = "Charactercard"
    normalcard = "normalcard"


class BangActionChance(AbstractActionChance):
    def __init__(self, card):
        logger = roomai.get_logger()
        if isinstance(card, PlayingCard):
            self.__type__ = BangActionChanceType.normalcard
            self.__card__ = card
            self.__key__  = card.key
        elif isinstance(card, CharacterCard):
            self.__type__ = BangActionChanceType.Charactercard
            self.__card__ = card
            self.__key__  = card.key
        elif isinstance(card, RoleCard):
            self.__type__ = BangActionChanceType.rolecard
            self.__card__ = card
            self.__key__  = card.key
        else:
            logger.fatal("In the constructor BangActionChance(card), the parameter card must be NormalCard, CharacterCard or RoleCard")
            raise TypeError("In the constructor BangActionChance(card), the parameter card must be NormalCard, CharacterCard or RoleCard")

    def __get_type__(self): return self.__type__
    type = property(__get_type__, doc = "the type of BangActionChance, e.g., type=%s, type=%s or type=%s"%(BangActionChanceType.rolecard, BangActionChanceType.normalcard, BangActionChanceType.Charactercard))

    def __get_card__(self): return  self.__card__
    card = property(__get_card__, doc = "the card of BangActionChance")

    def __get_key__(self):  return self.__card__.key
    key = property(__get_key__, doc = "the key of the BangActionChance. In fact, the key is the key of the card in this BangActionChance")

    @classmethod
    def lookup(self, key):
        logger = roomai.get_logger()
        if key is None or not isinstance(key,str):
            logger.fatal("In the constructor BangActionChance.lookup(key), the key must be a str")
            raise TypeError("In the constructor BangActionChance.lookup(key), the key must be a str")
        if key not in AllBangActionChanceDict:
            logger.fatal("In the constructor BangActionChance.lookup(key), the key must be the key of CharacterCard, RoleCard or NormalCard")
            raise ValueError("In the constructor BangActionChance.lookup(key), the key must be the key of CharacterCard, RoleCard or NormalCard")
        return AllBangActionChanceDict[key]

    def __deepcopy__(self, memodict={}):
        return AllBangActionChanceDict[self.__key__]

AllBangActionChanceDict = dict()
