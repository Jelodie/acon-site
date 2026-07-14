# Site du village d'Acon (Eure)

Site statique d'information sur la commune d'Acon (27570), **bénévole et non officiel**.
Aucune dépendance : de simples fichiers HTML + un CSS + un petit JS.
Hébergé sur GitHub Pages : https://jelodie.github.io/acon-site/

## Structure

```
acon-site/
├─ index.html            → Accueil (héros photo, accès rapides, vie du village)
├─ decouvrir.html        → Découvrir (situation, hameaux, église, dolmens, balades)
├─ histoire.html         → Histoire & Archives (frise, étymologie, démographie, où chercher)
├─ infos-pratiques.html  → Infos pratiques (mairie, urgences, municipales 2026) + accès aux pages ci-dessous
│   ├─ demarches.html    → Démarches (identité, état civil, élections, urbanisme)
│   ├─ ecole.html        → Écoles & transports (collège, lycée, Nomad)
│   ├─ emploi.html       → Emploi (France Travail, Mission Locale)
│   ├─ dechets.html      → Déchets & tri (collecte, déchèterie)
│   └─ eau-energie.html  → Eau & énergie (eau, Enedis, GRDF, fibre + urgences)
├─ entreprises.html      → Annuaire des entreprises
├─ apropos.html          → À propos (indépendance, crédits photos, contact)
├─ css/style.css         → tous les styles + les couleurs (variables en haut du fichier)
├─ js/main.js            → menu mobile + e-mail protégé des robots + année auto
├─ build.py              → génère toutes les pages (en-tête/nav/pied de page communs)
└─ assets/photos/        → photographies (Wikimedia Commons, CC BY-SA — voir apropos.html)
```

## Générer / modifier les pages

L'en-tête, la navigation et le pied de page sont **communs à toutes les pages**.
Pour éviter de les recopier à la main partout, ils sont définis une seule fois
dans `build.py`, qui régénère tous les `.html` :

```bash
python3 build.py
```

- Changer un **texte de contenu** : éditez directement le `.html`, ou la section
  correspondante dans `build.py` puis relancez-le.
- Changer le **menu / le pied de page / ajouter une page** : modifiez `build.py`
  (listes `NAV` / `PAGES`) puis relancez-le — toutes les pages restent cohérentes.

## Prévisualiser en local

```bash
python3 -m http.server 8000
# puis http://localhost:8000
```

## Adresse de contact

L'adresse e-mail n'apparaît **jamais en clair** dans le code (protection anti-robots) :
elle est reconstruite par `js/main.js` à partir des attributs `data-user` / `data-domain`
d'un lien `class="contact-mail"`. Pour la changer, modifiez la fonction `mail()` dans `build.py`.

## Photographies

Les photos proviennent de **Wikimedia Commons**, réutilisées sous licence
**Creative Commons BY-SA** (attribution + partage à l'identique). Les crédits figurent
sous chaque image et sur la page **À propos**. Toute nouvelle image doit être libre de droits
(ou publiée avec l'accord de son auteur) et créditée de la même façon.

## Mettre en ligne (rappel)

Déjà en place : dépôt public poussé sur `main`, GitHub Pages activé (branche `main`, dossier `/root`).
Chaque `git push` met le site à jour automatiquement en ~1 min. HTTPS automatique.
Domaine `acon.fr` (le jour venu) : Settings → Pages → *Custom domain*, puis DNS chez le registrar.

## Informations restant à confirmer localement

Écrites sur le site de façon prudente (renvoi à la source officielle) ; à préciser dès que possible :
école exacte de rattachement / RPI et lycée de secteur (→ mairie / DSDEN 27), numéro d'astreinte eau
24h/24 (→ facture Eaux de Normandie), horaires exacts de la mairie et de la déchèterie.
