import sys
from subprocess import Popen

class Echoer:
    def __init__(self, echostr):
        self.echostr = echostr
        self.subprocess = None

    def gimme(self):
        if self.subprocess is not None:
            return self.subprocess.communicate()
        else:
            return 'no'

    def __enter__(self):
        # An exception here will propagate to the caller, and the exception
        # should be provided to __exit__.
        self.subprocess = Popen(['echo', self.echostr])
        self.subprocess.__enter__()
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        try:
            if exc_type is not None and exc_value is None and traceback is None:
                if self.subprocess is None:
                    print('You __exit__ed without __enter__ing. Knock that off.')
            # Leave the exception alone to let it propagate, or handle it and
            # return True to suppress it.
        finally:
            # But make sure to clean up the subprocess too. Will we get a double exception here?
            if self.subprocess is not None:
                return self.subprocess.__exit__(exc_type, exc_value, traceback)

# Example usage:
if __name__ == '__main__':
    with Echoer(sys.argv[1]) as output:
        print(output.gimme())