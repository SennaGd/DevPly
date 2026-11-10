Datum 03 / 11 / 2026

## Inleiding
Dit document beschrijft het functioneel ontwerp van het development- en releaseplatform (DevPly) Het platform wordt gebruikt om de voortgang van een project(en) te raadplegen In  een project komen verschillende Requirements / Acceptatiecriteria, Ontwikkeltaken en Tests/Resultaten. Elke requirement kan gekoppelt worden aan een (of meerdere) Ontwikkeltaken, Afhankelijkheden en Tests. Dus op basis van de gemaakte taken, afhankelijkheden en geaccepteerde tests kan er uigehaald worden wanneer het project releaseklaar is. 
Projecten kunnen aangemaakt worden door een gebruiker (maakt niet uit wie het is iedereen mag een project starten), de aanmaker krijgt automatisch de rol als: _admin_. In het project zal de admin andere gebruikers kunnen uitnodigen. Deze gebruikers kunnen het verzoek weigeren/accepteren. ___DE GEBRUIKERS KUNNEN ZELF EEN ROL KIEZEN? DE ADMIN KIEST EEN ROL VOOR DE UITGENODIGDE GEBRUIKER? DE ADMIN GEEFT DE GEBRUIKERS EEN ROL NADAT ZE IN HET PROJECT ZITTEN___. 
Wanneer een gebruiker de rol als _manager_ krijgt zal deze gebruiker requirements van een project kunnen beheren en als _ontwikkelaar_ kan de gebruiker ontwikkeltaken, testgevallen/resultaten, afhankelijkheden toevoegen en deze koppelen aan gemaakte requirements.  

## Situatiebeschrijving
### Huidige Situatie
Momenteel om de voortgang te gebruiker kunnen bedrijven gebruik maken van programma's zoals _Github Projects_, _Trello_. Deze programma's zijn goed voor het verdelen van taken en om terug te zien wie wat heeft gemaakt. Maar het probleem met deze programma's is dat ze geen projectstatus or releasegereedheid kunnen terug halen.

### Gewenste Situatie
De applicatie zal ervoor zorgen dat teams verschillende projecten kunnen beheren waarbij managers de requirements van een project kunnen toevoegen en ontwikkelaars ontwikkeltaken, tests en afhankelijkheden aan de requirements kunnen toevoegen. Er komt ook een geintegreerde AI model in de applicatie waar missende tests, de status van het project kunnen opgehaald worden en voor ontwikkelaars ook nog ontwikkeltaken voorbereiden.  

## Requirements

## Use-Case
### Diagram![[DevPly_Use_Case.png]]

### Tabellen

| Naam                   | Maakt een account aan                                                                                                                                                                                                                                                |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | De gebruiker moet een nieuw account aanmaken, hiervoor gaat hij naar de pagina "sign up" waar hij een formulier met accountgegevens (email, wachtwoord en gebruikersnaam) die hij in moet vullen. Daarna klikt hij op "Maak Account" en zal ook direct ingelogd zijn |
| Uitzonderingen         | De gebruiker maakt een account aan met een email/gebruikersnaam die al in gebruik is.                                                                                                                                                                                |
| Niet-Functionele Eisen | De gebruiker moet zijn telefoonnummer gebruiken om een account aan te maken.                                                                                                                                                                                         |
| Postconditie           | De gebruiker kan gemakkelijk een account aanmaken met een geldig email, wachtwoord en gebruikersnaam.                                                                                                                                                                |

| Naam                   | Logged in                                                                                                                                                                                                            |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | De gebruiker gaat naar de login pagina waar hij een formulier krijgt van inlog-gegevens (email en wachtwoord) die hij in moet vullen met zijn gegevens. Daarna klikt hij op "log in" en zal succesvol ingelogd zijn. |
| Uitzonderingen         | De gebruiker typt een verkeed wachtwoord of gebruikersnaam/email in waardoor hij niet kan inloggen                                                                                                                   |
| Niet-Functionele Eisen | Email ontvangen zodra er een foute inlog-poging is gedaan.                                                                                                                                                           |
| Postconditie           | De gebruiker kan succesvol inloggen met de juiste inlog-gegevens.                                                                                                                                                    |

| Naam                   | Maakt nieuw project aan                                                                                                                                                                                                                    |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Scenario               | De gebruiker gaat naar de pagina "Projects" en klikt vervolgens op het knopje "New" waar hij een klein formulier krijgt om gegevens van het project in te typen. Dan klikt hij op "maak project" en zal er een nieuw project gemaakt zijn. |
| Uitzonderingen         | De gebruiker maakt een project aan zonder geldig projectnaam.<br><br>De gebruiker maakt een project aan met een projectnaam die al gebruikt is.                                                                                            |
| Niet-Functionele Eisen |                                                                                                                                                                                                                                            |
| Postconditie           | De gebruiker kan een nieuw project aanmaken.                                                                                                                                                                                               |

| Naam                   | Verwijderd project                                                                                                                                                                                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Scenario               | De gebruiker(admin) wilt een project verwijderen, hiervoor gaat hij naar de beheer pagina van het project en klikt op "Verwijder Project" hiervoor moet de gebruiker zijn eigen wachtwoord intypen als confirmatie, zodra dat gedaan is zal het project verwijderd zijn. |
| Uitzonderingen         | De admin typt een verkeerd wachtwoord in.                                                                                                                                                                                                                                |
| Niet-Functionele Eisen | Email verificatie.<br>Meerdere projecten in een keer verwijderen.                                                                                                                                                                                                        |
| Postconditie           | De gebruiker(admin) kan een project verwijderen.                                                                                                                                                                                                                         |

| Naam                   | Nodigt gebruikers uit naar project                                                                                                                                                      |
| ---------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | De gebruiker(admin) wilt gebruikers uitnodigen naar het project. Hiervoor gaat hij naar de beheer pagina van een project. Daar zoekt hij op gebruikersnaam en nodigt deze gebruiker uit |
| Uitzonderingen         | De admin nodigt een account uit die niet bestaat.                                                                                                                                       |
| Niet-Functionele Eisen | Meerdere gebruikers in een keer uitnodigen.                                                                                                                                             |
| Postconditie           | De admin kan gebruikers uitnodigen naar zijn project.                                                                                                                                   |

| Naam                   | Verwijderd gebruikers uit project                                                                                                                                                                  |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | De admin wilt een gebruiker verwijderen uit het project, hiervoor gaat hij naar de beheer pagina van het project. Dan naar het gebruikers stuk en klikt op "verwijder" bij de gebruiker zijn naam. |
| Uitzonderingen         | geen                                                                                                                                                                                               |
| Niet-Functionele Eisen | Meerdere gebruikers kunnen verwijderen uit het project in een keer.                                                                                                                                |
| Postconditie           | De admin kan gebruikers verwijderen uit het project.                                                                                                                                               |

| Naam                   | Geeft gebruikers een rol                                                                                                                                                           |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | De admin wilt nieuwe gebruikers een rol geven, dit doet hij op de beheer pagina van het project, bij de gebruikers is een dropdown knop met alle rollen: "Manager"/"Ontwikkelaar". |
| Uitzonderingen         | Geen                                                                                                                                                                               |
| Niet-Functionele Eisen | Meerdere rollen toevoegen aan een gebruiker.                                                                                                                                       |
| Postconditie           | De admin kan gebruikers rollen geven.                                                                                                                                              |

| Naam                   | Manager voegt requirements toe                                                                                                                                                                                                                                                                 |
| ---------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | Een gebruiker met de rol "manager" wilt een requirement toevoegen aan het project, hiervoor gaat deze gebruiker naar de requirements pagina en klikt op "voeg toe" waar de manager een titel geeft en een beschrijving. Daarna klikt hij op "Voeg toe" en zal een requirement toegevoegd zijn. |
| Uitzonderingen         | De gebruiker houdt de titel leeg.<br><br>De gebruiker houdt de beschrijving leeg                                                                                                                                                                                                               |
| Niet-Functionele Eisen | Meerdere requirements toevoegen in een keer.                                                                                                                                                                                                                                                   |
| Postconditie           | De gebruikers met de rol "manager" kunnen requirements toevoegen aan een project.                                                                                                                                                                                                              |

| Naam                   | Haalt status van project op                                                                                                                                                                                                                                               |
| ---------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | De gebruiker klikt op de AI prompt en vraagt om de status van het project "geef mij de releasegereedheid van het project". Waar de AI gaat kijken naar de voltooide taken, tests en afhankelijkheden van het project en geeft hier een korte duidelijke samenvatting van. |
| Uitzonderingen         | De gebruiker vraagt om de status van een onderwerp dat niet bestaat.                                                                                                                                                                                                      |
| Niet-Functionele Eisen |                                                                                                                                                                                                                                                                           |
| Postconditie           | Elke gebruiker in een project kan de status van een project ophalen.                                                                                                                                                                                                      |


| Naam                   | Ontwikkelaars voegen taken,tests of afhankelijkheden toe                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | Ontwikkelaars moeten taken, tests of afhankelijkheden toevoegen aan requirements. Dit wordt gedaan onder de pagina's: "taken", "tests", "afhankelijkheden". Op deze paginas staat een "voeg toe" knop waar de gebruiker op kan klikken om een "taak" of de andere toe te voegen. Hierbij wordt een formulier laten zien met een dropdown van de requirements waar de ontwikkelaar de taak of andere aan kan koppelen. Daarnaast ook een titel en beschrijving. Zodra deze zijn ingevult zal de ontwikkelaar op de knop "voeg toe" klikken en zal de taak of andere toegevoegd zijn aan het project |
| Uitzonderingen         | Titel, Beschrijving of requirement is leeg/niet geselecteerd.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
| Niet-Functionele Eisen | Meerdere taken, tests of afhankelijkheden toevoegen in een keer.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                   |
| Postconditie           | De ontwikkelaars kunnen een taak, test of afhankelijkheid toevoegen aan een requirement.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |

| Naam                   | Ontwikkelaars kunnen taken, tests of afhankelijkheden afvinken                                                                                                          |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | Een ontwikkelaar heeft zijn taak afgerond waardoor deze taak afgevinkt moet worden. De ontwikkelaar klikt op het vinkje waardoor de taak automatisch op afgerond staat. |
| Uitzonderingen         | geen                                                                                                                                                                    |
| Niet-Functionele Eisen | meerdere taken in een keer afvinken                                                                                                                                     |
| Postconditie           | De ontwikkelaars kunnen taken, tests of afhankelijkheden afvinken.                                                                                                      |


| Naam                   | Ontwikkelaars AI gebruiken om een ontwikkeltaak voortebereiden                                                                                                             |
| ---------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | De ontwikelaar vraagt aan de AI om te helpen met het maken/bedenken van ontwikkeltaken voor de requirements. Waar de ai een korte lijst geeft met mogelijke ontwikkeltaken |
| Uitzonderingen         | De ontwikkelaar vraagt aan de ai om 30 ontwikkeltaken toe te voegen aan het project terwijl de AI maximaal 3 taken kan voorstellen.                                        |
| Niet-Functionele Eisen | Meerdere taken in een keer toevoegen.                                                                                                                                      |
| Postconditie           | De ontwikkelaar kan gebruik maken van AI om taken, tests of afhankelijkheden voor te bereiden voor het project.                                                            |


| Naam                   | Missende tests/testresultaten/afhankelijkheden ophalen met AI                                                                                                                                                                                                                 |
| ---------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Scenario               | De ontwikkelaars willen graag weten of er tests zijn die missen in het project die er eigenlijk in moesten zitten, of testresultaten die missen van uitgevoerde tests. Hierbij toont de AI een lijst met tests die missen voor de requirements en/of missende testresultaten. |
| Uitzonderingen         | geen.                                                                                                                                                                                                                                                                         |
| Niet-Functionele Eisen | een test geschreven krijgen van de AI (dus als in code).                                                                                                                                                                                                                      |
| Postconditie           | De ontwikkelaars kunnen missende tests / testresultaten / afhankelijkheden ophalen met AI.                                                                                                                                                                                    |
## Kosten
Sinds het hosten van een platform niet gratis is zullen er eventuele kosten komen. 

- Domeinnaam:     __€10,- tot €100,-__
- Hosting service __€50,- tot €100,- p/m__

## Planning1

|     |     |
| --- | --- |
|     |     |

