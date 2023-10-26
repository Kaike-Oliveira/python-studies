# States

class Camera:
    def __init__(self, model, recording=False):
        self.model = model
        self.recording = recording

    def record(self):
        if self.recording:
            print(f'{self.model} already recording!')
            return

        print(f'{self.model} is recording')
        self.recording = True

    def take_picture(self):
        if self.recording:
            print(f'{self.model} can not record and take a picture!')
            return

        print(f'{self.model} took a picture!')


canon = Camera(model="Canon")
sony = Camera(model="Sony")
