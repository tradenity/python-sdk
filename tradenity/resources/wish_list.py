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


class WishList(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'description': 'str',
        'products': 'list[Product]',
        'customer': 'Customer'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'description': 'description',
        'products': 'products',
        'customer': 'customer'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, description=None, products=None, customer=None):
        """WishList - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._description = None
        self._products = None
        self._customer = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        if description is not None:
            self.description = description
        if products is not None:
            self.products = products
        self.customer = customer

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
        """Gets the meta of this WishList.


        :return: The meta of this WishList.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this WishList.


        :param meta: The meta of this WishList.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this WishList.


        :return: The name of this WishList.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WishList.


        :param name: The name of this WishList.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this WishList.


        :return: The description of this WishList.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WishList.


        :param description: The description of this WishList.
        :type: str
        """

        self._description = description

    @property
    def products(self):
        """Gets the products of this WishList.


        :return: The products of this WishList.
        :rtype: list[Product]
        """
        return self._products

    @products.setter
    def products(self, products):
        """Sets the products of this WishList.


        :param products: The products of this WishList.
        :type: list[Product]
        """

        self._products = products

    @property
    def customer(self):
        """Gets the customer of this WishList.


        :return: The customer of this WishList.
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this WishList.


        :param customer: The customer of this WishList.
        :type: Customer
        """

        self._customer = customer

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
        if issubclass(WishList, dict):
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
        if not isinstance(other, WishList):
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
    def find_all(cls, page_request=None):
        return cls.list_all_wish_lists()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_wish_lists(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_wish_lists(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_wish_list_by_id(id)

    def create(self):
        new_instance = self.create_wish_list(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_wish_list_by_id(self.id, self)

    def delete(self):
        return self.delete_wish_list_by_id(self.id)



    @classmethod
    def create_wish_list(cls, wish_list, **kwargs):
        """Create WishList

        Create a new WishList
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_wish_list(wish_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param WishList wish_list: Attributes of wishList to create (required)
        :return: WishList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_wish_list_with_http_info(wish_list, **kwargs)
        else:
            (data) = cls._create_wish_list_with_http_info(wish_list, **kwargs)
            return data

    @classmethod
    def _create_wish_list_with_http_info(cls, wish_list, **kwargs):
        """Create WishList

        Create a new WishList
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_wish_list_with_http_info(wish_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param WishList wish_list: Attributes of wishList to create (required)
        :return: WishList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wish_list']
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
        # verify the required parameter 'wish_list' is set
        if ('wish_list' not in params or
                params['wish_list'] is None):
            raise ValueError("Missing the required parameter `wish_list` when calling `create_wish_list`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'wish_list' in params:
            body_params = params['wish_list']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/wishLists', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WishList',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_wish_list_by_id(cls, wish_list_id, **kwargs):
        """Delete WishList

        Delete an instance of WishList by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_wish_list_by_id(wish_list_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wish_list_id: ID of wishList to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_wish_list_by_id_with_http_info(wish_list_id, **kwargs)
        else:
            (data) = cls._delete_wish_list_by_id_with_http_info(wish_list_id, **kwargs)
            return data

    @classmethod
    def _delete_wish_list_by_id_with_http_info(cls, wish_list_id, **kwargs):
        """Delete WishList

        Delete an instance of WishList by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_wish_list_by_id_with_http_info(wish_list_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wish_list_id: ID of wishList to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wish_list_id']
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
        # verify the required parameter 'wish_list_id' is set
        if ('wish_list_id' not in params or
                params['wish_list_id'] is None):
            raise ValueError("Missing the required parameter `wish_list_id` when calling `delete_wish_list_by_id`")

        collection_formats = {}

        path_params = {}
        if 'wish_list_id' in params:
            path_params['wishListId'] = params['wish_list_id']


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
            '/wishLists/{wishListId}', 'DELETE',
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
    def get_wish_list_by_id(cls, wish_list_id, **kwargs):
        """Find WishList

        Return single instance of WishList by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wish_list_by_id(wish_list_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wish_list_id: ID of wishList to return (required)
        :return: WishList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_wish_list_by_id_with_http_info(wish_list_id, **kwargs)
        else:
            (data) = cls._get_wish_list_by_id_with_http_info(wish_list_id, **kwargs)
            return data

    @classmethod
    def _get_wish_list_by_id_with_http_info(cls, wish_list_id, **kwargs):
        """Find WishList

        Return single instance of WishList by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_wish_list_by_id_with_http_info(wish_list_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wish_list_id: ID of wishList to return (required)
        :return: WishList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wish_list_id']
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
        # verify the required parameter 'wish_list_id' is set
        if ('wish_list_id' not in params or
                params['wish_list_id'] is None):
            raise ValueError("Missing the required parameter `wish_list_id` when calling `get_wish_list_by_id`")

        collection_formats = {}

        path_params = {}
        if 'wish_list_id' in params:
            path_params['wishListId'] = params['wish_list_id']


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
            '/wishLists/{wishListId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WishList',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_wish_lists(cls, **kwargs):
        """List WishLists

        Return a list of WishLists
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_wish_lists(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[WishList]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_wish_lists_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_wish_lists_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_wish_lists_with_http_info(cls, **kwargs):
        """List WishLists

        Return a list of WishLists
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_wish_lists_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[WishList]
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
            '/wishLists', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[WishList]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_wish_list_by_id(cls, wish_list_id, wish_list, **kwargs):
        """Replace WishList

        Replace all attributes of WishList
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_wish_list_by_id(wish_list_id, wish_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wish_list_id: ID of wishList to replace (required)
        :param WishList wish_list: Attributes of wishList to replace (required)
        :return: WishList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_wish_list_by_id_with_http_info(wish_list_id, wish_list, **kwargs)
        else:
            (data) = cls._replace_wish_list_by_id_with_http_info(wish_list_id, wish_list, **kwargs)
            return data

    @classmethod
    def _replace_wish_list_by_id_with_http_info(cls, wish_list_id, wish_list, **kwargs):
        """Replace WishList

        Replace all attributes of WishList
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_wish_list_by_id_with_http_info(wish_list_id, wish_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wish_list_id: ID of wishList to replace (required)
        :param WishList wish_list: Attributes of wishList to replace (required)
        :return: WishList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wish_list_id', 'wish_list']
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
        # verify the required parameter 'wish_list_id' is set
        if ('wish_list_id' not in params or
                params['wish_list_id'] is None):
            raise ValueError("Missing the required parameter `wish_list_id` when calling `replace_wish_list_by_id`")
        # verify the required parameter 'wish_list' is set
        if ('wish_list' not in params or
                params['wish_list'] is None):
            raise ValueError("Missing the required parameter `wish_list` when calling `replace_wish_list_by_id`")

        collection_formats = {}

        path_params = {}
        if 'wish_list_id' in params:
            path_params['wishListId'] = params['wish_list_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'wish_list' in params:
            body_params = params['wish_list']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/wishLists/{wishListId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WishList',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_wish_list_by_id(cls, wish_list_id, wish_list, **kwargs):
        """Update WishList

        Update attributes of WishList
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_wish_list_by_id(wish_list_id, wish_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wish_list_id: ID of wishList to update. (required)
        :param WishList wish_list: Attributes of wishList to update. (required)
        :return: WishList
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_wish_list_by_id_with_http_info(wish_list_id, wish_list, **kwargs)
        else:
            (data) = cls._update_wish_list_by_id_with_http_info(wish_list_id, wish_list, **kwargs)
            return data

    @classmethod
    def _update_wish_list_by_id_with_http_info(cls, wish_list_id, wish_list, **kwargs):
        """Update WishList

        Update attributes of WishList
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_wish_list_by_id_with_http_info(wish_list_id, wish_list, async=True)
        >>> result = thread.get()

        :param async bool
        :param str wish_list_id: ID of wishList to update. (required)
        :param WishList wish_list: Attributes of wishList to update. (required)
        :return: WishList
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['wish_list_id', 'wish_list']
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
        # verify the required parameter 'wish_list_id' is set
        if ('wish_list_id' not in params or
                params['wish_list_id'] is None):
            raise ValueError("Missing the required parameter `wish_list_id` when calling `update_wish_list_by_id`")
        # verify the required parameter 'wish_list' is set
        if ('wish_list' not in params or
                params['wish_list'] is None):
            raise ValueError("Missing the required parameter `wish_list` when calling `update_wish_list_by_id`")

        collection_formats = {}

        path_params = {}
        if 'wish_list_id' in params:
            path_params['wishListId'] = params['wish_list_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'wish_list' in params:
            body_params = params['wish_list']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/wishLists/{wishListId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WishList',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
