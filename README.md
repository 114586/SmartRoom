## Flask
In folder flask staat file main.py.
main.py is backend webserver. Frontend files meoten in static folder (default folder van flask). 
Frontend (interface) stuurt opdracht backend voert uit.

Methods:
    Get: krijg data van backend (default).
    Post: stuur en krijg data naar backend.

### Authentication
Voor authenticatie:
- installeer jwt: pip install pyjwt
- imopteer jwt
- meer info: [jwt](https://jwt.io)

Bij login route wordt token aangemaakt.
Token is nodig voor route light. token_required contoleert of gebruiker een valid token heeft.

## Postman
Simulator van frontend inteface sturt opdrachten naar backend voor testen.

## [Ionic framework](https://ionicframework.com/getting-started)

Source code frontend staat in folder ionic.
Moet worden gecompileerd naar Flask/static.

Tijdens ontwikkelen kan frontend code worden getest d.m.v. volgende commando: ionic serve. 
Vanuit command prompt in ionic folder.

ionic folder inhoud:
- .sourcemaps:
    invisible ionic (system)file (gecompileerd).
- node_modules:
    modules waarvan ionic en myApp afhankelijk is.
- src:
    source code.
    - app:
        kernfiles voor app.
    - assets:
        afbeeldingen voor app.
    - pages:
        paginas van app.
        - tabs:
            navigatie, knoppen voor paginas.
    - theme:
        styling, css/sass.
- www:
    cordova webserver system. Nodig om app tijdens tests te draaien.
- package.json:
    lijst van alle modules die nodig zijn voor de app. Zorgt voor instaleren van modules (met commando npm install).

pages:
    about = bediening

## Github
github koppelen aan git version control: git remote add github (url)
github loskoppelen: git remote remove github
status: git status
publiceren: git push github (branch)
binnenhalen: git pull github (branch)
branch maken: git branch (branch)
branch wisselen: git checkout (branch)

### Gitignore
Zet filenaam of foldernaam hierin, zodat git de folders niet in version control meeneemt.