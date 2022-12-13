#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/p1_EDU_Demo/game/krep09_kresanic/ck_actions.py
"""
Modul reprezentuje správce akcí, který řídí celkové chování
v závislosti na tom, je-li hra právě aktivní, a rozhoduje,
která akce dostane na starost zpracování aktuálního příkazu.
Současně obsahuje definice všech akcí.
"""
import dbg; dbg.start_mod(0, __name__)
############################################################################

from .              import ck_world as world
from .ck_scenarios  import *


############################################################################

def execute_command(command: str) -> str:
    """Zpracuje zadaný příkaz a vrátí text zprávy pro uživatele.
    """
    command = command.strip()   # Smaže úvodní a závěrečné bílé znaky
    if command == '':
        return _execute_empty_command()
    elif is_active:
        return _execute_standard_command(command)
    else:
        return NOT_START


def _execute_empty_command() -> str:
    """Zpracuje prázdný příkaz, tj. příkaz zadaný jako prázdný řetězec.
    Tento příkaz odstartuje hru, ale v běžící hře se nesmí použít.
    """
    global is_active    # Aby nevytvořil lokální proměnnou
    if is_active:
        return EMPTY
    else:
        is_active = True
        _initialize()
        return WELCOME


def _execute_standard_command(command: str) -> str:
    """Připraví parametry pro standardní akci hry,
    tuto akci spustí a vrátí zprávu vrácenou metodou dané akce.
    Byla-li zadána neexistující akce, vrátí oznámení.
    """
    words = command.lower().split()
    action_name = words[0]
    try:
        action  = NAME_2_ACTION[action_name]
    except KeyError:
        return UNKNOWN + action_name
    return action.execute(words)


def _initialize():
    """Inicializuje všechny součásti hry před jejím spuštěním."""
    global conditions
    conditions['has.quesadilla'] = False
    conditions['has.bageta'] = False
    conditions['has.rezeň'] = False
    conditions['has.sviečková'] = False
    conditions['has.set_up.table'] = False
    world.initialize()



############################################################################

class Action(world.ANamed):
    """Instance třídy řeší reakce na zadané příkazy
    a realizují tak požadované akce."""

    def __init__(self, name: str, description: str, execute):
        """Vytvoří akci se zadaným názvem, stručným popisem
        a funkcí pro zpracování zadaného příkazu."""
        super().__init__(name)
        self.description = description
        self.execute     = execute



############################################################################

def end(arguments: str) -> str:
    """Ukončí hru a převede ji do pasivního stavu."""
    global is_active
    is_active = False
    return END


def goto(arguments: list[str]) -> str:
    """Ověří, že zadaný prostor patří mezi sousedy aktuálního
    prostoru, hráče do něj přemístí."""
    if len(arguments) < 2:
        return MOVE_WA
    destination_name = arguments[1]
    destination = world._current_place \
                       .name_2_neighbor(destination_name)
    if destination:
        world._current_place = destination
        return (GOTO + destination.description)
    else:
        return (BAD_NEIGHBOR + destination_name)


def help(arguments: list[str]) -> str:
    """Zobrazí definované akce a jejich popisy."""
    result = (SUBJECT + '\n'
           + 'Hra umožňuje zadat následující příkazy:\n\n')
    for a in NAME_2_ACTION.values():
        result += f'{a.name}\n{a.description}\n\n'
    return result


def put(arguments: list[str]) -> str:
    """Ověří existenci zadaného h-objektu v košíku a je-li tam,
    vyjme jej z košíku a přesune do aktuálního prostoru."""
    if len(arguments) < 2:
        return PUT_DOWN_WA
    item_name = arguments[1]
    item      = world.BAG.remove_item(item_name)
    if item:
        world._current_place.add_item(item)
        return PUT_DOWN + item.name
    else:
        return NOT_IN_BAG + item_name


def take(arguments: list[str]) -> str:
    """Ověří existenci zadaného h-objektu v aktuálním prostoru
    a je-li tam, přesune jej do košíku."""
    if len(arguments) < 2:
        return TAKE_WA
    item_name = arguments[1]
    item      = world._current_place.remove_item(item_name)
    if not item:
        return BAD_ITEM + item_name
    if item.weight == world.Item.HEAVY:
        world._current_place.add_item(item)
        return UNMOVABLE + item.name
    if world.BAG.add_item(item):
        return TAKE + item.name
    else:
        world._current_place.add_item(item)
        return BAG_FULL + item.name

def cook(arguments: list[str]) -> str:
    """
    Skontroluje, či má v batohu potrebné suroviny a následne
    vybere suroviny z batohu, nastaví podmienku na
    tru a vloži do batohu jedlo.
    """
    def checks_for_needed_foods(needed_for_meal: [str]) -> bool:
        """
        Pozrie sa či sú v batohu potrebné ingrediencie.
        Ak sú vráti True inač False.
        """
        bag_content = [
            item.real_name for item in world.Bag.bag_content(world.BAG)
        ]

        if all(
            needed_food in bag_content for needed_food in needed_for_meal
        ):
            return True
        else:
            return False

    def remove_items(needed_for_meal: [str]):
        """Nájde itemy z argumentu a vyhodí ich z batohu."""
        for food in needed_for_meal:
            world.BAG.remove_from_game(food)

    def creates_meal(meal: str):
        """
        Vytvorí dané objekt a dá ho do batohu.
        """
        world.BAG.add_item(world.Item(f"_{meal}"))

    if len(arguments) < 2:
        return NS1_0Args
    meal = arguments[1].lower()
    ingredients = {
        'quesadilla': ['Bravčové', 'Tortilla', 'Paradajky'],
        'bageta': ['Pečivo', 'Šunka', 'Syr'],
        'rezeň': ['Kuracie', 'Strúhanka', 'Vajíčka'],
        'sviečková': ['Hovädzie', 'Knedlík', 'Omáčka']
    }
    if meal in ingredients.keys():
        if not conditions[f'has.{meal}']:
            if checks_for_needed_foods(ingredients[meal]):
                remove_items(ingredients[meal])
                creates_meal(meal)
                conditions[f'has.{meal}'] = True
                return NS_1 + meal
            else:
                return NS1_WRONG_ARGb + meal
        else:
            return NS1_WrongCond + meal
    else:
        return NS1_WRONG_ARGa + meal


def tidy_up(argument) -> str:
    """
    Ak stôl už nebol predom uprataný, tak ho uprace.
    """
    checked_conditions = all(condition for condition in conditions)
    if not checked_conditions:
        return NS0_WrongCond
    else:
        conditions['has.set_up.table'] = True
        return NS_0


def sleep(argument) -> str:
    """
    Skontroluje podmienky ukončenia hry, ak sú splnené ukončí ju.
    """
    if conditions['has.set_up.table']:
        if world.BAG.is_empty():
            global is_active
            is_active = False
            return SUCCESS
        else:
            return NOT_SUCCESS
    else:
        return NOT_SUCCESS


############################################################################

# Příznak toho, zda hra právě běží (True), anebo jen čeká na další spuštění
is_active: bool = False     # Na počátku hra čeká, až ji někdo spustí

# Slovník s podmínkami testovanými a nastavovanými
# při provádění nestandardních akcí
conditions:dict[str:object] = {
        'has.quesadilla': False,
        'has.bageta': False,
        'has.rezeň': False,
        'has.sviečková': False,
        'has.set_up.table': False
}

# Slovník, jehož klíče jsou názvy akcí převedené na malá písmena
# a hodnoty jsou příslušné akce
NAME_2_ACTION = {
'jdi':  Action('Jdi',
        'Presunie Vás do danej krajiny.',
        goto),
'vezmi':Action('Vezmi',
        'Vezme zadaný předmět a vloží jej do batohu.\n'
        'Předmět ale musí být v aktuálním prostoru, musí být přenositelný\n'
        'a v batohu pro něj musí být volné místo.',
        take),
'polož':Action('Polož',
        'Přesune zadaný předmět z košíku do aktuálního prostoru.',
        put),
'?':    Action('?',
        'Zobrazí seznam dostupných akcí spolu s jejich stručnými popisy.',
        help),
'konec':Action('Konec',
        'Ukončí hru a převede ji do pasivního stavu.',
        end),
'uvar':    Action('Uvar',
        'Uvarí dané jedlo.',
        cook),
'upratať':    Action('Upratať',
        'Uprace stôl u Vás doma.',
        tidy_up),
'spať':    Action('Spať',
        'Ukončíte hru a pojdete spať..',
        sleep),
}



############################################################################
dbg.stop_mod(1, __name__)
