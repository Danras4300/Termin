from pdb import Restart
import discord
import Answers as a
import Questions as q
import class_object as co
import Images.Landmark as l
import Images.Celeb as c

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

Players = {}

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
  contents = message.content
  if contents.startswith("!join"):
    globals()[user_id] = []
    Players.update({str(user_id): globals()[user_id]})
    #reply = ["you have now join the game", 
    #         co.get_grid_lines(co.grid)]
    reply = co.get_grid_lines(co.grid)
    await message.channel.send("\n".join(reply))
  elif str(user_id) in Players:
    if contents.startswith("!math"):
      points = int(contents[6:])
      if points in q.Math_q:
        reply = q.Math_q[points]
        await message.channel.send(reply)
      else:
        reply = points, "is not possible to pick"
        await message.channel.send(reply)
    elif contents.startswith("!Capital"):
      points = int(contents[9:])
      if points in q.Capital_q:
        reply = q.Capital_q[points]
        await message.channel.send(reply)
      else:
        reply = points, "is not possible to pick"
        await message.channel.send(reply)


  print(contents)
  print(user_id)
  print(Players)

token = get_token()
client.run(token)