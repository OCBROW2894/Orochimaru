from datetime import datetime
from random import randint

# Emoji variables to use in your project
world = '🌍🌎🌏'
python = 'Python 🐍'
fire = '🔥'
smile = '😊'
money = '💰'

# Emojis to copy and paste into your code:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Useful characters :',()*_/.#

# Function definitions
def roll_dice():
    max= input('How many sides does your dice have? ')
    print(f'That is a D {max}')
    roll= randint(1, int(max) )
    print(f'You rolled a {roll} {fire*roll}')
    
# Put code to run under here
print(f'Hello {world}')
print(f'Welcome to {python}')
print(f'{python} is good at maths!')
print(f'{2*4}')
print(f'{4**2}') #** - to the power
print(f'The Date and time is {datetime.now()}')
roll_dice()

print(f'I 💚 Programming in {python}')
print(f'{python} is the best programming language in the world {world}')
print(f'{python} makes me {smile}')
print(f'I would like to make {money * 3} with {python}')