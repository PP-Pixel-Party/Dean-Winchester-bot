async def loading(pr0fess0r_99, a, b, wait):
    c = await pr0fess0r_99.message.reply(f"{a}{a}{a}")
    await wait(0.2)
    d = await c.edit(f"{b}{a}{a}")
    await wait(0.2)
    e = await d.edit(f"{b}{b}{a}")
    await wait(0.2)
    f = await d.edit(f"{b}{b}{b}")
    await wait(0.2)
    await f.delete()
