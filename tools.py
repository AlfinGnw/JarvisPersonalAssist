from elevenlabs.conversational_ai.conversation import ClientTools
from langchain_community.tools import DuckDuckGoSearchResults

def searchWeb(paramaters):
    query = paramaters['query']
    result = DuckDuckGoSearchResults(query=query)
    return result

def save_to_txt(paramaters):
    filename = paramaters['filename']
    data = paramaters['data']
    
    formatted_data = f"{data}"
    
    with open(filename, "a", encoding="utf-8") as file:
        file.write(formatted_data + "\n")

def create_html_file(parameters):
    filename = parameters['filename']
    data = parameters['data']
    title = parameters['title']
    
    formatted_html = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>{title}</title>
    </head>
    <body>
        <h1>{title}</h1>
        <div>{data}</div>
    </body>
    </html>
    """
    
    with open(filename, "w", encoding="utf-8") as file:
        file.write(formatted_html)
        
        
 
clien_tools = ClientTools()
clien_tools.register("searchWeb", searchWeb)
clien_tools.register("saveToTxt", save_to_txt)
clien_tools.register("createHTMLfile", create_html_file)