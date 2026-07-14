#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Générateur du site d'Acon.
Un seul endroit pour l'en-tête, la navigation et le pied de page :
on évite ainsi de dupliquer (et de désynchroniser) le menu sur chaque page.
Lancer :  python3 build.py   → (re)génère tous les fichiers .html.
"""

CREST = (
    '<svg class="crest" viewBox="0 0 30 34" aria-hidden="true">'
    '<path d="M2 2 h26 v16 c0 8 -6 12 -13 14 C8 30 2 26 2 18 Z" fill="#2E6B47" stroke="#C79A3B" stroke-width="2"/>'
    '<path d="M15 9 c3 3 3 8 0 13 c-3 -5 -3 -10 0 -13 Z" fill="#C79A3B"/>'
    '<path d="M15 13 l4 2 M15 17 l-4 2" stroke="#E4CB92" stroke-width="1.4" fill="none" stroke-linecap="round"/>'
    '</svg>'
)

# (fichier, libellé, clé de page active)
NAV = [
    ("index.html", "Accueil", "accueil"),
    ("decouvrir.html", "Découvrir", "decouvrir"),
    ("histoire.html", "Histoire &amp; Archives", "histoire"),
    ("infos-pratiques.html", "Infos pratiques", "pratique"),
    ("entreprises.html", "Annuaire", "annuaire"),
    ("apropos.html", "À propos", "apropos"),
]

# Adresse e-mail protégée des robots : reconstruite en JS, jamais en clair dans le HTML.
def mail(label="Afficher l'adresse e-mail", subject="Site d'Acon"):
    return (f'<a class="contact-mail" data-user="elodie.saintemarie+Acon" '
            f'data-domain="gmail.com" data-subject="{subject}" href="#">{label}</a>')

def header(active):
    links = []
    for href, label, key in NAV:
        cur = ' aria-current="page"' if key == active else ''
        links.append(f'        <a href="{href}"{cur}>{label}</a>')
    nav = "\n".join(links)
    return f'''  <a class="skip" href="#contenu">Aller au contenu</a>
  <div class="notice">Site bénévole et indépendant, sans lien avec la mairie d'Acon — pour vos démarches officielles, voir <a href="https://www.service-public.fr">service-public.fr</a>.</div>

  <header class="site-header">
    <div class="wrap bar">
      <a class="brand" href="index.html" aria-label="Accueil — Acon">
        {CREST}
        <span><b>Acon</b><small>Eure · Normandie</small></span>
      </a>
      <button class="nav-toggle" aria-expanded="false" aria-controls="nav">Menu</button>
      <nav class="nav" id="nav" aria-label="Navigation principale">
{nav}
      </nav>
    </div>
  </header>
'''

FOOTER = '''  <footer class="site-footer">
    <div class="wrap">
      <div class="cols">
        <div>
          <h3>Acon</h3>
          <p><small>Le site de village d'Acon (Eure, 27), un coin de la vallée de l'Avre aux portes du Perche. Un lieu pour se sentir chez soi, entre le bourg et les hameaux des Brûlés, du Mesnil et du Rousset.</small></p>
        </div>
        <div>
          <h3>Le village</h3>
          <p><small>
            <a href="index.html">Accueil</a><br>
            <a href="decouvrir.html">Découvrir</a><br>
            <a href="histoire.html">Histoire &amp; Archives</a><br>
            <a href="entreprises.html">Annuaire</a><br>
            <a href="apropos.html">À propos</a>
          </small></p>
        </div>
        <div>
          <h3>Vie pratique</h3>
          <p><small>
            <a href="infos-pratiques.html">Infos pratiques</a><br>
            <a href="demarches.html">Démarches</a><br>
            <a href="ecole.html">Écoles &amp; transports</a><br>
            <a href="emploi.html">Emploi</a><br>
            <a href="dechets.html">Déchets &amp; tri</a><br>
            <a href="eau-energie.html">Eau &amp; énergie</a>
          </small></p>
        </div>
        <div>
          <h3>Officiel &amp; urgences</h3>
          <p><small>
            Mairie : 02 32 32 53 49<br>
            <a href="https://www.service-public.fr">Service-Public.fr</a><br>
            <a href="https://www.facebook.com/acon27570/">Facebook du village</a><br>
            Élec. (Enedis) : 09 72 67 50 27<br>
            Gaz (GRDF) : 0 800 47 33 33
          </small></p>
        </div>
      </div>
      <p class="foot-note"><small>Site d'information bénévole et non officiel, sans lien avec la mairie d'Acon. © <span class="js-annee">2026</span> · <a href="mentions-legales.html">Mentions légales</a> · crédits photos sur <a href="apropos.html">À propos</a>. Fait avec soin pour les Aconnais et les Aconnaises.</small></p>
    </div>
  </footer>
'''

def page(active, title, desc, body):
    return f'''<!DOCTYPE html>
<html lang="fr">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{title}</title>
  <meta name="description" content="{desc}" />
  <link rel="preconnect" href="https://fonts.googleapis.com" />
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
  <link href="https://fonts.googleapis.com/css2?family=Fraunces:ital,opsz,wght@0,9..144,400..600;1,9..144,400..500&family=Inter:wght@400;500;600&display=swap" rel="stylesheet" />
  <link rel="stylesheet" href="css/style.css" />
</head>
<body>
{header(active)}
  <main id="contenu">
{body}
  </main>

{FOOTER}
  <script src="js/main.js"></script>
</body>
</html>
'''

PAGES = {}

# ======================================================================
# ACCUEIL
# ======================================================================
PAGES["index.html"] = dict(active="accueil",
  title="Acon — le village de la vallée de l'Avre (Eure, Normandie)",
  desc="Bienvenue à Acon (Eure, 27570) : découvrir le village, son histoire, et toutes les infos pratiques du quotidien pour les habitants comme pour les visiteurs.",
  body=f'''    <section class="hero">
      <div class="wrap hero-media">
        <div>
          <span class="badge"><span class="dot"></span> Eure (27) · Normandie</span>
          <h1>Bienvenue à Acon</h1>
          <p class="sub">Un village de la vallée de l'Avre, entre Normandie et Perche.</p>
          <p class="lead">Ici, on connaît ses voisins, on entend l'Avre couler et on prend le temps. Ce site rassemble, au même endroit, tout ce qui fait la vie d'Acon et de ses trois hameaux — Les Brûlés, Le Mesnil et Le Rousset : son histoire, ses démarches du quotidien et les bonnes adresses. Que vous habitiez le village depuis toujours ou que vous veniez d'y poser vos valises, vous êtes chez vous.</p>
        </div>
        <figure class="hero-photo">
          <img src="assets/photos/eglise-saint-denis-01.jpg" alt="L'église Saint-Denis d'Acon" loading="eager">
          <figcaption>L'église Saint-Denis, au cœur du village. <span class="credit">Photo : Davitof — Wikimedia Commons (CC&nbsp;BY-SA&nbsp;3.0).</span></figcaption>
        </figure>
      </div>
      <div class="wrap">
        <div class="facts">
          <div><div class="n">478</div><div class="l">habitantes et habitants</div></div>
          <div><div class="n">3</div><div class="l">hameaux</div></div>
          <div><div class="n">27570</div><div class="l">code postal</div></div>
          <div><div class="n">Avre</div><div class="l">la rivière du village</div></div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
        <p class="eyebrow kicker">Par où commencer</p>
        <div class="grid">
          <a class="card lien" href="decouvrir.html">
            <span class="tag">Le village</span>
            <h3>Découvrir Acon</h3>
            <p>La vallée de l'Avre, les trois hameaux, l'église Saint-Denis et un patrimoine mégalithique rare.</p>
            <p class="arrow">→</p>
          </a>
          <a class="card lien" href="histoire.html">
            <span class="tag">Mémoire</span>
            <h3>Histoire &amp; Archives</h3>
            <p>Des dolmens du Néolithique à aujourd'hui : la longue histoire du village, et où retrouver ses archives.</p>
            <p class="arrow">→</p>
          </a>
          <a class="card lien" href="infos-pratiques.html">
            <span class="tag">Au quotidien</span>
            <h3>Infos pratiques</h3>
            <p>Mairie, démarches, écoles, déchets, eau et énergie, emploi : l'essentiel réuni et à jour.</p>
            <p class="arrow">→</p>
          </a>
          <a class="card lien" href="entreprises.html">
            <span class="tag">Économie locale</span>
            <h3>Annuaire</h3>
            <p>Commerces, artisans, producteurs et services d'Acon. Faites vivre — et connaître — l'activité du village.</p>
            <p class="arrow">→</p>
          </a>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">En bref</p>
        <h2>Un village du sud de l'Eure</h2>
        <p>Acon veille sur la vallée de l'Avre, au sud du département de l'Eure, tout près de l'Eure-et-Loir (28) et aux portes du Perche. La commune réunit 478 Aconnais et Aconnaises, répartis entre le bourg et les hameaux des Brûlés, du Mesnil et du Rousset. Elle fait partie du canton de Verneuil d'Avre et d'Iton et de la communauté d'agglomération Évreux Portes de Normandie. Son maire est <strong>Christophe Blin</strong>.</p>
        <p>Ce site est écrit bénévolement par une habitante. Il ne remplace pas la mairie : il donne simplement, avec le cœur, de quoi mieux connaître Acon et se faciliter la vie de tous les jours.</p>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Rester en lien</p>
        <h2>La vie du village</h2>
        <p>Pour ne rien manquer des nouvelles, des travaux et des rendez-vous de la commune :</p>
        <ul>
          <li><strong>Page Facebook « Commune d'Acon »</strong> — photos et actualités partagées par les habitants : <a href="https://www.facebook.com/acon27570/">facebook.com/acon27570</a></li>
          <li><strong>PanneauPocket</strong> — les alertes et informations de la mairie sur votre téléphone : <a href="https://app.panneaupocket.com/ville/970037196-acon-27570">appli PanneauPocket · Acon</a></li>
        </ul>
        <div class="tip">
          <span class="ico" aria-hidden="true">💬</span>
          <p>Une info à corriger, une photo ancienne à partager, une bonne adresse à ajouter ? Ce site grandit avec vous. {mail("Écrivez-moi")}</p>
        </div>
      </div>
    </section>''')

# ======================================================================
# DÉCOUVRIR
# ======================================================================
PAGES["decouvrir.html"] = dict(active="decouvrir",
  title="Découvrir Acon — village, hameaux, église et vallée de l'Avre",
  desc="Découvrir Acon (Eure) : sa situation aux portes du Perche, ses trois hameaux, l'église Saint-Denis (monument historique) et la nécropole dolménique néolithique.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Découvrir</span>
        <h1>Le village</h1>
        <p class="lead mesure">Posé de part et d'autre de la vallée de l'Avre, Acon mêle prairies, bois et cours d'eau, un patrimoine ancien et une vie de village tranquille, à la lisière de la Normandie et du Perche.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Situation</p>
        <h2>Aux confins de la Normandie et du Perche</h2>
        <p>Acon est une commune rurale du sud de l'Eure, limitrophe du département de l'Eure-et-Loir (28) et voisine du parc naturel régional du Perche. La route nationale 12 et la rivière Avre traversent le territoire : elles séparent le hameau des Brûlés, d'un côté, du Rousset et du Mesnil, de l'autre.</p>
        <p>Tout autour, les villages de la vallée — Tillières-sur-Avre, Breux-sur-Avre, Nonancourt, Verneuil d'Avre et d'Iton — dessinent un paysage de prairies humides, de haies et de bois où il fait bon marcher.</p>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
        <p class="eyebrow kicker">Le territoire</p>
        <h2>Trois hameaux, un village</h2>
        <div class="grid" style="margin-top:1.4rem">
          <div class="card">
            <h3>Les Brûlés</h3>
            <p>Sur une rive de l'Avre, séparé du reste de la commune par la N12. Son nom apparaît autrefois sous la forme « Les Bullez ».</p>
          </div>
          <div class="card">
            <h3>Le Mesnil</h3>
            <p>Anciennement « Le Mesnil-Pipaut », du nom d'une famille présente à l'époque des ducs de Normandie. « Mesnil » désigne un petit domaine rural.</p>
          </div>
          <div class="card">
            <h3>Le Rousset</h3>
            <p>Le hameau où se trouve la mairie, 8 rue de la Mairie. On l'écrivait jadis « Le Roiset ».</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Patrimoine</p>
        <h2>L'église Saint-Denis</h2>
        <p>Détruite pendant la guerre de Cent Ans, l'église Saint-Denis a été rebâtie au XVIᵉ siècle : la nef en 1514, puis le chœur vers 1540. Sous sa voûte de bois se cachent de belles peintures murales de la fin du XVIᵉ siècle et une poutre de gloire figurant le Christ en croix. L'édifice est <strong>inscrit au titre des monuments historiques depuis le 8 janvier 1998</strong>.</p>
      </div>
      <div class="wrap">
        <div class="duo">
          <figure class="photo">
            <img src="assets/photos/eglise-saint-denis-02.jpg" alt="L'église Saint-Denis d'Acon, vue extérieure" loading="lazy">
            <figcaption><b>Église Saint-Denis</b> — reconstruite aux XVIᵉ siècle. Photo : X-Javier, Wikimedia Commons (CC BY-SA 4.0).</figcaption>
          </figure>
          <figure class="photo">
            <img src="assets/photos/eglise-saint-denis-03.jpg" alt="L'église Saint-Denis d'Acon dans son enclos" loading="lazy">
            <figcaption><b>L'église et son enclos</b>, au bord de l'Avre. Photo : X-Javier, Wikimedia Commons (CC BY-SA 4.0).</figcaption>
          </figure>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Un trésor discret</p>
        <h2>La nécropole dolménique des Prés d'Acon</h2>
        <p>Dans la plaine de l'Avre subsiste un ensemble mégalithique exceptionnel : une <strong>nécropole dolménique du Néolithique moyen</strong>, vieille d'environ 5 800 ans et longue d'à peu près 110 mètres — une rareté dans tout le Bassin parisien. Repérée en 1972, elle est elle aussi <strong>inscrite aux monuments historiques (24 février 1998)</strong>. Un lien tangible avec les premiers habitants de la vallée, bien avant que le village ne porte son nom.</p>
        <div class="tip">
          <span class="ico" aria-hidden="true">🌿</span>
          <p><strong>Sur le terrain, restons discrets :</strong> le site est fragile et se trouve sur des terrains agricoles. On l'admire sans le déranger.</p>
        </div>
      </div>
    </section>

    <figure class="banner">
      <img src="assets/photos/pres-acon-01.jpg" alt="Paysage rural de la vallée de l'Avre à Acon">
      <figcaption class="banner-cap wrap">Les Prés d'Acon, dans la vallée de l'Avre. Photo : X-Javier, Wikimedia Commons (CC BY-SA 4.0).</figcaption>
    </figure>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Nature &amp; balades</p>
        <h2>Se promener autour d'Acon</h2>
        <p>La vallée de l'Avre invite à la marche. Le sentier de grande randonnée <strong>GR22</strong>, qui relie Paris au Mont-Saint-Michel, passe dans les environs et longe la rivière. Entre prairies, bois et chemins creux, on croise le patrimoine ordinaire du sud eurois : lavoirs, ponts et points de vue sur la vallée.</p>
        <div class="tip">
          <span class="ico" aria-hidden="true">📷</span>
          <p>Vous avez une belle photo d'Acon, un coin de balade préféré, un souvenir à raconter ? {mail("Partagez-le avec le village")}</p>
        </div>
      </div>
    </section>''')

# ======================================================================
# HISTOIRE & ARCHIVES
# ======================================================================
PAGES["histoire.html"] = dict(active="histoire",
  title="Histoire &amp; Archives d'Acon — du Néolithique à aujourd'hui",
  desc="L'histoire d'Acon (Eure) : nécropole dolménique néolithique, origines du nom, église Saint-Denis, seigneurs, démographie, et où consulter les archives.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Mémoire du village</span>
        <h1>Histoire &amp; Archives</h1>
        <p class="lead mesure">Acon a une histoire étonnamment longue : des bâtisseurs de dolmens il y a près de six mille ans jusqu'aux familles d'aujourd'hui. Voici quelques repères, et surtout où chercher pour aller plus loin.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Repères chronologiques</p>
        <h2>Quelques jalons</h2>
        <p>Une frise à taille de village, appuyée sur les sources publiques (Wikipédia, base Mérimée du ministère de la Culture, dictionnaire topographique de l'Eure).</p>
        <ol class="timeline">
          <li><span class="an">≈ 3800 av. J.-C.</span><p>Édification de la <strong>nécropole dolménique des Prés d'Acon</strong>, dans la vallée de l'Avre (Néolithique moyen).</p></li>
          <li><span class="an">XIIᵉ s.</span><p>Première mention écrite du nom, sous la forme <em>« Acun »</em>. Suivront <em>Agon</em> (1230), <em>Achon</em> (1234), <em>Acoin</em> et <em>Dacon</em> (1242).</p></li>
          <li><span class="an">XIIIᵉ–XVIIᵉ s.</span><p>Le fief d'Acon appartient à la <strong>famille d'Acon</strong>, aux confins de la Normandie et du royaume de France.</p></li>
          <li><span class="an">1514 &amp; 1540</span><p>Après les destructions de la guerre de Cent Ans, reconstruction de l'<strong>église Saint-Denis</strong> : la nef en 1514, le chœur vers 1540.</p></li>
          <li><span class="an">1734</span><p>Le fief passe à la <strong>famille de Guenet</strong>, par le mariage de Marie-Élisabeth de Tilly et François-Alexandre de Guenet.</p></li>
          <li><span class="an">1800</span><p>Maximum de population de la commune : <strong>819 habitants</strong>.</p></li>
          <li><span class="an">1998</span><p>L'église Saint-Denis (8 janvier) et la nécropole dolménique (24 février) sont <strong>inscrites aux monuments historiques</strong>.</p></li>
          <li><span class="an">Aujourd'hui</span><p>Une commune de <strong>478 Aconnais</strong>, réunissant les hameaux des Brûlés, du Mesnil et du Rousset.</p></li>
        </ol>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Le nom du village</p>
        <h2>D'où vient « Acon » ?</h2>
        <p>Le nom est attesté dès le XIIᵉ siècle et son origine reste débattue par les spécialistes. Trois pistes coexistent : une racine gauloise <em>acauno</em> (« la pierre, le rocher »), un thème germanique, ou encore un ancien nom de personne. Rien d'étonnant à cette part de mystère : les noms de nos villages ont traversé mille ans de bouches et de plumes.</p>

        <p class="eyebrow" style="margin-top:2.2rem">Les hameaux</p>
        <h2>Des noms qui racontent</h2>
        <p>Le <strong>Mesnil</strong> — de <em>Le Mesnil-Pipaut</em> — évoque un petit domaine rural et une famille médiévale, les Pipart. <strong>Les Brûlés</strong>, écrits autrefois « Les Bullez », et <strong>Le Rousset</strong>, jadis « Le Roiset », complètent le trio. Ensemble, ils forment la commune telle qu'on la connaît, de part et d'autre de l'Avre.</p>
        <p>C'est au <strong>Rousset</strong> que battait le cœur du village d'autrefois : les cartes postales du début du XXᵉ siècle y montrent l'<strong>école communale</strong>, un <strong>château</strong> et un <strong>manoir</strong>, le pont et le lavoir sur l'Avre — autant de lieux que l'on retrouve dans la collection ci-dessous.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Population</p>
        <h2>Le village au fil du temps</h2>
        <p>Comme beaucoup de communes rurales, Acon a connu un long reflux au XXᵉ siècle avant de retrouver des couleurs. De 819 habitants en 1800, la population est descendue jusqu'à 250 en 1975, avant de remonter régulièrement pour atteindre 478 aujourd'hui.</p>
        <div class="facts">
          <div><div class="n">819</div><div class="l">en 1800 (maximum)</div></div>
          <div><div class="n">250</div><div class="l">en 1975 (minimum)</div></div>
          <div><div class="n">407</div><div class="l">en 1999</div></div>
          <div><div class="n">478</div><div class="l">aujourd'hui</div></div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
        <p class="eyebrow kicker">Collection</p>
        <h2>Cartes postales anciennes</h2>
        <p class="mesure">Le village d'autrefois — l'église, le lavoir et le pont, les bords de l'Avre, le château et le manoir du Rousset — revit à travers ces cartes postales des années 1890 à 1950, conservées aux <strong>Archives départementales de l'Eure</strong> (série 8 Fi 2). Cliquez pour les voir en plus grand sur le site des Archives.</p>
        <div class="gallery">
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/eglise.jpg" alt="Carte postale ancienne : l'église d'Acon"></div></a><figcaption>Acon — L'église <span class="date">vers 1900 · AD Eure 8 Fi 2-4</span></figcaption></figure>
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/pont-lavoir.jpg" alt="Carte postale ancienne : le pont et le lavoir du Rousset d'Acon"></div></a><figcaption>Le Rousset — Le pont &amp; le lavoir <span class="date">AD Eure 8 Fi 2-11</span></figcaption></figure>
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/bord-avre.jpg" alt="Carte postale ancienne : les bords de l'Avre au Rousset d'Acon"></div></a><figcaption>Le Rousset — Bords de l'Avre <span class="date">AD Eure 8 Fi 2-10</span></figcaption></figure>
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/chateau.jpg" alt="Carte postale ancienne : le château d'Acon"></div></a><figcaption>Acon — Le château <span class="date">AD Eure 8 Fi 2-7</span></figcaption></figure>
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/manoir.jpg" alt="Carte postale ancienne : le manoir du Rousset d'Acon"></div></a><figcaption>Le Rousset — Le manoir <span class="date">AD Eure 8 Fi 2-8</span></figcaption></figure>
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/ecole.jpg" alt="Carte postale ancienne : l'école communale du Rousset d'Acon"></div></a><figcaption>Le Rousset — L'école communale <span class="date">AD Eure 8 Fi 2-3</span></figcaption></figure>
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/ferme-mesnil.jpg" alt="Carte postale ancienne : la ferme du Mesnil d'Acon"></div></a><figcaption>La ferme du Mesnil d'Acon <span class="date">AD Eure 8 Fi 2-9</span></figcaption></figure>
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/route-paris.jpg" alt="Carte postale ancienne : la route de Paris à Acon"></div></a><figcaption>Acon — La route de Paris <span class="date">AD Eure 8 Fi 2-1</span></figcaption></figure>
          <figure class="postcard"><a href="https://archives.eure.fr/search/results?q=Acon" target="_blank" rel="noopener"><div class="frame"><img src="assets/photos/cpa/route-paris-brest.jpg" alt="Carte postale ancienne : perspective de la route de Paris-Brest à Acon"></div></a><figcaption>Acon — Route de Paris-Brest <span class="date">AD Eure 8 Fi 2-2</span></figcaption></figure>
        </div>
        <p style="margin-top:1rem"><small>Reproductions : <strong>Archives départementales de l'Eure</strong>, série 8 Fi 2 (cartes postales, [1890]-[1950]). Différents photographes et éditeurs — <a href="https://archives.eure.fr/search/results?q=Acon">consulter le fonds « Acon »</a>.</small></p>
        <div class="tip">
          <span class="ico" aria-hidden="true">🖼️</span>
          <p>Vous possédez une carte postale ou une photo ancienne d'Acon ? On peut la numériser et l'ajouter ici, avec votre accord. {mail("Contribuer à la collection")}</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Aller plus loin</p>
        <h2>Où consulter les archives d'Acon</h2>
        <ul>
          <li><strong>Archives départementales de l'Eure</strong> — état civil, registres paroissiaux, cadastre napoléonien, registres militaires. En ligne sur <a href="https://archives.eure.fr/">archives.eure.fr</a> ; sur place au 2 rue de Verdun à Évreux (02 32 31 50 84).</li>
          <li><strong>Cassini / EHESS</strong> — l'histoire démographique des communes : <a href="http://cassini.ehess.fr/">cassini.ehess.fr</a>.</li>
          <li><strong>Base Mérimée (POP, ministère de la Culture)</strong> — les notices de l'<a href="https://pop.culture.gouv.fr/notice/merimee/PA27000027">église Saint-Denis</a> et de la <a href="https://pop.culture.gouv.fr/notice/merimee/PA27000024">nécropole dolménique</a>.</li>
          <li><strong>La mairie et les habitants</strong> — souvent la meilleure source : registres récents, souvenirs et albums de famille.</li>
        </ul>
        <div class="callout">
          <strong>Droits d'usage :</strong> les cartes postales ci-dessus proviennent du fonds des Archives départementales de l'Eure (série 8 Fi 2). Les vues, anciennes, sont pour la plupart tombées dans le domaine public ; la reproduction reste créditée aux Archives de l'Eure. Pour un usage commercial, adressez-vous directement aux Archives.
        </div>
      </div>
    </section>''')

# ======================================================================
# INFOS PRATIQUES (HUB)
# ======================================================================
PAGES["infos-pratiques.html"] = dict(active="pratique",
  title="Infos pratiques — Acon (Eure) : mairie, urgences, démarches",
  desc="Toutes les infos pratiques d'Acon (Eure) : contacter la mairie, numéros d'urgence, démarches, écoles, déchets, eau et énergie, emploi.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Au quotidien</span>
        <h1>Infos pratiques</h1>
        <p class="lead mesure">L'essentiel de la vie courante à Acon, réuni et tenu à jour. Pour toute démarche officielle, la mairie et service-public.fr restent vos interlocuteurs.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Mairie</p>
        <h2>Contacter la mairie</h2>
        <dl class="def">
          <dt>Maire</dt><dd>Christophe Blin</dd>
          <dt>Adresse</dt><dd>8 rue de la Mairie, Le Rousset, 27570 Acon</dd>
          <dt>Téléphone</dt><dd><a href="tel:+33232325349">02 32 32 53 49</a></dd>
          <dt>Courriel</dt><dd>acon.eure@wanadoo.fr</dd>
          <dt>Horaires</dt><dd>Lundi et mercredi de 17 h à 19 h. Les horaires peuvent évoluer : un coup de fil avant de se déplacer reste le plus sûr.</dd>
          <dt>Actualités</dt><dd>La <a href="https://www.facebook.com/acon27570/">page Facebook « Commune d'Acon »</a> et l'application PanneauPocket. <small>(L'ancien site mairie-acon.fr n'est plus en ligne.)</small></dd>
        </dl>
        <div class="result">
          <p class="eyebrow" style="margin-bottom:.4rem">Élections municipales 2026</p>
          <p>La liste <strong>« Acon, ensemble pour demain »</strong>, conduite par <strong>Christophe Blin</strong>, a été élue au premier tour avec <span class="pct">100 %</span> des suffrages (144 voix), remportant les 11 sièges du conseil municipal. Participation : 45,51 %. <br><small>Source : ministère de l'Intérieur.</small></p>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Urgences</p>
        <h2>Numéros à connaître</h2>
        <dl class="def">
          <dt>Urgences (n° européen)</dt><dd>112</dd>
          <dt>SAMU</dt><dd>15</dd>
          <dt>Police / Gendarmerie</dt><dd>17</dd>
          <dt>Pompiers</dt><dd>18</dd>
          <dt>Urgence sourds &amp; malentendants</dt><dd>114 (par SMS)</dd>
          <dt>Pharmacie de garde</dt><dd>3237</dd>
          <dt>Enfance en danger</dt><dd>119</dd>
        </dl>
        <div class="tip">
          <span class="ico" aria-hidden="true">⚡</span>
          <p><strong>Coupure d'eau, d'électricité ou odeur de gaz ?</strong> Les numéros des fournisseurs (Enedis, GRDF, Eaux de Normandie) sont sur la page <a href="eau-energie.html">Eau &amp; énergie</a>.</p>
        </div>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <p class="eyebrow kicker">Vos démarches, thème par thème</p>
        <div class="grid">
          <a class="card lien" href="demarches.html">
            <span class="tag">Administratif</span>
            <h3>Démarches</h3>
            <p>Papiers d'identité, actes d'état civil, élections, recensement, urbanisme.</p>
            <p class="arrow">→</p>
          </a>
          <a class="card lien" href="ecole.html">
            <span class="tag">Familles</span>
            <h3>Écoles &amp; transports</h3>
            <p>École, collège et lycée de secteur, transport scolaire Nomad.</p>
            <p class="arrow">→</p>
          </a>
          <a class="card lien" href="emploi.html">
            <span class="tag">Travail</span>
            <h3>Emploi</h3>
            <p>France Travail, Mission Locale et orientation, près de chez vous.</p>
            <p class="arrow">→</p>
          </a>
          <a class="card lien" href="dechets.html">
            <span class="tag">Environnement</span>
            <h3>Déchets &amp; tri</h3>
            <p>Collecte, consignes de tri et déchèterie de rattachement.</p>
            <p class="arrow">→</p>
          </a>
          <a class="card lien" href="eau-energie.html">
            <span class="tag">Maison</span>
            <h3>Eau &amp; énergie</h3>
            <p>Eau, assainissement, électricité, gaz, fibre — et les urgences.</p>
            <p class="arrow">→</p>
          </a>
          <a class="card lien" href="entreprises.html">
            <span class="tag">Local</span>
            <h3>Annuaire</h3>
            <p>Commerces, artisans, producteurs et services d'Acon.</p>
            <p class="arrow">→</p>
          </a>
        </div>
      </div>
    </section>''')

# ======================================================================
# DÉMARCHES
# ======================================================================
PAGES["demarches.html"] = dict(active="pratique",
  title="Démarches administratives — Acon (Eure)",
  desc="Vos démarches à Acon (Eure) : carte d'identité et passeport, actes d'état civil, listes électorales, recensement citoyen, urbanisme.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Administratif</span>
        <h1>Vos démarches</h1>
        <p class="lead mesure">De la carte d'identité au permis de construire : les bons interlocuteurs et les liens officiels, pour s'y retrouver sans perdre de temps.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Identité</p>
        <h2>Carte d'identité &amp; passeport</h2>
        <p>La mairie d'Acon n'est pas équipée pour recueillir les demandes de carte d'identité et de passeport. Il faut prendre rendez-vous dans une mairie équipée d'une station biométrique — vous pouvez choisir n'importe laquelle. Les plus proches sont :</p>
        <dl class="def">
          <dt>Verneuil d'Avre et d'Iton</dt><dd>La plus proche côté Eure — 02 32 32 10 81</dd>
          <dt>Nonancourt</dt><dd>02 32 58 01 90</dd>
          <dt>Autres</dt><dd>Dreux, Vernouillet, Brezolles (28), Évreux (27)…</dd>
        </dl>
        <p><strong>Avant le rendez-vous</strong>, faites la pré-demande en ligne et notez votre numéro : c'est ce qui fait gagner le plus de temps au guichet.</p>
        <ul>
          <li>Pré-demande : <a href="https://ants.gouv.fr/">ants.gouv.fr</a> ou l'application <a href="https://france-identite.gouv.fr/">France Identité</a>.</li>
          <li>Trouver une mairie équipée et un créneau : <a href="https://passeport.ants.gouv.fr/services/geolocaliser-une-mairie-habilitee">rendez-vous ANTS</a>.</li>
        </ul>
        <div class="tip"><span class="ico" aria-hidden="true">✅</span><p>La carte d'identité est <strong>gratuite</strong> (sauf perte ou vol). Ne passez jamais par un site payant intermédiaire.</p></div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">État civil</p>
        <h2>Actes de naissance, mariage, décès</h2>
        <p>La demande se fait auprès de la mairie du lieu de l'événement (né, marié ou décédé à Acon → mairie d'Acon ; ailleurs → mairie concernée). C'est <strong>gratuit</strong> et faisable en ligne sur <a href="https://www.service-public.fr/particuliers/vosdroits/N359">service-public.fr</a>.</p>

        <p class="eyebrow" style="margin-top:2.2rem">Citoyenneté</p>
        <h2>Élections &amp; recensement à 16 ans</h2>
        <dl class="def">
          <dt>Listes électorales</dt><dd>Inscription en mairie ou en ligne. Vérifiez votre situation sur <a href="https://www.service-public.fr/particuliers/vosdroits/services-en-ligne-et-formulaires/ISE">service-public.fr</a>.</dd>
          <dt>Recensement citoyen</dt><dd>Obligatoire dès 16 ans (en mairie ou <a href="https://www.service-public.fr/particuliers/vosdroits/F870">en ligne</a>), il ouvre la voie à la Journée défense et citoyenneté.</dd>
        </dl>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Habitat</p>
        <h2>Urbanisme &amp; travaux</h2>
        <p>Une clôture, un abri de jardin, une extension, des panneaux solaires, un ravalement ? La plupart des travaux nécessitent une <strong>déclaration préalable</strong> ou un <strong>permis de construire</strong>, à déposer en mairie d'Acon. La mairie vous indiquera le bon formulaire et les modalités de dépôt.</p>
        <ul>
          <li>Comprendre sa démarche : <a href="https://www.service-public.fr/particuliers/vosdroits/N319">service-public.fr — urbanisme</a>.</li>
          <li>Renseignements et dépôt : mairie d'Acon (02 32 32 53 49).</li>
        </ul>
        <div class="callout"><strong>Un doute sur la marche à suivre ?</strong> Le portail national <a href="https://www.service-public.fr">service-public.fr</a> couvre l'immense majorité des démarches, et la mairie vous orientera pour tout ce qui est local.</div>
      </div>
    </section>''')

# ======================================================================
# ÉCOLES & TRANSPORTS
# ======================================================================
PAGES["ecole.html"] = dict(active="pratique",
  title="Écoles, collège &amp; transports scolaires — Acon (Eure)",
  desc="Scolarité à Acon (Eure) : école de rattachement, collège Maurice de Vlaminck à Verneuil, lycée de secteur, transport scolaire Nomad, académie de Normandie.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Pour les familles</span>
        <h1>Écoles &amp; transports</h1>
        <p class="lead mesure">Où sont scolarisés les enfants d'Acon, et comment ils se rendent en classe. Les affectations dépendent de votre adresse : en cas de doute, la mairie et la DSDEN de l'Eure ont le dernier mot.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">École</p>
        <h2>École de rattachement</h2>
        <p>Acon n'a pas d'école sur son territoire : les jeunes enfants sont scolarisés dans une commune voisine de la vallée (du côté de Tillières-sur-Avre / Bérou-la-Mulotière selon les secteurs). L'école exacte et l'organisation dépendent de la convention scolaire de la commune.</p>
        <div class="tip"><span class="ico" aria-hidden="true">🏫</span><p><strong>Le plus sûr :</strong> demandez à la <strong>mairie d'Acon</strong> l'école de rattachement pour votre adresse. Vous pouvez aussi vérifier sur l'<a href="https://annuaire-education.fr/">Annuaire de l'Éducation nationale</a>.</p></div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Collège &amp; lycée</p>
        <h2>Après l'école</h2>
        <dl class="def">
          <dt>Collège de secteur</dt><dd><strong>Collège Maurice de Vlaminck</strong> — 328 avenue Maurice de Vlaminck, 27130 Verneuil d'Avre et d'Iton. (Secteur officiel de rattachement d'Acon.)</dd>
          <dt>Lycée</dt><dd>Le lycée public le plus proche est le <strong>Lycée Porte de Normandie</strong>, à Verneuil d'Avre et d'Iton. L'affectation dépend de la sectorisation académique : confirmez-la auprès de la DSDEN de l'Eure.</dd>
          <dt>Autorité</dt><dd>Académie de Normandie — DSDEN de l'Eure, 24 bd Georges Chauvin, Évreux — 02 32 29 64 00. Portail des collèges : <a href="https://moncollege.eure.fr/">moncollege.eure.fr</a>.</dd>
        </dl>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Transport scolaire</p>
        <h2>Se rendre en classe avec Nomad</h2>
        <p>En Normandie, les transports scolaires sont organisés par la <strong>Région Normandie</strong> via le réseau <strong>Nomad</strong>, de la maternelle au lycée. L'inscription est annuelle et se fait en ligne, en général avant l'été — pensez à vérifier la date limite chaque année.</p>
        <ul>
          <li>Inscription &amp; informations : <a href="https://nomad.normandie.fr/le-transport-scolaire-0">nomad.normandie.fr</a>.</li>
          <li>Renseignements (Évreux) : 02 22 55 00 10.</li>
        </ul>
        <p class="eyebrow" style="margin-top:2rem">Au quotidien</p>
        <h2>Cantine &amp; périscolaire</h2>
        <p>Restauration, garderie du matin et du soir, accueil de loisirs : ces services sont organisés au niveau de l'école de rattachement. La mairie d'Acon vous indiquera les lieux, horaires et tarifs en vigueur.</p>
      </div>
    </section>''')

# ======================================================================
# EMPLOI
# ======================================================================
PAGES["emploi.html"] = dict(active="pratique",
  title="Emploi &amp; insertion — Acon (Eure)",
  desc="Emploi près d'Acon (Eure) : agence France Travail de Verneuil, Mission Locale pour les jeunes, orientation et insertion.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Travail</span>
        <h1>Emploi &amp; insertion</h1>
        <p class="lead mesure">Les interlocuteurs de proximité pour chercher un emploi, se former ou être accompagné, à quelques kilomètres d'Acon.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Recherche d'emploi</p>
        <h2>France Travail</h2>
        <p>L'agence de proximité est celle de <strong>Verneuil d'Avre et d'Iton</strong> (ex-Pôle emploi).</p>
        <dl class="def">
          <dt>Adresse</dt><dd>135 rue Porte de Mortagne, 27130 Verneuil d'Avre et d'Iton</dd>
          <dt>Téléphone</dt><dd>3949 (service gratuit + prix d'un appel)</dd>
          <dt>En ligne</dt><dd><a href="https://www.francetravail.fr/">francetravail.fr</a> — offres, inscription, actualisation. Vérifiez votre agence via l'<a href="https://www.francetravail.fr/annuaire/">annuaire France Travail</a>.</dd>
        </dl>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Les 16-25 ans</p>
        <h2>Mission Locale</h2>
        <p>Les jeunes de 16 à 25 ans peuvent être accompagnés gratuitement, sur l'emploi mais aussi la formation, la santé, le logement et la mobilité.</p>
        <dl class="def">
          <dt>Antenne</dt><dd>Mission Locale Pays d'Évreux &amp; Eure Sud — antenne de Verneuil, 1 avenue Robert-Zaïgue, 27130 Verneuil d'Avre et d'Iton</dd>
          <dt>Téléphone</dt><dd>02 32 60 62 40</dd>
          <dt>En ligne</dt><dd><a href="https://missionlocaleevreux-euresud.net/">missionlocaleevreux-euresud.net</a></dd>
        </dl>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Se repérer</p>
        <h2>Orientation &amp; économie locale</h2>
        <ul>
          <li><strong>Onisep</strong> — métiers et formations : <a href="https://www.onisep.fr/">onisep.fr</a>.</li>
          <li><strong>Évreux Portes de Normandie</strong> — développement économique et aides du territoire : <a href="https://www.evreuxportesdenormandie.fr">evreuxportesdenormandie.fr</a>.</li>
        </ul>
        <div class="tip"><span class="ico" aria-hidden="true">🤝</span><p>Vous recrutez à Acon ou dans la vallée ? Signalez-le : votre offre peut être relayée dans l'<a href="entreprises.html">annuaire du village</a>. {mail("Proposer une offre")}</p></div>
      </div>
    </section>''')

# ======================================================================
# DÉCHETS & TRI
# ======================================================================
PAGES["dechets.html"] = dict(active="pratique",
  title="Déchets &amp; tri — Acon (Eure) : collecte et déchèterie",
  desc="Déchets à Acon (Eure) : collecte par Évreux Portes de Normandie, consignes de tri, déchèterie de La Madeleine-de-Nonancourt, calendrier.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Environnement</span>
        <h1>Déchets &amp; tri</h1>
        <p class="lead mesure">Bien trier, sortir ses bacs au bon moment et savoir où déposer le reste. À Acon, la collecte est gérée par l'agglomération Évreux Portes de Normandie.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Collecte</p>
        <h2>Qui s'en occupe, et quand</h2>
        <p>La collecte est assurée par la <strong>communauté d'agglomération Évreux Portes de Normandie</strong> (service prévention et gestion des déchets), et le traitement est confié au <strong>SETOM de l'Eure</strong>. Les jours de ramassage varient selon les rues et l'année : le calendrier « Acon » à jour est le seul repère fiable.</p>
        <dl class="def">
          <dt>Calendrier de collecte</dt><dd>À télécharger sur le <a href="https://www.evreuxportesdenormandie.fr/les-services-et-equipements/environnement/prevention-et-gestion-des-dechets/">portail déchets d'Évreux Portes de Normandie</a>.</dd>
          <dt>Service déchets (agglo)</dt><dd>02 32 31 98 51 — bal_gdd@epn-agglo.fr</dd>
          <dt>Sortie des bacs</dt><dd>La veille au soir ou avant l'heure de passage.</dd>
        </dl>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Bien trier</p>
        <h2>Les bons réflexes</h2>
        <ul>
          <li><strong>Bac / sac jaune</strong> — emballages plastique, métal et carton, briques et papiers. Inutile de les laver : il suffit de bien les vider.</li>
          <li><strong>Verre</strong> — bouteilles, bocaux et pots, sans bouchon ni couvercle, en borne d'apport volontaire (jamais dans le bac).</li>
          <li><strong>Ordures ménagères</strong> — tout ce qui ne se trie ni ne se composte.</li>
          <li><strong>Biodéchets</strong> — épluchures et restes : depuis 2024, le tri à la source est la règle. Le compostage reste la solution la plus simple au jardin.</li>
          <li><strong>En déchèterie</strong> — déchets verts, encombrants, gravats, bois, ferraille, appareils électriques, piles, ampoules, peintures et produits dangereux.</li>
        </ul>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Déchèterie</p>
        <h2>La déchèterie de rattachement</h2>
        <dl class="def">
          <dt>Adresse</dt><dd>Déchèterie de <strong>La Madeleine-de-Nonancourt</strong> — 16 rue de Damville, 27320 La Madeleine-de-Nonancourt.</dd>
          <dt>Accès</dt><dd>Sur présentation d'une carte d'accès (gratuite). Renseignez-vous auprès de la mairie ou de l'agglomération, avec un justificatif de domicile.</dd>
          <dt>Horaires</dt><dd>Généralement du lundi au samedi (sauf jeudi), matin et après-midi. Les horaires changent selon la saison : vérifiez sur le <a href="https://www.setom.fr">site du SETOM</a> avant de vous déplacer.</dd>
        </dl>
        <div class="tip"><span class="ico" aria-hidden="true">♻️</span><p><strong>Moins jeter, c'est possible :</strong> composter, coller un « Stop pub » sur la boîte aux lettres, donner ou réparer plutôt que jeter, déposer les textiles en bornes dédiées.</p></div>
      </div>
    </section>''')

# ======================================================================
# EAU & ÉNERGIE
# ======================================================================
PAGES["eau-energie.html"] = dict(active="pratique",
  title="Eau &amp; énergie — Acon (Eure) : eau, électricité, gaz, fibre",
  desc="Eau, assainissement, électricité, gaz et fibre à Acon (Eure) : fournisseurs, contacts et numéros d'urgence en cas de coupure ou de fuite.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Maison</span>
        <h1>Eau &amp; énergie</h1>
        <p class="lead mesure">Qui contacter pour l'eau, l'électricité, le gaz ou la fibre — et surtout les bons numéros à composer en cas de coupure, de fuite ou d'urgence.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap">
        <p class="eyebrow kicker">En cas d'urgence</p>
        <div class="contacts">
          <div class="contact-card">
            <h3>Électricité — Enedis</h3>
            <p class="num"><a href="tel:+33972675027">09 72 67 50 27</a></p>
            <p>Dépannage 24 h/24 dans l'Eure (coupure, panne, danger). Appel non surtaxé.</p>
          </div>
          <div class="contact-card">
            <h3>Sécurité gaz — GRDF</h3>
            <p class="num"><a href="tel:+33800473333">0 800 47 33 33</a></p>
            <p>Odeur de gaz, fuite : numéro vert national, gratuit, 24 h/24 et 7 j/7.</p>
          </div>
          <div class="contact-card">
            <h3>Eau — Eaux de Normandie</h3>
            <p class="num"><a href="tel:+33969327080">09 69 32 70 80</a></p>
            <p>Service client et urgence (fuite, coupure). Le numéro d'astreinte exact figure au dos de votre facture.</p>
          </div>
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Eau potable &amp; assainissement</p>
        <h2>L'eau à Acon</h2>
        <p>L'eau potable d'Acon est produite et distribuée en <strong>régie publique par l'agglomération Évreux Portes de Normandie</strong>. La gestion des abonnements, de la facturation et des urgences est confiée à <strong>Eaux de Normandie</strong> (groupe Suez) : c'est donc ce service que vous appelez au quotidien.</p>
        <dl class="def">
          <dt>Abonnement &amp; factures</dt><dd>Eaux de Normandie — 09 69 32 70 80</dd>
          <dt>Service eau de l'agglo</dt><dd>02 32 31 99 10 — eaupotable@epn-agglo.fr (raccordement, questions générales)</dd>
          <dt>Assainissement</dt><dd>Acon relève de l'assainissement non collectif (chaque logement a son installation). Le contrôle est assuré par le SPANC de l'agglomération.</dd>
          <dt>Qualité de l'eau</dt><dd>Résultats publics sur <a href="https://www.services.eaufrance.fr/commune/27002">services.eaufrance.fr</a>.</dd>
        </dl>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Électricité &amp; gaz</p>
        <h2>Réseaux &amp; fournisseurs</h2>
        <p><strong>Enedis</strong> gère le réseau électrique (le fil, le compteur, les pannes), quel que soit votre fournisseur d'énergie. Pour un déménagement ou un changement de contrat, vous contactez votre fournisseur ; pour une panne ou un danger, vous appelez Enedis. En cas d'odeur de gaz, on n'hésite jamais : on appelle GRDF et on aère.</p>

        <p class="eyebrow" style="margin-top:2.2rem">Internet</p>
        <h2>La fibre</h2>
        <p>Le déploiement de la fibre dans l'Eure est porté par le réseau public <strong>Eure Normandie Numérique</strong>. La couverture progresse vite dans les communes rurales : le mieux est de tester votre adresse.</p>
        <ul>
          <li>Tester mon éligibilité : <a href="https://www.eurenormandienumerique.fr/le-reseau-public-de-fibre/tester-mon-eligibilite/">eurenormandienumerique.fr</a>.</li>
          <li>Comparateur indépendant (ARCEP) : <a href="https://maconnexioninternet.arcep.fr">Ma connexion internet</a>.</li>
        </ul>
      </div>
    </section>''')

# ======================================================================
# ANNUAIRE DES ENTREPRISES
# ======================================================================
PAGES["entreprises.html"] = dict(active="annuaire",
  title="Annuaire des entreprises &amp; services d'Acon (Eure)",
  desc="Annuaire des commerces, artisans, producteurs et services installés à Acon (Eure). Faites-vous connaître gratuitement.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Économie locale</span>
        <h1>L'annuaire du village</h1>
        <p class="lead mesure">Commerces, artisans, producteurs et professionnels d'Acon : un carnet d'adresses pour faire vivre l'activité de la commune et se rendre service entre voisins.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <div class="callout">
          <strong>Cet annuaire se construit avec vous.</strong> Vous exercez une activité à Acon — artisan, producteur, service à domicile, profession libérale, chambre d'hôtes ? Faites-vous référencer gratuitement : quelques lignes suffisent. {mail("Ajouter mon activité")}
        </div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap">
        <p class="eyebrow kicker">Les catégories</p>
        <div class="grid">
          <div class="card"><h3>Commerces &amp; services</h3><p>Alimentation, coiffure, restauration, services du quotidien.</p></div>
          <div class="card"><h3>Artisans &amp; bâtiment</h3><p>Menuisier, maçon, électricien, paysagiste, couvreur…</p></div>
          <div class="card"><h3>Agriculture &amp; produits locaux</h3><p>Élevage, maraîchage, vente directe à la ferme.</p></div>
          <div class="card"><h3>Santé &amp; bien-être</h3><p>Infirmier·e, praticien·ne, aide et soins à domicile.</p></div>
        </div>
        <p style="margin-top:1.4rem;color:var(--gris)"><small>Les fiches seront ajoutées au fur et à mesure des demandes, avec l'accord de chaque professionnel.</small></p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Astuce</p>
        <h2>Retrouver les entreprises immatriculées</h2>
        <p>La liste des établissements enregistrés à Acon est consultable publiquement sur l'<strong>Annuaire des Entreprises</strong> de l'État, en filtrant par commune : <a href="https://annuaire-entreprises.data.gouv.fr/">annuaire-entreprises.data.gouv.fr</a>. Nous vérifions chaque fiche et demandons l'accord des professionnels avant de publier leurs coordonnées ici.</p>
      </div>
    </section>''')

# ======================================================================
# À PROPOS
# ======================================================================
PAGES["apropos.html"] = dict(active="apropos",
  title="À propos — le site du village d'Acon",
  desc="À propos du site d'Acon (Eure) : un projet personnel et bénévole, indépendant de la mairie, fait par une habitante pour les habitants.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> À propos</span>
        <h1>Ce site, en toute transparence</h1>
        <p class="lead mesure">Un site de village fait avec le cœur, par une habitante, pour les habitants et les curieux d'Acon.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Le mot de l'autrice</p>
        <h2>Pourquoi ce site</h2>
        <p>Je suis venue habiter à Acon il y a quelques années, et j'ai eu un vrai coup de cœur pour cette petite commune et la gentillesse de ses habitants. De ce quotidien est née l'envie de rassembler, au même endroit, tout ce qui aide à se sentir bien ici : découvrir le village et son histoire, mais aussi retrouver sans effort les infos utiles de tous les jours — écoles, déchets, eau, démarches, bonnes adresses.</p>
        <p style="font-family:var(--display); font-style:italic; color:var(--vert-fonce); margin-top:1.2rem">— Élodie</p>
        <div class="tip"><span class="ico" aria-hidden="true">✉️</span><p>Une remarque, une correction, une idée, une photo à partager ? Cette adresse est là pour ça : {mail("m'écrire")}</p></div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Indépendance</p>
        <h2>Un site sans lien avec la mairie</h2>
        <p>Ce site est <strong>totalement indépendant de la commune d'Acon</strong>. Il n'émane pas de la municipalité, ne l'engage en rien et n'a aucun caractère officiel. Pour toute démarche ou information officielle, la référence reste la mairie (02 32 32 53 49) et <a href="https://www.service-public.fr">service-public.fr</a>. <small>L'ancien site officiel <em>mairie-acon.fr</em> n'est plus en ligne depuis 2016 ; ce site d'entraide vise en partie à combler ce manque, sans s'y substituer.</small></p>
        <div class="callout"><strong>En toute bonne foi :</strong> ce site n'a d'autre but que d'informer et de rendre service. Si la mairie souhaitait un jour récupérer le nom de domaine ou reprendre le projet, je m'engage à le lui céder de bon cœur.</div>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Crédits</p>
        <h2>Photographies &amp; sources</h2>
        <p>Les photographies du village proviennent de <strong>Wikimedia Commons</strong> et sont réutilisées sous licence <strong>Creative Commons</strong>, avec attribution et partage dans les mêmes conditions. Les images ont pu être recadrées ou allégées pour le web.</p>
        <ul>
          <li>Église Saint-Denis (accueil) — <em>Davitof</em>, Wikimedia Commons, <a href="https://creativecommons.org/licenses/by-sa/3.0/deed.fr">CC BY-SA 3.0</a>.</li>
          <li>Église Saint-Denis (vues) &amp; Les Prés d'Acon — <em>X-Javier</em>, Wikimedia Commons, <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">CC BY-SA 4.0</a>.</li>
          <li>Informations et histoire : Wikipédia, base Mérimée (POP, ministère de la Culture), dictionnaire topographique de l'Eure, INSEE, et la communauté d'agglomération Évreux Portes de Normandie.</li>
        </ul>
        <p><small>Une photo vous appartient et vous souhaitez une correction d'attribution ou un retrait ? {mail("Écrivez-moi", "Crédit photo")} — j'y donnerai suite rapidement.</small></p>
      </div>
    </section>''')

# ======================================================================
# MENTIONS LÉGALES
# ======================================================================
PAGES["mentions-legales.html"] = dict(active="apropos",
  title="Mentions légales — le site du village d'Acon",
  desc="Mentions légales du site d'information d'Acon (Eure) : éditeur, hébergeur, propriété intellectuelle, crédits, données personnelles.",
  body=f'''    <section class="hero">
      <div class="wrap">
        <span class="badge"><span class="dot"></span> Informations légales</span>
        <h1>Mentions légales</h1>
        <p class="lead mesure">Qui édite ce site, où il est hébergé, et les règles qui s'y appliquent. Un site d'information bénévole, indépendant et non officiel.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Éditeur</p>
        <h2>Éditrice du site</h2>
        <p>Ce site est édité à titre <strong>personnel et bénévole</strong> par une habitante d'Acon (Élodie). Il ne poursuit aucun but commercial et n'émane d'aucune administration.</p>
        <dl class="def">
          <dt>Contact</dt><dd>{mail("Afficher l'adresse e-mail", "Mentions légales")}</dd>
          <dt>Directeur de la publication</dt><dd>L'éditrice du site.</dd>
        </dl>
        <div class="tip"><span class="ico" aria-hidden="true">ℹ️</span><p><strong>Site non officiel.</strong> Ce site est <strong>indépendant de la commune d'Acon</strong> : il ne la représente pas et ne l'engage en rien. Pour toute démarche officielle : mairie d'Acon (02 32 32 53 49) et <a href="https://www.service-public.fr">service-public.fr</a>.</p></div>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Hébergement</p>
        <h2>Hébergeur</h2>
        <p>Le site est hébergé par <strong>GitHub Pages</strong> — GitHub, Inc., 88 Colin P. Kelly Jr. Street, San Francisco, CA 94107, États-Unis (<a href="https://github.com">github.com</a>). Il s'agit de pages statiques, sans base de données.</p>
      </div>
    </section>

    <section class="section">
      <div class="wrap mesure">
        <p class="eyebrow">Contenus</p>
        <h2>Propriété intellectuelle &amp; crédits</h2>
        <ul>
          <li><strong>Textes</strong> — rédigés pour ce site à partir de sources publiques (Wikipédia, base Mérimée du ministère de la Culture, INSEE, service-public.fr, communauté d'agglomération Évreux Portes de Normandie).</li>
          <li><strong>Photographies du village</strong> — issues de <strong>Wikimedia Commons</strong>, sous licence <a href="https://creativecommons.org/licenses/by-sa/4.0/deed.fr">Creative Commons BY-SA</a> (auteurs Davitof et X-Javier), créditées sous chaque image et sur la page <a href="apropos.html">À propos</a>.</li>
          <li><strong>Cartes postales anciennes</strong> — reproductions des <strong>Archives départementales de l'Eure</strong> (série 8 Fi 2, [1890]-[1950]). Vues anciennes majoritairement dans le domaine public ; reproduction créditée aux Archives de l'Eure.</li>
        </ul>
        <p>Vous êtes titulaire de droits sur un contenu et souhaitez une correction ou un retrait ? {mail("Écrivez-moi", "Droits — retrait")} : j'y donnerai suite rapidement.</p>
      </div>
    </section>

    <section class="section section-alt">
      <div class="wrap mesure">
        <p class="eyebrow">Vie privée</p>
        <h2>Données personnelles &amp; cookies</h2>
        <p>Ce site <strong>ne collecte aucune donnée personnelle</strong>, ne dépose <strong>aucun cookie</strong> de suivi et n'utilise aucun outil de mesure d'audience. Si vous écrivez à l'adresse de contact, votre message et votre adresse e-mail servent uniquement à vous répondre, et ne sont ni conservés à d'autres fins ni transmis à des tiers.</p>
        <p><small>Les liens vers des sites tiers (service-public.fr, Facebook, Archives de l'Eure, fournisseurs…) sont fournis pour votre information ; leur contenu relève de leurs éditeurs respectifs.</small></p>
      </div>
    </section>''')

# ---------------------------------------------------------------------
import io, os
here = os.path.dirname(os.path.abspath(__file__))
for fname, p in PAGES.items():
    html = page(p["active"], p["title"], p["desc"], p["body"])
    with io.open(os.path.join(here, fname), "w", encoding="utf-8") as f:
        f.write(html)
    print("écrit :", fname)
print("Terminé —", len(PAGES), "pages.")
