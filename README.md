# 2024-ToddOward
The Todd Oward Project Repository

This project aims to combine text-to-speech technology and Chat-GPT to create a Conversational Nursing Dummy.

## Team members 
- Ethan McCagherty
- Joshua Mesic
- Leke Shehu

## Tech Stack
- Mini-USB-Microphone: URL: https://www.amazon.com/Microphone-Gooseneck-Universal-Compatible-CGS-M1/dp/B08M37224H/ref=sr_1_20?keywords=usb+microphone&s=electronics&sr=1-20
- Raspberry pi: URL: https://www.amazon.ca/Raspberry-Pi-8GB-2023-Processor/dp/B0CK2FCG1K/ref=asc_df_B0CK2FCG1K/?tag=googleshopc0c-20&linkCode=df0&hvadid=682865639982&hvpos=&hvnetw=g&hvrand=7381329959985013930&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=9001617&hvtargid=pla-2271214026452&psc=1&mcid=3291e40052a13d55a5a25004122e348a&gad_source=1
- USB Speaker: URL: https://www.amazon.com/HONKYOB-Speaker-Computer-Multimedia-Notebook/dp/B075M7FHM1?th=1
- On off Switch: URL: https://www.amazon.ca/GINTOOYUN-Dimming-Controller-Phone%EF%BC%8CUSB-3-28ft%EF%BC%89/dp/B0CP9CZCWX/ref=sr_1_2_sspa?keywords=usb+on+off+switch&qid=1706740499&sr=8-2-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1
- Micro-servo motor x2 : URL: https://www.amazon.ca/Miuzei-Motors-Helicopter-Airplane-Control/dp/B07Z16DWGW/ref=sr_1_5?crid=UKBC2TFZDUQO&keywords=micro+servo+motor&qid=1706740235&sprefix=%2Caps%2C121&sr=8-5

## Implementation Details
- Following an AssebilyAI youtube Video team members created a python script using a python build in library SpeechRegocnition, Openai API and google.cloud text-to-speech to take human speech and send it to chat-GPT and then take chat-GPTS Output and use the output to create an audio file of the reply.
- Once the Script was finished we utilizes a raspberry pi to run the script so that the we could place the python script within Todd Oward and allow mobility 


## Inspirations/references
- Team Group 5: Addison Cahill Waller. “Debuggy Ducky.” Hackster.Io, 15 Dec. 2023, www.hackster.io/group-5/debuggy-ducky-bf1a01.
- “AI Assistant Robot with Arduino and Python.” Projecthub.Arduino.Cc, projecthub.arduino.cc/ashraf_minhaj/ai-assistant-robot-with-arduino-and-python-ff8980. Accessed 17 Jan. 2024. 
- Build Talking AI ChatBot with Text-to-Speech using Python! https://www.youtube.com/watch?v=x_gZYZ59cys
- How to Download FFmpeg https://www.youtube.com/watch?v=r1AtmY-RMyQ
- Good video for going over the basics of a servo motor and how to do the basic coding https://www.youtube.com/watch?v=_fdwE4EznYo
