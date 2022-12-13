#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""
Dokumentační komentář modulu.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ...api.interfaces import INamed



############################################################################

# TODO Porovnat sloučení s compare_containers v modulu test_game
# @dbg.prSEd(2)
def compare_containers(str_cont:tuple[str], named_cont:tuple[INamed]):
    """Porovná názvy v kontejneru str_cont s názvy objektů
    v kontejneru named_cont bez ohledu na velikost písmen.
    Budou-li se lišit, vrátí dvojici stringů s jejich obsahy,
    nebudou-li se lišit, vrátí False.
    Jako vedlejší efekt si funkce nastaví své atributy
    from_scenario a from_game, v nichž uchovává příslušné názvy.
    """
    if not ('__iter__' in dir(named_cont)):
        raise Exception('Testovaný objekt hry není kontejner')
    # from_scenario = [item     .lower() for item in str_cont]  .sort()
    # from_game     = [item.name.lower() for item in named_cont].sort()
    from_scenario = sorted([item     .lower() for item in str_cont])
    from_game     = sorted([item.name.lower() for item in named_cont])
    # dbg.prIN(2, f'{60*"@"}'
    #             f'\n{from_scenario = }'
    #             f'\n{from_game     = }')
    result = False if from_scenario != from_game \
             else (f'{from_scenario}', f'{from_game}', )
    compare_containers.from_scenario = from_scenario
    compare_containers.from_game     = from_game
    # dbg.prIN(2, 0, 'test_by', f'\n{compare_containers.from_scenario = }'
    #                           f'\n{compare_containers.from_game     = }')
    return result



############################################################################
dbg.stop_mod(0, __name__)
