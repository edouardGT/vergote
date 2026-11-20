"""'Nu in de tuin': one short note per month (index 0 = January). Shown on the home page by site.js.

Checked against Flemish/Dutch garden calendars and ANB advice (hedges: not during the breeding season,
roughly mid-March to mid-August). Keep each note short: a title and at most two sentences.
"""

SEIZOENEN = {"winter": "Winter", "lente": "Lente", "zomer": "Zomer", "herfst": "Herfst"}

TUINJAAR = [
    {"maand": "januari", "kort": "jan", "seizoen": "winter",
     "titel": "De tuin rust",
     "tekst": "Op een droge dag zonder vorst is het een goed moment om fruitbomen te snoeien. En om rustig te bedenken wat er dit jaar anders mag.",
     "link": ("tuinonderhoud.html", "Over snoeien en onderhoud")},
    {"maand": "februari", "kort": "feb", "seizoen": "winter",
     "titel": "Snoeien voor het voorjaar",
     "tekst": "Struiken, fruitbomen en knotwilgen krijgen nu hun snoeibeurt, zolang ze nog in rust zijn. Hagen snoeit u het best vóór half maart, als de vogels beginnen te nestelen.",
     "link": ("tuinonderhoud.html", "Over snoeien en onderhoud")},
    {"maand": "maart", "kort": "mrt", "seizoen": "lente",
     "titel": "Alles wordt wakker",
     "tekst": "Tijd om de borders op te ruimen, oude stengels weg te knippen en de grond te voeden met compost. Vanaf half maart laten we de hagen met rust: het broedseizoen begint.",
     "link": ("tuinonderhoud.html", "Over tuinonderhoud")},
    {"maand": "april", "kort": "apr", "seizoen": "lente",
     "titel": "Planten en zaaien",
     "tekst": "De grond warmt op. Een goede maand om vaste planten en heesters te planten, of om een nieuw stuk tuin aan te leggen.",
     "link": ("tuinaanleg.html", "Over tuinaanleg")},
    {"maand": "mei", "kort": "mei", "seizoen": "lente",
     "titel": "Na de IJsheiligen",
     "tekst": "Na half mei is de kans op nachtvorst voorbij en mogen ook de gevoelige planten naar buiten. Het blad van de saffraankrokus verdort: de knollen gaan in zomerrust.",
     "link": ("saffraan.html", "Over de saffraan")},
    {"maand": "juni", "kort": "jun", "seizoen": "zomer",
     "titel": "Tijd om te genieten",
     "tekst": "De tuin staat in volle groei. Water geven op droge dagen, uitgebloeide bloemen wegknippen, en vooral: buiten zitten. In de hagen zitten nog jonge vogels.",
     "link": ("tuinonderhoud.html", "Over tuinonderhoud")},
    {"maand": "juli", "kort": "jul", "seizoen": "zomer",
     "titel": "Lange avonden",
     "tekst": "Geef water in de vroege ochtend of 's avonds, dan verdampt er het minst. Ook de zomersnoei van fruitbomen kan nu.",
     "link": ("tuinonderhoud.html", "Over tuinonderhoud")},
    {"maand": "augustus", "kort": "aug", "seizoen": "zomer",
     "titel": "De saffraan gaat de grond in",
     "tekst": "Vanaf half augustus worden saffraanknollen geplant. En na 15 augustus mogen de hagen weer in vorm: het broedseizoen is voorbij.",
     "link": ("saffraan.html", "Over de saffraan")},
    {"maand": "september", "kort": "sep", "seizoen": "herfst",
     "titel": "Een tweede lente",
     "tekst": "Warme grond en meer regen: een uitstekende maand om aan te leggen en te planten. De hagen krijgen hun tweede snoeibeurt.",
     "link": ("tuinaanleg.html", "Over tuinaanleg")},
    {"maand": "oktober", "kort": "okt", "seizoen": "herfst",
     "titel": "De saffraan bloeit",
     "tekst": "Oktober is oogstmaand. Mathieu en Juliaan plukken de paarse bloemen met de hand en halen er de rode draadjes uit.",
     "link": ("saffraan.html", "Over de saffraan")},
    {"maand": "november", "kort": "nov", "seizoen": "herfst",
     "titel": "Elk hout neemt wortel",
     "tekst": "„Op Sint-Catharina neemt elk hout wortel”, zegt het spreekwoord over 25 november. Het plantseizoen voor bomen, hagen en heesters is begonnen.",
     "link": ("tuinaanleg.html", "Over tuinaanleg")},
    {"maand": "december", "kort": "dec", "seizoen": "winter",
     "titel": "Rust en plannen",
     "tekst": "De tuin slaapt. Laat wat blad liggen als deken voor de borders, en denk rustig na over wat u volgend jaar wilt.",
     "link": ("contact.html", "Plannen bespreken met Mathieu")},
]

# Saffron year, shown as one line on the saffraan page (index 0 = January).
SAFFRAAN_NU = [
    "Na de bloei groeit het blad. De knol verzamelt kracht voor volgend jaar.",   # jan
    "Na de bloei groeit het blad. De knol verzamelt kracht voor volgend jaar.",   # feb
    "Na de bloei groeit het blad. De knol verzamelt kracht voor volgend jaar.",   # mrt
    "Het blad groeit nog. De knol verzamelt kracht voor volgend jaar.",           # apr
    "Het blad verdort en de knollen gaan in zomerrust.",                          # mei
    "De knollen rusten in de grond tot de nazomer.",                              # jun
    "De knollen rusten in de grond tot de nazomer.",                              # jul
    "Plantijd: vanaf half augustus gaan de saffraanknollen de grond in.",         # aug
    "De knollen wortelen en maken zich klaar om te bloeien.",                     # sep
    "Oogsttijd: de krokussen bloeien en worden met de hand geplukt.",             # okt
    "De oogst is binnen en gedroogd. Nu groeit het blad: de knol verzamelt kracht voor volgend jaar.",  # nov
    "Na de bloei groeit het blad. De knol verzamelt kracht voor volgend jaar.",   # dec
]
