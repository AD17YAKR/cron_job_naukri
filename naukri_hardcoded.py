import requests
import time

def update_profile():
    url = "https://www.naukri.com/cloudgateway-mynaukri/resman-aggregator-services/v1/users/self/fullprofiles"

    # Hardcoded credentials (INSECURE PRACTICE)
    AUTH_TOKEN = "Bearer eyJraWQiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MjIxMjExOTkwLCJzdWIiOiIyMzQ0MTk3NTIiLCJ1ZF91c2VybmFtZSI6ImFkaXR5YTAwMTEwNkBnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxMjkuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMjkuMCIsImlwQWRyZXNzIjoiNDkuMzcuMzIuMjM5IiwidWRfaXNUZWNoT3BzTG9naW4iOmZhbHNlLCJ1c2VySWQiOjIzNDQxOTc1Miwic3ViVXNlclR5cGUiOiIiLCJ1c2VyU3RhdGUiOiJBVVRIRU5USUNBVEVEIiwidWRfaXNQYWlkQ2xpZW50IjpmYWxzZSwidWRfZW1haWxWZXJpZmllZCI6dHJ1ZSwidXNlclR5cGUiOiJqb2JzZWVrZXIiLCJzZXNzaW9uU3RhdFRpbWUiOiIyMDI0LTA5LTAxVDAyOjM0OjE1IiwidWRfZW1haWwiOiJhZGl0eWFzaW5naC4xMTA2MDFAZ21haWwuY29tIiwidXNlclJvbGUiOiJ1c2VyIiwiZXhwIjoxNzM4MTY5ODg2LCJ0b2tlblR5cGUiOiJhY2Nlc3NUb2tlbiIsImlhdCI6MTczODE2NjI4NiwianRpIjoiYmM4MmJiZDBmOWFiNDhlNTlhYzFmNTc3OGEzMjYxNDAiLCJwb2RJZCI6InByb2QtY2Q1Zjk5NTZkLWJ0N2t4In0.dumBZ1nMCe_5jCk2fxXLedmMetUSDIrZnOOdHNX_rbafW7EfnWjgbix1wpogoEq31hZxe9P5AoezY9XjaVpvPxEo3vYoFfOLwl99Yx-APeAHulRJCqp3whfIdGIWNCIZg45EONJcDc0_M4PVJr5nN4IG278foM_-OT9DvTK45U83S4eMx7lXDnDvAE6Onc0X7rRchGxtB9oO2DeaGaiv9ge2MmM0vBmC87SWACx7TqxVd8EJvupOWeR4PXuO5OvodrJutKQ-wgTMlS8jJMk_HxFsU_IRXR2wJVGlTSSUkztc3zDeBRvLlHjPPIjPlBzRMNfRIN22KjFSUp7m_kq-eA"

    COOKIE = "_t_ds=24a474e81725138189-3524a474e8-024a474e8; ninjas_new_marketing_token=cd287e363a80eb60fe665f6b51ca777e; J=0; nauk_rt=bc82bbd0f9ab48e59ac1f5778a326140; nauk_sid=bc82bbd0f9ab48e59ac1f5778a326140; nauk_otl=bc82bbd0f9ab48e59ac1f5778a326140; NKWAP=f25357402bb2cbe253eabbf121da3308936b6d043451bc8d532d6e777cd4b0e9a684457db930ac6c08b05ee52a8d9794~29b622cb9dc327f30e3448fd2c87741477aec7aa4886df915b3c9934779b4d0e237376ccad94d1f7~1~0; MYNAUKRI[UNID]=c90c3cd069a84540b37f4c4673f2773c; test=naukri.com; nauk_ps=default; PS=29b622cb9dc327f30e3448fd2c87741477aec7aa4886df915b3c9934779b4d0e237376ccad94d1f7; ACTIVE=1737751390; _ff_ds=0247861001733988447-CFE54EF3AE02-E697832DD260; tStp=1736958010911; studio_rt=17e3b6eeb5fb4c8d9586e4165b77c59d; ninja_auth_token=5d6edd953c43ed51e43498fb607f842b; ph_phc_s4aJa5RpiiZlHbbxy4Y1Btjhosozg9ECrSuJNVrvZuP_posthog=%7B%22distinct_id%22%3A1610050%7D; PHPSESSID=u4u6fnhtk89sqinef2fjs5o2de; _t_r=1091%2F%2F; FFSESS=75bee1102d749a83593c4fe97b7f74da; _ff_r=2020%2F%2F; failLoginCount=0; nauk_at=eyJraWQiOiIyIiwidHlwIjoiSldUIiwiYWxnIjoiUlM1MTIifQ.eyJ1ZF9yZXNJZCI6MjIxMjExOTkwLCJzdWIiOiIyMzQ0MTk3NTIiLCJ1ZF91c2VybmFtZSI6ImFkaXR5YTAwMTEwNkBnbWFpbC5jb20iLCJ1ZF9pc0VtYWlsIjp0cnVlLCJpc3MiOiJJbmZvRWRnZSBJbmRpYSBQdnQuIEx0ZC4iLCJ1c2VyQWdlbnQiOiJNb3ppbGxhLzUuMCAoV2luZG93cyBOVCAxMC4wOyBXaW42NDsgeDY0OyBydjoxMjkuMCkgR2Vja28vMjAxMDAxMDEgRmlyZWZveC8xMjkuMCIsImlwQWRyZXNzIjoiNDkuMzcuMzIuMjM5IiwidWRfaXNUZWNoT3BzTG9naW4iOmZhbHNlLCJ1c2VySWQiOjIzNDQxOTc1Miwic3ViVXNlclR5cGUiOiIiLCJ1c2VyU3RhdGUiOiJBVVRIRU5USUNBVEVEIiwidWRfaXNQYWlkQ2xpZW50IjpmYWxzZSwidWRfZW1haWxWZXJpZmllZCI6dHJ1ZSwidXNlclR5cGUiOiJqb2JzZWVrZXIiLCJzZXNzaW9uU3RhdFRpbWUiOiIyMDI0LTA5LTAxVDAyOjM0OjE1IiwidWRfZW1haWwiOiJhZGl0eWFzaW5naC4xMTA2MDFAZ21haWwuY29tIiwidXNlclJvbGUiOiJ1c2VyIiwiZXhwIjoxNzM4MTY5ODg2LCJ0b2tlblR5cGUiOiJhY2Nlc3NUb2tlbiIsImlhdCI6MTczODE2NjI4NiwianRpIjoiYmM4MmJiZDBmOWFiNDhlNTlhYzFmNTc3OGEzMjYxNDAiLCJwb2RJZCI6InByb2QtY2Q1Zjk5NTZkLWJ0N2t4In0.dumBZ1nMCe_5jCk2fxXLedmMetUSDIrZnOOdHNX_rbafW7EfnWjgbix1wpogoEq31hZxe9P5AoezY9XjaVpvPxEo3vYoFfOLwl99Yx-APeAHulRJCqp3whfIdGIWNCIZg45EONJcDc0_M4PVJr5nN4IG278foM_-OT9DvTK45U83S4eMx7lXDnDvAE6Onc0X7rRchGxtB9oO2DeaGaiv9ge2MmM0vBmC87SWACx7TqxVd8EJvupOWeR4PXuO5OvodrJutKQ-wgTMlS8jJMk_HxFsU_IRXR2wJVGlTSSUkztc3zDeBRvLlHjPPIjPlBzRMNfRIN22KjFSUp7m_kq-eA; is_login=1; ak_bmsc=D576486A4372D13D4043504947163279~000000000000000000000000000000~YAAQ1Ew5F9QsNZiUAQAA9ULJshqZRVaTk0sNDj6OLjYJIil2Wz2p/1ZX/A5TP5xV7mlJqQNx6GVye/gFh50tWmR5Vz1SPzYvav+N6zj245Rnq9PqdoP2B4W+DtKrod7/XKYVqJCCVkd4UzRTm+uG7ukpAkYABWu+NXO8nSMSEUQdmSYCzFvFnh4inWAffnSQrlRsYC7hjVrpjYLTSXsMiGT4QAUoIPAkmvaOm0EyfnAGS2NY6BRbU4SvyRTXgfuKBWj/0A3tiIdUY+pYU81aqvTowf4mRAL7tkxQDX6biWC90TOPUmPABukIBGH2t8NFklh31f54varlK+4QmXY6cHK3w3qDJHRAYdeMiNS3XG5DIxNMuDzyFhSoOApx//7NoDQvSQbVyHyCm67p+yYt63mK4owaxuaJjybgYlyLQRR2ah2AnN/fizQgJA==; bm_mi=47139189404C195169CAEF25F6B335E3~YAAQ1Ew5F/YdNZiUAQAAjvzIshoCXywPAWtvkC7ueMIXaPALa8U7C5PcvrLsMnSLG7OhPJ3LRXVzChV4RLpiuYbKoW411yQdmOus3v7UY3hjOCZpnb1dbrHSWT+1Gt077pmjAyg1kNza9CfCzgmV5DQTvRccEG1Tu0Ow5z0vNQRkfkDRL1BhNoS8/1hQ+FegBEDjOUQywgLWHjRyUYFOMg2EJL/Hui8Fk9PXSnm+/QfUQpM0154N2ozpbymits46muP74LWeviWBEquH8qbThchDK4mCUSuML7qyx3+5p4D/FyQ3w4zt7nUQ7fz5M/X+8jigGdMnCJ416APgnw==~1; bm_sv=C034B16D7E919E265544A364CCAFDE6A~YAAQV3IsMeNxt3KUAQAAXCLJshq2mAjUCQJlNQeBsxdPJOfI/v/sjF3wb+8sDPGiwsXZX5crFi1ZI+baOdmhRnhE4TLTCIJRKAgojzC/lwGp6BTKQgEyWJr0rvCVCMxi+lvQw9oq77dQ+oyyifA2I3nUEWw/crN15zKnhPim8yO4kminoLastoVUa55/F5GM1VxTHd9EKLFobRGnSQK/qSYEb2a/4wPHOTX3RaEt3tFGx01y/EAGZm6IPZoXKMLxXw==~1"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:134.0) Gecko/20100101 Firefox/134.0",
        "Accept": "application/json",
        "Accept-Language": "en-US,en;q=0.5",
        "Content-Type": "application/json",
        "X-HTTP-Method-Override": "PUT",
        "clientid": "d3skt0p",
        "appid": "105",
        "systemid": "Naukri",
        "authorization": AUTH_TOKEN,
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "https://www.naukri.com",
        "Referer": "https://www.naukri.com/mnjuser/profile?id=&altresid&action=modalOpen",
        "Cookie": COOKIE
    }

    data = {
        "profile": {
            "resumeHeadline": "Software Developer | Software Engineer | Java Developer | Python Developer | Backend Developer | Flutter Developer | Mobile App Developer | JAVA | Spring Boot | Data Structures and Algorithms "
        },
        "profileId": "d0d3af836a9b0803508d7941edeb802fb62fa215fbede5b1f79fd6c296adc7b6"
    }

    try:
        response = requests.post(url, headers=headers, json=data)
        print(f"Update attempted at {time.ctime()}")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.text[:200]}...")  # Truncate long responses
    except Exception as e:
        print(f"Error occurred: {str(e)}")

if __name__ == "__main__":
    update_profile()