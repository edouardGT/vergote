"""Builds every page of the site (plain HTML) from this script. Usage: python3 tools/build.py .
The generated HTML is committed; GitHub Pages serves it as is (no build on GitHub)."""
import json
import pathlib
import sys

OUT = pathlib.Path(sys.argv[1])
SITE = "https://tuinenvergotemathieu.be"
PHONE_TXT = "0477 47 90 73"
PHONE_TEL = "+32477479073"
EMAIL = "info@tuinenvergotemathieu.be"
VAT = "BE 0681.298.009"
# Saffron Facebook page "De afspanning" (Gits), confirmed by the owner 2026-11-20.
FACEBOOK_URL = "https://www.facebook.com/profile.php?id=61563440602293"
FB_ICON = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false"><path fill="currentColor" d="M12 2a10 10 0 0 0-1.6 19.9v-7H7.9V12h2.5V9.8c0-2.5 1.5-3.9 3.8-3.9 1.1 0 2.2.2 2.2.2v2.5h-1.3c-1.2 0-1.6.8-1.6 1.6V12h2.8l-.4 2.9h-2.4v7A10 10 0 0 0 12 2z"/></svg>')


def fb_button():
    return f'<a class="button button--line" href="{FACEBOOK_URL}" rel="noopener">{FB_ICON}Volg De afspanning op Facebook</a>'


ICON = {
    "phone": '<rect x="7" y="2.5" width="10" height="19" rx="2.5"/><path d="M11 18.5h2"/>',
    "mail": '<rect x="3" y="5" width="18" height="14" rx="2"/><path d="m3.5 6.5 8.5 6.5 8.5-6.5"/>',
    "menu": '<path d="M4 8h16M4 16h16"/>',
}
SPRIG = ('<svg viewBox="0 0 24 24" aria-hidden="true" focusable="false">'
         '<path d="M12 21C12 15 12.5 10 15 5" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round"/>'
         '<path d="M12.4 13.5C9 13.6 6.6 11.6 6 8.4 9.4 8.3 11.8 10.3 12.4 13.5Z" fill="currentColor"/>'
         '<path d="M13.6 9.6C14 6.5 16.4 4.4 19.6 4 19.3 7.2 16.9 9.3 13.6 9.6Z" fill="currentColor"/></svg>')


def icon(name):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.8" '
            f'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICON[name]}</svg>')


def photo(name, alt="", sizes="100vw", lazy=True, priority=False, widths=None):
    """Responsive <img> for a photo in assets/img/photos/<name>-<w>.webp"""
    widths = widths or PHOTO_WIDTHS[name]
    srcset = ", ".join(f"assets/img/photos/{name}-{w}.webp {w}w" for w in widths)
    w = widths[-1]
    h = round(w * 2 / 3)
    attrs = ' loading="lazy" decoding="async"' if lazy else ""
    if priority:
        attrs += ' fetchpriority="high"'
    return (f'<img src="assets/img/photos/{name}-{w}.webp" srcset="{srcset}" sizes="{sizes}" '
            f'alt="{alt}" width="{w}" height="{h}"{attrs}>')


PHOTO_WIDTHS = {
    "tuin-grassen": [960, 1920],
    "bank-tussen-gras": [960, 1600],
    "handen-planten": [1000],
    "haag": [1000, 1920],
    "saffraankrokus": [1000],
    "saffraan-bloemen": [960, 1920],
    "grassen-wind": [960, 1600],
    "border-vaste-planten": [960, 1600],
    "saffraan-draadjes": [800, 1400],
}

NAV = [
    ("tuinaanleg.html", "Tuinaanleg"),
    ("tuinonderhoud.html", "Tuinonderhoud"),
    ("realisaties.html", "Realisaties"),
    ("saffraan.html", "Saffraan"),
    ("contact.html", "Contact"),
]


def header(current, over):
    cur = ' aria-current="page"'
    items = "\n".join(
        f'          <li><a href="{href}"{cur if href == current else ""}>{label}</a></li>'
        for href, label in NAV
    )
    cls = "site-header site-header--over" if over else "site-header"
    return f"""<a class="skip-link" href="#inhoud">Naar de inhoud</a>
<header class="{cls}">
  <div class="wrap header-inner">
    <a class="brand" href="./">{SPRIG}<span>Tuinen Vergote</span></a>
    <nav class="site-nav" aria-label="Hoofdmenu">
      <button class="menu-button" type="button" popovertarget="site-menu" popovertargetaction="toggle" aria-controls="site-menu">{icon("menu")}<span>Menu</span></button>
      <ul id="site-menu" class="site-menu" popover="auto">
{items}
      </ul>
    </nav>
    <a class="call" href="tel:{PHONE_TEL}" aria-label="Bel Mathieu op {PHONE_TXT}">{icon("phone")}<span class="call-number">{PHONE_TXT}</span></a>
  </div>
</header>"""


FOOTER = f"""<footer class="site-footer">
  <div class="wrap">
    <div class="footer-grid">
      <div>
        <p class="footer-name">Tuinen Vergote</p>
        <p>Tuinaanleg en tuinonderhoud in Gits en omgeving.</p>
      </div>
      <div>
        <h2>Contact</h2>
        <ul>
          <li><a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></li>
          <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        </ul>
      </div>
      <div>
        <h2>Gegevens</h2>
        <address>Tuinen Vergote Mathieu<br>Amersveldestraat 4<br>8830 Gits</address>
        <p>Ondernemingsnummer en btw {VAT}</p>
      </div>
    </div>
    <div class="footer-bottom">
      <span>&copy; <span id="jaar">2026</span> Tuinen Vergote Mathieu</span>
      <span>Sfeerfoto's: <a href="https://unsplash.com" rel="noopener">Unsplash</a></span>
      <a href="privacy.html">Privacyverklaring</a>
    </div>
  </div>
</footer>
<script src="assets/js/site.js" defer></script>"""


def contact_block():
    return f"""<section class="section section--salie" aria-labelledby="contact-title">
  <div class="wrap contact-block">
    <div>
      <h2 id="contact-title">Zin in een tuin waar u tot rust komt?</h2>
      <p>Bel of mail Mathieu en vertel wat u in gedachten hebt.</p>
      <a class="big-phone" href="tel:{PHONE_TEL}">{PHONE_TXT}</a>
      <div class="actions">
        <a class="button button--mos" href="mailto:{EMAIL}">{icon("mail")}Mail Mathieu</a>
      </div>
    </div>
    {photo("grassen-wind", sizes="(max-width: 52rem) 100vw, 50vw")}
  </div>
</section>"""


def page(filename, title, description, body, current=None, over=False, contact=True, extra_head="", preload=None):
    canonical = f"{SITE}/" if filename == "index.html" else f"{SITE}/{filename}"
    pre = ""
    if preload:
        name, widths = preload, PHOTO_WIDTHS[preload]
        srcset = ", ".join(f"assets/img/photos/{name}-{w}.webp {w}w" for w in widths)
        pre = f'\n<link rel="preload" as="image" type="image/webp" imagesrcset="{srcset}" imagesizes="100vw" fetchpriority="high">'
    html = f"""<!doctype html>
<html lang="nl-BE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{description}">
<link rel="canonical" href="{canonical}">
<meta property="og:type" content="website">
<meta property="og:locale" content="nl_BE">
<meta property="og:site_name" content="Tuinen Vergote Mathieu">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{canonical}">
<meta name="theme-color" content="#2B3B2D">
<link rel="icon" href="assets/img/favicon.svg" type="image/svg+xml">
<link rel="preload" href="assets/fonts/fraunces.woff2" as="font" type="font/woff2" crossorigin>
<link rel="preload" href="assets/fonts/figtree.woff2" as="font" type="font/woff2" crossorigin>{pre}
<link rel="stylesheet" href="assets/css/style.css">{extra_head}
</head>
<body>
{header(current, over)}
<main id="inhoud">
{body}
{contact_block() if contact else ""}
</main>
{FOOTER}
</body>
</html>
"""
    (OUT / filename).write_text(html, encoding="utf-8")


def page_hero(h1, lead, img):
    return f"""<section class="photo-hero page-hero">
  {photo(img, lazy=False, priority=True)}
  <div class="wrap">
    <h1>{h1}</h1>
    <p>{lead}</p>
  </div>
</section>"""


def page_head(h1, lead):
    return f"""<section class="page-head">
  <div class="wrap">
    <h1>{h1}</h1>
    <p>{lead}</p>
  </div>
</section>"""


# ---------- home ----------
jsonld = {
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Tuinen Vergote Mathieu",
    "description": "Tuinaanleg en tuinonderhoud in Gits en omgeving.",
    "url": f"{SITE}/",
    "telephone": PHONE_TEL,
    "email": EMAIL,
    "vatID": "BE0681298009",
    "address": {
        "@type": "PostalAddress",
        "streetAddress": "Amersveldestraat 4",
        "postalCode": "8830",
        "addressLocality": "Gits",
        "addressCountry": "BE",
    },
}
home = f"""<section class="photo-hero hero">
  {photo("tuin-grassen", lazy=False, priority=True)}
  <div class="wrap">
    <h1>Een tuin om in tot rust te komen</h1>
    <p>Mathieu Vergote legt tuinen aan en onderhoudt ze, voor particulieren en bedrijven in Gits en omgeving.</p>
    <div class="actions">
      <a class="button button--light" href="tel:{PHONE_TEL}">{icon("phone")}Bel {PHONE_TXT}</a>
      <a class="button button--glass" href="#aanbod">Wat Mathieu doet</a>
    </div>
  </div>
</section>

<section class="section intro" aria-labelledby="intro-title">
  <div class="wrap">
    <div class="sprig">{SPRIG}</div>
    <h2 id="intro-title">Rust, groen en tijd voor uzelf</h2>
    <p>Een tuin is de plek waar u thuiskomt. Mathieu zorgt dat hij er mooi bij ligt: van een nieuwe aanleg tot het snoeien van hagen, bomen en struiken. Het groenafval neemt hij mee. U hoeft alleen nog te genieten.</p>
  </div>
</section>

<section class="section" id="aanbod" aria-label="Wat Mathieu doet" style="padding-block-start:0">
  <div class="wrap offerings">
    <article class="offer">
      {photo("handen-planten", sizes="(max-width: 56rem) 100vw, 33vw")}
      <h3>Tuinaanleg</h3>
      <p>Een nieuwe tuin, of een tuin die opnieuw begint. Mathieu komt kijken, maakt een voorstel en legt de tuin aan.</p>
      <a class="text-link" href="tuinaanleg.html">Over tuinaanleg</a>
    </article>
    <article class="offer">
      {photo("haag", sizes="(max-width: 56rem) 100vw, 33vw", widths=[1000])}
      <h3>Tuinonderhoud</h3>
      <p>Hagen snoeien, bomen en struiken bijwerken, groenzones onderhouden. Eenmalig of op regelmatige basis.</p>
      <a class="text-link" href="tuinonderhoud.html">Over tuinonderhoud</a>
    </article>
    <article class="offer">
      {photo("saffraankrokus", sizes="(max-width: 56rem) 100vw, 33vw")}
      <h3>Saffraan</h3>
      <p>Samen met zijn zoon Juliaan kweekt Mathieu saffraan in Gits: de rode draadjes uit de bloem van de saffraankrokus.</p>
      <a class="text-link" href="saffraan.html">Over de saffraan</a>
    </article>
  </div>
</section>

<section class="photo-hero band" aria-labelledby="band-title">
  {photo("bank-tussen-gras")}
  <div class="wrap">
    <h2 id="band-title">U geniet. Mathieu doet het werk.</h2>
    <p>Hagen in vorm, struiken bijgewerkt, het snoeiafval opgeruimd. Zo blijft uw tuin een plek om te zitten en te kijken.</p>
    <div class="actions">
      <a class="button button--light" href="tuinonderhoud.html">Over tuinonderhoud</a>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="stappen-title">
  <div class="wrap">
    <div class="steps-head">
      <h2 id="stappen-title">Zo begint uw nieuwe tuin</h2>
      <p>Rustig, stap voor stap, en altijd in overleg.</p>
    </div>
    <ol class="steps">
      <li><h3>Kennismaking</h3><p>U vertelt wat u voor ogen hebt. Mathieu komt kijken naar de grond, de ligging en wat er al staat.</p></li>
      <li><h3>Voorstel</h3><p>U krijgt een duidelijk voorstel: wat er gebeurt en wat het kost.</p></li>
      <li><h3>Aanleg</h3><p>Mathieu gaat aan de slag en houdt u op de hoogte tot alles klaar is.</p></li>
      <li><h3>Onderhoud</h3><p>Wilt u dat de tuin mooi blijft? Mathieu neemt ook het onderhoud op zich.</p></li>
    </ol>
  </div>
</section>"""
page(
    "index.html",
    "Tuinen Vergote Mathieu | Tuinaanleg en tuinonderhoud in Gits",
    "Tuinen Vergote Mathieu uit Gits legt tuinen aan en onderhoudt ze, voor particulieren en bedrijven. Hagen snoeien, bomen en struiken, groenzones en afvoer van groenafval.",
    home,
    over=True,
    preload="tuin-grassen",
    extra_head='\n<script type="application/ld+json">' + json.dumps(jsonld, ensure_ascii=False) + "</script>",
)

# ---------- tuinaanleg ----------
aanleg = page_hero(
    "Tuinaanleg",
    "Een nieuwe tuin bij een nieuwbouw, of een bestaande tuin die helemaal opnieuw begint. Mathieu legt hem aan, met oog voor wat u wil en wat de plek aankan.",
    "border-vaste-planten",
) + """

<section class="section" aria-labelledby="aanpak-title">
  <div class="wrap">
    <div class="steps-head">
      <h2 id="aanpak-title">Zo verloopt een aanleg</h2>
      <p>Rustig, stap voor stap, en altijd in overleg.</p>
    </div>
    <ol class="steps">
      <li><h3>Kennismaking</h3><p>U vertelt wat u voor ogen hebt. Mathieu komt kijken naar de grond, de ligging en wat er al staat.</p></li>
      <li><h3>Voorstel</h3><p>U krijgt een duidelijk voorstel: wat er gebeurt en wat het kost.</p></li>
      <li><h3>Aanleg</h3><p>Mathieu gaat aan de slag en houdt u op de hoogte tot alles klaar is.</p></li>
      <li><h3>Onderhoud</h3><p>Wilt u dat de tuin mooi blijft? Mathieu neemt ook het <a href="tuinonderhoud.html">onderhoud</a> op zich.</p></li>
    </ol>
  </div>
</section>"""
page(
    "tuinaanleg.html",
    "Tuinaanleg in Gits | Tuinen Vergote Mathieu",
    "Een nieuwe tuin laten aanleggen in Gits en omgeving? Mathieu Vergote komt kijken, maakt een voorstel en legt uw tuin aan.",
    aanleg,
    current="tuinaanleg.html",
    over=True,
    preload="border-vaste-planten",
)

# ---------- tuinonderhoud ----------
onderhoud = page_hero(
    "Tuinonderhoud",
    "Mathieu houdt tuinen en groenzones netjes, voor particulieren en bedrijven, eenmalig of op regelmatige basis.",
    "haag",
) + f"""

<section class="section" aria-labelledby="wat-title">
  <div class="wrap">
    <h2 id="wat-title" class="section-title">Wat Mathieu voor u doet</h2>
    <ul class="tasks">
      <li><h3>Hagen snoeien</h3><p>Hagen netjes in vorm, zodat de tuin er verzorgd bij ligt.</p></li>
      <li><h3>Bomen en struiken</h3><p>Snoeien en zagen waar nodig, zodat alles gezond en in vorm blijft.</p></li>
      <li><h3>Groenzones</h3><p>Onderhoud van het groen rond woningen en bedrijven.</p></li>
      <li><h3>Groenafval</h3><p>Het snoeiafval neemt Mathieu mee en voert hij af. U houdt een opgeruimde tuin over.</p></li>
    </ul>
  </div>
</section>

<section class="section section--salie" aria-labelledby="bedrijven-title">
  <div class="wrap split">
    <h2 id="bedrijven-title">Ook voor bedrijven</h2>
    <div>
      <p>Ook bedrijven laten hun groenzone door Mathieu onderhouden. Spreek af wat er moet gebeuren en hoe vaak.</p>
      <div class="actions">
        <a class="button button--mos" href="tel:{PHONE_TEL}">{icon("phone")}Bel {PHONE_TXT}</a>
        <a class="button button--line" href="mailto:{EMAIL}">{icon("mail")}Mail Mathieu</a>
      </div>
    </div>
  </div>
</section>"""
page(
    "tuinonderhoud.html",
    "Tuinonderhoud in Gits | Tuinen Vergote Mathieu",
    "Tuinonderhoud voor particulieren en bedrijven in Gits en omgeving: hagen snoeien, bomen en struiken, groenzones en afvoer van groenafval.",
    onderhoud,
    current="tuinonderhoud.html",
    over=True,
    contact=False,
    preload="haag",
)

# ---------- realisaties (no stock photos here: this page is for Mathieu's own work) ----------
real = page_head(
    "Realisaties",
    "Tuinen die Mathieu aanlegde en onderhoudt.",
) + f"""

<section class="section" aria-labelledby="fotos-title">
  <div class="wrap split">
    <h2 id="fotos-title">Hier komen binnenkort foto's</h2>
    <div>
      <p>Mathieu verzamelt foto's van tuinen die hij aanlegde en onderhoudt. Wilt u nu al voorbeelden zien of horen? Bel of mail hem.</p>
      <div class="actions">
        <a class="button button--mos" href="tel:{PHONE_TEL}">{icon("phone")}Bel {PHONE_TXT}</a>
        <a class="button button--line" href="mailto:{EMAIL}">{icon("mail")}Mail Mathieu</a>
      </div>
    </div>
    <!--
      Foto's toevoegen: zet ze in assets/img/realisaties/ (.webp, ongeveer 1600 px breed)
      en vervang deze sectie door:

      <section class="section" aria-label="Foto's">
        <div class="wrap gallery">
          <figure>
            <img src="assets/img/realisaties/voorbeeld.webp" alt="Korte beschrijving van de tuin" width="1600" height="1200" loading="lazy">
            <figcaption>Waar en wat, bv. "Nieuwe haag en borders, Gits"</figcaption>
          </figure>
        </div>
      </section>
    -->
  </div>
</section>"""
page(
    "realisaties.html",
    "Realisaties | Tuinen Vergote Mathieu",
    "Foto's van tuinen die Tuinen Vergote Mathieu aanlegde en onderhoudt.",
    real,
    current="realisaties.html",
    contact=False,
)

# ---------- saffraan ----------
saff = page_hero(
    "Saffraan van Mathieu en Juliaan",
    "Mathieu en zijn zoon Juliaan kweken saffraan op hun veld in de Amersveldestraat in Gits.",
    "saffraan-bloemen",
) + f"""

<section class="section">
  <div class="wrap prose">
    <h2>Met de hand geplukt</h2>
    <p>De saffraankrokus (<i lang="la">Crocus sativus</i>) bloeit maar één keer per jaar, in oktober. Dan plukken Mathieu en Juliaan elke bloem met de hand. Daarna halen ze uit elke bloem de drie rode draadjes, de stempels, ook met de hand. De draadjes drogen enkele dagen en dan is de saffraan klaar.</p>
    <p>Voor één gram saffraan zijn ongeveer 300 bloemen nodig. Daarom is saffraan een van de duurste specerijen ter wereld, en daarom is een beetje genoeg.</p>

    <h2>Koken met saffraan</h2>
    <p>Een paar draadjes volstaan voor een gerecht. Laat ze eerst even weken in wat warm water, melk of bouillon: zo komen kleur en smaak het best vrij.</p>
    <a class="text-link" href="recepten.html">Zes recepten met saffraan</a>

    <h2>Saffraan bestellen</h2>
    <p class="note">Prijs, verpakking en bestellen: die info volgt hier binnenkort. Wilt u nu al saffraan? Bel of mail Mathieu.</p>
    <div class="actions">
      <a class="button button--mos" href="tel:{PHONE_TEL}">{icon("phone")}Bel {PHONE_TXT}</a>
      <a class="button button--line" href="mailto:{EMAIL}?subject=Saffraan">{icon("mail")}Mail over saffraan</a>
      {fb_button()}
    </div>
  </div>
</section>"""
page(
    "saffraan.html",
    "Saffraan uit Gits | Tuinen Vergote Mathieu",
    "Saffraan uit Gits, gekweekt door Mathieu en Juliaan Vergote en in oktober met de hand geplukt. Met recepten.",
    saff,
    current="saffraan.html",
    over=True,
    contact=False,
    preload="saffraan-bloemen",
)

# ---------- recepten ----------
sys.path.insert(0, str(pathlib.Path(__file__).parent))
from recepten_data import RECEPTEN, TIPS  # noqa: E402

tips_html = "\n".join(f'      <li><h3>{t}</h3><p>{d}</p></li>' for t, d in TIPS)
index_html = "\n".join(
    f'      <li><a href="#{r["id"]}"><span class="recipe-land">{r["land"]}</span>'
    f'<span class="recipe-name">{r["titel"]}</span>'
    f'<span class="recipe-meta">{r["personen"]}, {r["tijd"]}</span></a></li>'
    for r in RECEPTEN
)


def recipe_html(r):
    ing = "\n".join(f"          <li>{i}</li>" for i in r["ingredienten"])
    steps = "\n".join(f"          <li>{st}</li>" for st in r["stappen"])
    return f"""<article class="section recipe" id="{r['id']}" aria-labelledby="{r['id']}-titel">
  <div class="wrap">
    <p class="recipe-land">{r['land']}</p>
    <h2 id="{r['id']}-titel">{r['titel']}</h2>
    <p class="recipe-intro">{r['intro']}</p>
    <dl class="recipe-facts">
      <div><dt>Voor</dt><dd>{r['personen']}</dd></div>
      <div><dt>Tijd</dt><dd>{r['tijd']}</dd></div>
    </dl>
    <div class="recipe-body">
      <div class="recipe-ingredients">
        <h3>Ingrediënten</h3>
        <ul>
{ing}
        </ul>
      </div>
      <div class="recipe-steps">
        <h3>Bereiding</h3>
        <ol>
{steps}
        </ol>
        <p class="recipe-tip"><strong>Tip.</strong> {r['tip']}</p>
      </div>
    </div>
    <a class="text-link" href="#overzicht">Naar alle recepten</a>
  </div>
</article>"""


recepten = f"""<section class="page-head page-head--split">
  <div class="wrap">
    <div>
      <h1>Recepten met saffraan</h1>
      <p>Zes klassiekers uit de hele wereld, van Valencia tot Teheran. Met een paar draadjes saffraan maakt u ze zelf.</p>
      <a class="text-link" href="saffraan.html">Over de saffraan van Mathieu en Juliaan</a>
    </div>
    {photo("saffraan-draadjes", alt="Saffraandraadjes naast een glazen potje", sizes="(max-width: 52rem) 100vw, 40vw", lazy=False, priority=True)}
  </div>
</section>

<section class="section" aria-labelledby="tips-title">
  <div class="wrap">
    <h2 id="tips-title" class="section-title">Werken met saffraan</h2>
    <ul class="tips">
{tips_html}
    </ul>
  </div>
</section>

<section class="section section--salie" id="overzicht" aria-labelledby="overzicht-title">
  <div class="wrap">
    <h2 id="overzicht-title" class="section-title">Zes recepten</h2>
    <ul class="recipe-index">
{index_html}
    </ul>
  </div>
</section>

{chr(10).join(recipe_html(r) for r in RECEPTEN)}

<section class="section section--salie" aria-labelledby="bestel-title">
  <div class="wrap split">
    <h2 id="bestel-title">Zin om te koken met saffraan uit Gits?</h2>
    <div>
      <p>Bel of mail Mathieu voor saffraan. Nieuws over de oogst vindt u bij De afspanning op Facebook.</p>
      <div class="actions">
        <a class="button button--mos" href="tel:{PHONE_TEL}">{icon("phone")}Bel {PHONE_TXT}</a>
        <a class="button button--line" href="mailto:{EMAIL}?subject=Saffraan">{icon("mail")}Mail over saffraan</a>
        {fb_button()}
      </div>
    </div>
  </div>
</section>"""
page(
    "recepten.html",
    "Recepten met saffraan | Tuinen Vergote Mathieu",
    "Zes klassieke recepten met saffraan: risotto alla milanese, paella valenciana, mosselen in saffraanroom, Perzische saffraanrijst, lussekatter en kesar kheer.",
    recepten,
    current="saffraan.html",
    contact=False,
)

# ---------- contact ----------
contact = page_head(
    "Contact",
    "Een tuin laten aanleggen, onderhoud plannen of saffraan bestellen? Bel of mail Mathieu.",
) + f"""

<section class="section" aria-label="Contactgegevens">
  <div class="wrap">
    <dl class="facts">
      <div><dt>Telefoon</dt><dd><a href="tel:{PHONE_TEL}">{PHONE_TXT}</a></dd></div>
      <div><dt>E-mail</dt><dd><a href="mailto:{EMAIL}">info@<wbr>tuinenvergotemathieu.be</a></dd></div>
      <div><dt>Adres</dt><dd>Amersveldestraat 4, 8830 Gits</dd></div>
      <div><dt>Werkgebied</dt><dd>Gits en omgeving</dd></div>
      <div><dt>Ondernemingsnummer en btw</dt><dd>{VAT}</dd></div>
    </dl>
    <p class="prose" style="margin-block-start:3.5rem;color:var(--muted)">Er is bewust geen contactformulier: uw gegevens blijven tussen u en Mathieu. Lees ook de <a href="privacy.html">privacyverklaring</a>.</p>
  </div>
</section>"""
page(
    "contact.html",
    "Contact | Tuinen Vergote Mathieu",
    "Contacteer Tuinen Vergote Mathieu in Gits: telefoon 0477 47 90 73, e-mail info@tuinenvergotemathieu.be.",
    contact,
    current="contact.html",
    contact=False,
)

# ---------- privacy ----------
privacy = page_head(
    "Privacyverklaring",
    "Kort en duidelijk: wat er met uw gegevens gebeurt.",
) + f"""

<section class="section">
  <div class="wrap prose">
    <h2>Wie?</h2>
    <p>Tuinen Vergote Mathieu (Mathieu Vergote), Amersveldestraat 4, 8830 Gits, ondernemingsnummer 0681.298.009. Vragen: <a href="mailto:{EMAIL}">{EMAIL}</a>.</p>

    <h2>Deze website</h2>
    <p>Deze website gebruikt geen cookies, geen statistieken en geen formulieren. Ze draait op GitHub Pages (Verenigde Staten). GitHub verwerkt technische gegevens zoals uw IP-adres om de site te tonen.</p>

    <h2>Als u belt of mailt</h2>
    <p>Dan gebruikt Mathieu uw gegevens alleen om te antwoorden, een voorstel te maken, het werk uit te voeren en te factureren. Dat is nodig voor de overeenkomst en voor zijn boekhouding. Mails lopen via OVHcloud. Hij bewaart niets langer dan nodig; facturen zo lang als de wet vraagt.</p>

    <h2>Uw rechten</h2>
    <p>U kunt uw gegevens inkijken, laten verbeteren, wissen, beperken, overdragen of er bezwaar tegen maken via <a href="mailto:{EMAIL}">{EMAIL}</a>. Klachten: Gegevensbeschermingsautoriteit, <a href="https://www.gegevensbeschermingsautoriteit.be" rel="noopener">www.gegevensbeschermingsautoriteit.be</a>.</p>

    <p><em>Laatst bijgewerkt op 20 november 2026.</em></p>
  </div>
</section>"""
page(
    "privacy.html",
    "Privacyverklaring | Tuinen Vergote Mathieu",
    "Privacyverklaring van Tuinen Vergote Mathieu: geen cookies, geen statistieken, geen formulieren, en wat er gebeurt met uw gegevens als u belt of mailt.",
    privacy,
    contact=False,
)

# ---------- 404 ----------
nf = page_head("Deze pagina bestaat niet", "De link klopt niet, of de pagina is verhuisd.") + """

<section class="section" style="padding-block-start:3rem">
  <div class="wrap actions">
    <a class="button button--mos" href="./">Naar de startpagina</a>
    <a class="button button--line" href="contact.html">Contact</a>
  </div>
</section>"""
page("404.html", "Pagina niet gevonden | Tuinen Vergote Mathieu", "Deze pagina bestaat niet.", nf, contact=False)
p404 = OUT / "404.html"
t = p404.read_text(encoding="utf-8")
for a, b in [('href="assets/', 'href="/assets/'), ('src="assets/', 'src="/assets/'), ('href="./"', 'href="/"')]:
    t = t.replace(a, b)
for href, _ in NAV + [("privacy.html", "")]:
    t = t.replace(f'href="{href}"', f'href="/{href}"')
p404.write_text(t, encoding="utf-8")

print("written:", sorted(p.name for p in OUT.glob("*.html")))
