# Site du village d'Acon (Eure)

Site statique, sans build ni dépendance : de simples fichiers HTML + un CSS + un petit JS.
Idéal pour GitHub Pages et facile à faire évoluer avec **Claude Code**.

## Structure

```
acon-site/
├─ index.html            → Accueil
├─ decouvrir.html        → Découvrir le village
├─ histoire.html         → Histoire & Archives (frise + cartes postales)
├─ infos-pratiques.html  → Mairie, numéros utiles, vie locale
├─ css/style.css         → tous les styles + les couleurs (variables en haut du fichier)
├─ js/main.js            → menu mobile uniquement
└─ assets/cartes-postales/ → déposez ici les scans d'archives
```

## Prévisualiser en local

Ouvrez `index.html` dans un navigateur, ou lancez un petit serveur :

```bash
python3 -m http.server 8000
# puis http://localhost:8000
```

## Mettre en ligne avec GitHub Pages

1. Créez un dépôt sur votre GitHub perso et poussez ces fichiers.
2. **Settings → Pages** → *Deploy from a branch* → branche `main`, dossier `/root` → *Save*.
3. Le site s'affiche sur `https://votre-pseudo.github.io/nom-du-depot/`.
   - Rappel : sur un compte gratuit, le dépôt doit être **public** pour utiliser Pages.
     Pour garder le code privé, déployez plutôt via **Cloudflare Pages** ou **Netlify** (gratuit, dépôts privés acceptés).
4. **Domaine acon.fr** (une fois obtenu) : Settings → Pages → *Custom domain* → `acon.fr`.
   Chez votre registrar, créez les enregistrements DNS `A` du domaine racine vers les IP de GitHub Pages
   (et un enregistrement `CNAME` `www` vers `votre-pseudo.github.io`). HTTPS est automatique.

## À compléter (repères en rouge sur le site)

Les mentions en italique rouge `[entre crochets]` marquent le contenu à renseigner puis à retirer :
population INSEE, dates de la frise, nom du maire (après les municipales 2026),
collecte des déchets, associations, et surtout les **cartes postales** dans `histoire.html`.

## Ajouter une carte postale

Dans `histoire.html`, remplacez un cadre :

```html
<figure class="postcard">
  <div class="frame">Déposer un scan</div>
  <figcaption>Acon — [lieu] <span class="date">vers [année]</span></figcaption>
</figure>
```

par :

```html
<figure class="postcard">
  <div class="frame"><img src="assets/cartes-postales/acon-eglise-1910.jpg" alt="L'église d'Acon vers 1910"></div>
  <figcaption>Acon — L'église <span class="date">vers 1910</span></figcaption>
</figure>
```

⚠️ Vérifiez les droits de chaque image avant publication (voir la note « Droits d'usage » sur la page Histoire).

## Idées de prompts pour Claude Code

- « Ajoute une page `contact.html` avec un formulaire (via Formspree) et mets-la dans la navigation des 4 pages. »
- « Crée une page `mentions-legales.html` (éditeur, hébergeur, propriété des images) et lie-la dans le pied de page. »
- « Sur `histoire.html`, transforme la galerie pour ouvrir chaque carte postale en grand au clic (lightbox simple, sans dépendance). »
- « Remplis la frise chronologique de `histoire.html` à partir des dates que je te donne. »

## Couleurs

Définies en haut de `css/style.css` (variables `--vert-eure`, `--or`, `--rouge`, `--parchemin`…),
inspirées du vert du département de l'Eure et de l'or/rouge héraldiques de la Normandie.
Changez-les à un seul endroit pour reteinter tout le site.
