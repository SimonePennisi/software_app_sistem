import webbrowser as wb
import time

while True:
  azione = str(input("Cosa vuoi fare? "))

  if "app" in azione:
    if "youtube" in azione:
      wb.open("https://www.youtube.com/")
    elif "instagram" in azione:
      wb.open("https://www.instagram.com/")
    elif "facebook" in azione:
      wb.open("https://www.facebook.com/")
    elif "whatsapp" in azione:
      wb.open("https://web.whatsapp.com/")
    else:
      sito = str(input("Non ho capito il sito, potresti ridirmelo:"))
      sitoURL_generator = (f"https://www.{sito}.com/")
      wb.open(sitoURL_generator)

  elif "hour" in azione:
    orario = time.strftime("%H.%M")
    print(orario)
  else:
    print("non conosciuto")
