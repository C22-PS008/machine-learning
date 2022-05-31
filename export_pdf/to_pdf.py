import pandas as pd
import json
from jinja2 import Environment, FileSystemLoader
from weasyprint import HTML

def export_to_pdf(df, filename):
    file = open(filename, 'r')
    data=json.load(file)
    df.pd.json_normalize(data)
    name = df.loc[0, 'name']
    univ = df.loc[0, 'university']
    skills = df.loc[0, 'skills']
    profession = df.loc[0, 'profession']
    env=Environment(loader=FileSystemLoader('export_pdf/templates'))
    template=env.get_template('report_template.html')
    template_vars = {
        "name" : name,
        "university" : univ,
        "skills" : skills,
        "profession": profession
    }
    html_out = template.render(template_vars)
    HTML(string=html_out).write_pdf(filename+'_summary.pdf')
