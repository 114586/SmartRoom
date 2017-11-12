# es6 [SPA](https://nl.wikipedia.org/wiki/Single_Page_Application) (single page application)
Gebruiker blijft op dezelfde pagina, alleen onderdelen van de pagina worden aangepast.

Om een dergelijke app te maken is nodig:

## Node/NPM 
om te controleren of dit is geinstalleerd gebruik:
```
node -v
npm -v
```
Om nieuw project op te starten doe in de folder:
```
npm init
```
Beantwoord de vragen en dan wordt er een package.json file aangemaakt met projectinformatie.
In package.json staat alle informatie over project, zoals dependencies en scripts die je kan oproepen met NPM.
De meest gebruikte scripts zijn start en build.
Scripts run je door:
```
npm run (script_name)
```
Alleen bij start hoef je geen run toe te voegen.

Je kunt alle packages in package.json installeren met:
```
npm install
```

## [Webpack](https://webpack.js.org/guides/getting-started/)
package bundler
help met bundelen van code en testen en bekijken van het project.
Configuratie is opgeslagen in webpack.config.js

Middleware: maakt het mogelijk om extra functionaliteit toe te voegen aan bestaande app.

### Loaders
Loaders compileren code.
Babel doet js
Sass doet css

#### [Babel](https://babeljs.io/)
Helpt om nieuwe (2015 en later) javascript syntax te gebruiken. Vertaalt naar oude javascript code, zodat browsers het begrijpen.
```
npm install babel-loader babel-core babel-preset-env webpack
```

#### Style
Om sass te kunnen grbruiken moet je de volgende loaders (middleware) installeren:
- sass-loader
- css-loader
- style-loader
```
npm install sass-loader node-sass webpack --save-dev
npm install --save-dev css-loader
npm install style-loader --save-dev
```

## [SASS](http://sass-lang.com/)
sass maakt het mogelijk om variabelen te gebruiken bij het stylen.

### [Fonts](https://fonts.google.com/)
import fonts van google, zie main.scss in styles
Fonts variabelen zijn gedefinieerd in fonts.scss

### [Icons](https://material.io/icons/)
Google material icons, zie main.scss

### [Media queries](https://www.w3schools.com/cssref/css3_pr_mediaquery.asp)
zort ervoor dat je verschillende layouts kan toepassen voor verschillende apparaten aan de hand van schermgrootte.

### Loaders
we maken gebruik van css library [loaders.css](https://connoratherton.com/loaders).
```
npm install --save loaders.css
```
--save zorgt ervoor dat de library wordt opgenomen in package.json

### Animations
we maken gebruik van css library [animate.css](https://daneden.github.io/animate.css/).
```
npm install --save animate.css
```
--save zorgt ervoor dat de library wordt opgenomen in package.json

### [Flexbox](https://www.w3schools.com/css/css3_flexbox.asp)
Wij gebruiken flexbox module voor de layout van de app.

## Html 5

### [Semantic tags](https://www.w3schools.com/html/html5_semantic_elements.asp)
semantic tags geven aan wat voor onderdeel vand epagina ze bevatten.

### ID
Is om tag aan te spreken in javascript. Id is voor unieke toepassing.
Een tag kan maar een id hebben. 
```
<div id = 'id_naam'> </div>
```
Referentie naar id begint met een hashtag (#).

### Class
Is om tag aan te spreken in css. Class is voor generieke toepassing.
Een tag kan meer dan een class hebben.
```
<div class = 'class1 class2 class3 ...'> </div>
```
Referentie naar class begint met een punt (.).

### Style
Style overschrijft prperties die al in class gedefinieerd zijn, door [specificity rule](https://developer.mozilla.org/en-US/docs/Web/CSS/Specificity).

```
<div class = 'class1 class2 class3 ...' style = 'color:red'> </div>
```

specificity order:
1. style
2. id
3. class 

Als een style niet werk kijk naar specificity rule. Kun je zien in debugger.