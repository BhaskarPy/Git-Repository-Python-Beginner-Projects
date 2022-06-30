# Import Modules
import sys
import time
# Final Question
def final_qstn():
    time.sleep(1)
    story=(
        "Steve decided to proceed through the right door.\n"+
        "It seems like someone has decreased the brightness little more here and the tunnel floor has become slippery.\n"+
        "With great difficulty and keeping one hand on the wall he kept walking.\n"+
        "Suddenly he felt that he was not alone in the tunnel.\n"+
        "He could feel the someone else presence there.\n"+
        "Steve asked loudly - \'Who\'s there ?\'\n"+
        "No one answered. He again asked -\'Please answer. Anybody here?\'\n"+
        "A answer came. Someone spoke in hissing sound - \'Your shadow.\'\n"+
        "Steve could feel the chilling sense of fear running down his spine.\n"+
        "But without showing the fear in his voice he asked - \'What do you mean?\'\n"+
        "The voice answered - \'I am shadow of your greed.\'\n"+
        "Steve said - \'I am not greedy.\'\n"+
        "The voice quickly responded - \'Prove it. Answer my three questions correctly and leave with the treasure.\'\n"+
        "\'Otherwise you will have to spend rest of your life here.\'\n"+
        "Steve - \'ok. ask me.\'\n"+
        "Voice - \'Who is the best teacher?\'\n"
    )
    print(story)
    opt=input("Who is the best teacher ? Answer for Steve and save him. :: ").lower()
    time.sleep(1)
    if opt=="failure" or opt=="failures":
        story=(
            "Voice - \'As you have answered the first question correctly, now answer this question - What is the only truth ?\'\n"
        )
        print(story)
        opt=input("What is the only truth ? Answer for Steve and save him. :: ").lower()
        time.sleep(1)
        if opt=="death":
            story=(
                "Voice - \'Steve, you are truly an intelligent person.\'\n"+
                "\'Answer this final question and you can leave the tunnel with treasure.\'\n"+
                "\'Who is our real friend?\'\n"
            )
            print(story)
            opt=input("Who is our real friend ? Answer for steve and save him. :: ").lower()
            time.sleep(1)
            if opt=="god":
                story=(
                    "\'Well done Steve.\'\n"+
                    "\' You are not only a good person, you are also intelligent.\'\n"+
                    "\' Now you can leave the tunnel with all the treasures.\'\n"+
                    "So, Steve left the tunnel with the treasures and live happily ever after."
                )
                print(story)
            else:
                time.sleep(1)
                sys.exit("Wrong answer. Now stay here for eternity.")
        else:
            time.sleep(1)
            sys.exit("Wrong answer. Now stay here for eternity.") 
    else:
        time.sleep(1)
        sys.exit("Wrong answer. Now stay here for eternity.")
# Second question
def second_qstn():
    story=(
        "Steve started walking.\n"+
        "He could feel the cold, damp breeze coming from the dark tunnel.\n"+
        "He fasten his jacket little bit and searched for the torch inside his pocket.\n"+ 
        "Steve pulled out the torch and pressed the button.\n"+
        "A faint ray of light fall on the wall.\n"+
        "Steve thought \'I don\'t have much time left.\n"+
        "\'This torch could die in any minute.\n"+
        "He quickly moved forward.\n"+
        "After walking for 2 minutes he came to a point from where he can see three doors infront of him.\n"+
        "\'Which door should I take? left, middle or right ?\n"
    )
    print(story)
    opt=input("from which door should Steve proceed - left,middle or right ? Type(left/middle/right) : ").lower()
    if opt=='left':
        time.sleep(1)
        story=(
            "Steve decided to proceed through the left door.\n"+
            "It seems like someone has decreased the brightness little more here and the tunnel floor has become slippery.\n"+
            "Suddenly Steve slipped and fall on the hard tunnel floor.\n"+
            "A severe sense of pain ran through his spine.\n"+
            "For a minute or two he keep lying on the floor.\n"+
            "Then with great difficulty, he stood up.\n"+
            "He could not feel the torch in his hand.\n"+
            "\'Where is it ? Have I lost it ?\'\n"+
            "He tried to search for the torch but in vain.\n"+
            "\'I will not survive a minute without light . I must go back and will come back.\'\n"+
            "So, he turned back and keeping his hand on the wall he proceed.\n"+
            "Steve\'s story ends here.\n"
        )
        print(story)
        sys.exit()
    elif opt=='middle':
        time.sleep(1)
        story=(
            "Steve decided to proceed through the middle door.\n"+
            "It seems like someone has decreased the brightness little more here and the tunnel floor has become slippery.\n"+
            "Suddenly the torch turned off, leaving Steve in complete darkness.\n"+
            "Steve stand there for a while and thought \'What should I do ? Should I proceed or go back ?\'\n"+
            "\'If I go back all the hard works I have done so far will go in vain.\'\n"+
            "\'But, if I proceed I have to do it in complete darkness.\'\n"+
            "\'I think it is better to go back and I will come again with preparation.\'\n"+
            "\'Treasures and adventures can wait.\'\n"+
            "So, he turned back and keeping his hand on the wall he proceed.\n"+
            "Steve\'s story ends here."
        )
        print(story)
        sys.exit()
    elif opt=='right':
        time.sleep(1)
        final_qstn()
    else:
        print("Wrong choice.")
        sys.exit()      
# First Question
def first_qstn():
    story=(
        "After walking for long 3 hours, Steve ended up in front of a long dark tunnel.\n"+
        "\'Should I proceed or go back ?\'\n"+
        "\'There may be some hidden dangers inside.\'\n"+
        "\'If I proceed I have to face them.\'\n"+
        "\'But, if I go back I have to forget about the treasures.\'\n"+
        "\'What should I do?\'\n"
    )
    print(story)
    opt=input("What should steve do? Proceed ? (y/n) : ").lower()
    if opt=='y':
        second_qstn()
    else:
        sys.exit("Better luck next time.")
# Start the game
def start_game():
    print("########################################")
    print()
    print("# Welcome to text based adventure game #")
    print()
    print("########################################S")
    print()
    print("Read the story carefully.Think, answer and proceed.")
    print()
    first_qstn()
opt = input("Do you want to play the game ? (y/n) :").lower()
if opt=='y':
    start_game()
else:
    sys.exit("That\'s all for now.")
