command=""
started=False
while command!="quit":
    command=input("> ").lower()
    if command=="start":
        if started:
            print("Car is already started!")
            
        else :
           started=True
           print("Car started...")
    elif command=="stop":
        print("Car stopped.")
    elif command=="help":
        print("""
start-to start the car
stop-to stop the car
quit-to quit
              """)
    else:
        print("I do not understand that!")