from numpy import empty
import pandas as pd
import json
from reportlab.platypus import Paragraph, Spacer, Table, Image, SimpleDocTemplate, PageBreak
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib.pagesizes import letter



def export_to_pdf(json_filename, output_filename):
    file = open(json_filename, 'r')
    data=json.load(file)
    df=pd.json_normalize(data)
    name = df.loc[0, 'name']
    univ = df.loc[0, 'university']
    skills = df.loc[0, 'skills']
    profession = df.loc[0, 'profession']

    summarize= df.loc[0, 'summary']

    title_name="Konsult-in Chatbot Summary"
    output_filename='test2.pdf'
    user_info=f'''Name      : {name}<br/> 
                Institution : {univ}<br/> 
                Skills      : {skills}<br/> 
                Profession  : {profession}'''
    summary_text="Summary :"
    
    report=SimpleDocTemplate(output_filename, pagesize=A4)
    styles = getSampleStyleSheet()
    section_spacing=Spacer(0,20)
    empty_line=Spacer(0,10)
    ReportTitle = Paragraph(title_name)
    UserInformation = Paragraph(user_info)
    Summary = Paragraph(summary_text)
    ChatbotSummary = Paragraph(summarize)
    report.build([ReportTitle,section_spacing,UserInformation,section_spacing,Summary,empty_line,ChatbotSummary])

result=export_to_pdf('dataset.json','test.pdf')
print(result)