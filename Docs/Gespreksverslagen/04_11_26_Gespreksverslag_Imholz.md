Gespreksverslag Imholz - DevPly 

Datum: 04 / 11 / 2026  
Tijd: 11:00 -> 11:36
Locatie: Firda Harste 4-6, Lokaal: C111  
Aanwezig: Sven Imholz ( Productowner )  
Auteur: Senna Draaijer

Dit gesprek vond plaats om de benodigde functionaliteiten en eisen vast te stellen voor het development- en releaseplatform project, hierbij worden een aantal vragen gesteld aan de productowner om een beeld te krijgen van het gegeven project. Hierbij zijn een paar vragen vastgesteld. Deze staan onder het kopje _vragen_. 

De eerste vraag dat ik had gesteld was of het een github clone was, hierbij werd verteld dat het project niet een github clone is maar meer een inspiratie is van "github projects" / "github issues". Denk hieraan een management systeem/backlog systeem waar ontwikkelaars en managers een inzicht krijgen van het gemaakte project en eventuele releaseversies.

Bij de tweede vraag was of er meerdere gebruikers in een project kunnen zitten. Bij de vorige vraag was al geconcludeerd dat managers en ontwikkelaars een inzicht krijgen van hoe productieklaar een project is en wat voor functionaliteiten er nog gemaakt moet worden. 

Daarna vroeg ik of hoe de testomgeving werkte, hierop vertelde Imholz dat er geen bestanden worden opgeslagen in het systeem maar meer dat het een soort Trellobord is, dus voor het testen zullen de ontwikkelaars zelf moeten uitvoeren, waarop zij een checklist door kunnen gaan. 

Tijdens het vragen gingen wij ook door het document: Proefproeve_03_Development_en_releaseplatform heen. Hierbij werden een aantal eisen duidelijk. 

Daarna vroeg ik wat wordt er bedoeld met: "Afhankelijkheden", "Externe commits, issues of pull requests" voor het kopje "Afhankelijkheden" werd mij verteld dat Requirements gekoppelt kunnen worden aan taken, tests en releases. Zolang deze niet overeen komen zal er ook geen release kunnen plaatvinden.

Voor het ontwerp van de applicatie vroeg ik Imholz voor voorkeuren van thema's en kleuren. Hierop reageerde Imholz met "Ik heb eigenlijk geen voorkeuren" dus stelde ik voor om een licht/donker thema te implementeren waarop Imholz akkoord ging. 

Voor de versies van een project stelde meneer Imholz voor dat het drie type's van versies heeft, dit heeft de volgende structuur: "0.0.0" waar 0.0.X de ... is, de "0.X.0" veranderingen zijn in de api/functies dus denk hieraan een hello() functie die van hello() -> hello(name) gaat, stel het is zo dat de functie een standaard waarde heeft zal de versie "0.0.X" veranderen, dus hello(name="Senna") hierbij hoeft de gebruiker geen veranderingen te maken aan de software/code. Voor versies "X.0.0" is het project klaar voor productie, dus elke test is geslaagd en de benodigde eisen zijn gerealiseerd. 

Voor de laatste vraag(en) had ik gevraagd of ik twee keer in de week een onwikkelsgesprek kan hebben, de productowner zei dat ik er van uitmoest gaan dat hij minstens een keer in de week wel kan maar twee wordt wel moeilijker sinds hij ook een docent is met afwisselende taken. Dus heb ik afgesproken met Imholz dat ik hem een bericht zal sturen om een gesprek aan te vragen.

**Vragen**
- Is het een clone van github?
- Meerdere gebruikers in een project?
- hoe werkt de testomgeving?
- Voorkeur kleurenthema?
- Wat wordt er bedoeld met "Afhankelijk" en "externe commits, issues of pull requests"?

**Wijzigingsverzoeken**
Tijdens het bespreken van het project zijn er een paar wijzingen gemaakt, hieronder bevinden zich de gemaakte wijzigingen.

---
Bestand -> Proefproeve_03_Development_en_releaseplatform.docx
Kopje	-> 3.Functionele Scope 
Wijziging: onder het kopje "Gegevens en domeinobjecten" bevind zich een punt "Externe commits, issues of pull requests" hierbij heeft meneer Imholz aangegeven dat dit niet een verplichte eis is voor het project, sinds het product zonder externe commits zal kunnen werken.

---
Bestand -> Proefproeve_03_Development_en_releaseplatform.docx
Kopje	-> 3.Functionele Scope 
Wijziging: onder het kopje "Minimale Functionaliteit" staat een punt "Externe ontwikkelgegevens synchroniseren en verwerken." Hierbij heeft de productowner aangegeven dat deze functionaliteit niet een verplichte functionaliteit is. Net als het de vorige wijziging is het product niet hier afhankelijk van. Hierbij heb ik de productowner gevraagd of het een could have is waarop hij "Ja dat kan" antwoordde. 

Dat concludeerd de verandering de eis naar een Could-Have.

---
Bestand -> Proefproeve_03_Development_en_releaseplatform.docx
Kopje	-> X
Wijziging: Licht/Donker thema schakelaar/functie. Waar de gebruiker kan schakelen tussen een licht of donker thema. 
Hierop Antwoordde Imholz met "ja, is goed."

**Verbetervoorstellen**
Thema schakelaar -> licht/donker thema

