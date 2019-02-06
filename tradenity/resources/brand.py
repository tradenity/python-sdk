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


class Brand(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'status': 'str',
        'description': 'str',
        'photo': 'Photo'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'status': 'status',
        'description': 'description',
        'photo': 'photo'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, status=None, description=None, photo=None):
        """Brand - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._status = None
        self._description = None
        self._photo = None
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
        """Gets the meta of this Brand.


        :return: The meta of this Brand.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Brand.


        :param meta: The meta of this Brand.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Brand.


        :return: The name of this Brand.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Brand.


        :param name: The name of this Brand.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this Brand.


        :return: The slug of this Brand.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this Brand.


        :param slug: The slug of this Brand.
        :type: str
        """

        self._slug = slug

    @property
    def status(self):
        """Gets the status of this Brand.


        :return: The status of this Brand.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Brand.


        :param status: The status of this Brand.
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
        """Gets the description of this Brand.


        :return: The description of this Brand.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Brand.


        :param description: The description of this Brand.
        :type: str
        """

        self._description = description

    @property
    def photo(self):
        """Gets the photo of this Brand.


        :return: The photo of this Brand.
        :rtype: Photo
        """
        return self._photo

    @photo.setter
    def photo(self, photo):
        """Sets the photo of this Brand.


        :param photo: The photo of this Brand.
        :type: Photo
        """

        self._photo = photo

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
        if issubclass(Brand, dict):
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
        if not isinstance(other, Brand):
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
        return cls.list_all_brands(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_brands(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_brands(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_brand_by_id(id)

    def create(self):
        new_instance = self.create_brand(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_brand_by_id(self.id, self)

    def delete(self):
        return self.delete_brand_by_id(self.id)



    @classmethod
    def create_brand(cls, brand, **kwargs):
        """Create Brand

        Create a new Brand
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_brand(brand, async=True)
        >>> result = thread.get()

        :param async bool
        :param Brand brand: Attributes of brand to create (required)
        :return: Brand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_brand_with_http_info(brand, **kwargs)
        else:
            (data) = cls._create_brand_with_http_info(brand, **kwargs)
            return data

    @classmethod
    def _create_brand_with_http_info(cls, brand, **kwargs):
        """Create Brand

        Create a new Brand
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_brand_with_http_info(brand, async=True)
        >>> result = thread.get()

        :param async bool
        :param Brand brand: Attributes of brand to create (required)
        :return: Brand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['brand']
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
        # verify the required parameter 'brand' is set
        if ('brand' not in params or
                params['brand'] is None):
            raise ValueError("Missing the required parameter `brand` when calling `create_brand`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'brand' in params:
            body_params = params['brand']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/brands', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Brand',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_brand_by_id(cls, brand_id, **kwargs):
        """Delete Brand

        Delete an instance of Brand by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_brand_by_id(brand_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: ID of brand to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_brand_by_id_with_http_info(brand_id, **kwargs)
        else:
            (data) = cls._delete_brand_by_id_with_http_info(brand_id, **kwargs)
            return data

    @classmethod
    def _delete_brand_by_id_with_http_info(cls, brand_id, **kwargs):
        """Delete Brand

        Delete an instance of Brand by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_brand_by_id_with_http_info(brand_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: ID of brand to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['brand_id']
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
        # verify the required parameter 'brand_id' is set
        if ('brand_id' not in params or
                params['brand_id'] is None):
            raise ValueError("Missing the required parameter `brand_id` when calling `delete_brand_by_id`")

        collection_formats = {}

        path_params = {}
        if 'brand_id' in params:
            path_params['brandId'] = params['brand_id']


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
            '/brands/{brandId}', 'DELETE',
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
    def get_brand_by_id(cls, brand_id, **kwargs):
        """Find Brand

        Return single instance of Brand by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_brand_by_id(brand_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: ID of brand to return (required)
        :return: Brand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_brand_by_id_with_http_info(brand_id, **kwargs)
        else:
            (data) = cls._get_brand_by_id_with_http_info(brand_id, **kwargs)
            return data

    @classmethod
    def _get_brand_by_id_with_http_info(cls, brand_id, **kwargs):
        """Find Brand

        Return single instance of Brand by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_brand_by_id_with_http_info(brand_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: ID of brand to return (required)
        :return: Brand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['brand_id']
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
        # verify the required parameter 'brand_id' is set
        if ('brand_id' not in params or
                params['brand_id'] is None):
            raise ValueError("Missing the required parameter `brand_id` when calling `get_brand_by_id`")

        collection_formats = {}

        path_params = {}
        if 'brand_id' in params:
            path_params['brandId'] = params['brand_id']


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
            '/brands/{brandId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Brand',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_brands(cls, **kwargs):
        """List Brands

        Return a list of Brands
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_brands(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Brand]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_brands_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_brands_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_brands_with_http_info(cls, **kwargs):
        """List Brands

        Return a list of Brands
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_brands_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Brand]
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
            '/brands', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Brand]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_brand_by_id(cls, brand_id, brand, **kwargs):
        """Replace Brand

        Replace all attributes of Brand
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_brand_by_id(brand_id, brand, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: ID of brand to replace (required)
        :param Brand brand: Attributes of brand to replace (required)
        :return: Brand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_brand_by_id_with_http_info(brand_id, brand, **kwargs)
        else:
            (data) = cls._replace_brand_by_id_with_http_info(brand_id, brand, **kwargs)
            return data

    @classmethod
    def _replace_brand_by_id_with_http_info(cls, brand_id, brand, **kwargs):
        """Replace Brand

        Replace all attributes of Brand
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_brand_by_id_with_http_info(brand_id, brand, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: ID of brand to replace (required)
        :param Brand brand: Attributes of brand to replace (required)
        :return: Brand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['brand_id', 'brand']
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
        # verify the required parameter 'brand_id' is set
        if ('brand_id' not in params or
                params['brand_id'] is None):
            raise ValueError("Missing the required parameter `brand_id` when calling `replace_brand_by_id`")
        # verify the required parameter 'brand' is set
        if ('brand' not in params or
                params['brand'] is None):
            raise ValueError("Missing the required parameter `brand` when calling `replace_brand_by_id`")

        collection_formats = {}

        path_params = {}
        if 'brand_id' in params:
            path_params['brandId'] = params['brand_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'brand' in params:
            body_params = params['brand']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/brands/{brandId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Brand',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_brand_by_id(cls, brand_id, brand, **kwargs):
        """Update Brand

        Update attributes of Brand
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_brand_by_id(brand_id, brand, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: ID of brand to update. (required)
        :param Brand brand: Attributes of brand to update. (required)
        :return: Brand
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_brand_by_id_with_http_info(brand_id, brand, **kwargs)
        else:
            (data) = cls._update_brand_by_id_with_http_info(brand_id, brand, **kwargs)
            return data

    @classmethod
    def _update_brand_by_id_with_http_info(cls, brand_id, brand, **kwargs):
        """Update Brand

        Update attributes of Brand
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_brand_by_id_with_http_info(brand_id, brand, async=True)
        >>> result = thread.get()

        :param async bool
        :param str brand_id: ID of brand to update. (required)
        :param Brand brand: Attributes of brand to update. (required)
        :return: Brand
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['brand_id', 'brand']
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
        # verify the required parameter 'brand_id' is set
        if ('brand_id' not in params or
                params['brand_id'] is None):
            raise ValueError("Missing the required parameter `brand_id` when calling `update_brand_by_id`")
        # verify the required parameter 'brand' is set
        if ('brand' not in params or
                params['brand'] is None):
            raise ValueError("Missing the required parameter `brand` when calling `update_brand_by_id`")

        collection_formats = {}

        path_params = {}
        if 'brand_id' in params:
            path_params['brandId'] = params['brand_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'brand' in params:
            body_params = params['brand']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/brands/{brandId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Brand',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
