# Arta Abdullahu — Personal portfolio

A simple personal website built with HTML and CSS. No framework, JavaScript, dependencies, or build step is needed.

## Files

- `dist/index.html` — introduction, About, Projects, and contact sections.
- `dist/styles.css` — colors, typography, layout, and responsive styles.
- `archive/index-original.html` — the original NGO services draft, preserved before the portfolio changes. Outside the deployable `dist` folder.

## Preview

Open `dist/index.html` in a browser. Save changes in your editor and refresh the browser to see them.

Or run this from the project folder:

```sh
python3 -m http.server 8000 --bind 127.0.0.1 --directory dist
```

Visit `http://localhost:8000`. Press Control+C in the terminal to stop the server. VS Code's Live Server extension is also optional.

## Make it yours

1. Edit the introduction and About text in `dist/index.html`.
2. Add real projects by copying the project `<article>` and updating its title, description, and link.
3. The contact section links to your GitHub profile. Add an email or another contact link when ready.
4. Edit the colors at the top of `dist/styles.css` and the other styles below them.
5. Update the copyright year in the footer when needed.

## GitHub and publishing

The configured Git remote is `https://github.com/artaabdullahu/arta-abdullahu-website.git`.

The working folder replaces the original tracked root `index.html` and empty file named `dist` with a real `dist/` directory. Before committing, review `git status` and `git diff`. Stage the new files and those removals together to record this layout.

The website is ready for local preview. This checkout contains no hosting configuration, and this update does not publish the website. Deploy the contents of `dist/` when you choose a static hosting service.
