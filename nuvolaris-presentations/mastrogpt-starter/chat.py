from openai import AzureOpenAI

ROLE = "You are an helpful assistant"
MODEL = "gpt-35-turbo"

class Chat:

    def __init__(self, args):
        key = args.get("OPENAI_API_KEY")
        host = args.get("OPENAI_API_HOST")
        self.ai = AzureOpenAI(api_version="2023-12-01-preview", api_key=key, azure_endpoint=host)

    def req(self, inp, role):
        system = {"role": "system", "content": role }
        user = {"role": "user", "content": inp}
        request = [system, user]
        return request

    def ask(self, input, role=ROLE):
        request = self.req(input, role)
        comp = self.ai.chat.completions.create(model=MODEL, messages=request)
        content = "ERROR"
        if len(comp.choices) > 0:
            content = comp.choices[0].message.content
        return content
