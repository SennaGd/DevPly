# opdrachtgever -> Imholz

_development en release platform voor ontwikkelaars_

__Vragen__
- Einddatum / Projectduur
	-> Hoelang duurt het project?
- Meerdere gebruikers in een project?
- Testomgeving voor projecten of voor de dev-release platform?
- Kleurenthema? 
	-> donker, licht. rood, blauw, etc.
- Wat wordt er bedoeld met -> 3. Functionele scope (proefproeve)
	"externe commits, issues of pull requests"?
	"Afhankelijkheden"?
	
__Bijzaken voor Product owner__
- Meetings inplannen
- Contact via teams, meetings of ander programma

__MCP Use-cases__
1. Automatische code reviews
2. Geautomatiseerde feedback 
3. Issue tracking
4. Projectstatus onderzoeken -> hoe ver het project is voor productie
5. Ontbrekende testdekking 
6. Openstaande requirements vinden
7. Een ontwikkeltaak voorbereiden
8. Een releasesamenvatting voorbereiden

__Eisen__
1. MCP
2. RESTful / Passende API	-> Python (FastApi?)
3. Database					-> SQLModel (gemaakt voor FastApi ^^^) 
4. Authenticatie			-> 
5. Frontend Framework		-> Svelte (Leesbare Syntax) of Vue 3 (Duidelijke scheiding van elementen)
6. README met installatie-, configuratie en startinstructies 

__Security__
1. Gebruikers validatie		-> gebruiker zonder account zal niet gebruik kunnen maken van een LLM (voorkomt spam/server overload)
2. Input validatie			-> De validatie wordt door gestuurd naar een API-endpoint die checked tegen SQL-injecties 
3. Typescript				-> wordt gebruikt voor de base-validation geintigreerd met de zod validatie library  
4. .env						-> voor api-keys en secrets 
5. 2 factor authenticatie	-> extra laag voor veiligheid

__Pagina's__
_(Zonder Account)_
1. Homepagina	-> 
2. Inlogpagina  ->.

_(Standaard Gebruiker)_
3. Projecten
4. ↪ Project 
5.	 ↪ Taken				-> Taken die in project zitten (hierbij komen ook voltooide taken)
6.	 ↪ Tests				-> Testomgeving om het product live te testen <------------------------ Moeilijke taak
	   ↪ Testgevallen
	   ↪ Testresultaten
7.	 ↪ Releases				-> Alle gemaakte releases
8.   ↪ Project-Requirements -> Lijst met requirements voor het project

__Database Architectuur__
_Gebruiker/User_
- user_id	(Primary)
- username	(Len: 4)
- email		(Needs: "@" + ".")
- password	(Len: 8, Num: 4)

_Projecten/Projects_
- project_id (Primary)
- user_id	(Linked to `User`)
- project_name (Len: 4)
- 

