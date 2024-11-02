import asyncio

async def f():
    y = await z(x) # OK -  'await' and 'return' allowed in coroutines
    return y

async def g(x):
    yield x # OK - async generator

async def m(x):
    yield from gen(x) # NO - syntax error

def m(x):
    y = await z(x) # No - syntax error (no `async def` here)
    return y

