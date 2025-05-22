from datetime import datetime
from random import randint

# Emoji variables to use in your project
world = '🌍🌎🌏'
python = 'Python 🐍'
fire = '🔥'

# Emojis to copy and paste into your code:
# 🎊 🙌 🙌🏼 🙌🏽 🙌🏾 🙌🏿 # 😃 🕒 🎨 🎮 🔬 🎉 🕶️ 🎲 😊
# 👩‍🦽 👩🏼‍🦽 👩🏽‍🦽 👩🏾‍🦽 👩🏿‍🦽🧘 🧘🏼 🧘🏽 🧘🏾 🧘🏿 🙋 🙋🏼 🙋🏽 🙋🏾 🙋🏿
# 🦄 🚀 💯 ⭐ 💛 ❤️ 📚 ⚽ 🏏 🏀 🥋 🏆 ✨ 🥺 🌈 🔥 ♻️ 🌳

# Useful characters :',()*_/.#

# Function definitions
def roll_dice():
    print(f'You rolled a {randint(1, 6)}!')
    
# Put code to run under here
print(f'Hello {world}')
print(f'Welcome to {python}')
print(f'{python} is good at maths!')
print(f'{2*4}')
print(f'{4**2}') #** - to the power
print(f'The Date and time is {datetime.now()}')
roll_dice()