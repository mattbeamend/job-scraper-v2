import pandas as pd
import os
import LinkedInScraperV2
import IndeedScraper

r1 = LinkedInScraperV2.scrape("Software Engineer Intern", "London")
r2 = IndeedScraper.scrape("Software Engineer Intern", "London")

data = pd.DataFrame({
    'Title': r1[0],
    'Company': r1[1],
    'Location': r1[2],
    'Links': r1[3]
})

data['Links'] = '<a target="_blank" href=' + data['Links'] + '>Click Here</a>'
pd.set_option('colheader_justify', 'center')

data2 = pd.DataFrame({
    'Title': r2[0],
    'Company': r2[1],
    'Location': r2[2],
    'Links': r2[3]
})

data2['Links'] = '<a target="_blank" href=' + data2['Links'] + '>Click Here</a>'
pd.set_option('colheader_justify', 'center')

html_string = '''
    <html>
        <head><title>Software Engineering Internships</title></head>
        <link rel="stylesheet" type="text/css" href="df_style.css"/>
        <body>
            <h1>Software Engineer Internships</h1>
            <h3>LinkedIn</h3>
            {table1}
            <h3>Indeed</h3>
            {table2}
        </body>
    </html>.
    '''
with open('WebPage.html', 'w') as f:
    f.write(html_string.format(table1=data.to_html(classes='mystyle', escape=False),table2=data2.to_html(classes='mystyle', escape=False)))


print("Written successfully.")
os.system("start WebPage.html")