import os
import re

INDEX_PATH = "docs/index.md"
COOKBOOKS_DIR = "cookbooks"

# Der Marker-Text muss exakt wie in index.md stehen!
MARKER_START = "<!-- AUTO-COOKBOOKS-START -->"
MARKER_END = "<!-- AUTO-COOKBOOKS-END -->"

def cookbook_card(name):
    """Erzeugt eine Grid Card für ein Cookbook."""
    return f"""::{{grid-item-card}} {name}
:shadow: md
:link: ../production/{name}/index.html
:img-top: https://placehold.co/300x200?text={name}
Auto-generated preview for cookbook '{name}'.
:::
"""

def main():
    # 1. index.md einlesen
    with open(INDEX_PATH, encoding="utf-8") as f:
        content = f.read()

    # 2. Marker finden
    pattern = re.compile(
        rf"({re.escape(MARKER_START)})(.*)({re.escape(MARKER_END)})",
        re.DOTALL
    )

    match = pattern.search(content)
    if not match:
        raise RuntimeError(
            f"Marker {MARKER_START} und {MARKER_END} nicht in {INDEX_PATH} gefunden!"
        )

    # 3. Alle Cookbooks-Ordner finden
    cookbooks = [
        d for d in sorted(os.listdir(COOKBOOKS_DIR))
        if os.path.isdir(os.path.join(COOKBOOKS_DIR, d)) and not d.startswith(".")
    ]

    # 4. Cards generieren
    cards = "\n".join([cookbook_card(cb) for cb in cookbooks])

    # 5. Content ersetzen
    new_content = (
        content[:match.start(2)]
        + "\n" + cards + "\n"
        + content[match.end(2):]
    )

    # 6. index.md speichern
    with open(INDEX_PATH, "w", encoding="utf-8") as f:
        f.write(new_content)

if __name__ == "__main__":
    main()