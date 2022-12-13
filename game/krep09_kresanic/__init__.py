#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/p1_EDU_Demo/game/krep09_kresanic/__init__.py
"""
Žádné
"""
import dbg; dbg.start_pkg(1, __name__)
###########################################################################q

# Login autora/autorky programu zadaný VELKÝMI PÍSMENY
AUTHOR_ID = 'KREP09'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní,
# tj. nejprve příjmení psané velkými písmeny a za ním křestní jméno,
# u nějž bude velké pouze první písmeno a ostatní písmena budou malá.
# Má-li autor programu více křestních jmen, může je uvést všechna.
AUTHOR_NAME = 'KRESANIČ Peter'

# Jméno autora/autorky programu ve formátu PŘÍJMENÍ Křestní
# zapsané v jeho/jejím rodném jazyce
AUTHOR_NATIVE_NAME = 'KRESANIČ Peter'

# Čas začátku kroužku, který navštěvujete (AUTHOR_GROUP)
GROUP_TIME = '1245'  # Zadejte čtyřčíslí odpovídající času začátku kroužku



###########################################################################q

def NAME_2_SCENARIO():
    """Vrátí odkaz na slovník převádějící názvy scénářů na dané scénáře
    Scénáře musejí být instancemi třídy `game.api.scenario.Scenario`
    """
    from . import ck_scenarios
    return ck_scenarios.NAME_2_SCENARIO


def GAME():
    """Vrátí odkaz na hru, která musí implementovat protokol
    `game.api.interfaces.IGame`
    """
    from . import ck_main
    return ck_main



###########################################################################q
# Testy

# Definované hladiny - na dané hladině se testuje:
# FACTORY     = 0 # Jenom initor balíčku
# HAPPY       = 1 # Jen šťastný scénář
# SCENARIOS   = 2 # Čtyři základní scénáře: startovní, šťastný,
#                 # chybový a chybový scénář nadstandardních akcí
# ARCHITECTURE= 3 # Přítomnost požadovaných objektů a metod
# START       = 4 # Hra úspěšně odstartuje
# WORLD       = 5 # Hra úspěšně vybuduje svůj svět
# BASIC       = 6 # Zprovoznění základních akcí při korektním zadání
# MISTAKES    = 7 # Základní akce jsou navržené robustní
# RUNNING     = 8 # Zprovoznění všech akcí při korektním zadání
# WHOLE       = 9 # Úspěšné zprovoznění hry, všechny akce jsou robustní
# MODIFIED    =10 # Aplikace s nadstavbovými úpravami pro obhajobu
# EXTENDED    =11 # Aplikace upravená pro obhajobu s dalším scénářem


# @dbg.prSEd()
def self_test():
    """Otestuje, zda stav projektu odpovídá zadané hladině rozpracovanosti.
    """
    from game.tests import Level
    LEVEL = Level.WHOLE      # Nastavení hladiny rozpracovanosti aplikace

    from importlib import import_module
    me = import_module(__package__)   # Importuje modul svého balíčku
    from game.tests import test
    print(f'Testuji řešení v balíčku: {me.__name__}')
    test(me, LEVEL)         # Testuje implementaci na nastavené hladině


# Test spustíte nastavením požadované hladiny a zadáním příkazů:
# from add import add_tree as at;  at('../p1_EDU_Demo'); \
# import game.krep09_kresanic as at; at.self_test()


###########################################################################q
dbg.stop_pkg(1, __name__)
