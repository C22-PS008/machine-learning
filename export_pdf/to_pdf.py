import pandas as pd
import json
from reportlab.platypus import Paragraph, Spacer, Table, Image, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter
from sklearn import datasets

def export_to_pdf(json_filename, output_filename):
    file = open(filename, 'r')
    data=json.load(file)
    df=pd.json_normalize(data)
    name = df.loc[0, 'name']
    univ = df.loc[0, 'university']
    skills = df.loc[0, 'skills']
    profession = df.loc[0, 'profession']

file = open('dataset.json', 'r')
data=json.load(file)
df=pd.json_normalize(data)
name = df.loc[0, 'name']
univ = df.loc[0, 'university']
skills = df.loc[0, 'skills']
profession = df.loc[0, 'profession']
title_name="Test"
output_filename='test2.pdf'
user_info=f"Name : {name} Institution: {univ} Skills: {skills} Profession: {profession}"
document=["name", "university", "skills", "profession"]
report=SimpleDocTemplate(output_filename, pagesize=A4)
styles = getSampleStyleSheet()
empty_line=Spacer(0,20)
ReportTitle = Paragraph(title_name)
UserInformartion = Paragraph(user_info)
report.build([ReportTitle,empty_line,UserInformartion])
