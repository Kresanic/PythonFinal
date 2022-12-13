#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/p1_INP/game/tests/visitor/__init__.py
"""
Balíček návštěvníků, přičemž v initoru balíčku je definována
třída `Visitor`, která je jejich společným rodičem.
"""
import dbg; dbg.start_pkg(1, __name__, __doc__)
###########################################################################q

from ...api.scenario    import ScenarioStep, Scenario
from ...api.interfaces  import IPkgInitor, IGame
from .. import Level, test_scenario
from  ..common.utils    import compare_containers
from  ..common.errors   import error



############################################################################

class Visitor:
    """Společný rodič tříd návštěvníků testů.
    Definuje sadu funkcí požadovaných od návštěvníka testů
    schopných ovlivnit způsob testování hry podle jimi známých dispozic.

    Slouží především k tomu, aby bylo možno doplnit základní testy
    o doplňkové kontroly prověřující, zda byly správně zapracovány
    všechny úpravy vyžadované při obhajobách aplikace.

    Třída definuje všechny metody návštěvníka jako prázdné s tím,
    že pro každé zadání požadované modifikace pro obhajobu
    bude definován odpovídající potomek kontrolující správnost řešení.
    """

    def __init__(self, portal:IPkgInitor, level:Level):
        self.portal = portal
        self.level  = level
        try:
            self.game:IGame = portal.GAME()
        except:
            raise Exception(f'\nPortál nedodal hru k testování.')


    @staticmethod
    def are_imperfect_scenarios_allowed(self) -> None:
        """Vrátí informaci o tom, je-li v prověřovaném zadání povoleno
        testování hry i v případě, kdy správce scénářů neprojde verifikací.
        """
        return False


    def before_game_start(self) -> None:
        """ Akce, která se má provést před spuštěním hry.
        Cílem metody je prověřit scénáře a případné další pomocné kódy.
        """


    # @dbg.prSEda()
    def after_game_start(self, scenario:Scenario) -> None:
        """ Akce, která se má provést po provedení startovacího kroku hry
        (tj. ve chvíli, kde je hra již inicializována), ale před jeho testem,
        tj. před ověřením, že stav hry odpovídá scénáři.
        Cílem metody je připravit potřebné informace o testované hře.
        """
        # dbg.prIN(1, f'{self.level = }')
        if self.level >= Level.RUNNING:
            if not compare_containers(test_scenario.ALL_ACTIONS,
                                      self.game.all_actions()):
                error('Seznam dostupných akcí', scenario, scenario.steps[0],
                   self.game, compare_containers.from_scenario,
                              compare_containers.from_game)
        self.scenario = scenario


    def before_step_test(self, step:ScenarioStep, answer:str) -> None:
        """Akce, která se má provést po provedení kroku hry, ale před jeho
        testem, tj. před ověřením, že stav hry odpovídá scénáři.
        Parametr »step« představuje aktuálně testovaný krok scénáře
        a parametr »answer« představuje odpověď hry.
        """


    def after_step_test(self, step:ScenarioStep, answer:str) -> None:
        """Akce, která se má provést po testu aktuálního kroku.
        Parametr »step« představuje aktuálně testovaný krok scénáře
        a parametr »answer« představuje odpověď hry.
        """


    def after_game_end(self, verbose_message:str='',
              exception:Exception=None, summary:'GameSummary'=None) -> None:
        """Akce, která se má provést po testu posledního kroku.
        Význam parametrů je následující:
        »step«      - Kompletní zpráva o průběhu testu
        »exception« - Případná vyhazovaná výjimka
        »summary«   - Přepravka s informacemi o předpokládaném průběhu hry
                      podle scénářů
        """


    def __repr__(self):
        """Systémový podpis instance -- vrátí název třídy
        a autora testované aplikace. """
        return f'{self.__class__.__module__}.{self.__class__.__name__}(' \
               f'{self.portal.__name__})'



###########################################################################q
dbg.stop_pkg(1, __name__)
