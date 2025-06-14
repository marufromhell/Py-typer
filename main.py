import colorama
import os
import sys, tty, termios
import timeit


def starttime():
    """Starts the timer if ENABLE_TIMER is True."""
    global start_time
    start_time = timeit.default_timer()

elapsed_time=0 #same thing
def endtime():
    """Ends the timer and calculates elapsed time if ENABLE_TIMER is True."""
    global elapsed_time
    if start_time is not None:
        elapsed_time = round(timeit.default_timer() - start_time, 2)
        return elapsed_time
    else:
        elapsed_time = 0

class LowPrint:
    """Low level printing, requires newline at the end of string"""

    def __lt__(self, thing):
        try:
            sys.stdout.write(str(thing))
            sys.stdout.flush()
        except IOError as e:
            print(f"IO Error: {e}", file=sys.stderr)


lp = LowPrint()
lp< 'EOF to exit... '
class _GetchUnix:

    def __call__(self):
            fd = sys.stdin.fileno()
            old_settings = termios.tcgetattr(fd)
            try:
                tty.setraw(sys.stdin.fileno())
                ch = sys.stdin.read(1)
                if ch == '\x04':#eof char
                    lp<"Exit... "
            finally:
                termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
            return ch
        

getch = _GetchUnix()

def typer(sentence):
    os.system('clear')
    lp<sentence+'\n'
    typed = []
    incorrect = 0
    timer_started = False 

    for char in sentence:
        while True:
            a = getch()
            if not timer_started:
                starttime()  # idk how much latency this adds idrk
                timer_started = True

            if a == char:
                # success case
                typed.append(char)
                os.system('clear')
                lp < colorama.Fore.GREEN + ''.join(typed) + colorama.Style.RESET_ALL
                lp < ''.join(sentence[len(typed):])
                break
            else:
                # incorrect case
                os.system('clear')
                incorrect += 1
                lp < colorama.Fore.GREEN + ''.join(typed) + colorama.Style.RESET_ALL
                lp < colorama.Fore.RED + a + colorama.Style.RESET_ALL
                lp < ''.join(sentence[len(typed):])

    # End of typing session
    endtime()
    total_chars = len(sentence)
    correct_chars = len(typed) - incorrect
    acc = round((correct_chars / total_chars) * 100, 2)
    wpt = correct_chars / 5 # 5 char estimate
    wpm = round(wpt / (elapsed_time / 60), 2)
    return f"acc: {acc}%  wpm: {wpm}"

os.system('clear')
levels = [
    'The quick brown fox jumps over the lazy dog.',
    'The five boxing wizards jump quickly.',
    'Pack my box with five dozen liquor jugs.',
    'Go, lazy fat vixen; be shrewd, jump quick.',
    'Amazingly few discotheques provide jukeboxes.',
    'Watch \"Jeopardy!\", Alex Trebek\'s fun TV quiz game.'
]
results=[]
os.system('clear')
lp<'\n'
for level in levels:
    results.append(typer(level))
os.system('clear')
lp<'\n'
for result in results:
    lp<result+'\n'