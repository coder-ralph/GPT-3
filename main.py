import openai

def gpt3(stext):
    openai.api_key = 'your api here' # api keys
    response = openai.Completion.create(
        engine="davinci-instruct-beta",
        prompt=stext,
                tempeture=0.1,
                max_tokens=1000,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text

query = 'What is Python?'
response = gpt3(query)
print(response)