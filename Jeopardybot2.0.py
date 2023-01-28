from pdb import Restart
import discord
import Answers as a
import Questions as q
import class_object as co
import Messages as M

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True
intents.members = True

client = discord.Client(intents=intents)

TOK_FILE = "token.txt"

Players = {}

q_str = ["!Math", "!math", "!Capital", "!capital", "!Celeb", "!celeb", "!Astro", "!astro", "!Landmark", "!landmark"]
q_math = ["!Math", "!math"]
q_capi = ["!Capital", "!capital"]
q_celeb = ["!Celeb", "!celeb"]
q_astro = ["!Astro", "!astro"]
q_land = ["!Landmark", "!landmark"]
a_str = ["!What", "!what", "!Who", "!who"]

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
  print(contents.startswith(""))
  if contents[0] == "!":
    if str(user_id) not in Players:
      if contents.startswith("!join"):
        globals()[user_id] = []
        Players.update({str(user_id): globals()[user_id]})
        reply = co.get_grid_lines(co.grid)
        await message.channel.send("\n".join(reply))
    elif str(user_id) in Players:
      if contents.startswith("!points"):
        points = 0
        for p in Players[str(user_id)]:
          points += p
        reply = points
        await message.channel.send(reply)

      #elif contents.startswith("!help"):

      #evt. en til at vise gridet?
      #husk questions og answers lige skal være færdige lavede nogle små rettelser mens jeg svarede på spørgsmål

      elif co.runs == 0: 
        if contents.startswith("!Math"):
          await message.channel.send(M.Math(contents))
        elif contents.startswith("!Capital"):
          await message.channel.send(M.Capi(contents))
        elif contents.startswith("!Celeb"):
          await message.channel.send(file=M.Celb(contents))
        elif contents.startswith("!Astro"):
          points = int(contents[7:])
          if points == 200:
            await message.channel.send(file=M.Astro(contents))
          else:
            await message.channel.send(M.Astro(contents))
        elif contents.startswith("!Landmark"):
          await message.channel.send(file=M.Land(contents))
        else:
          reply = "Not a valid command. Use help function"
          await message.channel.send(reply)

      elif co.runs == 1:
        if contents.startswith("!Math"):
          reply = "Wait for the current question to be answered"
          await message.channel.send(reply)
        elif contents.startswith("!Capital"):
          reply = "Wait for the current question to be answered"
          await message.channel.send(reply)
        elif contents.startswith("!Celeb"):
          reply = "Wait for the current question to be answered"
          await message.channel.send(reply)
        elif contents.startswith("!Astro"):
          reply = "Wait for the current question to be answered"
          await message.channel.send(reply)
        elif contents.startswith("!Landmark"):
          reply = "Wait for the current question to be answered"
          await message.channel.send(reply) 
        elif contents.startswith("!What") or contents.startswith("!Who"):
          if contents in a.Math_a[co.points] or contents in a.Capital_a[co.points] or contents in a.Celeb_a[co.points] or contents in a.Astronomy_a[co.points] or contents in a.Landmark_a[co.points]:
            globals()[user_id].append(co.points)
            await message.channel.send("\n".join(M.Answers(contents)))
          else:
            globals()[user_id].append(-co.points)
            await message.channel.send(M.Answers(contents))
        else:
          reply = "Not a valid command. Use help function"
          await message.channel.send(reply)
        

  print(contents)
  print(user_id)
  print(Players)
  print(a.Math_a[co.points])

token = get_token()
client.run(token)