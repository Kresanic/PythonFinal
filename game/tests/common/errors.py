#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
"""\
Dokumentační komentář modulu.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from .texts import *

from ...api.interfaces  import INamed, IGame, IPkgInitor
from ...api.scenario    import ScenarioStep, Scenario
from ...api import BasicActions, state_of



############################################################################

def error(reason:str, scenario:Scenario, step:ScenarioStep, game:IGame,
          expected:(tuple[str]|str), obtained:(list[INamed]|str)) -> None:
    """Zobrazí chybové hlášení upozorňující na příčinu chyby
    zapříčiněnou nesouhlasem objektů scénáře a hry.
    """
    message = (f'Při vyhodnocování {step.index}. kroku scénáře '
                 f'{scenario.name} byla odhalena chyba:\n'
               f'Chybným objekt:   {reason}\n'
               f'Očekávaný objekt: {str(expected)}\n'
               f'Obdržený objekt:  {str(obtained)}\n\n')
    print(message)
    print(f'Očekávaný stav hry po provedení testovaného příkazu:\n'
          f'{step}')
    print(f'\nObdržený stav hry po provedení testovaného příkazu:')
    print(f'{state_of(game)}')
    raise Exception



############################################################################

class CompareException:
    """Výjimka vyhazovaná při objevu závažných chyb v průběhu testování.
    """



############################################################################
#
# def clear_err_msgs():
#     """Vyčistí seznam chybových zpráv na počátku dalšího testu.
#     """
#     _ERR_MSGs.clear()
#
#
# def get_err_msgs():
#     """Vrátí kopii seznamu chybových zpráv.
#     """
#     return _ERR_MSGs[:]
#
#
# def add_err_msg(err_msg:str):
#     """Přidá do seznamu chybových zpráv další zprávu.
#     """
#     _ERR_MSGs.append(err_msg)
#



############################################################################

_ERR_MSGs:list[str] = []



############################################################################
dbg.stop_mod(0, __name__)
