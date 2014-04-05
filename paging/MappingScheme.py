class MappingScheme(object):
    def __init__(self, *hierarchy):
        self.hierarchy = hierarchy

    def page_base(self, vaddr):
        page = self.hierarchy[-1]
        return vaddr - vaddr % page.size

    def page_table_base(self, level, vaddr):
        if level >= len(self.hierarchy) - 1:
            raise Exception('invalid page table level %d' % level)
        coverage = self.hierarchy[0].vmsize
        i = 0
        base = 0
        while True:
            if i == level:
                return base
            segment_sz = coverage / self.hierarchy[i].entries
            segment = vaddr / segment_sz
            vaddr = vaddr % segment_sz
            coverage = coverage / segment_sz
            base += segment * coverage
            i += 1
        pass

    def page_table_index(self, level, vaddr):
        if level >= len(self.hierarchy) - 1:
            raise Exception('invalid page table level %d' % level)
        coverage = self.hierarchy[0].vmsize
        i = 0
        segment = 0
        while True:
            if i == level:
                return segment
            segment_sz = coverage / self.hierarchy[i].entries
            segment = vaddr / segment_sz
            vaddr = vaddr % segment_sz
            coverage = coverage / segment_sz
            i += 1
