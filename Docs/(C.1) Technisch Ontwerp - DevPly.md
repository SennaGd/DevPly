Datum 11 / 11 / 2026


## Inleiding
Dit document beschrijft de technische architectuur en realisatie van de applicatie "DevPly", gebaseerd op de functionele eisen.
In het doucment [[(B.1) Functioneel Ontwerp - DevPly]] bevindt zich de informatie over de applicatie. De doelstelling van dit document is om de functionaliteiten/usecases te realiseren en uit te pakken. De keuzes gemaakt in dit document zijn gebaseerd op de tijd gegeven voor het project (10 weken).


## Plan van Aanpak - DevPly
**Doel:** Realisatie van de webapplicatie "DevPly" voor projectbeheer (requirements, taken, tests) inclusief een AI support en API als backend.

#### **Tijdlijn (10 weken)**
- **Weken 1–2 (Ontwerp en Voorbereiding):** UI-ontwerp in Figma, technische opzet (Git/GitHub, Neovim) en structuur bepalen.
- **Weken 3–5 (Backend en API):** Database opzetten en API-endpoints ontwikkelen. 
- **Weken 6–8 (Frontend en AI):** Ontwikkelen van de web-applicatie (HTML, CSS, TypeScript) en integreren van de AI.
- **Week 2-10 (Testen & Optimaliseren):** Meerdere browsers testen (Google Chrome en Firefox) en API testen (Postman of grep).
- **Week 10 (Oplevering):** Laatste benodigdheden realiseren, product opleveren aan productowner

#### **Belangrijkste Producten**
- **Web-applicatie:** Online bereikbaar voor gebruikers (HTML/CSS/TypeScript).
- **Backend API & Database:** Python FastAPI voor database communicatie en MCP support.
- **Documentatie & Versiebeheer:** Obsidian (notities/documentatie) en GitHub (codebeheer).

## Op te leveren producten
De producten die opgeleverd worden in het project "DevPly" staan hieronder beschreven:

- Een web-applicatie
	Een applicatie die gerealiseerd zal zijn op het internet, die elke werknemer kan bezoeken via een link.
- Een backend API / Database
	Een eindpunt voor het opslaan van data/gebruiken van AI modellen.

## Interfaces
Voor de interfaces voor DevPly zullen er twee hoofd-interfaces zijn, deze staan hieronder beschreven:

- **Web-Applicatie**
	Homepagina
	
	Inlogpagina
	Registreerpagina
	Accountpagina
	Account-beheer-pagina
	
	Projectenpagina
	Projectpagina (Workspace, Requirements, Taken, Tests, Afhankelijkheden)
	Project-beheer-pagina
	Project-workspace-pagina AI Chat 
	
- **API-endpoints**
	Projectstatus ophalen
	Project requirements, ontwikkeltaken, tests en afhankelijkheden ophalen
	
	

## Ontwikkelomgeving
De applicatie wordt ontwikkeld is een web-applicatie, dit betekend dat de applicatie ook moet ontwikkeld/getest worden in een browser. De browser die ik als ontwikkelaar ga gebruiken is "Firefox" maar voor het testen wordt echter ook "Google Chrome" gebruiken sinds deze browser veel wordt gebruikt door bedrijven/mensen.  
  

## Schemas
### Systeemarchitectuur
*high level diagram*
![[System architecture.png]]


### Database Architectuur
![[Database diagram.png]]

## Technischeinfrastructuur
Om de applicatie te werken zijn er bepaalde benodigdheden nodig om dit te realiseren. 

### Activity Diagram
![[Activity diagram — Project platform.png]]
### Ontwikkeltools
Voor dit project worden er verschillende ontwikkeltooks gebruikt. Die staan hieronder beschreven.

**Programmeertalen**
Voor dit project was vastgesteld dat het een web-applicatie is, daardoor zijn staan drie programmeertalen direct al vast: "HTML", "CSS" en "JavaScript/TypeScript" dit zijn essentiele programmeertalen voor het project. Om het eenvoudiger en leesbaarder te realiseren wordt er gebruik gemaakt van de framework "Sveltekit".
Ook wordt er een API opgebouwd, dit zal worden gemaakt in Python met FastApi sinds dit een MCP support. 

-- Samenvatting Programmeertalen --
**Framework**
- Sveltekit | Snel en eenvoudig

**Website**
- HTML | Zit vast aan web-applicaties
- CSS    | Zit vast aan web-applicaties
- TypeScript | JavaScript Zit vast aan web-applicaties, TypeScript is beter voor een stabiele applicatie

**API / MCP**
- Python

**Versiebeheersysteem**
Om versies te beheren voor dit project wordt er gebruik gemaakt van github. SInds github het makkelijk maakt om code te uploaden en bij te houden. Met het gebruik van "Git" zal er efficient een versiebeheer bijgehouden worden.

-- Samenvatting Versiebeheersysteem --
- Github
- Git

**IDE (Code Editor)**
Code editors zijn meer persoonlijke keuzen dan essentiele keuzes voor het project, toch is het goed om uit te leggen waarom de gekozen code editor gebruikt wordt. Voor dit project maak ik gebruikt van NeoVim (Nvim). Dit komt omdat de editor snel opstart, snel is kwa code schrijven, veranderen, verwijderen of opzoeken.

-- Samenvatting IDE --
- Neovim | Snel & Praktisch

**Testtools**
Voor het testen van de applicatie zullen er meerdere programma's gebruikt worden, sinds het een web-applicatie is zal er gebruik gemaakt moeten worden van een browser. De browser om het programma te testen is "Firefox" en "Google Chrome" dit komt omdat verschillende browsers sommige HTML/CSS functionaliteiten nog niet ondersteunen. 
Voor het testen van de API endpoints zal er gebruik gemaakt worden van Postman of het Cli programma "Curl". Om verschillende requests te maken naar de API.

-- Samenvatting Testtools --
**Web-Applicatie**
- Firefox
- Google Chrome

**API**
- Postman
- Curl

**Documentatie- en Projectmanagementtools**
Voor dit project zullen er een paar documentatie/projectmanagement tools worden gebruikt. De documentatie die is geschreven voor dit project wordt gedaan in **Obsidian**. Dit is een markdown text editor om gemakkelijk markdown te typen.

Daarnaast voor de diagrammen wordt er gebruik gemaakt van **Figma**, dit programma wordt veel gebruikt onder de "Mediaformgevers" en is mij aanbevolen door een student die zelf ook die opleiding doet.

Het project is opgeslagen op Github, dit is gedaan omdat Github ook al het versiebeheer regelt. Hiervoor kan je dus ook gemakkelijk oude versies terughalen van de documentatie.

-- Samenvatting Documentatie- en Projectmanagementtools --

- Obsidian | Tekst Editor
- Figma | Diagrammen
- Github | Opslaan