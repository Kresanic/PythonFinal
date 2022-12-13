#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/p1_INP/game/api/__init__.py
"""
Balíček definující společné API všech her.¤
Obsahuje moduly definující společně používané objekty
a vedle nich i moduly definující protokoly .

Moduly:
    __init__    - Initor balíčku deklaruje povinné atributy initorů balíčků
                  odevzdaných semestrálních prací
    game_types  - Protokoly deklarující povinné atributy objektů hry
    scen_types  - Typy scénářů a jejich kroků
    scenarios   - Třídy kroků scénáře a scénářů
    gui         - Grafické uživatelské rozhraní pro hry dodržující api

"""
def version(): return '22w.02.9139_2022-11-17'
import dbg; dbg.start_pkg(0, __name__, __doc__)
############################################################################

from collections import namedtuple

BasicActions = namedtuple('BasicActions',
    'MOVE_NAME PUT_DOWN_NAME TAKE_NAME HELP_NAME END_NAME')
BasicActions.__doc__ = """Přepravka s názvy povinných akcí."""



############################################################################

# Modul interfaces musí být importován až definici modulu BasicActions,
# Protože v modulu Interfaces je modul BasicActions používán
from .interfaces import IGame

def state_of(game:IGame) -> str:
    """Vrátí string s popisem aktuálního stavu, tj. s názvem
    aktuálního prostoru, jeho sousedů a h-objektů a obsahu batohu.
    """
    cp = game.world().current_place()
    result = (f'Aktuální prostor:    {cp}\n'
              f'Sousedé prostoru:    {list(cp.neighbors)}\n'
              f'Předměty v prostoru: {cp.items}\n'
              f'Předměty v batohu:   {game.world().BAG.items}\n'
              f'Nastavené příznaky:  {game.conditions()}')
    return result



############################################################################
dbg.stop_pkg(0, __name__)
