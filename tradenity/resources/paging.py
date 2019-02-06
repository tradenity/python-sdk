class PageRequest(object):
    def __init__(self, page=0, size=10, sort=None):
        self.page = page
        self.size = size
        self.sort = sort

    def to_dict(self):
        d = dict(page=self.page, size=self.size)
        if self.sort:
            d["sort"] = self.sort
        return d

class PageInfo(object):
    def __init__(self, href=None, total_pages=1, total_elements=0, page_number=0, page_size=10, number_of_elements=0):
        self.href = href
        self.total_pages = total_pages
        self.total_elements = total_elements
        self.page_number = page_number
        self.page_size = page_size
        self.number_of_elements = number_of_elements


class Page(object):
    def __init__(self, items, page_info=None):
        self.items = items or []
        self.page_info = page_info


    def is_empty(self):
        return len(self.items) <= 0

    def __len__(self):
        return self.items.__len__()

    def __getitem__(self, key):
        return self.items[key]

    def __iter__(self):
        return self.items.__iter__()