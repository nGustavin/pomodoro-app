import time
import notify2

interval = 60 * 25

iconPath = '/home/heroesz/gpm-ups-000-charging.svg'

notify2.init("Pomodoro App")

n = notify2.Notification(None, icon = iconPath)

n.set_urgency(notify2.URGENCY_NORMAL)

n.set_timeout(10000)

def pomodoro():

    n.update('Stating Pomodoro in 10 seconds',
    'See you in 25 minutes!, remember, to this works you should not be able to distract yourself or get off your task from the next 25 minutes')

    n.show()

    time.sleep(10)

    n.update('Start, lets go!')

    n.show()

    time.sleep(interval)

    n.update('Finishing up!', 'You finish that job, go take some air, walk a little bit, get the eyes off the screen, in five minutes come back to work')

    n.show()

    time.sleep(300)


while True:
    pomodoro()

