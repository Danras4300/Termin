from pdb import Restart
import discord
import Answers as a
import Questions as q
import Grid as co

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
  if contents[0] == "!":
    if contents.startswith("!join"):
      globals()[user_id] = []
      Players.update({str(user_id): globals()[user_id]})
      #reply = ["you have now join the game", 
      #         co.get_grid_lines(co.grid)]
      reply = co.get_grid_lines(co.grid)
      await message.channel.send("\n".join(reply))
    elif str(user_id) in Players:
      if co.runs == 0: 
        if contents.startswith("!Math"):
          points = int(contents[6:])
          if points in q.Math_q:
            reply = q.Math_q[points]
            await message.channel.send(reply)
            co.runs = 1
            co.points = points
          else:
            reply = points, "is not possible to pick"
            await message.channel.send(reply)
        elif contents.startswith("!Capital"):
          points = int(contents[9:])
          if points in q.Capital_q:
            reply = q.Capital_q[points]
            await message.channel.send(reply)
            co.runs = 1
            co.points = points
          else:
            reply = points, "is not possible to pick"
            await message.channel.send(reply)
        elif contents.startswith("!Celeb"):
          points = int(contents[7:])
          if points in q.Celeb_q:
            reply = q.Celeb_q[points]
            await message.channel.send(reply)
            co.runs = 1
            co.points = points
          else:
            reply = points, "is not possible to pick"
            await message.channel.send(reply)
        elif contents.startswith("!Astronomy"):
          points = int(contents[11:])
          if points in q.Astronomy_q:
            if points == 300:
              await message.channel.send("What is:", file=discord.File('./Images/Astronomi/300.jpg'))
            else:
              reply = q.Astronomy_q[points]
              await message.channel.send(reply)
            co.runs = 1
            co.points = points
          else:
            reply = points, "is not possible to pick"
            await message.channel.send(reply)
        elif contents.startswith("!Landmark"):
          points = int(contents[10:])
          if points in q.Landmark_q:
            reply = q.Landmark_q[points]
            await message.channel.send("Shot by a knife", file=discord.File('./Users/danielhansen/Documents/GitHub/Termin/Images/Landmark/100.png'))
            co.runs = 1
            co.points = points
          else:
            reply = points, "is not possible to pick"
            await message.channel.send(reply)
      elif co.runs == 1:
        if contents.startswith("!Math" or "!Capital" or "!Celeb" or "!Astronomy" or "!Landmark"):
          reply = "Wait for the current question to be answered"
          await message.channel.send(reply)
        elif contents.startswith("!What" or "!Who"):
          if contents == a.Math_a[co.points] or a.Capital_a[co.points] or a.Celeb_a[co.points] or a.Astronomy_a[co.points] or a.Landmark_a[co.points]:
            reply = "That's right! Choose next question."
            await message.channel.send(reply)
            co.runs = 0
          else:
            reply = "That's wrong..."
            await message.channel.send(reply)
            co.runs = 0
        else:
          reply = "Not a valid command. Use help function"
          await message.channel.send(reply)

  print(contents)
  print(user_id)
  print(Players)
  print(type(co.points))
  print(type(co.points))
  print(a.Math_a[co.points])

token = get_token()
client.run(token)