"""A Future is a special low-level awaitable object that represents an eventual result of an asynchronous operation."""

"""
async def main():
    await function_that_returns_a_future_object()

    # this is also valid:
    await asyncio.gather(
        function_that_returns_a_future_object(),
        some_python_coroutine()
    )
"""