from pathlib import Path
import re

root = Path(__file__).parent
posts_dir = root / "_posts"

# 既に完成した11月のページをひな形にする
template = (root / "archive-2026-11.html").read_text(
    encoding="utf-8"
)

# 記事のファイル名から年月を集める
months = set()

for post in posts_dir.iterdir():
    match = re.match(r"^(\d{4})-(\d{2})-\d{2}-", post.name)
    if match:
        months.add((match.group(1), match.group(2)))

# 月別ページを作成
for year, month in sorted(months):
    page = template.replace(
        "2026年11月",
        f"{year}年{int(month)}月"
    ).replace(
        "2026-11",
        f"{year}-{month}"
    ).replace(
        "/archive/2026/11/",
        f"/archive/{year}/{month}/"
    )

    filename = root / f"archive-{year}-{month}.html"
    filename.write_text(page, encoding="utf-8")
    print(f"Generated: {filename.name}")

print(f"合計 {len(months)} か月分")
