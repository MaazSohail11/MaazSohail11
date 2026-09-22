# Profile artwork

These SVGs are self-contained and served directly from this repository. They do
not load fonts, scripts, icons, statistics, or other images from external services.

To change the artwork, edit `scripts/build_assets.py` and run:

```sh
python scripts/build_assets.py
```

Commit the generated SVGs with the README so GitHub can render them immediately.
The narrow-screen header, product illustrations, and diagrams are selected with
standard HTML `picture` elements. All graphics scale to the available width. Project details and links remain
normal README text for accessibility, search, and small screens.

Project descriptions were checked against the linked public project READMEs and
product pages during the redesign. Recheck those sources when changing claims.
The artwork illustrates workflows; it does not show measured activity or usage.

The older `profile-3d-contrib` assets and their workflow remain available, but the
main profile no longer embeds contribution widgets or remote image services.
