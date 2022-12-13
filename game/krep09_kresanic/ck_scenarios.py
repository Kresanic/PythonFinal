#Příliš žluťoučký kůň úpěl ďábelské ó - PŘÍLIŠ ŽLUŤOUČKÝ KŮŇ ÚPĚL ĎÁBELSKÉ Ó
#P:/p1_EDU_Demo/game/a1g_mistakes/ck_scenarios.py
"""
Základní čtveřice scénářů pro hru inspirovanou pohádkou o Červené Karkulce.
"""
import dbg; dbg.start_mod(1, __name__)
###########################################################################q

from game.api.scenario   import ScenarioStep, Scenario
from game.api.scen_types import *  # Především typu kroků



###########################################################################q
ScenarioStep.next_index = 0   # Index prvního kroku za startem

SUBJECT = (
        'Zablúdili ste v Španielsku a\n'
        'potrebujete sa vrátiť domov do Slovenska.\n'
        'Bohužiaľ, nemáte na lístky domov.\n'
        'Ale existuje možnosť ako sa môžete dostať domov.\n'
        'V každej krajine majú svojé obľúbené jedlo.\n'
        'Vašou úlohou je pozbierať všetky tri základné suroviny,\n'
        'ktoré potrebujete na uvarenie jedla.\n'
        'Následne všetky jedlá doniesť domov.\n\n'
        'Začínate v Španielsku, kde budete variť quesadillu.\n'
        'V Španielsku je Bravčové, Cukor, Šľahačka, Tortilla,\n'
        'Mobil, Paradajky, Plachta, Taška, \
        Uterák, Servítky, Lampa a Skriňa.\n\n'
        'Nebudete-li si vědět rady, zadejte znak ?.'
    )
# Základní úspěšný scénář demonstrující průběh hry, při němž hráč
# nezadává žádné chybné příkazy a dosáhne zadaného cíle.
HAPPY = Scenario(stHAPPY, (
    START_STEP :=
    ScenarioStep(tsSTART, '',
        WELCOME := 'Vítajte!\n' + SUBJECT,
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),
        (),
        # Počáteční stavy stavových proměnných
         sets={'has.quesadilla': False,
               'has.bageta': False,
               'has.rezeň': False,
               'has.sviečková': False,
               'has.set_up.table': False,
               },
        ),
    ScenarioStep(tsTAKE, 'Vezmi Bravčové',              # Zadaný příkaz
        (TAKE := 'Dali ste do batohu: ') + 'Bravčové',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),
        ('Cukor', 'Šľahačka', 'Tortilla', 'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa', ),
        ('Bravčové',),                               # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi Tortilla',           # Zadaný příkaz
        TAKE + 'Tortilla',
        'Španielsko',  # Aktuální prostor
         ('Francúzsko' , 'Portugalsko',),  # Aktuální sousedé
         ('Cukor', 'Šľahačka', 'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa', ),
         ('Bravčové', 'Tortilla',),                   # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi Paradajky',           # Zadaný příkaz
        TAKE + 'Paradajky',
        'Španielsko',  # Aktuální prostor
         ('Francúzsko' , 'Portugalsko',),  # Aktuální sousedé
         ('Cukor', 'Šľahačka', 'Mobil',
          'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa', ),  # H-objekty v prostoru
         ('Bravčové', 'Tortilla', 'Paradajky',),
        ),
    ScenarioStep(tsNS_1, 'Uvar Quesadilla',          # Zadaný příkaz
        (NS_1 := 'Uvarili ste: ') + 'Quesadilla',
        'Španielsko',                                # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),    # Aktuální sousedé
        ('Cukor', 'Šľahačka', 'Mobil',
          'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa',),
        ("Quesadilla", ),
         needs={'has.quesadilla': False,
                'has.bageta': False,
                'has.rezeň': False,
                'has.sviečková': False,
                'has.set_up.table': False},
         sets={'has.quesadilla': True},
        ),
    ScenarioStep(tsGOTO, 'Jdi Francúzsko',
        (GOTO := 'Dorazili ste do: \n') + \
        'Franúzska, ich obľúbené jedlo je Bageta.\n'
        'Nachádza sa tu Bageta, Riasy, Syr, Šunka a Čokoláda',
        'Francúzsko',                                      # A
        ('Španielsko', 'Belgicko', 'Nemecko',),
        ('Pečivo', 'Riasy', 'Syr', 'Šunka', 'Čokoláda', ),
        ("Quesadilla", ),                     # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi Pečivo',           # Zadaný příkaz
        TAKE + 'Pečivo',
        'Francúzsko',
        ('Španielsko', 'Belgicko', 'Nemecko',),
        ('Riasy', 'Syr', 'Šunka', 'Čokoláda', ),         # H
        ("Quesadilla", 'Pečivo',),              # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi Šunka',           # Zadaný příkaz
        TAKE + 'Šunka',
        'Francúzsko',  # Aktuální prostor
         ('Španielsko', 'Belgicko', 'Nemecko',),
         # Aktuální sousedé
         ('Riasy', 'Syr', 'Čokoláda',),  # H-objekty v prostoru
         ("Quesadilla", 'Pečivo', 'Šunka',),             # H-
        ),
    ScenarioStep(tsTAKE, 'Vezmi Syr',           # Zadaný příkaz
        TAKE + 'Syr',
        'Francúzsko',  # Aktuální prostor
         ('Španielsko', 'Belgicko', 'Nemecko',),
         # Aktuální sousedé
         ('Riasy', 'Čokoláda',),  # H-objekty v prostoru
         ("Quesadilla", 'Pečivo', 'Šunka', 'Syr', ),
        ),
    ScenarioStep(tsNS_1, 'Uvar Bageta',  # Zadaný příkaz
         NS_1 + 'Bageta',
         'Francúzsko',  # Aktuální prostor
        ('Španielsko', 'Belgicko', 'Nemecko',),
        ('Riasy', 'Čokoláda',),
        ("Quesadilla", "Bageta", ),
        needs = {'has.quesadilla': True,
                'has.bageta':  False,
                'has.rezeň': False,
                'has.sviečková':  False,
                'has.set_up.table': False},
        sets  = {'has.bageta': True},
        ),
    ScenarioStep(tsGOTO, 'Jdi Nemecko',                 # Zadaný příkaz
        GOTO + \
        'Nemecka, ich obľúbené jedlo je Rezeň.\n'
        'Nachádza sa tu Ryža, Kuracie, Strúhanka, Cestoviny a Vajíčka',
        'Nemecko',
        ('Francúzsko', 'Česko', 'Švajčiarsko',), # Aktuální sousedé
        ('Ryža', 'Kuracie', 'Strúhanka', 'Cestoviny', 'Vajíčka', ),
        ("Quesadilla", "Bageta", ),      # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi Kuracie',           # Zadaný příkaz
        TAKE + 'Kuracie',
        'Nemecko',  # Aktuální prostor
         ('Francúzsko', 'Česko', 'Švajčiarsko',),
         ('Ryža', 'Strúhanka', 'Cestoviny', 'Vajíčka', ),
         ("Quesadilla", 'Bageta', 'Kuracie',),  # H-Objekty v batohu
         ),
    ScenarioStep(tsTAKE, 'Vezmi Strúhanka',           # Zadaný příkaz
        TAKE + 'Strúhanka',
        'Nemecko',  # Aktuální prostor
         ('Francúzsko', 'Česko', 'Švajčiarsko',),
         ('Ryža', 'Cestoviny', 'Vajíčka', ),  # H-objekty v prostoru
         ("Quesadilla", 'Bageta', 'Kuracie', 'Strúhanka',),
         ),
    ScenarioStep(tsTAKE, 'Vezmi Vajíčka',           # Zadaný příkaz
        TAKE + 'Vajíčka',
        'Nemecko',  # Aktuální prostor
         ('Francúzsko', 'Česko', 'Švajčiarsko',),
         ('Ryža', 'Cestoviny', ),  # H-objekty v prostoru
         ("Quesadilla", 'Bageta', 'Kuracie', 'Strúhanka', 'Vajíčka',),
         ),
    ScenarioStep(tsNS_1, 'Uvar Rezeň',  # Zadaný příkaz
         NS_1 + 'Rezeň',
         'Nemecko',  # Aktuální prostor
         ('Francúzsko', 'Česko', 'Švajčiarsko',),
         ('Ryža', 'Cestoviny', ),  # H-objekty v prostoru
         ("Quesadilla", 'Bageta', 'Rezeň',),
         needs={'has.quesadilla': True,
                'has.bageta': True,
                'has.rezeň': False,
                'has.sviečková': False,
                'has.set_up.table': False},
         sets={'has.rezeň': True},
        ),
    ScenarioStep(tsGOTO, 'Jdi Česko',                 # Zadaný příkaz
        GOTO + \
        'Česka, ich obľúbené jedlo je Sviečková.\n'
        'Nachádza sa tu Knedlík, Hovädzie, Špagety, Zemiaky a Omáčka',
        'Česko',
        ('Slovensko', 'Nemecko', 'Poľsko',), # Aktuální sousedé
        ('Knedlík', 'Hovädzie', 'Špagety', 'Zemiaky', 'Omáčka',),
        ("Quesadilla", "Bageta", "Rezeň",),     # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi Knedlík',           # Zadaný příkaz
        TAKE + 'Knedlík',
        'Česko',  # Aktuální prostor
         ('Slovensko', 'Nemecko', 'Poľsko',),
         ('Hovädzie', 'Špagety', 'Zemiaky', 'Omáčka',),
         ('Knedlík', "Quesadilla", 'Bageta', 'Rezeň',),
         ),
    ScenarioStep(tsTAKE, 'Vezmi Hovädzie',           # Zadaný příkaz
        TAKE + 'Hovädzie',
        'Česko',  # Aktuální prostor
         ('Slovensko', 'Nemecko', 'Poľsko',),
         ('Špagety', 'Zemiaky', 'Omáčka',),  # H-objekty v prostoru
         ("Quesadilla", 'Bageta', 'Rezeň', 'Hovädzie', 'Knedlík',),
         ),
    ScenarioStep(tsTAKE, 'Vezmi Omáčka',           # Zadaný příkaz
        TAKE + 'Omáčka',
        'Česko',  # Aktuální prostor
         ('Slovensko', 'Nemecko', 'Poľsko',),
         ('Špagety', 'Zemiaky',),  # H-objekty v prostoru
         ("Quesadilla", 'Bageta', 'Rezeň', 'Hovädzie', 'Knedlík',
          'Omáčka',),
         ),
    ScenarioStep(tsNS_1, 'Uvar Sviečková',  # Zadaný příkaz
         NS_1 + 'Sviečková',
         'Česko',  # Aktuální prostor
        ('Slovensko', 'Nemecko', 'Poľsko',),
        ('Špagety', 'Zemiaky',),
        ("Quesadilla", "Bageta", "Rezeň", 'Sviečková', ),
        needs = {'has.quesadilla': True,
                'has.bageta':  True,
                'has.rezeň': True,
                'has.sviečková': False,
                'has.set_up.table': False},
        sets  = {'has.sviečková': True},
        ),
    ScenarioStep(tsGOTO, 'Jdi Slovensko',
        GOTO + \
        'Dorazili ste domov!\n'
        'Stačí Vám Upratať stôl a všetky jedlá položiť naň a Spať.',
        'Slovensko',
        ('Česko', 'Poľsko',),
        ('Stôl',),         # H-objekty v prostoru
        ("Quesadilla", "Bageta", "Rezeň", 'Sviečková',),
        ),
    ScenarioStep(tsNS_0, 'Upratať',                 # Zadaný příkaz
        NS_0 := 'Není možné upratať pokiaľ není všetko\
                         vybrané z batohu.',
        'Slovensko',
        ('Česko', 'Poľsko',),
        ("Stôl",),         # H-objekty v prostoru
        ("Quesadilla", "Bageta", "Rezeň", 'Sviečková',),
        needs = {'has.quesadilla': True,
                'has.bageta':  True,
                'has.rezeň': True,
                'has.sviečková': True,
                'has.set_up.table': False},
        sets = {'has.set_up.table': True},
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož Rezeň',       # Zadaný příkaz
        (PUT_DOWN := 'Položili ste: ') + 'Rezeň',
        'Slovensko',
        ('Česko', 'Poľsko',),
        ("Stôl","Rezeň",), # H-objekty v prostoru
        ("Quesadilla", "Bageta", 'Sviečková',),
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož Bageta',       # Zadaný příkaz
        PUT_DOWN + 'Bageta',
        'Slovensko',
        ('Česko', 'Poľsko',),
         ("Stôl","Rezeň", 'Bageta',),  # H-objekty v prostoru
         ("Quesadilla", 'Sviečková', ),
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož Quesadilla',
        PUT_DOWN + 'Quesadilla',
        'Slovensko',  # Aktuální prostor
         ('Česko', 'Poľsko',),
         ("Stôl","Rezeň", 'Bageta', 'Quesadilla', ),
         ( 'Sviečková',),
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož Sviečková',
        PUT_DOWN + 'Sviečková',
        'Slovensko',  # Aktuální prostor
         ('Česko', 'Poľsko',),
         ("Stôl","Rezeň", 'Bageta', 'Quesadilla', 'Sviečková',),
         (),
        ),
    ScenarioStep(tsSUCCESS, 'Spať',
        SUCCESS := (
        'Všetko ste vyložili a išli ste spať do svojej postele.\n'
        'Úspešneste ukončili hru.\n'
        'Ďakujeme a veríme, že ste sa zabavili.'
        ),
        'Slovensko',
        ('Česko', 'Poľsko',),
         ("Stôl","Rezeň", 'Bageta', 'Quesadilla', 'Sviečková',),
        (),
                 needs={'has.quesadilla': True,
                        'has.bageta': True,
                        'has.rezeň': True,
                        'has.sviečková': True,
                        'has.set_up.table': True},
                 sets={},
        ),

    )   # N-tice
)   # Konstruktor



############################################################################

ScenarioStep.next_index = +1  # Index prvního kroku za startem

BASIC = Scenario(stBASIC, (
    START_STEP,
    ScenarioStep(tsGOTO, 'Jdi Francúzsko',                 # Zadaný příkaz
        GOTO + 'Franúzska, ich obľúbené jedlo je bageta.\n'
        'Nachádza sa tu Bageta, Riasy, Syr, Šunka a Čokoláda',
        'Francúzsko',
         ('Španielsko', 'Belgicko', 'Luxembursko', 'Nemecko', 'Švajčiarsko',
          'Španielsko', 'Taliansko',),
         ('Pečivo', 'Riasy', 'Syr', 'Šunka', 'Čokoláda',),
         (),  # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi Pečivo',            # Zadaný příkaz
        TAKE + 'Pečivo',
        'Francúzsko',
        ('Španielsko', 'Belgicko', 'Luxembursko', 'Nemecko', 'Švajčiarsko',
         'Španielsko', 'Taliansko',),
        ('Riasy', 'Syr', 'Šunka', 'Čokoláda', ),
        ('Pečivo',),                              # H-Objekty v batohu
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož Pečivo',        # Zadaný příkaz
        PUT_DOWN + 'Pečivo',
        'Francúzsko',
        ('Španielsko', 'Belgicko', 'Luxembursko', 'Nemecko', 'Švajčiarsko',
         'Španielsko', 'Taliansko',),
        ('Riasy', 'Syr', 'Šunka', 'Čokoláda', 'Pečivo', ),
        (),                                       # H-Objekty v batohu
        ),
    ScenarioStep(tsHELP, '?',                       # Zadaný příkaz
        SUBJECT,
        'Francúzsko',
        ('Španielsko', 'Belgicko', 'Luxembursko', 'Nemecko', 'Švajčiarsko',
         'Španielsko', 'Taliansko',),
        ('Riasy', 'Syr', 'Šunka', 'Čokoláda', 'Pečivo', ),
        (),                                       # H-Objekty v batohu
        ),
    ScenarioStep(tsEND, 'KONEC',                    # Zadaný příkaz
        END := 'Ukončili jste hru.\nDěkujeme, že jste si zahráli.',
        'Francúzsko',
        ('Španielsko', 'Belgicko', 'Luxembursko', 'Nemecko', 'Švajčiarsko',
         'Španielsko', 'Taliansko',),
        ('Riasy', 'Syr', 'Šunka', 'Čokoláda', 'Pečivo', ),
        (),
        ),
    )   # N-tice
)   # Konstruktor



############################################################################
# Základní chybový scénář demonstrující průběh hry, při němž hráč
# zadává chybně příkazy k provedení základních akcí
# a současně vyzkouší vyvolání nápovědy a nestandardní ukončení.

ScenarioStep.next_index = -1  # Index kroku před korektním startem

WRONG_START = ScenarioStep(tsNOT_START, 'start', # Zadaný příkaz
        NOT_START := (
        'Prvním příkazem není startovací příkaz.\n' 
        'Hru, která neběží, lze spustit pouze startovacím příkazem.\n'),
        '',                                         # Aktuální prostor
        (),                                         # Aktuální sousedé
        (),                                         # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        )

ScenarioStep.next_index = +1  # Index prvního kroku za startem

MISTAKE = Scenario(stMISTAKES, (
    WRONG_START,
    START_STEP,
    ScenarioStep(tsEMPTY, '',                       # Zadaný příkaz
        EMPTY := 'Prázdný příkaz lze použít pouze pro start hry',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),   # H-objekty v prostoru
        (),
        ),
    ScenarioStep(tsUNKNOWN, 'maso',                 # Zadaný příkaz
        UNKNOWN := 'Tento příkaz neznám: maso',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa',  ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsMOVE_WA, "jdi",                  # Zadaný příkaz
        MOVE_WA := ('Nevím, kam mám jít.\n'
                    'Je třeba zadat název cílového prostoru.'),
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE_WA, "vezmi",                # Zadaný příkaz
        TAKE_WA := ('Nevím, co mám zvednout.\n'
                    'Je třeba zadat název zvedaného objektu.'),
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),   # H-objekty v prostoru
        (),                                          # H-Objekty v batohu
        ),
    ScenarioStep(tsPUT_DOWN_WA, "polož",            # Zadaný příkaz
        PUT_DOWN_WA := ('Nevím, co mám položit.\n'
                        'Je třeba zadat název pokládaného objektu.'),
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsBAD_NEIGHBOR, "jdi do_háje", # Zadaný příkaz
         (BAD_NEIGHBOR := 'Do zadaného prostoru se odsud jít nedá: ')
                        + 'do_háje',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),   # H-objekty v prostoru
        (),                                         # H-Objekty v batohu
        ),
    ScenarioStep(tsBAD_ITEM, "vezmi whisky",        # Zadaný příkaz
        (BAD_ITEM := 'Zadaný objekt v prostoru není: ') + 'whisky',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa',  ),   # H-objekty v prostoru
        (),                                          # H-Objekty v batohu
        ),
    ScenarioStep(tsUNMOVABLE, "Vezmi Skriňa",         # Zadaný příkaz
        (UNMOVABLE := 'Zadaný objekt není možno zvednout: ') + 'Skriňa',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil',
         'Paradajky','Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),   # H-objekty v prostoru
        (),                                          # H-Objekty v batohu
        ),
    ScenarioStep(tsTAKE, 'Vezmi Paradajky',              # Zadaný příkaz
        TAKE + 'Paradajky',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Tortilla',
         'Mobil', 'Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),
        ('Paradajky',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Tortilla',           # Zadaný příkaz
        TAKE + 'Tortilla',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka',
         'Mobil', 'Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),
        ('Paradajky', 'Tortilla',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Bravčové',           # Zadaný příkaz
        TAKE + 'Bravčové',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ( 'Cukor', 'Šľahačka',
         'Mobil', 'Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),
        ('Paradajky', 'Tortilla', 'Bravčové',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Šľahačka',           # Zadaný příkaz
        TAKE + 'Šľahačka',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ( 'Cukor',
         'Mobil', 'Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),
        ('Paradajky', 'Tortilla', 'Bravčové', 'Šľahačka',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Cukor',           # Zadaný příkaz
        TAKE + 'Cukor',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ( 'Mobil', 'Skriňa', 'Plachta', 'Taška',
         'Uterák',
         'Servítky', 'Lampa', ),
        ('Paradajky', 'Tortilla', 'Bravčové', 'Šľahačka','Cukor',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Servítky',           # Zadaný příkaz
        TAKE + 'Servítky',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ( 'Mobil', 'Skriňa', 'Plachta', 'Taška',
         'Uterák', 'Lampa', ),
        ('Paradajky', 'Tortilla', 'Bravčové', 'Šľahačka','Cukor',
         'Servítky',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Plachta',           # Zadaný příkaz
        TAKE + 'Plachta',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ( 'Mobil', 'Skriňa', 'Taška',
         'Uterák', 'Lampa', ),
        ('Paradajky', 'Tortilla', 'Bravčové', 'Šľahačka','Cukor',
         'Servítky', 'Plachta',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Taška',           # Zadaný příkaz
        TAKE + 'Taška',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ( 'Mobil', 'Skriňa',
         'Uterák', 'Lampa', ),
        ('Paradajky', 'Tortilla', 'Bravčové', 'Šľahačka','Cukor',
         'Servítky', 'Plachta','Taška',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Uterák',           # Zadaný příkaz
        TAKE + 'Uterák',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ( 'Mobil', 'Skriňa', 'Lampa', ),
        ('Paradajky', 'Tortilla', 'Bravčové', 'Šľahačka','Cukor',
         'Servítky', 'Plachta','Taška','Uterák',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Lampa',           # Zadaný příkaz
        TAKE + 'Lampa',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ( 'Mobil', 'Skriňa',),
        ('Paradajky', 'Tortilla', 'Bravčové', 'Šľahačka','Cukor',
         'Servítky', 'Plachta','Taška','Uterák', 'Lampa',),
        ),
    ScenarioStep(tsBAG_FULL, 'Vezmi Mobil',       # Zadaný příkaz
        (BAG_FULL := 'Zadaný objekt se už do košíku nevejde: ') + 'Mobil',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Mobil',),
        ('Paradajky', 'Tortilla',),
        ),
    ScenarioStep(tsNOT_IN_BAG, 'polož Mobil',     # Zadaný příkaz
        (NOT_IN_BAG := 'Zadaný objekt v košíku není: ') + 'Mobil',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Mobil', 'Skriňa',),
        ('Paradajky', 'Tortilla',),
        ),
    ScenarioStep(tsHELP, '?',                       # Zadaný příkaz
        SUBJECT,
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),
        ('Bravčové', 'Cukor', 'Šľahačka', 'Mobil', 'Skriňa',),
        ('Paradajky', 'Tortilla',),
        ),
    ScenarioStep(tsEND, 'KONEC',                    # Zadaný příkaz
        END,
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),          # Aktuální sousedé
        ('Bravčové', 'Cukor', 'Šľahačka', 'Mobil', 'Skriňa',),
        ('Paradajky', 'Tortilla',),
        ),
    )   # N-tice
)   # Konstruktor



############################################################################
# Základní chybový scénář demonstrující průběh hry, při němž hráč
# zadává chybně příkazy k provedení povinně definovaných akcí.
ScenarioStep.next_index = 4    # Index prvního nestandardního kroku
MISTAKE_NS = Scenario(stMISTAKES_NS, (
        HAPPY.steps[0],
        HAPPY.steps[1],   # Vezmi víno
        HAPPY.steps[2],   # Vezmi Bábovka
        HAPPY.steps[3],   # Jdi les
    ScenarioStep(tsNS0_WrongCond, 'Upratať',        # Zadaný příkaz
        NS0_WrongCond := 'Není možné upratať pokiaľ není všetko\
                         vybrané z batohu.',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),
        ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa',),   # H-objekty v prostoru
        ('Bravčové', 'Tortilla', 'Paradajky',),
         needs={'has.quesadilla': True,
                'has.bageta': True,
                'has.rezeň': True,
                'has.sviečková': True,
                'has.set_up.table': False},
        ),
    ScenarioStep(tsNS1_0Args, 'Uvar',             # Zadaný příkaz
        NS1_0Args := 'Neviem čo mám uvariť.',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),
        ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa',),   # H-objekty v prostoru
        ('Bravčové', 'Tortilla', 'Paradajky',),
        ),
    ScenarioStep(tsPUT_DOWN, 'Polož Bravčové',       # Zadaný příkaz
        (PUT_DOWN := 'Položili ste: ') + 'Bravčové',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),
        ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa','Bravčové', ),   # H-objekty v prostoru
        ('Tortilla', 'Paradajky',),
        ),
    ScenarioStep(tsNS1_WRONG_ARG, 'Uvar Quesadilla',    # Zadaný příkaz
        (NS1_WRONG_ARGb := 'Nemáte potrebné suroviny na uvarenie: ') +
                 'Quesadilla',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),
        ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa','Bravčové', ),
        ('Tortilla', 'Paradajky',),
        ),
    ScenarioStep(tsTAKE, 'Vezmi Bravčové',              # Zadaný příkaz
        (TAKE := 'Dali ste do batohu: ') + 'Bravčové',
        'Španielsko',                                  # Aktuální prostor
        ('Francúzsko' , 'Portugalsko',),
        ('Cukor', 'Šľahačka','Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa', ),
        ('Bravčové','Tortilla', 'Paradajky',),
        ),
    ScenarioStep(tsNS_1, 'Uvar Quesadilla',
         (NS_1 := 'Uvarili ste: ') + 'Quesadilla',
         'Španielsko',  # Aktuální prostor
         ('Francúzsko' , 'Portugalsko',),
         ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa',),
         ("Quesadilla",),  # H-Objekty v batohu
         needs={'has.quesadilla': False},
         sets={'has.quesadilla': True},
         ),
    ScenarioStep(tsNS1_WrongCond, 'Uvar Quesadilla', # Zadaný příkaz
        ((NS1_WrongCond := 'Nejde uvariť jedlo, ktoré už máte uvarene: ')
                         + 'Quesadilla'),
        'Španielsko',  # Aktuální prostor
         ('Francúzsko', 'Portugalsko',),  # Aktuální sousedé
         ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa', ),
         ("Quesadilla",),  # H-Objekty v batohu
         needs={'has.quesadilla': False,
                'has.bageta': False,
                'has.rezeň': False,
                'has.sviečková': False,
                'has.set_up.table': False},
        ),
    ScenarioStep(tsNS1_WRONG_ARG, 'Uvar Stôl',    # Zadaný příkaz
        (NS1_WRONG_ARGa := 'Neviem uvariť: ') + 'Stôl',
        'Španielsko',
        ('Francúzsko' , 'Portugalsko',),
        ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa', ),   # H-objekty v prostoru
        ('Bravčové', 'Tortilla', 'Paradajky',),
        ),
    ScenarioStep(tsNOT_SUCCESS, 'Spať',           # Zadaný příkaz
        NOT_SUCCESS := 'Nemôžte ísť spať pokiaľ ste neupratali \
a nevyložili veci.',
        'Španielsko',  # Aktuální prostor
         ('Francúzsko', 'Portugalsko',),  # Aktuální sousedé
         ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa', ),
         ("Quesadilla",),
         needs={'has.quesadilla': True,
                'has.bageta': True,
                'has.rezeň': True,
                'has.sviečková': True,
                'has.set_up.table': True},
         ),
    ScenarioStep(tsEND, 'konec',
        END,
        'Španielsko',  # Aktuální prostor
         ('Francúzsko', 'Portugalsko',),
         ('Cukor', 'Šľahačka', 'Mobil',
         'Skriňa', 'Plachta', 'Taška', 'Uterák',
         'Servítky', 'Lampa', ),
         ("Quesadilla",),
        ),
    )   # N-tice
)   # Konstruktor



###########################################################################q

# Slovník převádějící názvy scénářů na scénáře
NAME_2_SCENARIO = {
    HAPPY       .name: HAPPY,     # Základní úspěšný (= šťastný) scénář
    BASIC       .name: BASIC,     # Scénář obsahující jen povinné akce
    MISTAKE     .name: MISTAKE,   # Scénář chybně zadaných povinných akcí
    MISTAKE_NS  .name: MISTAKE_NS,# Scénář chybně zadaných dodatečných akcí
}



###########################################################################q
dbg.stop_mod(0, __name__)
