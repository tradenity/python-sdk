from booby import Model

from tradenity.sdk import Tradenity
from.paging import Page, PageRequest


class BaseEntity(Model):
    RESOURCE_NAME = ''
    WRITABLE_FIELDS = []
    ALL_FIELDS = []

    @classmethod
    def client(cls):
        return Tradenity.get_client()

    @classmethod
    def base_url(cls):
        return Tradenity.END_POINT

    def __getitem__(self, k):
        # todo this is a temporary hack
        return getattr(self, k)

    @property
    def id(self):
        return self.get_id()

    def get_id(self):
        if hasattr(self, "_id") and self._id is not None:
            return self._id
        elif hasattr(self, "_links"):
            return self._get_id_from_links(self._links)

    @id.setter
    def id(self, value):
        self._id = value

    @classmethod
    def resource_base_path(cls):
        return "{base}/{res}".format(base=cls.base_url(), res=cls.RESOURCE_NAME)

    @classmethod
    def resource_path(cls, resource_id):
        return "{base}/{id}".format(base=cls.resource_base_path(), id=resource_id)

    @classmethod
    def _get_id_from_links(cls, links):
        if links is not None and "self" in links and "href" in links["self"]:
            href = links["self"]["href"]
            return href.split("/")[-1]

    @classmethod
    def _convert_to_page(cls, result):
        if "_embedded" in result:
            content = result["_embedded"][cls.RESOURCE_NAME]
            page_info = result["page"]
            list = []
            for e in content:
                links = e["_links"]
                del e["_links"]
                entity = cls(**e)
                entity.id = cls._get_id_from_links(links)
                list.append(entity)
            return Page(list, page_info["number"], page_info["size"])
        else:
            return Page([], 0, 0)

    @classmethod
    def find_all(cls, **kwargs):
        if kwargs is not None:
            page_request = kwargs.get('page_request', None)
            if page_request is not None and isinstance(page_request, PageRequest):
                page_request = kwargs['page_request']
                kwargs.update(page_request.to_dict())
        else:
            kwargs = dict()
        result = cls.client().get(cls.resource_base_path(), data=kwargs)
        return cls._convert_to_page(result.json())

    @classmethod
    def _search(cls, **kwargs):
        page_request = kwargs.get('page_request', None)
        if page_request is not None and isinstance(page_request, PageRequest):
            page_request = kwargs['page_request']
            kwargs.update(page_request.to_dict())
        result = cls.client().get(cls.resource_base_path(), data=kwargs)
        return cls._convert_to_page(result.json())

    @classmethod
    def find_by_id(cls, entity_id):
        result = cls.client().get(cls.resource_path(entity_id))
        return cls(**result.json())

    def as_dict(self, prefix=None):
        if prefix is None:
            return dict(self)
        else:
            return dict([("{p}{k}".format(p=prefix, k=k), v) for k, v in dict(self).items()])

    def _get_create_data(self):
        all_data = self.as_dict()
        return dict([(field, all_data[field]) for field in self.WRITABLE_FIELDS if field in all_data])

    def _get_update_data(self):
        all_data = self.as_dict()
        return dict([(field, all_data[field])
                     for field in self.WRITABLE_FIELDS
                     if field in all_data and all_data[field] is not None])

    def create(self):
        result = self.client().post(self.resource_base_path(), data=self._get_create_data())
        return self.__class__(**result.json())

    def update(self):
        result = self.client().put(self.resource_base_path(), data=self._get_update_data())
        return self.__class__(**result.json())

    def delete(self):
        result = self.client().post(self.resource_base_path(), self.to_json())
        return True

    def update_model(self, *args, **kwargs):
        self._update(dict(*args, **kwargs))




