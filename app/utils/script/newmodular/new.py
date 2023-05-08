import os


class NewViewModular:
    def __init__(self, name):
        self.name = name

    # 判断当前是否是否已经存在
    def path_is_exists(self):
        return os.path.exists(f"app/views/{self.name.split('/')[0]}")



