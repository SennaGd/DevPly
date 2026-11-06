# opdrachtgever -> Imholz

_development en release platform voor ontwikkelaars_

__Vragen__
- Gewenste taal? -> taal schakelaar? 
- Wie kan een nieuw project aanmaken?
- Wie beheerd de rollen (managers/ontwikkelaars)
- Zitten er ook wegingen op ontwikkeltaken om de voortgang eventueel duidelijker te maken?
- Wie bepaald wanneer een project af is? zijn dat de managers of ontwikkelaars?
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

