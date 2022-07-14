import json
import os

##############################################################################

def join_strings(strings,separator):
    return separator.join(strings)

def htmlify(strings):
    return join_strings(strings,'\n')

##############################################################################

# TEMPLATES

s1 = """<!DOCTYPE html>

<html lang="en">

<link rel="stylesheet" href="mystyle.css" type="text/css">

 <head>

   <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>

   <script>
     $(function() {
       $("#header").load("header.html");
       $("#footer").load("footer.html");
     });
   </script>

   <meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate" />

   <meta http-equiv="Pragma" content="no-cache" />

   <meta http-equiv="Expires" content="0" />

   <meta charset="UTF-8">

   <meta name="viewport" content="width=device-width,initial-scale=1">"""


s2 = """</head>

<body>

  <div id="header"></div>

  <div class="main">
  
  <article>"""
  
s3 = """</article>

  </div>

  <p class="small-space"></p>

  <div id="footer"></div>

</body>

</html>
"""
  
def s_pagetitle(title):
    return "<title>" + title + "</title>"

def s_description(description):
    return "<meta name=\"description\" content=\""+ description + "\">"

def s_author(author):
    return "<meta name=\"author\" content=\""+ author + "\">"
    
def s_title(title):
    return "<p id=\"title\">"+title+"</p>"

def s_header1(title):
    return "<h1>"+title+"</h1>"

def s_header2(subtitle):
    return "<h2>"+subtitle+"</h2>"

def s_time(time):
    return "<p><time datetime=\""+time+"\">"+time+"</time></p>"

def s_body(body):
    return "<p>"+body+"</p>"

def s_figure(figure_link,figure_alt,figure_caption):
    strings = ["<figure>","<img src=",figure_link," alt=",figure_alt,">,<figcaption>",figure_caption,"</figcaption>","</figure>"]
    return join_strings(strings,'')
 
def s_attribute(attribute_place,attribute_link):
    strings = ["<p>Originally published in <a href=",attribute_link,">",attribute_place,"</a>.</p>"]
    return join_strings(strings,'')

def build_site(title,
               subtitle,
               description,
               author,
               time,
               body):
               # figure_link,
               # figure_alt,
               # figure_caption,
               # attribute_place,
               # attribute_link):
    
    strings = [s1,
           s_pagetitle(title),
           s_description(description),
           s_author(author),
           s2,
           s_title(title),
           s_header1(title),
           s_header2(subtitle),
           s_time(time),
           s_body(body),
           # s_figure(figure_link,figure_alt,figure_caption),
           # s_attribute(attribute_place,attribute_link),
           s3]
    
    return htmlify(strings)
    
##############################################################################

# BUILD PAGES


for filename in os.listdir("articles"):
    if filename.endswith(".json") : 
         with open("articles/"+filename) as json_file:
             data = json.load(json_file)
             html_text = build_site(data["title"],
               data["subtitle"],
               data["description"],
               data["author"],
               data["time"],
               data["body"])
               # data["figure_link"],
               # data["figure_alt"],
               # data["figure_caption"],
               # data["attribute_place"],
               # data["attribute_link"])
             html_file= open(str(filename.split('.')[0])+".html","w")
             html_file.write(html_text)
             html_file.close()
    else:
        continue


# BUILD HOMEPAGE