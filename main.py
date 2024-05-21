from sync_operations import sync_add, sync_subtract, sync_multiply, sync_divide
from async_operations import async_add, async_subtract, async_multiply, async_divide
import asyncio

# Synchronous operations
print(sync_add(5, 3))
print(sync_subtract(5, 3))
print(sync_multiply(5, 3))
print(sync_divide(5, 3))

# Asynchronous operations
async def main():
    print(await async_add(5, 3))
    print(await async_subtract(5, 3))
    print(await async_multiply(5, 3))
    print(await async_divide(5, 3))

asyncio.run(main())
