import argparse
import sys
from pathlib import Path
import pandas as pd
from html import escape
import re


def build_row(paper_id: str, title: str, authors: str, year: int) -> str:
    pid = str(paper_id).strip()
    title_txt = escape(str(title).strip())
    authors_txt = escape(str(authors).strip())

    base = f"https://bmva-archive.org.uk/bmvc/{year}/assets/papers/Paper_{pid}"
    pdf = f'{base}/paper.pdf'
    poster = f'{base}/poster.pdf'
    video = f'{base}/video.mp4'

    return f'''
        <tr id="paper">
            <td class="text-center"><strong> </strong><br /><span style="opacity: 0.5;"><strong>{pid}</strong></span></td>
            <td><strong><a href="/proceedings/{pid}/">{title_txt}</a></strong><br />
            {authors_txt}<br />
            <a class="btn btn-primary btn-sm mt-1" href="{pdf}" role="button">PDF</a>&nbsp;
            <a class="btn btn-primary btn-sm mt-1" href="{poster}" role="button">Poster</a>&nbsp;
            <a class="btn btn-primary btn-sm mt-1" href="{video}" role="button">Video (Right click to download)</a>&nbsp;
            </td>
        </tr>
    '''.rstrip()


def build_page(df: pd.DataFrame, col_id: str, col_title: str, col_authors: str, year: int, email: str) -> str:
    header = '''
<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-left">
    <table class="table table-striped table-bordered">
        <tbody>
'''.lstrip("\n")
    rows = []
    def _id_key(x):
        try:
            return int(str(x).strip())
        except Exception:
            return str(x).strip()

    df_sorted = df.copy()
    if col_id in df_sorted.columns:
        df_sorted = df_sorted.sort_values(by=col_id, key=lambda s: s.map(_id_key))

    for i, r in df_sorted.iterrows():
        pid = r.get(col_id, "")
        title = r.get(col_title, "")
        authors = r.get(col_authors, "")

        # 基础校验
        if pd.isna(pid) or pd.isna(title) or pd.isna(authors):
            # 跳过不完整行
            continue

        rows.append(build_row(pid, title, authors, year))

    footer = f'''
        </tbody>
    </table>
    <p>If there are any mistakes on this page, please do not hesitate to contact 
    <a href="mailto:{escape(email)}">{escape(email)}</a></p>
</div>
'''.rstrip() + "\n"

    return header + "\n".join(rows) + "\n" + footer


def main():
    parser = argparse.ArgumentParser(description="Generate BMVC {YEAR} HTML from Excel")
    parser.add_argument("-i", "--input", default="CameraReadyPapers.xlsx", help="")
    # parser.add_argument("-i", "--input", default="CameraReadyPapers_New.xls", help="")
    parser.add_argument("-o", "--output", default="conf_proc.html", help="")
    parser.add_argument("--sheet", default=0, help="")
    parser.add_argument("--year", type=int, default=2025, help="")
    parser.add_argument("--email", default=None, help="")
    parser.add_argument("--col-id", default="ID", help="")
    parser.add_argument("--col-title", default="Title", help="")
    parser.add_argument("--col-authors", default="Authors", help="")

    args = parser.parse_args()

    xlsx = Path(args.input)
    if not xlsx.exists():
        print(f"[ERROR] 找不到输入文件：{xlsx}", file=sys.stderr)
        sys.exit(1)

    email = args.email or f"bmvc@bmvc{args.year}.org"
    
    #* install xlrd == 2.0.1 if reading .xls files
    try:
        if xlsx.suffix.lower() == ".xls":
            engine = "xlrd"
        else:
            engine = "openpyxl"

        df = pd.read_excel(xlsx, sheet_name=args.sheet, engine=engine)
    except Exception as e:
        print(f"[ERROR] 读取 Excel 失败：{e}", file=sys.stderr)
        sys.exit(2)

    missing = [c for c in [args.col_id, args.col_title, args.col_authors] if c not in df.columns]
    if missing:
        print(f"[ERROR] Excel 缺少必要列：{missing}", file=sys.stderr)
        print(f"当前列：{list(df.columns)}", file=sys.stderr)
        sys.exit(3)

    html = build_page(
        df=df,
        col_id=args.col_id,
        col_title=args.col_title,
        col_authors=args.col_authors,
        year=args.year,
        email=email,
    )
    
    # html = re.sub(r">\s*\n\s*<tr", "><tr", html)
    html = re.sub(r"\n\s*\n+", "\n", html)

    out = Path(args.output)
    try:
        out.write_text(html, encoding="utf-8")
    except Exception as e:
        print(f"[ERROR] 写出 HTML 失败：{e}", file=sys.stderr)
        sys.exit(4)

    print(f"[OK] 已生成：{out.resolve()}")


if __name__ == "__main__":
    main()
