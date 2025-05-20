import yaml
import sys
import os

preview_mode = "--preview" in sys.argv
print(f"PREVIEW MODE: {preview_mode}")

gallery_path = "notebook_gallery.yaml"


if not preview_mode:
    if os.path.exists(gallery_path):
        try:
            with open(gallery_path) as f:
                gallery = yaml.safe_load(f) or {}
        except Exception as e:
            print(f"Fehler beim Laden von {gallery_path}: {e}")
            gallery = {}
    else:
        print("notebook_gallery.yaml nicht gefunden – neue Struktur wird erstellt")
        gallery = {}

    if "domains" not in gallery or not isinstance(gallery["domains"], dict):
        gallery["domains"] = {}


with open('issue_body.txt') as f:
    body = f.read()

print("📝 Full Issue Body:")
print(body)


fields = {
    "Repository URL": "",
    "Cookbook Title": "",
    "Short Description": "",
    "Thumbnail Image URL": "",
    "Root Path Name": ""
}

lines = body.splitlines()
current_label = None

for line in lines:
    line = line.strip().lstrip("#").strip()
    if line in fields:
        current_label = line
    elif current_label and line:
        fields[current_label] = line
        current_label = None


repo_url = fields["Repository URL"]
title = fields["Cookbook Title"]
description = fields["Short Description"]
thumbnail = fields["Thumbnail Image URL"]
root_path = fields["Root Path Name"]

print("\n🔍 Extracted Fields:")
print(f"→ Repo URL     : {repo_url}")
print(f"→ Title        : {title}")
print(f"→ Description  : {description}")
print(f"→ Thumbnail    : {thumbnail}")
print(f"→ Root Path    : {root_path}")


missing = [k for k, v in fields.items() if not v]
if missing:
    raise ValueError(f"Fehlende Felder im Issue Body: {', '.join(missing)}")


username_repo = repo_url.replace("https://github.com/", "")
url = f"https://katharinastarzer21.github.io/dedl-notebook-template/cookbooks/{root_path}/index.html"


if not preview_mode:
    print(f"\n📚 Eintrag wird hinzugefügt: {root_path}")
    gallery['domains'][root_path] = {
        'title': title,
        'branch': 'main',
        'root_path': root_path,
        'description': description,
        'thumbnail': thumbnail,
        'url': url,
    }

    with open(gallery_path, 'w') as f:
        yaml.dump(gallery, f, sort_keys=False)
    print("notebook_gallery.yaml wurde erfolgreich aktualisiert")

with open(os.environ['GITHUB_ENV'], 'a') as env_file:
    env_file.write(f"REPO_URL={repo_url}\n")
    env_file.write(f"ROOT_PATH={root_path}\n")
print("Umgebungsvariablen exportiert")
