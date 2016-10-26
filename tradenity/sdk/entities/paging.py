class Page(object):
    def __init__(self, content, page, size):
        self.content = content or []
        self.page_number = page
        self.page_size = size

    def __iter__(self):
        return self.content.__iter__()

    @property
    def first(self):
        if self.content is not None and len(self.content) > 0:
            return self.content[0]

    def is_empty(self):
        return self.content is None or len(self.content) <= 0


class PageRequest(object):
    def __init__(self, page=0, size=10):
        self.page_number = page
        self.page_size = size

    @classmethod
    def from_dict(cls, d):
        return cls(
            page=d.get("page", 0),
            size=d.get("size", 10)
        )

    def to_dict(self):
        return {"page": self.page_number, "size": self.page_size}
