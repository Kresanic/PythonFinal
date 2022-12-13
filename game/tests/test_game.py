#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/p1_INP/game/tests/test_game.py
"""
Modul s testy běhu hry.
"""
import dbg
dbg.start_mod(0, __name__)
############################################################################

from ..api import BasicActions, scen_types, state_of
from ..api.interfaces   import IPkgInitor, IGame
from ..api.scenario     import ScenarioStep, Scenario
from .visitor           import Visitor
from .                  import Level



############################################################################

# Nastavení, zda se budou vypisovat stavy hry po provedení jednotlivých akcí
Scenario.print_state = True



############################################################################

# @dbg.prSEd()
def test_game_from(portal:IPkgInitor, level:Level,
                   visitorClass:type=Visitor) -> None:
    """Test hry podle zadaných scénářů
    """
    visitor = visitorClass(portal, level)
    n2s = portal.NAME_2_SCENARIO
    if not isinstance(n2s, dict):
        n2s = n2s()
    global game
    game = portal.GAME()
    fss  = n2s
    # dbg.prIN(1,f'{level = }')
    # dbg.prIN(1,f'{fss   = }')
    # dbg.prIN(1,f'{LEVEL_2_SCENARIOS = }')
    # dbg.prIN(1,f'{LEVEL_2_SCENARIOS[level] = }')
    scen_list = []
    for scen_name in LEVEL_2_SCENARIOS[level]:
        # dbg.prIN(1, f'{i = },   {fss[i] = }')
        item = fss[scen_name]
        scen_list.append(item)
    scenarios = tuple(scen_list)
    # scenarios = tuple(fss[i] for i in ID_2_SCENARIOS[Level(ID)])
    # def prep_scen():
    #     result = []
    #     for i in ID_2_SCENARIOS[Level(ID)]:
    #         dbg.prIN(1, f'{i = }')
    #         dbg.prIN(1, f'{fss[i] = }')
    #         result.append(fss[i])
    #     return tuple(result)
    
    # dbg.prSE(
    # scenarios = prep_scen()
    
    print(f'\nSCENARIOS: {scenarios}\n')
    visitor.before_game_start()
    NL = '\n'
    for s in scenarios:
        print(f'\n{2*(75*"T"+NL)}Testovaný scénář: {s.name}')
        _test_by(s, visitor)



############################################################################
#
# def _get_scenarios_for(ID:Level, portal:IPkgInitor) -> tuple[Scenario]:
#     """Podle zadaného ID vrátí správnou n-tici scénářů.
#     """
#     scenarios = portal.scenarios()
#     if ID <= Level.BASIC:
#         return (scenarios[3],)
#     if ID == Level.MISTAKES:
#         return (scenarios[3], scenarios[3], scenarios[1],)
#     if ID >= Level.WHOLE:
#         return (scenarios[0], scenarios[0], scenarios[1], scenarios[2],)
#

def _get_visitor_for(ID:Level, portal:IPkgInitor) -> Visitor:
    """Vrátí návštěvníka odpovídajícího zadané hladině.
    """
    # if ID <= Level.WHOLE:
    #     return Visitor(portal)
    # if ID == Level.z01:
    #     from .test_z01 import Visitor_z01
    #     return Visitor_z01(portal)
    # if ID == Level.z11:
    #     from .test_z11 import Visitor_z11
    #     return Visitor_z11(portal)
    # if ID == Level.z12:
    #     from .test_z12 import Visitor_z12
    #     return Visitor_z12(portal)
    # if ID == Level.z13:
    #     from .test_z13 import Visitor_z13
    #     return Visitor_z13(portal)
    # if ID == Level.z14:
    #     from .test_z14 import Visitor_z14
    #     return Visitor_z14(portal)
    # if ID == Level.z21:
    #     from .test_z21 import Visitor_z21
    #     return Visitor_z21(portal)
    # raise Exception (
    #     f'\nVe funkci test_game._get_visitor_for() není zadán návštěvník '
    #     f'pro hladinu {ID}')


# @dbg.prSEda()
def _test_by(scenario:Scenario, visitor:Visitor) -> None:
    """Otestuje zadanou hru podle zadaného scénáře
    za pomoci zadaného návštěvníka.
    """
    from_scenario:list[str]
    from_game    :list[str]

    def _error(reason:str, step:ScenarioStep, expected, obtained):
        """Zobrazí chybové hlášení upozorňující na příčinu chyby.
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

    # TODO Porovnat sloučení s compare_containers v modulu utils
    # @dbg.prSEdar()
    def compare_containers(scen_cont:tuple[str],
                           game_cont:tuple['INamed']) -> bool:
        """Porovná názvy v kontejneru scen_cont s názvy objektů
        v kontejneru game_cont bez ohledu na velikost písmen
        a vrátí informaci o tom, zda se liší (liší se = True).
        """
        if not ('__iter__' in dir(game_cont)):
            _error('objekt hry není kontejner', step, scen_cont, game_cont)
        nonlocal from_scenario, from_game
        from_scenario = [item     .lower() for item in scen_cont].sort()
        from_game     = [item.name.lower() for item in game_cont].sort()
        return from_scenario != from_game

    # Zde začíná vlastní tělo funkce
    step:ScenarioStep
    for step in scenario.steps:
        print(f'{step.index}. {(command:=step.command)}\n{30*"-"}')
        try:
            answer = game.execute_command(command)
            print(f'{answer}')
            if Scenario.print_state:
                print(f'{30*"-"}\n{state_of(game)}')
            print(f'{30*"="}\n')
        except Exception as ex:
            print(f'Při vykonávání příkazu '
                  f'{step.index}. {(command:=step.command)}\n'
                  f'byla vyhozena výjimka {ex}')
            raise ex

        # print(f'Očekávaný stav hry po provedení testovaného příkazu:\n'
        #       f'{step}')
        # print(f'\nObdržený stav hry po provedení testovaného příkazu:')
        # print(f'{state_of(game)}')

        if step.typeOfStep == scen_types.tsSTART:
            visitor.after_game_start(scenario)
        visitor.before_step_test(step, answer)
        if (not answer or
            step.message.lower() != answer[:len(step.message)].lower()
        ):
            _error('odpověď hry', step, step.message, answer)
        if step.typeOfStep == scen_types.tsNOT_START:
            continue
        current_place = game.world().current_place()
        if step.place != current_place.name:
            _error('aktuální prostor', step, step.place, current_place)
        if compare_containers(step.neighbors, current_place.neighbors):
            _error('aktuální sousedé', step, from_scenario, from_game)
        if compare_containers(step.items, current_place.items):
            _error('objekty v aktuálním prostoru', step, from_scenario,
                                                         from_game)
        if compare_containers(step.bag, game.bag().items):
            _error('objekty v batohu', step, from_scenario, from_game)
        visitor.after_step_test(step, answer)
    visitor.after_game_end()
    if game.is_alive():
        _error('Po ukončení scénáře není hra ukončena', step, (), ())


def _verify_is_alive(step:ScenarioStep, the_last:bool):
    """Prověří, jestli testovaná hra správně hlásí svoji spuštěnost
    (před startem a po skončení ne, jinak ano).
    """
    game_is_alive = game.is_alive()
    if (step.typeOfStep == scen_types.tsNOT_START)  or  the_last:
        if game_is_alive:
            prefix = ("Po ukončení hry" if the_last
                else  "Před startem hry ")
            raise Exception(prefix + " hra hlásí, že je spuštěná,"
                                   + " přestože má být vypnutá")
    else:
        if not game_is_alive:
            raise Exception("Hra tvrdí, že je vypnutá přestože má běžet")



############################################################################
# Následující proměnné jsou zavedeny pro zpřehlednění n-tice názvů
# scénářů postupně používaných při testování na jednotlivých hladinách
HAPPY_   = scen_types.HAPPY_NAME
BASIC_   = scen_types.BASIC_NAME
MISTAKE_ = scen_types.MISTAKE_NAME
MIST_NS_ = scen_types.MISTAKE_NS_NAME
FOURTH_  = 'FOURTH' # Přidaný scénář pro modifikace s přidanou akcí


# Testovací posloupnosti scénářů pro jednotlivé hladiny testování
LEVEL_2_SCENARIOS = {
    Level.START     : (BASIC_, ),
    Level.WORLD     : (BASIC_, ),
    Level.BASIC     : (BASIC_, BASIC_, ),
    Level.MISTAKES  : (BASIC_, BASIC_, MISTAKE_, ),
    Level.RUNNING   : (HAPPY_, HAPPY_, ),
    Level.WHOLE     : (HAPPY_, HAPPY_, MISTAKE_, MIST_NS_, ),
    Level.MODIFIED  : (HAPPY_, HAPPY_, MISTAKE_, MIST_NS_, ),
    Level.EXTENDED  : (HAPPY_, HAPPY_, MISTAKE_, MIST_NS_, FOURTH_, ),
}


############################################################################
dbg.stop_mod(0, __name__)
