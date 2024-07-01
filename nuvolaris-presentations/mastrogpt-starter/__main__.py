#--kind python:default
#--param OPENAI_API_KEY $OPENAI_API_KEY
#--param OPENAI_API_HOST $OPENAI_API_HOST

import chat

def main(args):
    #print(args)
    ai = chat.Chat(args)
    inp = args.get("input", "")
    out = "Please provide some input"
    if inp != "":
        out = ai.ask(inp)

    res = {
        "output": out
    }

    html = f"<h1>{inp}</h1><p>{out}</p>"
    res['html'] = html
    return {
        "body": res
    }
    
    