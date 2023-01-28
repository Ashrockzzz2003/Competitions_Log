from traceback import print_tb


log_name = "coding_competitions_log.md"

f = open(log_name, 'r')
content = f.readlines()

for i in range(len(content)):
    content[i] = content[i].rstrip()

content.remove(content[0])
content.remove('')

competitions = []

inner_contents = []

html = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="style.css">
    <link href="https://fonts.googleapis.com/icon?family=Material+Icons"
      rel="stylesheet">
    <title>Competitions</title>
</head>
<body>
    <h1>Coding Competitions Log</h1>
    <div class="competition_list">
"""

for i in range(len(content)):
    x = []
    if('\t' not in content[i] and '-' in content[i]):
        competitions.append(content[i])
        j = i+1
        while(('\t' in content[j] and '-' in content[j])):
            x.append(content[j])
            j += 1
            if(j > len(content) - 1):
                break
    if(x != []):
        inner_contents.append(x)

for i in range(len(competitions)):
    competitions[i] = (competitions[i]).replace('- ', '')
    for j in range(len(inner_contents[i])):
        inner_contents[i][j] = (inner_contents[i][j]).replace('\t- ', '')

for i in range(len(competitions)):
    html += f"""
    <div class="competition_item">
            <span class="date">{(inner_contents[i][0]).replace("Date: ", "")}</span>
            <h3>{competitions[i]}</h3>
            <div class="about_list">
    """

    for j in range(1, len(inner_contents[i])):
        if("`" in inner_contents[i][j]):
            link = inner_contents[i][j].split('`')[1::2]
            html += f"""<div class="link_item">Proof: <a target="_blank" href="{str(link[0])}">View</a></div>"""
        elif "Rating: " in inner_contents[i][j]:
            html += f"""<div class="about_item">Rating: """
            inner_contents[i][j] = (inner_contents[i][j]).replace("Rating: ", "")
            # print(inner_contents[i][j])
            for k in range(int(inner_contents[i][j])):
                html += f"""<i class="material-icons" id="star_{int(inner_contents[i][j])}">star</i>"""
            html += """</div>"""
        else:
            html += f"""<div class="about_item">{inner_contents[i][j]}</div>"""

    html += """
            </div>
    </div>
    """

html += """
</div>
</body>
</html>
"""
f.close()

f = open("index.html", "w")
f.write(html)

f.close()