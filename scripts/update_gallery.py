import os
import sys
import argparse
import yaml

def load_gallery(path):
    if os.path.exists(path):
        with open(path, "r") as f:
            return yaml.safe_load(f) or {"domains": {}}
    return {"domains": {}}

def save_gallery(data, path):
    with open(path, "w") as f:
        yaml.dump(data, f, default_flow_style=False)

def update_gallery(cookbook_dir, mode):
    meta_path = os.path.join(cookbook_dir, "meta.yaml")
    if not os.path.exists(meta_path):
        print(f"No meta.yaml in {cookbook_dir}, skipping.")
        return
    with open(meta_path) as f:
        meta = yaml.safe_load(f)
    gallery = load_gallery("gallery/notebook_gallery.yaml")
    # Add or update entry
    gallery["domains"][meta['root_path']] = {
        "title": meta.get("title", ""),
        "url": f"/production/{meta['root_path']}/" if mode=="production" else f"/preview/{meta['root_path']}/",
        "thumbnail": meta.get("thumbnail", ""),
        "description": meta.get("description", ""),
    }
    save_gallery(gallery, "gallery/notebook_gallery.yaml")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--cookbook_dir", required=True)
    parser.add_argument("--mode", choices=["preview", "production"], required=True)
    args = parser.parse_args()
    update_gallery(args.cookbook_dir, args.mode)