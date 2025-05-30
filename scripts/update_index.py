import yaml
from pathlib import Path

INDEX_PATH = Path("docs/index.md")
GALLERY_YAML = Path("gallery/notebook_gallery.yaml")

def load_gallery():
    if GALLERY_YAML.exists():
        with GALLERY_YAML.open() as f:
            return yaml.safe_load(f).get("domains", {})
    return {}

def generate_card(entry):
    return f"""
:::{{
    grid-item-card
}} {entry['title']}
:shadow: md
:link: {entry['url']}
:img-top: {entry.get('thumbnail', 'https://via.placeholder.com/300')}
{entry['description']}

:::
"""

def update_index():
    if not INDEX_PATH.exists():
        print("❌ docs/index.md not found.")
        return

    with INDEX_PATH.open() as f:
        content = f.read()

    if "::::{grid} 2" not in content:
        print("❌ Grid section not found.")
        return

    before, grid_and_after = content.split("::::{grid} 2", 1)
    grid_start = "::::{grid} 2"
    grid_content = grid_and_after.strip().split("::::", 1)[0]  # remove any trailing :::

    gallery = load_gallery()
    new_cards = "\n".join([generate_card(entry) for entry in gallery.values()])

    updated_grid = f"{grid_start}\n:gutter: 3\n{grid_content}\n{new_cards}\n::::"

    final_content = f"{before}{updated_grid}"

    with INDEX_PATH.open("w") as f:
        f.write(final_content)

    print("✅ docs/index.md successfully updated.")

if __name__ == "__main__":
    update_index()
