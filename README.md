# bot-not-working


####Error

Anivi has connected to Discord!
CMDS has connected to Bot!
Kitsu1 connected
Ignoring exception in command animu
Traceback (most recent call last):
  File "C:\Users\Fida\AppData\Local\Programs\Python\Python39\lib\site-packages\discord\ext\commands\core.py", line 85, in wrapped
    ret = await coro(*args, **kwargs)
  File "c:\Users\Fida\Documents\bot\cogs\kitsu.py", line 54, in animu
    init = await (title, 1)
TypeError: object tuple can't be used in 'await' expression

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "C:\Users\Fida\AppData\Local\Programs\Python\Python39\lib\site-packages\discord\ext\commands\bot.py", line 939, in invoke
    await ctx.command.invoke(ctx)
  File "C:\Users\Fida\AppData\Local\Programs\Python\Python39\lib\site-packages\discord\ext\commands\core.py", line 863, in invoke
    await injected(*ctx.args, **ctx.kwargs)
  File "C:\Users\Fida\AppData\Local\Programs\Python\Python39\lib\site-packages\discord\ext\commands\core.py", line 94, in wrapped
    raise CommandInvokeError(exc) from exc
discord.ext.commands.errors.CommandInvokeError: Command raised an exception: TypeError: object tuple can't be used in 'await' expression
