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
