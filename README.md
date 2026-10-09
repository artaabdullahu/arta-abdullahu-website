# Arta Abdullahu — Data Engineer

A professional portfolio built with HTML and CSS. No JavaScript, dependencies, or build step is required.

## Files

- `dist/index.html` — introduction, skills, selected experience, public repositories, and contact links.
- `dist/styles.css` — responsive layout, typography, and navy/mint palette.
- `archive/index-original.html` — the original NGO services draft.
- `archive/portfolio-v1/` — the previous personal portfolio, including its stylesheet.

## Local preview

Open `dist/index.html` directly in a browser, or run from the project folder:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Visit `http://localhost:8000`. Save edits and refresh the browser. Press Control+C in the server terminal to stop it.

## Content and sources

The owner’s supplied CV is the source of truth for employment dates, employer names, responsibilities, education, and research. The site prioritizes data engineering and excludes customer support positioning. Contact uses the email and LinkedIn profile supplied by the owner. Earlier research on the public XING profile was superseded by the supplied CV.

Featured projects cover photovoltaic sensor data with Raspberry Pi/Cassandra and Kosovo business data analysis. Additional conference work appears in an expandable section. No performance metrics or project repository links have been invented.

Public repositories were checked through GitHub's public API and their source files on October 9, 2026:

- [flask-test](https://github.com/artaabdullahu/flask-test): Python/Flask routing experiment with a welcome template.
- [kreotive](https://github.com/artaabdullahu/kreotive): a fork of a Flask application framework with MongoDB integration. It is labeled as a fork.
- [arkep](https://github.com/artaabdullahu/arkep): a Jekyll Modern Blog theme repository. The page acknowledges its template origin.

Empty and introductory repositories are excluded from the selected projects. The project illustrations and lifecycle diagram are made in HTML/CSS; they are not screenshots of deployed applications or an employer's architecture.

## Personalize

Keep experience dates and responsibilities up to date in `dist/index.html`. Add a project by copying a project article and replacing its description, technologies, and repository link with verified information. Contact links use email, LinkedIn, and GitHub.

## Publishing

Deploy only `dist/`. The archive is outside that folder. The repository remote is `https://github.com/artaabdullahu/arta-abdullahu-website.git`; pushing code does not automatically publish the website. This checkout has no hosting configuration.
