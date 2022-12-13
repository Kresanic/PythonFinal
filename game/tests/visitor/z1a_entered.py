#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/p1_INP/game/tests/visitor/z1a_entered.py
"""
Modul testuje správnou funkci řešení ha hladině Level.MISTAKES,
požadující robustní definici základní šestice akcí.
"""
import dbg
from .. import Level

dbg.start_mod(0, __name__)
############################################################################

from ...api.interfaces  import IPkgInitor, IGame
from ...api.scen_types  import tsSTART, tsEMPTY, tsNOT_START, tsUNKNOWN
from ...api.scenario    import ScenarioStep, Scenario
from .                  import Visitor
from ..common.errors    import error



############################################################################

class Visitor_Mistakes(Visitor):
    """Pomáhá kontrolovat správnost řešení popsaného v dokumentaci modulu.
    """

    def __init__(self, portal:IPkgInitor):
        super().__init__(portal, Level.MISTAKES)


    def after_game_start(self, scenario:Scenario):
        """ Akce, která se má provést po provedení startovacího kroku hry
        (tj. ve chvíli, kde je hra již inicializována), ale před jeho testem,
        tj. před ověřením, že stav hry odpovídá scénáři.
        Prověří, že hra deklaruje právě ty akce, které jsou deklarované
        ve scénářích a uloží seznam jejich abecedně seřazených názvů.
        """
        super().after_game_start(scenario)
        # Porovná úvodní hlášení hry se situací odvozenou ze scénářů

        # Nastaví výchozí stav potřebných proměnných
        self._entered = []


    def after_step_test(self, step:ScenarioStep, answer:str):
        """Akce, která se má provést po testu aktuálního kroku.
        """
        if step.typeOfStep == tsNOT_START:
            return
        # Aktualizuje  potřebné proměnné
        command = step.command
        words   = command.strip().split()
        if not (step.typeOfStep in NO_COMMAND):
            action_name = words[0].lower()
            if action_name not in self._entered:
                self._entered.append(action_name)
                self._entered.sort()
        # Najde a zkontroluje poslední řádek
        parts  = answer.split('\n')
        last_line = parts[-1]
        if not last_line.startswith(START):
            error('Závěrečný řádek nemá požadovaný začátek',
                  self.scenario, step, self.game, START, last_line)
        rest     = last_line[len(START):].strip()
        required = str(self._entered)
        if rest != required:
            error('Seznamy si neodpovídají',
                  self.scenario, step, self.game, required, rest)





############################################################################

TEST_ID     = '22w01'
NO_COMMAND  = {tsSTART, tsEMPTY, tsNOT_START, tsUNKNOWN, }
START       = '§Doposud zadáno: '



############################################################################
dbg.stop_mod(0, __name__)
