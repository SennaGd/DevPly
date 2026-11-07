Gemaakt door Senna Draaijer
Datum 02 / 11 / 2026

---
## Inleiding
Ik heb de opdracht gekregen van Sven Imholz, om een development- en releaseplatform te programmeren geinspireerd op _github projects_ / _trello_. Het project is in het kort een projectmanagementtool waar softwareteams hun werk en planning kunnen beheren. Hierdoor krijgt iedereen in het team een inzicht wat er gedaan moet worden, wat al af is en wat de eisen zijn voor het project. 

Dit projectplan beschrijft het probleem, de doelen het gewenste resultaat de afbakening eisen risicos randvoorwaarden en een globale planning een 

---
## Projectomschrijving
Binnen softwareteams/bedrijven wordt vaak de vraag gesteld _Wat is de voortgang van een product?_ of _Wat heeft programmeur X gemaakt?_, Vaak is er geen goed inzicht voor managers/werknemers om te checken wat de programmeurs hebben gedaan. Als oplossing wordt er veel gebruikt gemaakt van projectmanagementtools zoals _Github Projects_ en _Trello_, met deze programma's kunnen managers requirements opschrijven waar de ontwikkelaars verschillende taken aan kunnen koppelen. Maar, het probleem met deze applicaties is dat ze geen goed inzicht geven over hoe ver een project voor release is. Voor dit project wordt er een applicatie gemaakt waarin de volledige voortgang van requirement tot release tracebaar is en door een AI-agent onderzocht kan worden. De geintegreerde AI zal missende requirements op kunnen halen, taken maken voor een requirement en de projectstatus/releasegereedheid kunnen ophalen.

Het project is een success wanneer er een goed functionerend, betrouwbaar en transparant platform staat waarin de volledige ontwikkeltraject van verschillende projecten moeiteloos te volgen zijn. Voor zowel managers als ontwikkelaars moet het in een oogopslag helder zijn wat de status van een project is. Daarnaast moet er een AI-agent via een MCP-koppeling aantoonbaar actuele data uit de applicatie kunnen gebruiken om vragen over de projectstatus, releaseblokkers en testresultaten correct te beantwoorden. 

Zodra alle functionaliteiten beschreven in de MoSCoW gerealiseerd zijn zal het product getest moeten worden, wanneer alle _test-cases_ en _acceptatie-testcases_  behaald zijn zal het product af zijn. 

---
## Doelstelling
- Om de voorgang van een project te krijgen.
- Een overzicht te krijgen hoe ver een product klaar is voor release.
- Om te kunnen zien wat verschillende programmeurs hebben gemaakt/bezig mee zijn.
- Om het ontwikkelproces aan te kunnen tonen voor managers/oprachtgevers.


## Resultaat
Een gebruiker zal een nieuw project kunnen starten, zodra er een nieuw project is gemaakt zal de aanmaker een _hoofdgebruiker_ / _admin_ zijn over het project waardoor deze gebruiker volledige controle heeft over het project. De admin kan in het project een beschrijving toevoegen om voor andere ontwikkelaars / managers aan te kunnen tonen wat het project inhoudt. 
De hoofgebruiker zal in het project gebruikers kunnen uitnodigen en deze een rol geven, de rollen zijn: _Manager_ / _Ontwikkelaar_.  De gebruikers die als rol _manager_ hebben gekregen zullen de requirements van het project kunnen toevoegen waarbij de _ontwikkelaars_ weer taken kunnen toevoegen. De ontwikkelaars kunnen hierbij ook verschillende ontwikkeltaken, testgevallen/resultaten, afhankelijkheden toevoegen en deze koppelen aan requirements. 
Voor de voortgang/releasegereedheid te bepalen van een project zal er gekeken worden naar de requirements, zodra alle requirements zijn gerealiseerd zal het product klaar voor release zijn. 
De ontwikkelaars kunnen gebruik maken van de geintegreerde AI om missende requirements,  gefaalde/niet gemaakte testresultaten op te kunnen halen en om ontwikkeltaken/releasesamenvatting voortebereiden.
Voor managers is het vooral belangrijk om de status van een project te krijgen. Hiervoor wordt ook gebruik gemaakt van de AI, die zal door het project kijken naar de requirements, gemaakte ontwikkeltaken en testresultaten. Hiermee zal de AI aan de manager de status/releasegereedheid meegeven.


### Samenvatting resultaten
**Project aanmaken & eigenaar**
*   Een gebruiker kan een nieuw project starten.
*   De aanmaker wordt automatisch **admin** (hoofdgebruiker) en heeft volledige controle.

**Projectinformatie**
*   De admin kan een beschrijving toevoegen zodat iedereen begrijpt waar het project over gaat.

**Uitnodigen & Rollen**
*   De admin kan mensen uitnodigen en hun een rol geven:
    *   **Manager:** Mag *requirements* (eisen/wensen) aanmaken.
    *   **Ontwikkelaar:** Mag *taken* aanmaken, testen uitvoeren/resultaten noteren en afhankelijkheden leggen. Ontwikkelaars koppelen hun werk aan de requirements van de manager.

**Voortgang & Release**
*   Een project is **klaar voor release** zodra *alle* requirements zijn afgerond.

**Hulp van AI (voor Ontwikkelaars)**
*   Ontwikkelaars kunnen de AI vragen om:
    *   Ontbrekende requirements te vinden.
    *   Mislukte of ontbrekende testresultaten op te sporen.
    *   Een voorbereiding te maken voor ontwikkeltaken of een releasesamenvatting.

**Hulp van AI (voor Managers)**
*   Managers krijgen van de AI een **overzicht van de status** en **releasegereedheid**.
*   De AI kijkt daarvoor naar: requirements, gemaakte taken en testresultaten.

---
## Afbakening - MoSCoW

| ID     | EIS                                                                             | Prioriteit  |
| ------ | ------------------------------------------------------------------------------- | ----------- |
| E - 1  | Inloggen / Account aanmaken                                                     | Must-Have   |
| E - 2  | Projecten aanmaken                                                              | Must-Have   |
| E - 3  | Projecten beheren                                                               | Must-Have   |
| E - 4  | Releasegereedheid op kunnen halen met de geintegreerde AI                       | Must-Have   |
| E - 5  | Gebruikers uitnodigen aan projecten                                             | Must-Have   |
| E - 6  | Projectuitnodigingen accepteren                                                 | Must-Have   |
| E - 7  | Gebruikers rollen beheren (hoofdgebruiker)                                      | Must-Have   |
| E - 8  | Requirements kunnen toevoegen (manager)                                         | Must-Have   |
| E - 9  | Ontwikkeltaken toevoegen aan project (ontwikkelaar)                             | Must-Have   |
| E - 10 | Tests / Testresultaten toevoegen aan project (ontwikkelaar)                     | Must-Have   |
| E - 11 | Requirements koppelen aan taken, tests en releases (ontwikkelaar)               | Must-Have   |
| E - 12 | Ontwikkeltaken, Tests, Testresultaten afvinken (ontwikkelaar)                   | Must-Have   |
| E - 13 | Releasegereedheid kunnen ophalen met de geintegreerde AI                        | Must-Have   |
| E - 14 | Ontwikkeltaken voorbereiden/aanmaken met de geintegreerde AI                    | Must-Have   |
| E - 15 | Ontbrekende testresultaten voor de requirements ophalen met de geintegreerde AI | Must-Have   |
| E - 16 | Projectbeschrijving aan project toevoegen                                       | Should-Have |
| E - 17 | Licht / Donker thema knop                                                       | Could-Have  |
| E - 18 | Uitloggen                                                                       | Could-Have  |
| E - 19 | Account bewerken                                                                | Could-Have  |
| E - 20 | Projecten zoeken met een form                                                   | Could-Have  |
| E - 21 | Meerdere AI Modellen                                                            | Wont-Have   |

---
## Risicoanalyse
| Risico                                                                                 | Impact op opdrachtgever | Kans   |
| :------------------------------------------------------------------------------------- | :---------------------- | :----- |
| Onvoldoende/te late feedback door beperkte **beschikbaarheid**                         | Hoog                    | Hoog   |
| AI-output onbetrouwbaar / **hallucinaties** in requirements en taken                   | Hoog                    | Hoog   |
| Opdrachtgever is ziek, waardoor er **geen feedback/beslissingen mogelijk zijn**        | Middel                  | Middel |
| SQL-Injectie beveiligingsrisico, waardoor bots/gebruikers de database kunnen leeghalen | Hoog                    | Laag   |
|                                                                                        |                         |        |

---

## Randvoorwaarde
- De opdrachtgever is elke week minimaal 30 minuten fysiek beschiktbaar voor het beantwoorden van vragen
- De opdrachtgever is elke twee weken beschiktbaar voor het testen van de applicatie.
- De opdrachtgever is beschiktbaar via teams om vragen te beantwoorden.

---
## Fasering

| Fase                              | Periode                         | Belangrijkste Activiteiten                                                                                                                                           | OpleverProduct                                                                   |
| :-------------------------------- | :------------------------------ | :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------- |
| **1. Requirements & Analyse**     | Week 1/2<br>(02 – 15 nov)       | project-start, eisen verzamelen/valideren met opdrachtgever, gebruikersrollen & rechten definieren, acceptatie criteria.                                             | Programma van Eisen (PvE) + Acceptatiecriteria                                   |
| **2. Design**                     | Week 2-3<br>(11 – 22 nov)       | Functioneel ontwerp (user flows, UI wireframes), Technisch ontwerp (architectuur, database, API-verbindingen, AI-service laag), Teststrategie & testcases opstellen. | Functioneel Ontwerp, Technisch Ontwerp, Testplan, Wireframes, Testcases/Testplan |
| **3. Realisatie Core**            | Week 4 – 6<br>(25 nov – 20 dec) | Auth, Project/gebruikersbeheer, rollen, Requirements CRUD, Taken CRUD, Testen CRUD, Koppelingen, Status flows.                                                       | Werkende Core Applicatie (Zonder AI)                                             |
| **4. Realisatie & AI-Integratie** | Week 7 – 9<br>(6 – 24 jan)      | AI-service laag bouwen, Taken genereren (E-14), Missende req/tests detecteren (E-13, E-15), Releasegereedheid (E-4).                                                 | Werkende Applicatie met AI-functies                                              |
| **5. Testing & Validatie**        | Week 3 – 9<br>(25 nov – 24 jan) | Unit/Integratietesten tijdens bouwen.<br>end to end testen van alle rollen, AI-output validatie (kwaliteit), Acceptatietesten met opdrachtgever (2-wekelijks).       | Testrapporten, Ondertekende Acceptatieformulieren                                |
| **6. Oplevering**                 | Week 10<br>(20 – 22 jan)        | Laatste bugfixes, Documentatie (README, Handleiding, API), Demo voorbereiden, Formele overdracht aan opdrachtgever.                                                  | Geaccepteerd Product + Documentatie                                              |

---
## Planning

| Dag      | Taak                                                                                         | Uren |
| :------- | :------------------------------------------------------------------------------------------- | :--: |
| 06-11-26 | Projectplan en Opzet (Repo, Project structuur)                                               |  5   |
| 11-11-26 | Functioneel ontwerp (Use cases, Datamodel)                                                   |  7   |
| 13-11-26 | Schetsen / Wireframes ontwerpen                                                              |  7   |
| 15-11-26 | Technisch ontwerp (Architectuur, API contracts, AI-service laag)                             |  7   |
| 18-11-26 | Programmeren: Admin beheer (E-2, E-3)                                                        |  5   |
| 20-11-26 | Programmeren: Uitnodigingen en Gebruikers Acceptaties (E-5, E-6)                             |  7   |
| 22-11-26 | Programmeren: Rollen en Rechten beheer (E-7) (E-16)                                          |  7   |
| 25-11-26 | Programmeren: Requirements (E-8)                                                             |  5   |
| 27-11-26 | Programmeren: Ontwikkeltaken CRUD en Koppelen Req-Taken (E-9, E-11)                          |  7   |
| 29-11-26 | Programmeren: Testgevallen/Resultaten CRUD en Koppelen (E-10, E-11)                          |  7   |
| 02-12-26 | Programmeren: Status flow en Afvinken Taken/Tests (E-12)                                     |  5   |
| 04-12-26 | Testen: Integratietesten Project/Gebruikers/Requirements/Taken                               |  7   |
| 06-12-26 | Testrapporten typen en Bugfixes Sprint 1-3                                                   |  7   |
| 09-12-26 | Technisch proef API, Prompts, Response parsing                                               |  7   |
| 11-12-26 | Programmeren: Service laag en Taken voorbereiden (E-14)                                      |  7   |
| 13-12-26 | Programmeren: Missende requirements/testen ophalen (E-13, E-15)                              |  7   |
| 16-12-26 | Programmeren: Releasegereedheid en Samenvatting (E-4)                                        |  5   |
| 18-12-26 | Testen: AI-functies (Validatie output, Edge cases, Prompt tuning)                            |  7   |
| 20-12-26 | Programmeren: Fixen van eventuele bugs van het testen                                        |  7   |
| 23-12-26 | **Kerstvakantie**                                                                            |  -   |
| 25-12-26 | **Kerstvakantie**                                                                            |  -   |
| 27-12-26 | **Kerstvakantie**                                                                            |  -   |
| 30-12-26 | **Kerstvakantie**                                                                            |  -   |
| 01-01-27 | **Kerstvakantie**                                                                            |  -   |
| 03-01-27 | **Kerstvakantie**                                                                            |  -   |
| 06-01-27 | End-to-End Testen: Alle rollen en Flows (Opdrachtgever testronde)                            |  5   |
| 08-01-27 | Bugfixes en UI Polish (Feedback verwerken)                                                   |  7   |
| 10-01-27 | Testen: Releasegereedheid validatie en AI output kwaliteit                                   |  7   |
| 13-01-27 | Documentatie: README, API docs, Gebruikshandleiding                                          |  5   |
| 15-01-27 | Bufferdag: Onvoorziene bugs / Performance / Beveiliging check en testen van de applicatie    |  7   |
| 17-01-27 | Bufferdag: Laatste afronding                                                                 |  7   |
| 20-01-27 | Opleveren Product: Finale acceptatietest / Reflectieverslag Schrijven en opdracht overdragen |  5   |
| 22-01-27 | **Deadline**                                                                                 |  -   |

---

## Algemene Informatie
Productowner: Sven Imholz
Uitvoerder(s): Senna Draaijer

---