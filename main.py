import pandas as pd
import os
import LinkedInScraperV2

r = LinkedInScraperV2.scrape("Software Engineer Intern", "London")

data = pd.DataFrame({
    'Title': r[0],
    'Company': r[1],
    'Location': r[2],
    'Links': r[3]
})

data['Links'] = '<a target="_blank" href=' + data['Links'] + '>Click Here</a>'
pd.set_option('colheader_justify', 'center')

html_string = '''
    <html>
        <head><title>Software Engineering Internships</title></head>
        <link rel="stylesheet" type="text/css" href="df_style.css"/>
        <body>
            <h1>Software Engineer Internships</h1>
            {table}
        </body>
    </html>.
    '''
with open('WebPage.html', 'w') as f:
    f.write(html_string.format(table=data.to_html(classes='mystyle', escape=False)))

print("Written successfully.")
os.system("start WebPage.html")