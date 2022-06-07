import requests
import time

channel_id = 974557115421184020
message = """
:dizzy: :tada:  __**[INVESTMENT] Selling Prison Resource With Resell Rights**__ :tada: :dizzy: 

    :dollar:  *Generates $35+ Per/Month*
    :star:  *Accumulates 2 five star reviews Per/Month*
    :timer:  *Completely idle investment, just requires bumps*

:mcm:  __https://www.mc-market.org/threads/698720/__
            **Or just PM me on Discord __@Baguette#3918__ **

||Send me an offer while it lasts, these things go quick||
"""

auth = "NzA1MDc3OTg1Mjk1NzI4NzUw.G669jW.KCwRNBQiY3o3XYso-E4debxJj0S6IhFPglhIhA"

payload = {
    'content': message
}

header = {
    'authorization': auth
}

if __name__ == "__main__":
    # Run a task every 2 hours
    while True:
        r=requests.post(f"https://discordapp.com/api/channels/{channel_id}/messages", headers=header, json=payload)
        print(r.status_code)
        print(r.text)
        print("\n")
        time.sleep(7230)