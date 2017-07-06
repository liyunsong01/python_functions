import webbrowser
import time

total_breaks=3
count_breaks=0

print ("the program started on"+time.ctime())
while (count_breaks<total_breaks):
 time.sleep(0.5*60*60)
 webbrowser.open("https://www.youtube.com/watch?v=5hcq95lN-wg")
 count_breaks=count_breaks+1
