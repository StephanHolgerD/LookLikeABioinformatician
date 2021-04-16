import shutil
import random
from time import sleep

size=shutil.get_terminal_size((80, 20))


#green \u001b[32m
#print(dir(size))
#\u001b[33m
#blue \u001b[34m
randHighlight=[0]*50+[1]*5
print('\n')
nucs=["\u001b[31mA\u001b[1m", "\u001b[33mC\u001b[1m", "\u001b[34mT\u001b[1m" , "\u001b[32mG\u001b[1m"]

nucsH=["\u001b[47;1m\u001b[31mA\u001b[0m", "\u001b[47;1m\u001b[33mC\u001b[0m", "\u001b[47;1m\u001b[34mT\u001b[0m" , "\u001b[47;1m\u001b[32mG\u001b[0m"]+75*["\u001b[31mA\u001b[1m", "\u001b[33mC\u001b[1m", "\u001b[34mT\u001b[1m" , "\u001b[32mG\u001b[1m"]

while True:
    if size != shutil.get_terminal_size((80, 20)):
        size = shutil.get_terminal_size((80, 20))
        print('\n')
    sleep(0.5)
    if random.choice(randHighlight)==0:
        print(''.join([random.choice(nucs) for x in range(size.columns)]))
    else:
        print(''.join([random.choice(nucsH) for x in range(size.columns)]))
