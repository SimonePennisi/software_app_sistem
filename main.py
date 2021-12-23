import webbrowser as wb
import time
app_aprire = str(input("Cosa vuoi fare? "))

if "app" in app_aprire:
  if "youtube" in app_aprire:
    wb.open("https://www.youtube.com/")
  elif "instagram" in app_aprire:
    wb.open("https://www.instagram.com/")
  elif "facebook" in app_aprire:
    wb.open("https://www.facebook.com/")
  elif "whatsapp" in app_aprire:
    wb.open("https://web.whatsapp.com/")
elif "hour" in app_aprire:
  orario = time.strftime("%H.%M")
  print(orario)
else:
  print("non conosciuto")
