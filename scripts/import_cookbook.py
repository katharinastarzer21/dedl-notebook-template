import argparse
import os
import shutil
import subprocess

def clone_repo(repo_url, dest_dir):
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    subprocess.check_call(['git', 'clone', repo_url, dest_dir])

def copy_root(src_dir, root_path, dest_dir):
    src_root = os.path.join(src_dir, root_path)
    if not os.path.exists(src_root):
        raise FileNotFoundError(f"Root path {root_path} not found in repo.")
    if os.path.exists(dest_dir):
        shutil.rmtree(dest_dir)
    shutil.copytree(src_root, dest_dir)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--repo_url', required=True)
    parser.add_argument('--root_path', required=True)
    args = parser.parse_args()

    temp_dir = "_temp_repo"
    clone_repo(args.repo_url, temp_dir)
    copy_root(temp_dir, args.root_path, os.path.join("cookbooks", args.root_path))
    shutil.rmtree(temp_dir)