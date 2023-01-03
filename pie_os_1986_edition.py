
from playsound import playsound
from time import sleep

print("Booting...")
sleep(2)
print("Boot complete. Loading system42...")
sleep(4)
print("system24 loaded.")
sleep(1)
print("Launching PIE OS 1986 TM.")
sleep(4)
print("WELCOME TO PIE OS!")
sleep(1)

# =
#for playing Windows 7 startup.mp3 file
playsound('Windows 7 Startup.mp3') # After an hour of work with my dad, we finally got this to work!!!! Thank goodness.
while True: # creates loop
    print("""
    
    YOU ARE CURRENTLY IN: HOME
    ---------------------------
    - LSC: SHOWS LIST OF COMMANDS
    - @GAMES: GOES TO A LIST OF YOUR INSTALLED GAMES.
    - ASSISTANT: NOT WORKING AS OF PIE OS. 1986 TM. [3.06.2]
    - UNFINISHED: DON'T EVEN TRY TO RUN IT. TRUST ME.
    
    """)
    sleep(1)
    print(" ")
    answer = input("PLEASE TYPE WHAT YOU WISH TO DO. ")
    if answer == "LSC":
        print("Loading...")
        sleep(0.5)
        print("""
        
        BASIC COMMANDS:
        ----------------
        
        - LSC - SHOWS LIST OF COMMANDS
        - @GAMES - GOES TO GAMES FOLDER
        - ASSISTANT - NOT WORKING
        - INFO - INFORMATION ABOUT PIE OS 2022 EDITION
        
        ADVANCED COMMANDS:
        -------------------
        - @WRD - STARTS A BASIC TEXT EDITOR 
        - EXONUS - RUNS A BOOT SEQUENCE 
        - DEMO - RUNS A DEMO OF THE NEXT PIE OS VERSION (COMING NOVEMBER 12TH 1988) 
    
        SECRET COMMANDS:
        -----------------
        - SURPRISE - IS IT YOUR BIRTHDAY? HOWS' ABOUT A BIRTHDAY SURPRISE!
        - NOSTALGIA - AHHH... RELIVE THE GOOD OLD DAYS OF COMPUTING
        - HELLO! - HOW YA' DOIN'?
        
        """)
        back = input("PRESS ENTER TO GO BACK HOME (NOTE: THIS MAY TAKE A WHILE, SO BE PATIENT)  ")
    elif answer == "INFO":
        print("""
        
        PIE OS TM. BY SCHMAUMER INC. 
        
        CURRENT OS VERSION: PIE OS 1986 EDITION VERSION 3.06.2
        HARDWARE MODEL: XQC RYZEN NITRO AN1515-42
        MEMORY: 1.0 GB
        PROCESSOR: XQC RYZEN 3 150U WITH RADIX VEGA PLUS
        DISK CAPACITY: 10.0 GB
        
        OS NAME: PIE OS 1986 3.06.2
        OS TYPE: 8-BIT
        DEVICE NUMBER: 2416279
        SOFTWARE UPDATES: NONE
        
        """)
        back = input("PRESS ENTER TO GO BACK HOME (NOTE: THIS MAY TAKE A WHILE, SO BE PATIENT)  ")
    elif answer == "SURPRISE":
        print("3...")
        sleep(1)
        print("2...")
        sleep(1)
        print("1...")
        sleep(1)
        playsound('Microsoft Windows 3.1 Startup Sound.mp3')
        print("HAPPY BIRTHDAY!")
        print("GO TREAT YOURSELF TO SOME CAKE.")
        back = input("PRESS ENTER TO GO BACK HOME (NOTE: THIS MAY TAKE A WHILE, SO BE PATIENT)   ")
    elif answer == "UNFINISHED":
        playsound('Windows XP Shutdown.mp3')
        print("UH OH! LOOKS LIKE YOU RAN SOMETHING THAT DOESN'T EXIST.")
        sleep(3)
        print("WAIT A MINUTE... I TOLD YOU NOT TO RUN THIS!")
        sleep(3)
        print("WELL, YOU KNOW WHAT THEY SAY, CURIOSITY KILLED THE CAT. COME ON, OFF YOU GO. ")
        sleep(4)
        back = input("PRESS ENTER TO GO BACK HONE (NOTE: THIS MAY TAKE A WHILE, SO BE PATIENT)   ")
    elif answer == "NOSTALGIA":
        print("THERE'S NOT MUCH NOSTALGIA HERE, HUH.")
        sleep(3)
        print("YOU'RE JUST TALKING TO ME-")
        sleep(1)
        playsound('Microsoft Windows 95 Startup Sound.mp3')
        print("OKAY, THAT'S WHY IT'S CALLED 'NOSTALGIA' ")
        sleep(3)
        print("I MISS THE GOOD OLD DAYS WHEN I WAS JUST A MERE CIRCUIT BOARD.")
        sleep(4)
        print("GO, EXPLORE THE COMPUTER. I'LL STAY HERE A WHILE.")
        sleep(3)
        back = input("PRESS ENTER TO GO BACK HOME (NOTE: THIS MAY TAKE A WHILE, SO BE PATIENT)   ")
    elif answer == "HELLO!":
        playsound('Windows XP Logon Sound.mp3')
        print("WHAT'S UP? :-)")
        sleep(3)
        back = input("HEY? WHY YOU LEAVING? SEE YOU, I GUESS :-( (PRESS ENTER TO GO BACK HOME)")
    elif answer == "EXONUS":
        print("DEVELOPER IS TOO LAZY TO MAKE A BOOT SEQUENCE. SOZ, LOL - TOTALLY NOT THE DEVELOPER")
        sleep(4)
    elif answer == "@WRD":
        document = input("Type what you want here: ")
        print("This masterpiece won't be saved, by the way. Why am I suddenly typing in lowercase? I dunno.")
        sleep(4)
    elif answer == "@GAMES":
        print("WAIT, DO I REALLY HAVE TO MAKE GAMES FOR THIS? UGH, NOT NOW. I'LL BE BACK IN SEVEN YEARS.")
        sleep(5)
    elif answer == "ASSISTANT":
        print("THIS DOESN'T EXIS-")
        sleep(0.5)
        playsound('Windows XP Logon Sound.mp3')
        sleep(1)
        print("NEW MESSAGE RECIEVED. THE DEVELOPER GOT OFF OF HIS ASS LAZING AROUND AND MADE THE ASSISTANT!")
        sleep(5)
        print("YEAH, NO. I'M NOT GONNA RUN THAT.")
        sleep(3)
        print("WHAT?")
        sleep(3)
        print("WHY ARE YOU STILL HERE?")
        sleep(2)
        print("FINE.... I'LL LET YOU USE THE ASSISTANT.")
        sleep(3)
        print("HERE-")
        sleep(1)
        playsound('Windows XP Shutdown.mp3')
        sleep(1)
        print("SENTIENT_COMPUTER.EXE HAS CRASHED. REBOOTING PIE OS...")
        sleep(4)
    elif answer == "DEMO":
        print("Booting...")
        sleep(3)
        print("PIE OS 7200 EDITION LOADS 95% FASTER THAN PIE OS 1986 EDITION.")
        sleep(3)
        print("THIS CURRENT OS CANNOT LOAD THE DEMO THAT FAST.")
        sleep(3)
        print("Running CPU checks...")
        sleep(3)
        print("Check.edux is loading...")
        sleep(2)
        print("YOUR COMPUTER WILL NOW RUN A MEMORY INTENSIVE SIMULATION WHICH WILL SHOW HOW FAST THE OS CAN LOAD THINGS.")
        sleep(6)
        print("""
        -------------------------------------------TEST-----------------------------------------------
        PLEASE NOTE THAT MOST OTHER PROCESSES WILL BE MOMENTARILY PAUSED TO RUN THIS.
        THIS TEST WILL COMPLETE IN AROUND 7 SECONDS.
        THE GAME BEING RAN IS: PYRO MANAGER - MOST POPULAR AND MEMORY INTENSIVE GAME OF 1986
        COMPLETING SOON...
        
        """)
        sleep(10)
        playsound('Windows XP Logon Sound.mp3')
        print("TEST COMPLETE. SHOWING RESULTS...")
        sleep(2)
        print("""
        ---------------------------------------TEST RESULTS-----------------------------------------------
        PIE OS 1986 EDITION:                                          PIE OS 7200 EDITION:
        LOAD TIME: 20 SECS                                            LOAD TIME: 5 SECS
        MEMORY USED: 596 MB / 1.0GB                                   MEMORY USED: 119 MB / 5.12 GB
        PROCESSOR: XQC RYZEN                                          PROCESSOR: ZBD NEXUS 2012 
        SPECIAL FEATURES: RADIX VEGA PLUS                             SPECIAL FEATURES: JOTIX PROCESSING 2
        
        
        
        PIE OS 1986 EDITION COSTS: £1200                              PIE OS 7200 EDITION COSTS: £986 
                """)
        back = input("PRESS ENTER TO GO HOME (THIS MAY TAKE A WHILE, SO BE PATIENT)   ")

