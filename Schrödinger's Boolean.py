class Omnibool(object):
    def __eq__(self, omni):
        return isinstance(omni, bool)
omnibool = Omnibool()
