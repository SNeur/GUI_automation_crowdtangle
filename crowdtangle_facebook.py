# Script to automatically put facebook posts from excel links into crowdtangle folders


# mouse positions need to be adjusted to the respective pc
# to get a real time position terminal for mouse position:
# open cmd, run python, import pyautogui, pyautogui.displayMousePosition()


# start script by having the DW Sendungen cell selected in excel
# have crowdtangle open in first browser tab, with saved post section open to reveal individual folders
# scrolling down in saved posts window may be necessary to reveal all groups

import pyautogui
import pyperclip
import time


##############################################################################################
# if you want to escape loop while it is running slam mouse cursor into top left corner
def movepost(xdrag, ydrag):

    pyautogui.press("left")
    pyautogui.press("left")
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "c") # copy link
    time.sleep(0.1)


    # This Block is needed if facebook links aren't formatted properly
    pyautogui.moveTo(350, 10) # move to not fuck up
    pyautogui.click(350, 10) # click second browser tab, where facebook should be
    time.sleep(0.1)
    pyautogui.moveTo(750, 50)
    pyautogui.click(750, 50) # click url window in browser
    pyautogui.click(750, 50) # if you any of these everything will break ¯\_(ツ)_/¯
    pyautogui.click(750, 50) # click url window in browser
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "v")
    time.sleep(2)
    pyautogui.press("enter") # enter to load page
    time.sleep(5.5)
    
    pyautogui.click(860, 400) # click video to change link
    time.sleep(1.3)
    pyautogui.click(750, 50) # click url window again
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "c") # copy link with channel name
    time.sleep(0.1)
    string = pyperclip.paste()
    list = string.split("/?v")
    string = str(list[0])
    print(string)
    time.sleep(0.1)
    pyperclip.copy(string)
    time.sleep(0.1)
    # Block End

    
    pyautogui.click(150, 20) # click first browser tab, where crowdtangle should be open
    time.sleep(0.1)
    pyautogui.click(870, 300) # click search window
    pyautogui.click(870, 300) # click search window
    pyautogui.click(870, 300) # click search window
    pyautogui.press("backspace") # delete old url

    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "v") # paste formatted url into crowdtangle search bar
    pyautogui.click(1400, 300) # clicks out of the search box
    time.sleep(0.5)
    pyautogui.moveTo(1345, 345) # move to search button
    pyautogui.click(1340, 345) # click search, usually once is not enough
    pyautogui.click(1340, 345) # click search
    time.sleep(3)
    pyautogui.click(1340, 345) # click search
    time.sleep(2.5)

    pyautogui.moveTo(1200, 610) # to be on the first post in the search results
    pyautogui.dragTo(xdrag, ydrag, duration=0.6) # drag post into folder determined by screen position given in function arguments
    # make sure that drag goes into right folder, crowdtangle isn't fast with updating over which folder you hover

    pyautogui.moveTo(-1000, 50) # go back to excel and readjust position
    pyautogui.click(-1000, 50) 
    time.sleep(0.1)
    pyautogui.press("right")
    pyautogui.press("right")
##############################################################################################  



# Call function to sort post, give position coordinates of respective folder as first 2 arguments
# Sendung needs to be formatted like "Editor's Choice\r\n"

i=100 # choose number of links script should work through


# if you want to escape loop while it is running slam mouse cursor into top left corner

while i>0:
    pyautogui.moveTo(-1000, 50)
    pyautogui.click(-1000, 50) # click excel window, currently open on second screen
    time.sleep(0.1)
    pyautogui.press("down") # one cell down
    time.sleep(0.1)
    pyautogui.hotkey("ctrl", "c") # copy Sendung
    time.sleep(0.1)

    if pyperclip.paste() == "\r\n": # move post depending on what value was in excel Sendungen cell
        movepost(570, 480)

    elif pyperclip.paste() == "Editor's Choice\r\n": # add any show or folder you like, but remember to change name and coordinates of folder
        movepost(570, 630)

    elif pyperclip.paste() == "Jaafar Talk\r\n":
        movepost(570, 740)

    elif pyperclip.paste() == "Weil ich eine Frau bin\r\n":
        movepost(570, 930)

    elif pyperclip.paste() == "messaeya\r\n":
        movepost(570, 760)
    
    elif pyperclip.paste() == "Dr.Heart\r\n":
        movepost(570, 590)
        
    elif pyperclip.paste() == "Quirky Customs\r\n":
        movepost(570, 845)
        
    elif pyperclip.paste() == "Birds Eye\r\n":
        movepost(570, 505)
        
    elif pyperclip.paste() == "Now you know\r\n":
        movepost(570, 802)
        
    elif pyperclip.paste() == "Going Wild\r\n":
        movepost(570, 695)

    elif pyperclip.paste() == "DIY\r\n":
        movepost(570, 660)

    elif pyperclip.paste() == "Europe the Max\r\n":
        movepost(570, 660)

    elif pyperclip.paste() == "Now you Know\r\n":
        movepost(570, 660)
        
    elif pyperclip.paste() == "Try This\r\n":
        movepost(570, 570)
        
    elif pyperclip.paste() == "How to Bauhaus\r\n":
        movepost(570, 718)

    else:
        i = 0 # script will end on first cell where Sendung is not recognized

    i-=1



# Ghalia and Firas have no folder, therefore not included in loop; possibly filter them out if you want



        



