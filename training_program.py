
### ARCHERY TRAINING AT HOME ###
# !! Exercises from: worldarcherycentre.org !!
# Link to the PDF: https://worldarcherycentre.org/wp-content/uploads/2020/04/Archery-Home-training-tips_WAEC_TEC-PHY_GER_V1.4_b.pdf


# IMPORT MODULES
import time
from tkinter.constants import FALSE


# USER INPUT: Beginner, Advanced or Pro?
input_missing = True
while input_missing == True:
    status = input("Chose your status: \n \
        b ... beginner \n \
        a ... advanced \n \
        p ... pro \n \
    Enter letter b, a or p: ").lower()

    if (status == 'b') or (status == 'beginner'):
        status = 1
        level = 'Beginner'
        input_missing = False
    elif (status == 'a') or (status == 'advanced'):
        status = 2
        level = 'Advanced'
        input_missing = False
    elif (status == 'p') or (status == 'pro'):
        status = 3
        level = 'Pro'
        input_missing = False
    else:
        print("No valid value. Try again.")
        input_missing = True


print("\nChosen Level: {}. Take your bow and get ready for your first exercise.".format(level))
time.sleep(6)


# DEFINITION OF COUNTDOWN
def countdown(seconds):
    temp = seconds
    while temp > 0:
        print(temp)
        time.sleep(1)
        temp -= 1

#CLASSES
class Exercise_Hold:
    def __init__(self, ex_name="", holdtime=0, pause=0, repetition=0, explanation="", advice="", action=""):
        self.ex_name = ex_name
        self.holdtime = holdtime
        self.pause = pause
        self.repetition = repetition
        self.explanation = explanation
        self.advice = advice
        self.action = action


    def printouts(self):
        print("\nStart of Exercise {}.".format(self.ex_name))
        time.sleep(5)
        print("\nExplanation: {}".format(self.explanation))
        time.sleep(10)
        print("\nAdvice: {}".format(self.advice))
        time.sleep(10)
        print("\nAlright. Get ready!")
        time.sleep(2)

        while self.repetition > 0:
            print("\nRepetitions left: {}".format(self.repetition))
            time.sleep(2)
            print("\n{}".format(self.action))
            time.sleep(3)

            print("\nHold for {} seconds.".format(self.holdtime))
            countdown(self.holdtime)
        
            print("\nBack to relaxed position.")
            time.sleep(2)

            print("\nShort break.")
            countdown(self.pause)

            self.repetition -= 1

        print("\nExercise {} completed!".format(self.ex_name))
        print("---------------------------------------")

class Exercise_Reps:
    def __init__(self, ex_name, reps, part1, part2, pause, repetition, explanation, advice, action):
        self.ex_name = ex_name
        self.reps = reps
        self.part1 = part1
        self.part2 = part2
        self.pause = pause
        self.repetition = repetition
        self.explanation = explanation
        self.advice = advice
        self.action = action


    def printouts(self):
        print("\nStart of Exercise {}.".format(self.ex_name))
        time.sleep(5)
        print("\nExplanation: {}".format(self.explanation))
        time.sleep(10)
        print("\nAdvice: {}".format(self.advice))
        time.sleep(10)
        print("\nAlright. Get ready!")
        time.sleep(2)

        while self.repetition > 0:
            print("\nRepetitions left: {}".format(self.repetition))
            time.sleep(2)
            print(self.action)
            time.sleep(3)

            repeat = self.reps

            while repeat > 0:
                print(self.part1)
                time.sleep(4)
                print(self.part2)
                time.sleep(4)
                repeat -= 1
                    
            print("\nBack to relaxed position.")
            time.sleep(2)

            print("\nShort break.")
            countdown(self.pause)

            self.repetition -= 1

        print("\nExercise {} completed!".format(self.ex_name))
        print("---------------------------------------")

# DEFINITION OF EXERCISES
def create_ex_03(status):
    if status == 1:
        holdtime = 20
        pause = 10
        repetition = 2
    else:
        holdtime = 30
        pause = 10
        repetition = 2
    
    ex_name = "#3 Special Strength: Lift bow (right arm)"
    explanation = "Lift bow with right arm, hold for {} sec. / pause for {} sec. -> {} repetitions".format(holdtime, pause, repetition)
    advice = "Maintain the 'T-position' and make sure the upper body does not tilt back. Focus your sight while doing this."
    action = "Lift bow with right arm."

    return Exercise_Hold(ex_name, holdtime, pause, repetition,explanation, advice, action)

def create_ex_04a(status):
    if status == 1:
        reps = 2
        pause = 10
        repetition = 4
    else:
        reps = 3
        pause = 6
        repetition = 5
    
    ex_name = "#4a Special Strength: Hold pull-out position"
    explanation = "Full extension -> tilt down (front) and up (back) {}x while maintaining extension position, {} sec rest -> {} repetitions".format(reps, pause, repetition)
    advice = "Tilt your upper body down (forward) and up (backward) in full extension without an arrow in the bow.\n \
        Make sure that the 'T-position' remains constant and stable and that the shoulders remain at the same height."
    part1 = "Tilt down (forward)."
    part2 = "Tilt up (backward)."
    action = "Get into draw position."

    return Exercise_Reps(ex_name, reps, part1, part2, pause, repetition,explanation, advice, action)

# EXECUTION
ex_03 = create_ex_03(status)
ex_03.printouts()

time.sleep(3)
ex_04 = create_ex_04a(status)
ex_04.printouts()