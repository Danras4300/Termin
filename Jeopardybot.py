from pdb import Restart
import discord
import class_object as co
import Images.Landmark as l
import Images.Celeb as c

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

@client.event
async def on_message(message):
  user_id = message.author.id
  info = message.content
  if info == "join":
    
  print(info)
  print(user_id)

token = get_token()
client.run(token)