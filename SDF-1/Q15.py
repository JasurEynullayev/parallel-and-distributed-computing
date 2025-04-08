# 15. asyncio ilə kod və məntiq
# asyncio nədir?
# Asinxron proqramlaşdırma üçün istifadə olunur.
# IO-bound prosesləri gözlətmədən digər işləri icra etməyə imkan verir.
# Single-thread, amma konkurrent işləyir.

# Kod:

import asyncio

async def salam(ad):
    print(f"Salam, {ad}")
    await asyncio.sleep(1)
    print(f"Sağol, {ad}")

async def main():
    await asyncio.gather(
        salam("Ali"),
        salam("Aysel"),
        salam("Murad")
    )

asyncio.run(main())

# İzah:
# async def → Asinxron funksiya
# await → digər əməliyyatların icrasına icazə verir
# asyncio.gather() → birdən çox tapşırığı eyni vaxtda gözləyir