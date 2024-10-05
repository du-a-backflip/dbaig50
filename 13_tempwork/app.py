# Dua Baig
# Wild Blasters
# SoftDev
# K13 -- Template for Success
# 2024-09-30
# time spent: 1.1

from flask import Flask, render_template
app = Flask(__name__)    

import csv
import random

# makes dictionary of all values in csv, then loops through that dictionary to make 3 lists for each column
with open("data/occupations.csv", newline="") as csvfile:
    #creates a dictionary for every row that can be parsed through
    reader = csv.DictReader(csvfile)
    jobs = []
    percents = []
    links = []
    for row in reader:
        jobs.append(row['Job Class']), percents.append(float(row['Percentage'])), links.append(row['Links'])
        
def RandomManual():
    # find a valid percentage, subtract percents until random <=0 and we can return the corresponding jobs
    rand = random.random() * percents[-1]
    for i in range(len(percents)):
        rand -= percents[i]
        if rand <= 0:
            return "Fated Career: " + jobs[i] + " <a href=" + "\"" + links[i] + "\">(Helpful Link for " + jobs[i] + " Career)"+ "</a>" 

# old html template

# html_website = '''
# <!DOCTYPE html>
#     <head>
#         <title>
#             TITLE
#         </title>
#         <style>
#         STYLE
#         </style>
#         HEADER
#     </head>
#     <body>
#         BODY
#     </body>
# </html>'''


def make_table(lists, lists1):
    #html table template
    html_table = '''
        <table class="table" border=1>
            <thead>
                _THEAD_
            </thead>
            <tbody>
                _TBODY_
            </tbody>
        </table>'''
    html_table = html_table.replace("_THEAD_", "<th>Occupations</th><th>Links</th>")
    tbody = ""
    #loops through lists made earlier to make table html
    for i in range (len(lists)-1):
        tbody += "<tr><td>" + lists[i] + "</td>"+ "<td>" + " <a href=" + "\"" + links[i] + "\">Helpful Link for " + lists[i] + " Career"+ "</a>" + "</td></tr>\n\t"
    html_table = html_table.replace("_TBODY_", tbody[:-2])
    return html_table


# def htmlOut(template):
#     template = template.replace("HEADER", "<h1>Team Name: Wild Blasters - Roster: Stanley Hoo, Marco Quintero, Dua Baig</h1>\n")
#     template = template.replace("TITLE", "Template for Success\n")
#     body = "<h2>Period 4</h2>\n"
#     body += f"<p>{RandomManual()}</p>\n"
#     body += make_table(jobs,links)
#     template = template.replace("BODY", body)
#     return template    

@app.route("/wdywtbwygp")
def htmlTemplate():
    header = "<h1>Team Name: Wild Blasters - Roster: Stanley Hoo, Marco Quintero, Dua Baig</h1>\n"
    title = "Template for Success"
    body = "<h2>Period 4</h2>\n"
    body += f"<p>{RandomManual()}</p>\n"
    body += make_table(jobs,links)
    return render_template('tablified.html', HEADING = header, TITLE = title, TABLE = body)

# def hello_world():
#     print(__name__)                  
#     a = htmlOut(html_website)
#     print(a)
#     return a

if __name__ == "__main__":
    app.debug = True
    app.run()     
