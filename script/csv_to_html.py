import pandas as pd


def csv_to_html_table(csv_path):
    df = pd.read_csv(csv_path)

    html = '<table border="1">\n<thead>\n<tr><th>ID</th><th>Title</th></tr>\n</thead>\n<tbody>\n'

    for i in range(len(df)):
        number = df.loc[i, 'number']
        title = df.loc[i, 'title']
        if pd.isna(number):
            continue
        html += f'<tr><td>{int(number)}</td><td>{title}</td></tr>\n'

    html += '</tbody>\n</table>'

    return html


if __name__ == "__main__":
    csv_path = 'data/accepted_papers.csv'
    html = csv_to_html_table(csv_path)
    with open(csv_path.replace('csv', 'html'), 'w', encoding='utf-8') as f:
        f.write(html)
