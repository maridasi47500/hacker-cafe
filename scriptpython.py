import subprocess
class Scriptpython:
    def __init__(self,name=""):
        self.name=name
    def lancer(self):
        x=subprocess.check_output(["sh","./uploads/lancer_"+self.name+".sh"])
        return x

