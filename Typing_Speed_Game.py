from time import time

def typingErrors(prompt):
    global iwords

    words = prompt.split()
    errors = 0

    for i in range(len(iwords)):
        if i in (0,len(iwords)-1):
            if iwords[i] == words[i]:
                continue
            else:
                errors +=1 
        else:
            if (iwords[i] == words[i]):
                if (iwords[i+1] == words[i+1]) & (iwords[i-1] == words[i-1]):
                    continue
                else:
                    errors +=1
            else:
                errors +=1
    return errors

def typingSpeed(iprompt,stime,etime):
    global time
    global iwords

    iword = iprompt.split()
    twords = len(iword)
    speed = twords/stime

    return speed

def timeElapsed(stime,etime):
    time = etime - stime
    return time

input("Press Enter when You are Ready!")
if __name__ == '__main__':
    prompt = "Python is best programming language"
    print("Type this :- '",prompt,"'")
    
    stime = time()
    iprompt = input()
    etime = time()

    time = round(timeElapsed(stime,etime),2)
    speed = typingSpeed(iprompt,stime,etime)
    errors = typingErrors(iprompt)

    print("Total Time Elapsed :- ",time,"s")
    print("Your Average Typing Spped wwas :- ",speed,"words/min")
    print("With Total of :- ",errors," errors")