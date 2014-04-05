class PagingScheme(object):
    def __init__(self, vmsize, *schemes):
        self.vmsize = vmsize
        self.schemes = schemes
