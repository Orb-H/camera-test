from model_manager.model_info import ModelInfo


class ModelLoader(object):
    models = []

    # Singleton
    def __new__(cls):
        if not hasattr(cls, "_instance"):
            cls._instance = object.__new__(cls)
        return cls._instance

    def load_model(self, path, pos=None, rot=None, scale=None):
        mi = ModelInfo(pos, rot, scale)
        f = open(path)
        content = f.readlines()

        for item in content:
            data = item.split(" ")
            if item.startswith("v "):
                mi.add_vertex(data[1:])
            elif item.startswith("vn "):
                mi.add_normal_vector(data[1:])
            elif item.startswith("f "):
                mi.add_face(data[1:])
        self.models.append(mi)
