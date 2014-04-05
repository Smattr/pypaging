from Page import Page
from PageTable import PageTable
from PageDirectory import PageDirectory
from PagingScheme import PagingScheme
from MappingScheme import MappingScheme

KB = 1024
MB = 1024 * KB
GB = 1024 * MB
TB = 1024 * GB

page4k = Page(4 * KB)
page4m = Page(4 * MB)
pt = PageTable(4 * KB, 1024)
pd = PageTable(4 * KB, 1024)
ia32 = PagingScheme(4 * GB,
    MappingScheme(pd, pt, page4k),
    MappingScheme(pd, page4m))

page2m = Page(2 * MB)
pt = PageTable(4 * KB, 512)
pd = PageTable(4 * KB, 512)
pd_index = PageTable(128, 4)
pae = PagingScheme(4 * GB,
    MappingScheme(pd_index, pd, pt, page4k),
    MappingScheme(pd_index, pd, page2m))

page1g = Page(1 * GB)
pd_index = PageTable(2 * KB, 512)
pd = PageTable(4 * KB, 512)
pt1 = PageTable(4 * KB, 512)
pt2 = PageTable(4 * KB, 512)
x86_64 = PagingScheme(256 * TB,
    MappingScheme(pd_index, pd, pt1, pt2, page4k),
    MappingScheme(pd_index, pd, pt1, page2m),
    MappingScheme(pd_index, pd, page1g))

page = Page(4 * KB)
large_page = Page(64 * KB)
section = Page(1 * MB)
super_section = Page(16 * MB)
pt = PageTable(1 * KB, 256)
pds = map(lambda x: PageTable(x, x / 4), list(reversed(range(7, 15))))
schemes = []
for pd in pds:
    schemes += [
        MappingScheme(pd, pt, page),
        MappingScheme(pd, pt, large_page),
        MappingScheme(pd, section),
        MappingScheme(pd, super_section),
    ]
arm = PagingScheme(4 * GB, *schemes)
