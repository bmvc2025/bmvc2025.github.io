import pandas as pd
import re
from pathlib import Path
from html import escape
from typing import Optional

# ============================================
# Workshop 缩写 -> 全名 + 链接
# ============================================
WORKSHOP_INFO = {
    "SHUM": {
        "name": "From Scene Understanding to Human Modeling",
        "url": "https://sites.google.com/view/su2hm/home",
    },
    "MVCC": {
        "name": "Machine Vision for Climate Change",
        "url": "https://mvcc-bmvc.github.io/",
    },
    "PFATCV": {
        "name": "Privacy, Fairness, Accountability and Transparency in Computer Vision",
        "url": "https://sites.google.com/view/pfatcvbmvc25/home",
    },
    "MAAAI": {
        "name": "Media Authenticity in the Age of Artificial Intelligence",
        "url": "https://dbhowmik.github.io/MediaTrust/workshops/",
    },
    "DIFA": {
        "name": "Deep Learning-based Information Fusion and Its Applications",
        "url": "https://difa2025-bmvc.github.io/",
    },
    "MVEO": {
        "name": "Workshop on Machine Vision for Earth Observation and Environment Monitoring",
        "url": "https://mveo.github.io/index.html",
    },
    "Smart": {
        "name": "Smart Cameras for Smarter Autonomous Vehicles and Robots",
        "url": "https://supercamerai.github.io/",
    },
    "MPI": {
        "name": "Multisensory Intelligence for Human Perception",
        "url": "https://weihaox.github.io/bmvc2025mpi",
    },
    "SRBS": {
        "name": "2nd Workshop on Synthetic Realities and Biometric Security: Advances in Forensic Analysis and Threat Mitigation (SRBS 2025)",
        "url": "https://sites.google.com/view/srbs-bmvc2025/home",
    },
}


# ============================================
# 辅助函数
# ============================================
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


# ============================================
# 构建单行 Paper
# ============================================
def build_row(workshop, paper_id, title, authors, files, year=2025):
    """生成单个论文行"""
    pid = str(int(paper_id)).strip() if not pd.isna(paper_id) else ""
    title_txt = escape(str(title).strip())
    authors_txt = escape(str(authors).strip())

    base_url = f"https://bmva-archive.org.uk/bmvc/{year}/assets/workshop/{workshop}/Paper_{pid}"
    pdf_link = f"{base_url}/paper.pdf"

    supp_file = detect_supp_file(files)

    buttons = f'<a class="btn btn-primary btn-sm mt-1" href="{pdf_link}" role="button">PDF</a>&nbsp;'
    if supp_file:
        supp_link = f"{base_url}/{supp_file}"
        buttons += f'<a class="btn btn-primary btn-sm mt-1" href="{supp_link}" role="button">Supplementary</a>&nbsp;'

    # 输出行：第一列是 Paper ID
    return f'''
        <tr id="paper">
            <td class="text-center"><strong>{pid}</strong></td>
            <td>
                <strong><a href="{pdf_link}">{title_txt}</a></strong><br />
                {authors_txt}<br />{buttons}
            </td>
        </tr>
    '''.strip()


# ============================================
# 构建单个 Workshop 表格
# ============================================
def build_table(workshop_abbr, df_group, year=2025):
    """为单个 workshop 构建一个完整的 <div><table> 块"""
    workshop_key = str(workshop_abbr).strip()
    info = WORKSHOP_INFO.get(workshop_key, {"name": workshop_key, "url": ""})
    workshop_name = escape(info["name"])
    link = info["url"]

    # Workshop 标题 + 链接
    if link:
        header_title = f'<h3 class="mt-4 mb-2"><a href="{link}" target="_blank">{workshop_name}</a></h3>'
    else:
        header_title = f'<h3 class="mt-4 mb-2">{workshop_name}</h3>'

    header = f'''
{header_title}
<div class="row pl-2 pr-2 pt-2 pb-2 mx-auto justify-content-left">
    <table class="table table-striped table-bordered">
        <thead>
            <tr><th class="text-center" style="width: 100px;">ID</th><th>Paper</th></tr>
        </thead>
        <tbody>
'''.lstrip("\n")

    rows = []
    for _, row in df_group.iterrows():
        rows.append(
            build_row(
                workshop_abbr,
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


# ============================================
# 构建完整页面
# ============================================
def build_full_page(df, year=2025, email="bmvc@bmvc2025.org"):
    workshops = [w for w in df["Workshop"].dropna().unique()]
    sections = []

    for ws in workshops:
        df_ws = df[df["Workshop"] == ws]
        sections.append(build_table(ws, df_ws, year))

    html_page = "\n\n---\n\n".join(sections)
    html_page += f'\n\n<p>If there are any mistakes on this page, please do not hesitate to contact <a href="mailto:{email}">{email}</a></p>'
    return html_page


# ============================================
# 主入口
# ============================================
def main():
    input_file = "CameraReadyPapers_Workshop.xlsx"
    output_file = "work_proc.html"

    df = pd.read_excel(input_file)
    html = build_full_page(df)
    Path(output_file).write_text(html, encoding="utf-8")

    print(f"[OK] Workshop 页面已生成: {Path(output_file).resolve()}")


if __name__ == "__main__":
    main()
