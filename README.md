# Arta Abdullahu - Professional Portfolio

Responsive one-page portfolio for Arta Abdullahu, Data Engineer and Technical Data Professional. An original isometric portfolio atlas introduces the work, followed by a readable CV layout with pinned desktop section navigation and a single-column mobile layout. On phones, a fixed, horizontally scrollable section bar stays available while reading and marks the current section. Deployable files are in `dist/`; no dependency installation or build is required.

## Files

- `dist/index.html`: page content, SEO metadata, and Person structured data.
- `dist/styles.css`: responsive layout, pinned desktop and mobile section navigation, focus states, and reduced-motion support.
- `dist/favicon.svg`: lightweight local favicon.
- `dist/favicon.ico`: browser-compatible version of the same personal logo.
- `dist/arta-logo.svg` and `dist/arta-logo.ico`: explicitly named tab icons that avoid previously cached Hostinger favicon URLs; the default favicon files remain as fallbacks.
- `dist/arta-tab-icon.png` and `dist/apple-touch-icon.png`: current tab and Apple touch icons, rendered from the same personal logo.
- `archive/`: retained earlier website versions; excluded from the deployment directory.

## Local preview

Open `dist/index.html` in a browser, or run from the repository folder:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Visit `http://localhost:8000`. Save changes and refresh. Stop the server with Control+C.

## Content accuracy checklist

| Website section | Authoritative source |
| --- | --- |
| Home, title, location | Approved website brief; availability wording removed at Arta’s request |
| About | Previously supplied CV career history; ISA role omitted at owner request |
| Expertise | Previously supplied CV and Arta's explicit confirmation of Java, Databricks, and AWS use |
| Raiffeisen experience | Supplied CV and subsequent technology clarification; title and dates retained |
| Kosovo ICT Support | Supplied CV responsibilities; latest brief changes end date to January 2026 |
| UBT and Central Election Commission | Supplied CV responsibilities and latest brief's official titles/dates |
| Business analysis, IoT, alumni projects | Supplied CV project descriptions and latest selection |
| Personal Portfolio Website | This repository's actual HTML/CSS implementation |
| Certifications & learning | Arta’s supplied credential text: six exact titles, issuers, issue/completion dates; Databricks Associate expiration and Lakehouse no-expiry statement; four personal credential URLs |
| Education | Latest approved brief |
| Contact | Approved email, LinkedIn URL, and location; job-search wording removed at Arta’s request |

The latest brief supplies updated dates and titles. Website copy uses direct first-person descriptions; punctuation changes do not change the roles or dates. The page presents Arta’s background without job-search or remote-work availability wording. No invented metrics, certifications, testimonials, project screenshots, or publication links are included.

## Missing source materials

No CV PDF, certificate PDFs, or certificate images were found in the repository. The website omits the CV download button. Certifications are now displayed from credential text supplied by Arta; no preview images are available. To add downloads or previews, provide:

- A current CV file intended for public download, with private details removed as appropriate.
- Certificate PDFs/images whose contents clearly show certificate name and issuing organization. Dates, expiration, credential IDs, and verification URLs are included only when supplied or visible.
- Confirmation of any additional cloud skills before adding them.

Unconfirmed ELT, AWS Glue, Athena, EMR, Reveal, Logikcull, IPRO, and specific eDiscovery workflows have not been added to Expertise.

## Publishing

Production entry point: `dist/index.html`. Deploy the contents of `dist/` only. The canonical URL and Open Graph URL are set to `https://artaabdullahu.com/`, the intended domain; this does not configure hosting or DNS.

The repository remote is `https://github.com/artaabdullahu/arta-abdullahu-website.git`. Every push to `main` runs `.github/workflows/deploy-hostinger.yml` and publishes the contents of `dist/` to Hostinger's `/public_html` folder. The workflow can also be run manually from GitHub Actions. Local edits go live after they are committed and pushed to `main`.

The FTP password is stored in the encrypted GitHub repository secret `HOSTINGER_FTP_PASSWORD`. Update that secret if the FTP password changes. No password is stored in this repository. Deployment uses verified TLS for both authentication and file transfers, checks each uploaded file's SHA-256 hash, and publishes `index.html` after its assets. Existing remote files are retained; deleting a local file does not delete its remote copy. The workflow also checks that the public HTTPS homepage matches the deployed HTML. Hostinger may deny the GitHub runner's HTTP request with 403; this produces a workflow warning, while the required FTPS file verification still runs. Other HTTP errors or an HTML mismatch fail deployment verification.

## Validation

- `git diff --check`: passed.
- Python structural checks: HTML nesting, heading hierarchy, section links, local assets, SVG favicon, and Person JSON-LD passed.
- Primary text color combinations meet 4.5:1 contrast.
- Isolated headless Chrome checks at 320, 390, 768, 1440, and 1920 px: no horizontal page overflow; all six navigation targets are visible after selection; the sidebar stays pinned on desktop and flows normally on mobile; reduced motion is respected. Desktop/mobile screenshots were reviewed.
- Keyboard interaction exposes visible focus styling.
- `curl` checks returned HTTP 200 for the GitHub and LinkedIn profile URLs. The mailto link matches the supplied email.
- No package manifest, build command, or lint configuration exists; the three static production files require no compilation.

Validation scripts, temporary browser profiles, and screenshots are kept outside the repository.

## Theme

The current design uses an off-white paper background, ink-blue text, restrained teal accents, serif headings, and a custom inline SVG data-system diagram. The diagram connects databases and code to clickable Experience, Expertise, and Projects destinations. It is an illustrative toolkit map, not a claimed production architecture. Larger shortcut links support phone navigation. Desktop section navigation remains pinned; on phones, a fixed swipeable section bar keeps navigation within reach and highlights the section currently in view. Certificate records use an open layout with ruled dividers.

The design was implemented directly in HTML/CSS/SVG with a small inline script to highlight the current section, without a purchased theme, copied reference-site code, or external fonts. Visual exclusivity across the internet cannot be guaranteed. Reduced-motion preferences disable route animation. All seven professional content sections are unchanged; Languages and ISA Consulting remain removed.

Theme checks: HTML/SVG nesting, unique IDs, internal anchors, and exact preservation of the seven content sections passed. Chrome checks passed at 320, 390, 768, 1440, and 1920 px: no page overflow, all seven section links and three diagram links navigate correctly, reduced motion works, and keyboard Tab/Enter exposes visible focus and activates diagram links. Desktop/mobile screenshots were reviewed. The text palette and diagram labels meet 4.5:1 contrast. `git diff --check` passed. Files changed for this redesign: `dist/index.html`, `dist/styles.css`, `dist/favicon.svg`, and this README. Backups and QA artifacts are outside the repository. Changes have not been committed or pushed.

## Earlier data engineering visual refinement

The previous palette used deep navy, slate blue, and teal. The original clickable atlas remains, with blue processing blocks, a teal database, and connected routes. A four-stage toolkit diagram in Expertise groups verified tools under Sources, Processing, Storage, and Operations; it illustrates skills, not a claimed employer architecture. All tools come from the supplied CV and approved website content. Employment, selected projects, education, and contact text are unchanged.

Changed files: `dist/index.html`, `dist/styles.css`, `dist/favicon.svg`, and this README. No dependencies or build steps were added. Checks used Python structural validation, `git diff --check`, and isolated headless Chrome. Five viewport widths (320, 390, 768, 1440, 1920 px), anchor navigation, keyboard interaction, and reduced-motion behavior passed. Desktop and mobile screenshots of the opening map and new toolkit diagram were reviewed. Missing CV and certificate assets remain the only source-material gaps described above.

ISA Consulting was removed from Professional Experience and About at the owner’s request. The experience introduction was adjusted to match the remaining roles.


## Supplied credentials

Added six credential records and a Certifications navigation link. Certifications, accreditation, and course completions are labeled separately. Databricks Data Engineer Associate is explicitly expired on April 13, 2025; no renewal is assumed. Lakehouse Fundamentals is marked as not expiring, as supplied. Microsoft expiration dates were not supplied and are omitted. No new employment skills are inferred from exam descriptions. Four supplied personal credential links are used; no Microsoft verification URLs or preview images were invented. Browser retrieval of the four credential pages failed, so their contents have not been independently verified. All record details are supported by the owner’s pasted credential content.

Removed remote-work availability and job-search statements from Home, the sidebar, About, and Contact at Arta’s request. About now closes with existing teaching and troubleshooting experience. Contact offers email, LinkedIn, and GitHub without recruiting language.
