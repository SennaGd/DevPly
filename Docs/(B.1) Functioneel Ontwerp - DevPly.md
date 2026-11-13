Datum 03 / 11 / 2026

## Inleiding
Dit document beschrijft het functioneel ontwerp van het development- en releaseplatform (DevPly) Het platform wordt gebruikt om de voortgang van een project(en) te raadplegen In  een project komen verschillende Requirements / Acceptatiecriteria, Ontwikkeltaken en Tests/Resultaten. Elke requirement kan gekoppelt worden aan een (of meerdere) Ontwikkeltaken, Afhankelijkheden en Tests. Dus op basis van de gemaakte taken, afhankelijkheden en geaccepteerde tests kan er uigehaald worden wanneer het project releaseklaar is. 
Projecten kunnen aangemaakt worden door een gebruiker (maakt niet uit wie het is iedereen mag een project starten), de aanmaker krijgt automatisch de rol als: _admin_. In het project zal de admin andere gebruikers kunnen uitnodigen. Deze gebruikers kunnen het verzoek weigeren/accepteren. De gebruikers hebben allemaal een eigen rol of meerdere rollen die op het account zit. De admin kan vervolgens ook nog rollen aanpassen in een project dan zal de gebruiker voor dat project de gekozen rol hebben maar voor anderen nogsteeds de standaard rollen behouden.
Wanneer een gebruiker de rol als _manager_ krijgt zal deze gebruiker requirements van een project kunnen beheren en als _ontwikkelaar_ kan de gebruiker ontwikkeltaken, testgevallen/resultaten, afhankelijkheden toevoegen en deze koppelen aan gemaakte requirements.  

## Situatiebeschrijving
### Huidige Situatie
Momenteel om de voortgang te gebruiker kunnen bedrijven gebruik maken van programma's zoals _Github Projects_, _Trello_. Deze programma's zijn goed voor het verdelen van taken en om terug te zien wie wat heeft gemaakt. Maar het probleem met deze programma's is dat ze geen projectstatus or releasegereedheid kunnen terug halen.

### Gewenste Situatie
De applicatie zal ervoor zorgen dat teams verschillende projecten kunnen beheren waarbij managers de requirements van een project kunnen toevoegen en ontwikkelaars ontwikkeltaken, tests en afhankelijkheden aan de requirements kunnen toevoegen. Er komt ook een AI model in de applicatie waar missende tests, de status van het project kunnen opgehaald worden en voor ontwikkelaars ook nog ontwikkeltaken voorbereiden.  

## Requirements

## Use-Case
### Diagram![[DevPly_Use_Case.png]]

### Tabellen

| Naam                   | Maakt een account aan                                                                                                                                                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                                                                                  |
| Actor                  | Gebruiker                                                                                                                                                                                                                                                            |
| Preconditie            | De gebruiker is op de "Sign up pagina"<br>De gebruiker is ingelogd                                                                                                                                                                                                   |
| Scenario               | De gebruiker moet een nieuw account aanmaken, hiervoor gaat hij naar de pagina "sign up" waar hij een formulier met accountgegevens (email, wachtwoord en gebruikersnaam) die hij in moet vullen. Daarna klikt hij op "Maak Account" en zal ook direct ingelogd zijn |
| Uitzonderingen         | De gebruiker maakt een account aan met een email/gebruikersnaam die al in gebruik is.                                                                                                                                                                                |
| Niet-Functionele Eisen | De gebruiker moet zijn telefoonnummer gebruiken om een account aan te maken.                                                                                                                                                                                         |
| Postconditie           | De gebruiker kan gemakkelijk een account aanmaken met een geldig email, wachtwoord en gebruikersnaam.                                                                                                                                                                |

| Naam                   | Logged in                                                                                                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                                  |
| Actor                  | Gebruiker                                                                                                                                                                                                            |
| Preconditie            | De gebruiker is op de "login pagina"<br>De gebruiker is ingelogd                                                                                                                                                     |
| Scenario               | De gebruiker gaat naar de login pagina waar hij een formulier krijgt van inlog-gegevens (email en wachtwoord) die hij in moet vullen met zijn gegevens. Daarna klikt hij op "log in" en zal succesvol ingelogd zijn. |
| Uitzonderingen         | De gebruiker typt een verkeed wachtwoord of gebruikersnaam/email in waardoor hij niet kan inloggen                                                                                                                   |
| Niet-Functionele Eisen | Email ontvangen zodra er een foute inlog-poging is gedaan.                                                                                                                                                           |
| Postconditie           | De gebruiker kan succesvol inloggen met de juiste inlog-gegevens.                                                                                                                                                    |

| Naam                   | Maakt nieuw project aan                                                                                                                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                      |
| Actor                  | Gebruiker                                                                                                                                                                                                |
| Preconditie            | De gebruiker is op de pagina "Projects"<br>De gebruiker is ingelogd                                                                                                                                      |
| Scenario               | De gebruiker klikt vervolgens op het knopje "New" waar hij een klein formulier krijgt om gegevens van het project in te typen. Dan klikt hij op "maak project" en zal er een nieuw project gemaakt zijn. |
| Uitzonderingen         | De gebruiker maakt een project aan zonder geldig projectnaam.<br><br>De gebruiker maakt een project aan met een projectnaam die al gebruikt is.                                                          |
| Niet-Functionele Eisen | Meerdere projecten in een keer aanmaken.                                                                                                                                                                 |
| Postconditie           | De gebruiker kan een nieuw project aanmaken.                                                                                                                                                             |

| Naam                   | Verwijderd project                                                                                                                                                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Versie                 | 1.0                                                                                                                                                                                                                                                                      |
| Actor                  | Gebruiker / Admin                                                                                                                                                                                                                                                        |
| Preconditie            | De gebruiker is op de pagina beheer pagina van project X (waar X de projectnaam is)<br>De gebruiker is ingelogd                                                                                                                                                          |
| Scenario               | De gebruiker(admin) wilt een project verwijderen, hiervoor gaat hij naar de beheer pagina van het project en klikt op "Verwijder Project" hiervoor moet de gebruiker zijn eigen wachtwoord intypen als confirmatie, zodra dat gedaan is zal het project verwijderd zijn. |
| Uitzonderingen         | De admin typt een verkeerd wachtwoord in.                                                                                                                                                                                                                                |
| Niet-Functionele Eisen | Email verificatie.<br>Meerdere projecten in een keer verwijderen.                                                                                                                                                                                                        |
| Postconditie           | De gebruiker(admin) kan een project verwijderen.                                                                                                                                                                                                                         |

| Naam                   | Nodigt gebruikers uit naar project                                                                                                                                                      |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                     |
| Actor                  | Gebruiker / Admin                                                                                                                                                                       |
| Preconditie            | De admin gaat naar de invite pagina van project X<br>De gebruiker is ingelogd                                                                                                           |
| Scenario               | De gebruiker(admin) wilt gebruikers uitnodigen naar het project. Hiervoor gaat hij naar de beheer pagina van een project. Daar zoekt hij op gebruikersnaam en nodigt deze gebruiker uit |
| Uitzonderingen         | De admin nodigt een account uit die niet bestaat.                                                                                                                                       |
| Niet-Functionele Eisen | Meerdere gebruikers in een keer uitnodigen.                                                                                                                                             |
| Postconditie           | De admin kan gebruikers uitnodigen naar zijn project.                                                                                                                                   |

| Naam                   | Verwijderd gebruikers uit project                                                                                                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                |
| Actor                  | Gebruiker / Admin                                                                                                                                                                                  |
| Preconditie            | De Admin is op de beheer pagina van project X                                                                                                                                                      |
| Scenario               | De admin wilt een gebruiker verwijderen uit het project, hiervoor gaat hij naar de beheer pagina van het project. Dan naar het gebruikers stuk en klikt op "verwijder" bij de gebruiker zijn naam. |
| Uitzonderingen         | geen                                                                                                                                                                                               |
| Niet-Functionele Eisen | Meerdere gebruikers kunnen verwijderen uit het project in een keer.                                                                                                                                |
| Postconditie           | De admin kan gebruikers verwijderen uit het project.                                                                                                                                               |

| Naam                   | Geeft gebruikers een rol                                                             |
| ---------------------- | ------------------------------------------------------------------------------------ |
| Versie                 | 1.0                                                                                  |
| Actor                  | Gebruiker / Admin                                                                    |
| Preconditie            | De Admin gaat naar de beheer pagina van project X en is bij de lijst van gebruikers. |
| Scenario               | bij de gebruikers is een dropdown knop met alle rollen: "Manager"/"Ontwikkelaar".    |
| Uitzonderingen         | Gebruiker heeft de gewenste rol al                                                   |
| Niet-Functionele Eisen | Meerdere rollen toevoegen aan een gebruiker.                                         |
| Postconditie           | De admin kan gebruikers rollen geven.                                                |

| Naam                   | Manager voegt requirements toe                                                                                                                                                                                                                  |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                                                             |
| Actor                  | Gebruiker / Manager                                                                                                                                                                                                                             |
| Preconditie            | De Manager bevindt zich in project X op de requirements pagina<br>De gebruiker is ingelogd                                                                                                                                                      |
| Scenario               | Een gebruiker met de rol "manager" wilt een requirement toevoegen aan het project, de gebruiker klikt op "voeg toe" waar de manager een titel geeft en een beschrijving. Daarna klikt hij op "Voeg toe" en zal een requirement toegevoegd zijn. |
| Uitzonderingen         | De gebruiker houdt de titel leeg.<br><br>De gebruiker houdt de beschrijving leeg                                                                                                                                                                |
| Niet-Functionele Eisen | Meerdere requirements toevoegen in een keer.                                                                                                                                                                                                    |
| Postconditie           | De gebruikers met de rol "manager" kunnen requirements toevoegen aan een project.                                                                                                                                                               |

| Naam                   | Haalt status van project op                                                                                                                                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                                                                                       |
| Actor                  | Gebruiker / Admin / Manager / Tester                                                                                                                                                                                                                                      |
| Preconditie            | De gerbruiker bevindt zich op de pagina van project X<br>De gebruiker is ingelogd                                                                                                                                                                                         |
| Scenario               | De gebruiker klikt op de AI prompt en vraagt om de status van het project "geef mij de releasegereedheid van het project". Waar de AI gaat kijken naar de voltooide taken, tests en afhankelijkheden van het project en geeft hier een korte duidelijke samenvatting van. |
| Uitzonderingen         | De gebruiker vraagt om de status van een onderwerp dat niet bestaat.                                                                                                                                                                                                      |
| Niet-Functionele Eisen | Meerdere statussen van verschillende projecten ophalen.                                                                                                                                                                                                                   |
| Postconditie           | Elke gebruiker in een project kan de status van een project ophalen.                                                                                                                                                                                                      |


| Naam                   | Ontwikkelaars voegen taken of afhankelijkheden toe                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Versie                 | 1.0                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| Actor                  | Gebruiker / Ontwikkelaar                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| Preconditie            | De Ontwikkelaar bevindt zich op de pagina "taken" of "afhankelijkheden" van project X <br>De gebruiker is ingelogd                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Scenario               | Ontwikkelaars moeten taken of afhankelijkheden toevoegen aan requirements. Dit wordt gedaan onder de pagina's: "taken" of "afhankelijkheden". Op deze paginas staat een "voeg toe" knop waar de gebruiker op kan klikken om een "taak" of de andere toe te voegen. Hierbij wordt een formulier laten zien met een dropdown van de requirements waar de ontwikkelaar de taak of andere aan kan koppelen. Daarnaast ook een titel en beschrijving. Zodra deze zijn ingevult zal de ontwikkelaar op de knop "voeg toe" klikken en zal de taak of andere toegevoegd zijn aan het project |
| Uitzonderingen         | Titel, Beschrijving of requirement is leeg/niet geselecteerd.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| Niet-Functionele Eisen | Meerdere taken of afhankelijkheden toevoegen in een keer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Postconditie           | De ontwikkelaars kunnen een taak, test of afhankelijkheid toevoegen aan een requirement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

| Naam                   | Ontwikkelaars kunnen taken of afhankelijkheden afvinken                                                                                                                                                                                       |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                                                           |
| Actor                  | Gebruiker / Ontwikkelaar                                                                                                                                                                                                                      |
| Preconditie            | De Ontwikkelaar bevindt zich op de pagina "taken" of "afhankelijkheden" van project X <br>De gebruiker is ingelogd                                                                                                                            |
| Scenario               | Een ontwikkelaar heeft zijn taak afgerond waardoor deze taak afgevinkt moet worden. De ontwikkelaar klikt op het vinkje waardoor de taak automatisch op afgerond staat. De taak kan pas afgevinkt worden zodra alle tests ook zijn afgevinkt. |
| Uitzonderingen         | geen                                                                                                                                                                                                                                          |
| Niet-Functionele Eisen | meerdere taken in een keer afvinken                                                                                                                                                                                                           |
| Postconditie           | De ontwikkelaars kunnen taken, tests of afhankelijkheden afvinken.                                                                                                                                                                            |

| Naam                   | Testers kunnen tests toevoegen en koppelen                                                                                                                                                                                                    |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                                                           |
| Actor                  | Gebruiker / Tester                                                                                                                                                                                                                            |
| Preconditie            | De Tester bevindt zich op de pagina "tests" of "afhankelijkheden" van project X <br>De gebruiker is ingelogd                                                                                                                                  |
| Scenario               | Een ontwikkelaar heeft zijn taak afgerond waardoor deze taak afgevinkt moet worden. De ontwikkelaar klikt op het vinkje waardoor de taak automatisch op afgerond staat. De taak kan pas afgevinkt worden zodra alle tests ook zijn afgevinkt. |
| Uitzonderingen         | geen                                                                                                                                                                                                                                          |
| Niet-Functionele Eisen | meerdere taken in een keer afvinken                                                                                                                                                                                                           |
| Postconditie           | De ontwikkelaars kunnen taken, tests of afhankelijkheden afvinken.                                                                                                                                                                            |


| Naam                   | Ontwikkelaars AI gebruiken om een ontwikkeltaak voortebereiden                                                                                                             |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                        |
| Actor                  | Gebruiker / Ontwikkelaars                                                                                                                                                  |
| Preconditie            | De Ontwikkelaar bevindt zich op de pagina project X (waar X de projectnaam is)<br>De gebruiker is ingelogd                                                                 |
| Scenario               | De ontwikelaar vraagt aan de AI om te helpen met het maken/bedenken van ontwikkeltaken voor de requirements. Waar de ai een korte lijst geeft met mogelijke ontwikkeltaken |
| Uitzonderingen         | De ontwikkelaar vraagt aan de ai om 30 ontwikkeltaken toe te voegen aan het project terwijl de AI maximaal 3 taken kan voorstellen.                                        |
| Niet-Functionele Eisen | Meerdere taken in een keer toevoegen.                                                                                                                                      |
| Postconditie           | De ontwikkelaar kan gebruik maken van AI om taken, tests of afhankelijkheden voor te bereiden voor het project.                                                            |


| Naam                   | Missende tests/testresultaten/afhankelijkheden ophalen met AI                                                                                                                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Versie                 | 1.0                                                                                                                                                                                                                                                                           |
| Actor                  | Gebruiker / Tester                                                                                                                                                                                                                                                            |
| Preconditie            | De Ontwikkelaar bevindt zich op de pagina project X (waar X de projectnaam is)<br>De gebruiker is ingelogd                                                                                                                                                                    |
| Scenario               | De ontwikkelaars willen graag weten of er tests zijn die missen in het project die er eigenlijk in moesten zitten, of testresultaten die missen van uitgevoerde tests. Hierbij toont de AI een lijst met tests die missen voor de requirements en/of missende testresultaten. |
| Uitzonderingen         | geen.                                                                                                                                                                                                                                                                         |
| Niet-Functionele Eisen | een test geschreven krijgen van de AI (dus als in code).                                                                                                                                                                                                                      |
| Postconditie           | De ontwikkelaars kunnen missende tests / testresultaten / afhankelijkheden ophalen met AI.                                                                                                                                                                                    |

## Wireframes
De wireframes van het project bevindt zich in het document: "[[(B.2) Wireframes - DevPly]]"


## Kosten
Sinds het hosten van een platform niet gratis is zullen er eventuele kosten komen. 

- Domeinnaam: __€10,- tot €100,- p/yr__
- Hosting service __€50,- tot €100,- p/m__

## Planning

| Dag      | Fase                       | Taak                                                                           | Uren |
| -------- | -------------------------- | ------------------------------------------------------------------------------ | ---- |
| 04-11-26 | Requirements & Analyse     | Kennismakingsgesprek                                                           | 0.5  |
| 06-11-26 | Requirements & Analyse     | Projectplan opzetten en repository opstellen                                   | 7    |
| 07-11-26 | Design & Ontwerp           | Functioneel ontwerp opzetten                                                   | 7    |
| 09-11-26 | Design & Ontwerp           | Wireframes ontwerpen                                                           | 7    |
| 11-11-26 | Design & Ontwerp           | Functioneel ontwerp afronden                                                   | 2    |
| 11-11-26 | Requirements & Analyse     | Voortgangsgesprek productowner                                                 | 0.5  |
| 11-11-26 | Design & Ontwerp           | Technisch ontwerp opzetten                                                     | 3    |
| 13-11-26 | Design & Ontwerp           | Technisch ontwerp afronden                                                     | 4    |
| 13-11-26 | Realisatie Core            | Programmeer omgeving opstellen                                                 | 3    |
| 15-11-26 | Realisatie Core            | Homepagina & Authenticatie realiseren                                          | 7    |
| 18-11-26 | Realisatie Core            | Admin pagina realiseren (E-2, E-3)                                             | 3.5  |
| 18-11-26 | Design & Ontwerp           | Testplan opstellen                                                             | 3.5  |
| 20-11-26 | Realisatie Core            | Project(en) aanmaken                                                           | 3    |
| 20-11-26 | Realisatie Core            | Uitnodigingen en Gebruikers Acceptaties (E-5, E-6)                             | 4    |
| 22-11-26 | Realisatie Core            | Rollen en Rechten beheer (E-7, E-16)                                           | 3    |
| 22-11-26 | Realisatie Core            | Project beheer pagina                                                          | 4    |
| 25-11-26 | Realisatie Core            | Project requirements beheren (E-8)                                             | 3    |
| 25-11-26 | Realisatie Core            | Ontwikkeltaken beheren/koppelen (E-9, E-11)                                    | 4    |
| 27-11-26 | Realisatie Core            | Tests beheren/koppelen (E-10, E-11)                                            | 3    |
| 27-11-26 | Realisatie Core            | Afvinken Taken/Tests (E-12)                                                    | 2    |
| 27-11-26 | Testen & Validatie         | Testen van de applicatie                                                       | 1    |
| 27-11-26 | Testen & Validatie         | ^^^^^^^ --> Testrapport Schrijven                                              | ^    |
| 29-11-26 | Realisatie & AI Intigratie | API Koppeling maken voor MCP                                                   | 7    |
| 02-12-26 | Realisatie & AI Intigratie | AI chat                                                                        | 7    |
| 04-12-26 | Realisatie & AI Intigratie | MIssende requirements/testen ophalen (E-13, E-15)                              | 7    |
| 06-12-26 | Realisatie & AI Intigratie | Releasegereedheid en Samenvatting (E-4)                                        | 7    |
| 09-12-26 | Testen & Validatie         | AI-functies (Validatie output, Edge cases, Prompt tuning)                      | 3    |
| 09-12-26 | Testen & Validatie         | ^^^^^^^ --> Testrapport Schrijven                                              | ^    |
| 09-12-26 | Realisatie AI Intigratie   | Bugs fixen van vorige test                                                     | 4    |
| 11-12-26 | Testen & Validatie         | End-End Testen met de opdrachtgever                                            | 3    |
| 11-12-26 | Testen & Validatie         | ^^^^^^^ --> Testrapport Schrijven                                              | ^    |
| 11-12-26 | Testen & Validatie         | ^^^^^^^ --> Bugs fixen van vorige test                                         | ^    |
| 13-12-26 | Realisatie Core            | Front-end verbeteren                                                           | 4    |
| 13-12-26 | Oplevering                 | README, API docs, Gebruikshandleiding                                          | 3    |
| 16-12-26 | Testen & Validatie         | Onvoorziene bugs / Performance / Beveiliging check en testen van de applicatie | 7    |
| 22-01-27 | **Deadline**               |                                                                                | -    |
