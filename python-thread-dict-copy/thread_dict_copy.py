#!/usr/bin/env python3

import threading
import time

class ThingPrinter:
    def __init__(self, thing):
        self.thing = thing
        print(f"ThingPrinter's initial thing is {self.thing} at {id(self.thing)}")
    
    def run(self):
        while True:
            print(f"ThingPrinter contains {self.thing} at {id(self.thing)}")
            time.sleep(1)

    def update_the_thing(self, thing):
        self.thing = thing
    

class ThingUpdater:
    def __init__(self, thing, iterations, printer=None):
        self.thing = thing
        self.iterations = iterations
        self.printer = printer
        print(f"ThingUpdater's initial thing is {self.thing} at {id(self.thing)}")

    def run(self):
        for i in range(self.iterations):
            self.thing = {i: "it me"}
            print(f"ThingUpdater contains {self.thing} at {id(self.thing)}")
            if self.printer:
                self.printer.update_the_thing(self.thing)
            time.sleep(1)

    def join(self):
        self.update_thread.join()

if __name__ == "__main__":
    thing = {}
    printer = ThingPrinter(thing)
    updater = ThingUpdater(thing, 5, printer)

    print(f"Initial thing is {thing} at {id(thing)}")
    update_thread = threading.Thread(target=updater.run)
    update_thread.start()

    print_thread = threading.Thread(target=printer.run, daemon=True)
    print_thread.start()
    
    update_thread.join()