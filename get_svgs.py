import json
import re

template = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 -64 1024 1000" style="transform: scaleY(-1);">
<path fill="currentColor" d="{pathData}"/>
</svg>"""

with open("rpgawesome-webfont.svg", "r", encoding="utf-8") as f:
    content = f.read()

res = []

for line in content.split("\n"):
    if "glyph-name" in line:
        name = re.search(r'glyph-name="(.+?)"', line).group(1)
        print(name)
        res.append({"name": name, "path": f"rpg-awesome-svg/{name}.svg"})
        pathdata = re.search(r' d="(.+?)"', line).group(1)
        with open(f"rpg-awesome-svg/{name}.svg", "w", encoding="utf-8") as f:
            f.write(template.format(pathData=pathdata))
        # break

with open("preview.js", "w", encoding="utf-8") as f:
    f.write(
        f"""const svg_list={json.dumps(res)}"""
        + """
let sample = document.getElementById("sample")
svg_list.map((i) =>
  sample.insertAdjacentHTML(
    "beforeend",
    `<div class="svg-item"><img src="./${i.path}"/><div>${i.name}</div></div>`
  )
)
"""
    )
