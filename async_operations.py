import asyncio

async def async_add(a, b):
    await asyncio.sleep(1)  # Simulate asynchronous operation
    return a + b

async def async_subtract(a, b):
    await asyncio.sleep(1)  # Simulate asynchronous operation
    return a - b

async def async_multiply(a, b):
    await asyncio.sleep(1)  # Simulate asynchronous operation
    return a * b

async def async_divide(a, b):
    await asyncio.sleep(1)  # Simulate asynchronous operation
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b
