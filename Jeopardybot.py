from pdb import Restart
import discord

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

def get_token():
  tokfile = open(TOK_FILE, 'r')
  token = tokfile.read()
  tokfile.close()
  return token

@client.event
async def on_ready():
    print("Connected!")

class Catagory:
    def __init__(self, name, question, answers):
        self.name = name
        self.question = question
        self.answers = answers


Math_q = {100 : 'What is: (2/1)*2', 200 : 'What is: 10*24', 300 : '', 400 : '', 500 : ''}

Capitals =  {100 : 'what is the capital of Denmark', 200 : 'what is the capital of Sweden', 300 : 'what is the capital of America', 400 : 'what is the capital of Japan', 500 : 'what is the capital of Jamaica'}

Celebs =  {100 : 'Image', 200 : 'Image', 300 : 'Image', 400 : 'Image', 500 : 'Image'}

Planets = {100 : '', 200 : '', 300 : '', 400 : '', 500 : 'what is the temputure of the suns surface'}

landmarks = {100 : 'Image', 200 : 'Image', 300 : 'Image', 400 : 'Image', 500 : 'Image'}





token = get_token()
client.run(token)
