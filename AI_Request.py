from openai import OpenAI

def ai_request(text):

    prompt = "Please provide brief and clear notes on the following text in markdown format:\n" + text

    client = OpenAI(
        organization="",
        project="",
        api_key= ""
    )

    completion = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You are a note-taking assistant to help make notes about college lectures."},
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return (completion.choices[0].message.content)