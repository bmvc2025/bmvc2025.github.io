import pandas as pd
import re
from pathlib import Path
from html import escape
from typing import Optional


WORKSHOP_LINKS = {
    "SU2HM": "https://sites.google.com/view/su2hm/home",
    "MVCC": "https://mvcc-bmvc.github.io/",
    "PFATCV": "https://sites.google.com/view/pfatcvbmvc25/home",
    "MAI": "https://dbhowmik.github.io/MediaTrust/workshops/",
    "DIFA": "https://difa2025-bmvc.github.io/",
    "MVEO": "https://mveo.github.io/index.html",
    "SCAVR": "https://supercamerai.github.io/",
    "MPI": "https://weihaox.github.io/bmvc2025mpi",
    "SRBS": "https://sites.google.com/view/srbs-bmvc2025/home",
}


def detect_supp_file(files: str) -> Optional[str]:
    if not isinstance(files, str):
        return None
    fl = files.lower()
    if "supp" not in fl:
        return None
    if "supp.pdf" in fl:
        return "supp.pdf"
    if "supp.zip" in fl:
        return "supp.zip"
    return None


def build_row(workshop, paper_id, title, authors, files, year=2025):
    """生成单个论文行"""
    workshop = str(workshop).strip()
    pid = str(int(paper_id)).strip() if not pd.isna(paper_id) else ""
    title_txt = escape(str(title).strip())
    authors_txt = escape(str(authors).strip())

    base_url = f"https://bmva-archive.org.uk/bmvc/{year}/assets/workshop/{workshop}/Paper_{pid}"
    pdf_link = f"{base_url}/paper.pdf"

    # 判断是否存在 supplement 文件
    supp_file = detect_supp_file(files)

    # 构建按钮
    buttons = f'<a class="btn btn-primary btn-sm mt-1" href="{pdf_link}" role="button">PDF</a>&nbsp;'
    if supp_file:
        supp_link = f"{base_url}/{supp_file}"
        buttons += f'<a class="btn btn-primary btn-sm mt-1" href="{supp_link}" role="button">Supplementary</a>&nbsp;'

    # ✅ 新增：Workshop 名称加超链接
    workshop_key = workshop.strip().upper()
    link = WORKSHOP_LINKS.get(workshop_key)
    if link:
        workshop_html = f'<a href="{link}" target="_blank">{escape(workshop)}</a>'
    else:
        workshop_html = escape(workshop)

    # 构建 HTML 行（只改这一部分）
    return f'''
        <tr id="paper">
            <td class="text-center"><strong> </strong><br />
                <span style="opacity: 0.8;"><strong>{workshop_html}</strong></span></td>
            <td><strong><a href="{pdf_link}">{title_txt}</a></strong><br />
                {authors_txt}<br />{buttons}
            </td>
        </tr>
    '''.strip()


def build_table(workshop_name, df_group, year=2025):
    header = f'''
<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-left">
    <table class="table table-striped table-bordered">
        <tbody>
'''.lstrip("\n")

    rows = []
    for _, row in df_group.iterrows():
        rows.append(
            build_row(
                workshop_name,
                row.get("ID", ""),
                row.get("Title", ""),
                row.get("Authors", ""),
                row.get("Files", ""),
                year,
            )
        )

    footer = '''
        </tbody>
    </table>
</div>
'''.rstrip()

    html = header + "\n".join(rows) + "\n" + footer
    html = re.sub(r">\s*\n\s*<tr", "><tr", html)
    html = re.sub(r"\n\s*\n+", "\n", html)
    return html


def build_full_page(df, year=2025, email="bmvc@bmvc2025.org"):
    workshops = [w for w in df["Workshop"].dropna().unique()]
    sections = []

    for ws in workshops:
        df_ws = df[df["Workshop"] == ws]
        sections.append(build_table(ws, df_ws, year))

    html_page = "\n\n---\n\n".join(sections)
    html_page += f'\n\n<div><p>If there are any mistakes on this page, please do not hesitate to contact <a href="mailto:{email}">{email}</a></p></div>'
    
    return html_page


def main():
    input_file = "CameraReadyPapers_Workshop.xlsx"
    output_file = "work_proc.html"

    df = pd.read_excel(input_file)
    html = build_full_page(df)
    Path(output_file).write_text(html, encoding="utf-8")

    print(f"[OK] Workshop 页面已生成: {Path(output_file).resolve()}")


if __name__ == "__main__":
    main()
