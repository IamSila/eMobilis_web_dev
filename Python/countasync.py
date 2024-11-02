#!/usr/bin/env python3
#countasync.py

import asyncio

async def count():
    print("One")
    await asyncio.sleep(10)
    print("two")


async def main():
    await asyncio.gather(count(), count(), count(), count())

if __name__ == "__main__":
    asyncio.run(main())


###contrast above program to this
import time
def count():
    print("one")
    time.sleep(1)
    print("two")

def main():
    for i in range(3):
        count()

if __name__ == "__main__":
    main()
