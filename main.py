
import openai
openai.api_key = "sk-proj-6AVl81YNIHWjiiiukcANT3BlbkFJwPa53dde4HNTabwwRBdL"

def get_recommendation(user_input):
    prompt =  """
    Give me 3 movie recommendations like {}.
    """.format(user_input)
    response = openai.Completion.create(
        engine='davinci-002',
        prompt=prompt,
        max_tokens=200
    )
    return response.choices[0].text.strip()

user_input = input('What would you like a recommendation for?: ' )
recommendation = get_recommendation(user_input)
print("Recommendations based on '{}':".format(user_input))
print(recommendation)


# from openai import OpenAI
# client = OpenAI()
  
# assistant = client.beta.assistants.create(
#   name="Math Tutor",
#   instructions="You are a personal math tutor. Write and run code to answer math questions.",
#   tools=[{"type": "code_interpreter"}],
#   model="gpt-4-turbo",
# )

# thread = client.beta.threads.create()

# message = client.beta.threads.messages.create(
#   thread_id=thread.id,
#   role="user",
#   content="I need to solve the equation `3x + 11 = 14`. Can you help me?"
# )


# run = client.beta.threads.runs.create_and_poll(
#   thread_id=thread.id,
#   assistant_id=assistant.id,
#   instructions="Please address the user as Jane Doe. The user has a premium account."
# )


# if run.status == 'completed': 
#   messages = client.beta.threads.messages.list(
#     thread_id=thread.id
#   )
#   print(messages)
# else:
#   print(run.status)