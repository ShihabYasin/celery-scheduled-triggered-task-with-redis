import random
import time
import runner
import datetime

if __name__ == '__main__':
    for idx, trigger_task in enumerate(range(10)):
        print(f"Sending Triggered Task no: {idx}")
        runner.triggered_task.delay(datetime.datetime.now())
        time.sleep(float(random.randint(1,8))) # Simulating trigger task
