try:
    import requests, ctypes, random, string, time, json, os, shutil, subprocess, pystyle, colored
    from pystyle import Write, Add, Colorate, Colors
    from colored import fg
    from itertools import cycle
    from multiprocessing.spawn import spawn_main
    from pystyle import Add, Center, Anime, Colors, Colorate, Write, System
    import requests, os, sys, re, time, random, os.path, string, subprocess, random, threading, ctypes, shutil
    import discord
    from discord.ext import commands
    import fileinput
except ModuleNotFoundError:
    os.system("pip install request")
    os.system("pip install ctypes")
    os.system("pip install colores")
    os.system("pip install otertools")
    os.system("pip install multiprocessing.spawn")
    os.system("pip install pystyle")
    os.system("pip install discord")
    os.system("pip instaññ fileinput")

import os, requests, random, threading, json, time, multiprocessing
from colorama import Fore


random = fg(98)
blue = fg(14)
gray = fg(8)
magenta = fg(5)
dark_blue = fg(4)
yellow12 = fg(226)


while True:
    Write.Print("""
    \t\t\t────────────────By: F3fe & C4rl0s─────────────────────
    \t\t\t─██████──██████─██████████████─██████████─████████████──
    \t\t\t─██░░██──██░░██─██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░████─
    \t\t\t─██░░██──██░░██─██░░██████░░██─████░░████─██░░████░░░░██─
    \t\t\t─██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─
    \t\t\t─██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─
    \t\t\t─██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─                                                                                          
    \t\t\t─██░░██──██░░██─██░░██──██░░██───██░░██───██░░██──██░░██─
    \t\t\t─██░░░░██░░░░██─██░░██──██░░██───██░░██───██░░██──██░░██─
    \t\t\t─████░░░░░░████─██░░██████░░██─████░░████─██░░████░░░░██─
    \t\t\t───████░░████───██░░░░░░░░░░██─██░░░░░░██─██░░░░░░░░████─
    \t\t\t─────██████─────██████████████─██████████─████████████──
    \t\t\t───────────────────────For Discord─────────────────────
                
    """, Colors.purple_to_blue, interval=0.000)
    print()
    print(f"{magenta}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    print(f"\t\t\t{blue}[{random}1{blue}]{random} Fastest Banall\t\t\t")
    print(f"\t\t\t{blue}[{random}2{blue}]{random} Role Creator \t\t\t")
    print(f"\t\t\t{blue}[{random}3{blue}]{random} Role Deleter \t\t\t")
    print(f"\t\t\t{blue}[{random}4{blue}]{random} Fastest Channel Creator\t\t\t")
    print(f"\t\t\t{blue}[{random}5{blue}]{random} Fastest Channel Deleter\t\t\t")
    print(f"\t\t\t{blue}[{random}6{blue}]{random} Spamer\t\t\t")
    print(f"{magenta}════════════════════════════════════════════════════════════════════════════════════════════════════════════════════════")

    opc = input("root@voidtool> ")

    if opc == "1":
        # Token y prefijo para el bot
        token1 = input("Bot Token: ")
        prefix1 = input("Prefix: ")

        # Configura el bot
        bot = commands.Bot(command_prefix=prefix1, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f"Token bot: {token1}")
            print(f"Prefix: {prefix1}")
            print(f"Comando: {prefix1}banall")

        @bot.command(name="banall")
        async def banall(ctx):
            await ctx.message.delete()
                        
            for member in ctx.guild.members:
                try:
                    await member.ban()
                    print(f"Baneado: {member.name}")
                except Exception as e:
                    print(f"No se pudo banear a {member.name}: {e}")

        # Inicia el bot
        bot.run(token1)
                
            
                 
        bot.run(token1)
    
    if opc == "2": 
        token2 = input("token: ")
        prefix2 = input("Prefix: ")
        name2 = input("Nombre de los roles: ")
        bot = commands.Bot(command_prefix=prefix2, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f"Token Bot: {token2}")
            print(f"Prefix: {prefix2}")
            print(f"command: {prefix2}create_roles")
        @bot.command(name="create_role")
        async def create_role(ctx):
            await ctx.message.delete()
            while True:
                await ctx.guild.create_role(name=name2)
        bot.run(token2)

    if opc == "3": 
        token2 = input("token: ")
        prefix2 = input("Prefix: ")
        bot = commands.Bot(command_prefix=prefix2, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f"Token Bot: {token2}")
            print(f"Prefix: {prefix2}")
            print(f"command: {prefix2}delete_roles")
        @bot.command(name="delete_role")
        async def delete_role(ctx):
            await ctx.message.delete()
            for role in ctx.guild.roles:             
                if role.name != "@everyone":
                    await role.delete()
                    print("rol enliminado")
        bot.run(token2)

    if opc == "4": 
        token3 = input("Token Bot: ")
        prefix3 = input("Prefix Bot: ")
        name1 = input("Channel name: ")

        bot = commands.Bot(command_prefix=prefix3, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f"Token bot: {token3}")
            print(f"Prefix: {prefix3}")
            print(f"Comando: {prefix3}create")
        @bot.command(name="create")
        async def create(ctx):
            await ctx.message.delete()
            while True:                   
                await ctx.guild.create_text_channel(name1)
                print(f"Canal {name1} creado con éxito")
            
        bot.run(token3)
    
    if opc == "5":
        token3 = input("Token Bot: ")
        prefix3 = input("Prefix Bot: ")

        bot = commands.Bot(command_prefix=prefix3, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f"Token bot: {token3}")
            print(f"Prefix: {prefix3}")
            print(f"Comando: {prefix3}create")
        @bot.command(name="delete")
        async def create(ctx, ):
            await ctx.message.delete()
            for channel in ctx.guild.text_channels or ctx.guild.voice_channels:
                await channel.delete()
                print(f"Canal {channel} borrado  con éxito")
            
        bot.run(token3)
                       
    if opc == "6":
        print("Debe de poner .spam en cada canal que quiera spamear, es posible spamear multiples a la vez.\n")
        token3 = input("Token Bot: ")
        prefix3 = input("Prefix Bot: ")
        texto = input("¿Que quieres spamear?: ")

        bot = commands.Bot(command_prefix=prefix3, intents=discord.Intents.all())

        @bot.event
        async def on_ready():
            print(f"Token Bot: {token3}")
            print(f"Prefix: {prefix3}")
            print(f"Command {prefix3}spam")
        @bot.command(name="spam")
        async def spam(ctx):
            await ctx.message.delete()
            channel = ctx.guild.text_channels
            
            for channel in range(0,1500):
                await ctx.send(texto)
        bot.run(token3)

        
