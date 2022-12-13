#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/p1_INP/game/tests/__init__.py
"""\
Balíček s testy hry v jednotlivých fázích vývoje.¤

Data:
    LIMITS          - Minimální povinné počty klíčových objektů

Třídy:
    Level           - Výčtový typ definující hladinu testování

Funkce:
    print_err_msg() - Tiskne zásobník s popisem aktuální chyby

Podbalíčky:
    common          - Balíček modulů s pomocnými programy

Moduly:
    test_portal    - Test továrního objektu
    test_scenario   - Test scénářů
    test_game       - Test hry

Soubory:


"""
import dbg; dbg.start_pkg(0, __name__, __doc__)
############################################################################

from collections import namedtuple

LIMITS = (namedtuple('Limits', 'minSteps minPlaces minVisited minNSActions')
          (12,  # Minimální počet kroků scénáře HAPPY
            5,  # Minimální počet prostorů
            5,  # Minimální počet navštívených prostorů
            2)) # Minimální počet vlastních (= nestandardních) akcí



############################################################################

from enum import IntEnum

class Level(IntEnum):
    """Hladiny rozpracovanosti aplikace a jim odpovídajících testů.
    """
    # Definované hladiny - na dané hladině se testuje:
    FACTORY     = 0 #_ Jenom initor balíčku
    HAPPY       = 1 #a Jen šťastný scénář
    SCENARIOS   = 2 #b Čtyři základní scénáře: startovní, šťastný,
                    #c chybový a chybový scénář nadstandardních akcí
    ARCHITECTURE= 3 #d Přítomnost požadovaných objektů a metod
    START       = 4 #e Hra úspěšně odstartuje
    WORLD       = 5 #f Hra úspěšně vybuduje svůj svět
    BASIC       = 6 #g Zprovoznění základních akcí při korektním zadání
    MISTAKES    = 7 #h Základní akce jsou navržené robustní
    RUNNING     = 8 #i Zprovoznění všech akcí při korektním zadání
    WHOLE       = 9 #j Úspěšné zprovoznění hry, všechny akce jsou robustní
    MODIFIED    =10 #k Aplikace s nadstavbovými úpravami pro obhajobu
    EXTENDED    =11 #l Aplikace upravená pro obhajobu s dalším scénářem


    # # Demonstrační rozšiřující zadání
    # z00 = 8     # Výchozí stav totožný s kompletní hrou
    # z01 = 101
    # # Rozšiřující zadání popsaná v dokumentaci testovacího modulu
    # z11 = 111;    z21 = 121
    # z12 = 112;    z22 = 122
    # z13 = 113;    z23 = 123
    # z14 = 114;    z24 = 124
    # z15 = 115;    z25 = 125
    # z16 = 116;    z26 = 126
    # z17 = 117;    z27 = 127
    # z18 = 118;    z28 = 128
    # z19 = 119;    z29 = 129

    # def __lt__(self, other): return self.value <  other.value
    # def __le__(self, other): return self.value <= other.value
    # def __ge__(self, other): return self.value >= other.value
    # def __gt__(self, other): return self.value >  other.value



############################################################################

from ..api.interfaces   import IPkgInitor

# @dbg.prSEd(1, f'({__package__ = })')
def test(module:IPkgInitor, ID:Level) -> bool:
    """Otestuje zadaný tovární objekt a jím poskytnuté objekty hry.
    Zprávu o testu tiskne na standardní výstup.
    """
    # from . import test_interface as ti; print(f'test_interface = {ti}')
    from .test_interface import test
    test(module, ID)



############################################################################

def print_err_msg():
    """Zjistí si aktuální chybu a vytiskne výpis zásobníku.
    """
    import sys, traceback as TB
    tbo = sys.exc_info()[2]
    TB.print_tb(tbo)



############################################################################
dbg.stop_pkg(0, __name__)
