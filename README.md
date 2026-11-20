# vergote

Website for **Tuinen Vergote Mathieu** (garden design and maintenance, Gits): https://tuinenvergotemathieu.be (not live yet).

Plain HTML + CSS, no build step, served by GitHub Pages. Text is in Dutch.

| Page | File |
|---|---|
| Home | `index.html` |
| Tuinaanleg | `tuinaanleg.html` |
| Tuinonderhoud | `tuinonderhoud.html` |
| Realisaties (photos) | `realisaties.html` |
| Saffraan | `saffraan.html` |
| Contact | `contact.html` |
| Privacy (GDPR) | `privacy.html` |
| Not found | `404.html` |

Shared style: `assets/css/style.css`. Menu script: `assets/js/site.js`. Images: `assets/img/`.
The header and footer are repeated in every page, so a change there means editing all 8 files.

## Design

The feel is an early morning in a natural garden: lots of space, a slow rhythm, soft light. The look was inspired by the photo-led layout of tuinenvanlerberghe.be, made calmer: no pop-ups, no cookie banner, more space.

- **Colours:** dew `#F7F8F4` (page), sage `#E4EADF`, moss `#3E5641` / `#2B3B2D`, saffron gold `#9A6F22` (underlines, numerals), crocus `#6E5A9B` (saffron only).
- **Type:** Fraunces (soft, light) for headings and Figtree for text. Both are self-hosted in `assets/fonts/` under the SIL Open Font License; the `OFL-*.txt` files must stay next to them.
- **Motion:** only the home photo settles slowly on load, and not at all for visitors who prefer reduced motion.
- **Menu:** a native popover that collapses only when the links don't fit; older browsers fall back to a simple toggle.

## Photos (temporary mood photos)

The photos in `assets/img/photos/` are free Unsplash photos (Unsplash License: free for commercial use, no attribution required). They set the mood only and are **not Mathieu's work**; `privacy.html` says so. Replace them with Mathieu's own photos when he has them. The Realisaties page deliberately has no stock photos.

| File | Photographer | Unsplash |
|---|---|---|
| `tuin-grassen-*` (home) | Tatyana Rubleva | https://unsplash.com/photos/nOCFJqFK4f4 |
| `bank-tussen-gras-*` (home band) | wen qiao | https://unsplash.com/photos/zDNB0mOaZ2s |
| `handen-planten-*` | Jonathan Kemper | https://unsplash.com/photos/4z3lnwEvZQw |
| `haag-*` | Haberdoedas II | https://unsplash.com/photos/G0H2TJW3wm0 |
| `saffraankrokus-*` | Mohammad Amiri | https://unsplash.com/photos/6aNGn5Ykkh8 |
| `saffraan-bloemen-*` | Mohammad Amiri | https://unsplash.com/photos/oUAuc3a0Xoc |
| `grassen-wind-*` | Benjamin Cheng | https://unsplash.com/photos/bxU2um8kUec |
| `border-vaste-planten-*` | T (@tanyabarrow) | https://unsplash.com/photos/vC-j7Vy3blU |

## Preview locally

```sh
python3 -m http.server 8793
```

Then open http://localhost:8793.

## Privacy choices

No cookies, no analytics, no contact form, no external fonts, maps or CDNs. If one of these is added, update `privacy.html`.

## Content to get from Mathieu

- [ ] **Photos** for Realisaties. The how-to is in an HTML comment in `realisaties.html`.
- [ ] **Saffron:** what it is exactly (own harvest?), price, packaging, how to order.
- [ ] **Service area:** the site says "Gits en omgeving". Confirm or name the towns.

## Wording to confirm with Mathieu

These sentences were written as a proposal, not taken from his invoices:

- [ ] The 4 steps on `tuinaanleg.html`: site visit, proposal with a price, works, maintenance afterwards.
- [ ] "eenmalig of op regelmatige basis" (tuinonderhoud).
- [ ] "Mathieu denkt mee" and "Hij bekijkt graag wat er mogelijk is".
- [ ] "zijn eigen saffraan" (saffraan, home).
- [ ] The privacy statement as a whole: Mathieu is the controller, so he must agree with it.

The facts come from his invoices: trading name, address, phone number, VAT number, and the services billed (hedge trimming, tree sawing, green-zone maintenance, green waste removal, private and business customers).

## Go-live checklist

1. Mathieu has approved the text.
2. Make the repo public (GitHub Pages on a free plan needs a public repo).
3. Settings → Pages: deploy from branch `main`, folder `/`.
4. Custom domain `tuinenvergotemathieu.be` (this creates a `CNAME` file), then tick **Enforce HTTPS** once the certificate is ready.
5. DNS zone at OVHcloud: delete the parking `A` records (`213.186.33.5`) for `@` and `www` and the OVH `TXT` records `"1|www…"` / `"3|welcome"`. Add:
   - `@` A `185.199.108.153`, `185.199.109.153`, `185.199.110.153`, `185.199.111.153`
   - `www` CNAME `edouardgt.github.io.`
   - Leave the MX and SPF records alone: they carry the info@ mail redirect.
6. Test `info@tuinenvergotemathieu.be`. It forwards to Mathieu's Telenet address, so warn him first.
