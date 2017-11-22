import webbrowser
import time

count = 0;

while(count < 3):
    time.sleep(5);
    webbrowser.open('https://www.youtube.com/watch?v=lZbb7MOtcl8');
    count = count + 1;
