from openai import openAI

client =openAI(
    api_key ='PASTE_YOUR_API_KEY_HERE'

)
response=client.response.creat(
    model='gpt4o mini',
    input="can i know about cricket player ms dhoni"
)
print(response.output_text)
