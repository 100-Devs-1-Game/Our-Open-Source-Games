import glob
import yaml

OUT = ["# Our Games\n"]

for path in sorted(glob.glob("items/*.yaml")):
    print(f"Processing {path}...")
    with open(path) as f:
        g = yaml.safe_load(f)

    OUT.append(f"## {g['title']}\n")
    OUT.append(f"{g['description']}\n\n")
    OUT.append(f"![Screenshot](screenshots/{g['screenshot']}.png)\n\n")
    OUT.append(f"[Repo]({g['repo']}) | [itch.io]({g['itch']}) | [Discord]({g['discord']})")
    if 'gdd' in g and g['gdd']:
      OUT.append(f" | [Game Design Document]({g['gdd']})")
    OUT.append("\n\n")

with open("README.md", "w") as f:
    f.write("\n".join(OUT))
