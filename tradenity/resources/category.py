# coding: utf-8

"""
    Tradenity API

    Tradenity eCommerce Rest API

    Contact: support@tradenity.com

"""


from __future__ import absolute_import

import re
import pprint

# python 2 and python 3 compatibility library
import six

from tradenity.api_client import ApiClient


class Category(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'status': 'str',
        'description': 'str',
        'photo': 'Photo',
        'depth': 'int',
        'position': 'int',
        'parent_category': 'Category'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'status': 'status',
        'description': 'description',
        'photo': 'photo',
        'depth': 'depth',
        'position': 'position',
        'parent_category': 'parentCategory'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, status=None, description=None, photo=None, depth=None, position=None, parent_category=None):
        """Category - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._status = None
        self._description = None
        self._photo = None
        self._depth = None
        self._position = None
        self._parent_category = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        self.status = status
        if description is not None:
            self.description = description
        if photo is not None:
            self.photo = photo
        if depth is not None:
            self.depth = depth
        if position is not None:
            self.position = position
        if parent_category is not None:
            self.parent_category = parent_category

    @property
    def id(self):
        if self._id:
            return self._id
        elif self.meta is None:
            return None
        else:
            self._id = self.meta.href.split("/")[-1]
            return self._id

    @id.setter
    def id(self, new_id):
        self._id = new_id

    @property
    def meta(self):
        """Gets the meta of this Category.


        :return: The meta of this Category.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Category.


        :param meta: The meta of this Category.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Category.


        :return: The name of this Category.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Category.


        :param name: The name of this Category.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Category.


        :return: The slug of this Category.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Category.


        :param slug: The slug of this Category.
        :type: str
        """

        self._slug = slug

    @property
    def status(self):
        """Gets the status of this Category.


        :return: The status of this Category.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Category.


        :param status: The status of this Category.
        :type: str
        """
        allowed_values = ["enabled", "disabled"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

    @property
    def description(self):
        """Gets the description of this Category.


        :return: The description of this Category.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Category.


        :param description: The description of this Category.
        :type: str
        """

        self._description = description

    @property
    def photo(self):
        """Gets the photo of this Category.


        :return: The photo of this Category.
        :rtype: Photo
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """Sets the photo of this Category.


        :param photo: The photo of this Category.
        :type: Photo
        """

        self._photo = photo

    @property
    def depth(self):
        """Gets the depth of this Category.


        :return: The depth of this Category.
        :rtype: int
        """
        return self._depth

    @depth.setter
    def depth(self, depth):
        """Sets the depth of this Category.


        :param depth: The depth of this Category.
        :type: int
        """

        self._depth = depth

    @property
    def position(self):
        """Gets the position of this Category.


        :return: The position of this Category.
        :rtype: int
        """
        return self._position

    @position.setter
    def position(self, position):
        """Sets the position of this Category.


        :param position: The position of this Category.
        :type: int
        """

        self._position = position

    @property
    def parent_category(self):
        """Gets the parent_category of this Category.


        :return: The parent_category of this Category.
        :rtype: Category
        """
        return self._parent_category

    @parent_category.setter
    def parent_category(self, parent_category):
        """Sets the parent_category of this Category.


        :param parent_category: The parent_category of this Category.
        :type: Category
        """

        self._parent_category = parent_category

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Category, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Category):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other

    @classmethod
    def get_api_client(cls):
        if cls.api_client is None:
            cls.api_client = ApiClient.instance()
        return cls.api_client


    @classmethod
    def find_all(cls, **kwargs):
        return cls.list_all_categories(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_categories(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_categories(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_category_by_id(id)

    def create(self):
        new_instance = self.create_category(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_category_by_id(self.id, self)

    def delete(self):
        return self.delete_category_by_id(self.id)



    @classmethod
    def create_category(cls, category, **kwargs):
        """Create Category

        Create a new Category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_category(category, async=True)
        >>> result = thread.get()

        :param async bool
        :param Category category: Attributes of category to create (required)
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_category_with_http_info(category, **kwargs)
        else:
            (data) = cls._create_category_with_http_info(category, **kwargs)
            return data

    @classmethod
    def _create_category_with_http_info(cls, category, **kwargs):
        """Create Category

        Create a new Category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_category_with_http_info(category, async=True)
        >>> result = thread.get()

        :param async bool
        :param Category category: Attributes of category to create (required)
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category' is set
        if ('category' not in params or
                params['category'] is None):
            raise ValueError("Missing the required parameter `category` when calling `create_category`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'category' in params:
            body_params = params['category']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/categories', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Category',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_category_by_id(cls, category_id, **kwargs):
        """Delete Category

        Delete an instance of Category by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_category_by_id(category_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str category_id: ID of category to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_category_by_id_with_http_info(category_id, **kwargs)
        else:
            (data) = cls._delete_category_by_id_with_http_info(category_id, **kwargs)
            return data

    @classmethod
    def _delete_category_by_id_with_http_info(cls, category_id, **kwargs):
        """Delete Category

        Delete an instance of Category by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_category_by_id_with_http_info(category_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str category_id: ID of category to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `delete_category_by_id`")

        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/categories/{categoryId}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def get_category_by_id(cls, category_id, **kwargs):
        """Find Category

        Return single instance of Category by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_category_by_id(category_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str category_id: ID of category to return (required)
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_category_by_id_with_http_info(category_id, **kwargs)
        else:
            (data) = cls._get_category_by_id_with_http_info(category_id, **kwargs)
            return data

    @classmethod
    def _get_category_by_id_with_http_info(cls, category_id, **kwargs):
        """Find Category

        Return single instance of Category by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_category_by_id_with_http_info(category_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str category_id: ID of category to return (required)
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `get_category_by_id`")

        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/categories/{categoryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Category',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_categories(cls, **kwargs):
        """List Categories

        Return a list of Categories
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_categories(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Category]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_categories_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_categories_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_categories_with_http_info(cls, **kwargs):
        """List Categories

        Return a list of Categories
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_categories_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Category]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['page', 'size', 'sort']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        if 'page' in params:
            query_params.append(('page', params['page']))
        if 'size' in params:
            query_params.append(('size', params['size']))
        if 'sort' in params:
            query_params.append(('sort', params['sort']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/categories', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Category]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_category_by_id(cls, category_id, category, **kwargs):
        """Replace Category

        Replace all attributes of Category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_category_by_id(category_id, category, async=True)
        >>> result = thread.get()

        :param async bool
        :param str category_id: ID of category to replace (required)
        :param Category category: Attributes of category to replace (required)
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_category_by_id_with_http_info(category_id, category, **kwargs)
        else:
            (data) = cls._replace_category_by_id_with_http_info(category_id, category, **kwargs)
            return data

    @classmethod
    def _replace_category_by_id_with_http_info(cls, category_id, category, **kwargs):
        """Replace Category

        Replace all attributes of Category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_category_by_id_with_http_info(category_id, category, async=True)
        >>> result = thread.get()

        :param async bool
        :param str category_id: ID of category to replace (required)
        :param Category category: Attributes of category to replace (required)
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'category']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `replace_category_by_id`")
        # verify the required parameter 'category' is set
        if ('category' not in params or
                params['category'] is None):
            raise ValueError("Missing the required parameter `category` when calling `replace_category_by_id`")

        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'category' in params:
            body_params = params['category']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/categories/{categoryId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Category',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_category_by_id(cls, category_id, category, **kwargs):
        """Update Category

        Update attributes of Category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_category_by_id(category_id, category, async=True)
        >>> result = thread.get()

        :param async bool
        :param str category_id: ID of category to update. (required)
        :param Category category: Attributes of category to update. (required)
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_category_by_id_with_http_info(category_id, category, **kwargs)
        else:
            (data) = cls._update_category_by_id_with_http_info(category_id, category, **kwargs)
            return data

    @classmethod
    def _update_category_by_id_with_http_info(cls, category_id, category, **kwargs):
        """Update Category

        Update attributes of Category
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_category_by_id_with_http_info(category_id, category, async=True)
        >>> result = thread.get()

        :param async bool
        :param str category_id: ID of category to update. (required)
        :param Category category: Attributes of category to update. (required)
        :return: Category
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['category_id', 'category']
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        query_params = []

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                query_params.append((key, val))
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'category_id' is set
        if ('category_id' not in params or
                params['category_id'] is None):
            raise ValueError("Missing the required parameter `category_id` when calling `update_category_by_id`")
        # verify the required parameter 'category' is set
        if ('category' not in params or
                params['category'] is None):
            raise ValueError("Missing the required parameter `category` when calling `update_category_by_id`")

        collection_formats = {}

        path_params = {}
        if 'category_id' in params:
            path_params['categoryId'] = params['category_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'category' in params:
            body_params = params['category']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/categories/{categoryId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Category',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
