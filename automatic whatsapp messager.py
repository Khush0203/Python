import pywhatkit as kit
import pyttsx3
speaker = pyttsx3.init()


num = input("Enter the number you want to send the message to(with country code): ")
mes = input("Enter the message you want to send: ")
hour = int(input("Enter hour of time you want to send the message: "))
min = int(input("Enter minute of time you want to send the message: "))


kit.sendwhatmsg(num, mes,hour,min)
speaker.say("Message sent")
speaker.runAndWait()
