import discord
import Answers as a
import Questions as q
import Grid as co
import Jeopardybot2 as j

def Help():
    reply = ['"!join" makes you join the game and you are now able to ask for questions',
             '"!points" sents the amount of points you have',
             '"!show" shows the grid as it is at the moment',
             '"!Math" ask for a question in the math category follow by a number from 100 - 500',
             '"!Capital" ask for a question in the capital category follow by a number from 100 - 500',
             '"!Celeb" ask for a question in the celeberity category follow by a number from 100 - 500',
             '"!Astro" ask for a question in the Astronomy category follow by a number from 100 - 500',
             '"!Landmark" ask for a question in the Landmark category follow by a number from 100 - 500',
             '"!What" Answer a question by the command follow be the answer, "!Who" is also possible']
    return reply

def Math(message):
    points = int(message[6:])
    if points in q.Math_q:
      reply = q.Math_q[points]
      del q.Math_q[points]
      co.runs = 1
      co.points = points
      co.edit_grid(co.grid, points, "!Math")
    else:
          reply = points, "is not possible to pick"
    return reply

def Capi(message):
    points = int(message[9:])
    if points in q.Capital_q:
        reply = q.Capital_q[points]
        del q.Capital_q[points]
        co.runs = 1
        co.points = points
        co.edit_grid(co.grid, points, "!Capital")
    else:
        reply = points, "is not possible to pick"
    return reply

def Celb(message):
    points = int(message[7:])
    if points in q.Celeb_q:
        if points == 100:
            reply = discord.File('./Images/Celeb/100.jpg')
        elif points == 200:
            reply = discord.File('./Images/Celeb/200.jpg')
        elif points == 300:
            reply = discord.File('./Images/Celeb/300.jpg')
        elif points == 400:
            reply = discord.File('./Images/Celeb/400.jpg')
        elif points == 500:
            reply = discord.File('./Images/Celeb/500.jpg')
        del q.Celeb_q[points]
        co.runs = 1
        co.points = points
        co.edit_grid(co.grid, points, "!Celeb")
    else:
        reply = points, "is not possible to pick"
    return reply

def Astro(message):
    points = int(message[7:])
    if points in q.Astronomy_q:
        if points == 200:
            reply = discord.File('./Images/Astronomi/200.jpg')
        else:
            reply = q.Astronomy_q[points]
        del q.Astronomy_q[points]
        co.runs = 1
        co.points = points
        co.edit_grid(co.grid, points, "!Astronomy")
    else:
        reply = points, "is not possible to pick"
    return reply

def Land(message):
    points = int(message[10:])
    if points in q.Landmark_q:
        if points == 100:
            reply = discord.File('./Images/Landmark/100.jpg')
        elif points == 200:
            reply = discord.File('./Images/Landmark/200.jpg')
        elif points == 300:
            reply = discord.File('./Images/Landmark/300.jpg')
        elif points == 400:
            reply = discord.File('./Images/Landmark/400.jpg')
        elif points == 500:
            reply = discord.File('./Images/Landmark/500.jpg')
        del q.Landmark_q[points]
        co.runs = 1
        co.points = points
        co.edit_grid(co.grid, points, "!Landmark")
    else:
        reply = points, "is not possible to pick"
    return reply

def Answers(contents):
    if contents in a.Math_a[co.points] or contents in a.Capital_a[co.points] or contents in a.Celeb_a[co.points] or contents in a.Astronomy_a[co.points] or contents in a.Landmark_a[co.points] :
        reply = ["That's right! Choose next question.", "",
                    "\n".join(co.get_grid_lines(co.grid))]
        co.runs = 0
    else:
        reply = "That's wrong..."
        co.runs = 0
    return reply
