color_reference = {1: 'red', 2: 'blue',3: 'yellow', 4: 'green', 5: 'purple'}

class MyDictKeyError(Exception):
    def __init__(self, key):
        self.key = key
    def __str__(self):
        return '辞書にkeyが登録されていません {0}'.format(self.key)

def 
