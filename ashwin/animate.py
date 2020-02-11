import threading
import time


def animate(start, end, func, args, frames, slep=0):
    '''runs a function with each specified value in the given range'''
    def anim(start, end, func, args, frames, slep=0):
        diff = []
        inc = []

        for f in range(len(start)):
            diff.append(end[f] - start[f])


        '''for f in range(len(start)):
            if start[f] < end[f]:
                sign.append(1)
            else:
                sign.append(-1)'''

        for l in range(frames):
            for i in diff:
                inc.append(i/frames)

            for c,i in enumerate(start):
                #start[c] = i + (sign[c] * inc[c])
                start[c] = i + inc[c]
                print(start)
            
            func(*args, start)
            time.sleep(slep)
    
    anim_handler = threading.Thread(target=anim, args=(start, end, func, args, frames, slep))
    anim_handler.run()
