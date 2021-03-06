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


class Address(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'street_line1': 'str',
        'street_line2': 'str',
        'city': 'str',
        'state': 'State',
        'zip_code': 'str',
        'country': 'Country'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'street_line1': 'streetLine1',
        'street_line2': 'streetLine2',
        'city': 'city',
        'state': 'state',
        'zip_code': 'zipCode',
        'country': 'country'
    }

    api_client = None

    def __init__(self, id=None, meta=None, street_line1=None, street_line2=None, city=None, state=None, zip_code=None, country=None):
        """Address - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._street_line1 = None
        self._street_line2 = None
        self._city = None
        self._state = None
        self._zip_code = None
        self._country = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.street_line1 = street_line1
        if street_line2 is not None:
            self.street_line2 = street_line2
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.country = country

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
        """Gets the meta of this Address.


        :return: The meta of this Address.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Address.


        :param meta: The meta of this Address.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def street_line1(self):
        """Gets the street_line1 of this Address.


        :return: The street_line1 of this Address.
        :rtype: str
        """
        return self._street_line1

    @street_line1.setter
    def street_line1(self, street_line1):
        """Sets the street_line1 of this Address.


        :param street_line1: The street_line1 of this Address.
        :type: str
        """

        self._street_line1 = street_line1

    @property
    def street_line2(self):
        """Gets the street_line2 of this Address.


        :return: The street_line2 of this Address.
        :rtype: str
        """
        return self._street_line2

    @street_line2.setter
    def street_line2(self, street_line2):
        """Sets the street_line2 of this Address.


        :param street_line2: The street_line2 of this Address.
        :type: str
        """

        self._street_line2 = street_line2

    @property
    def city(self):
        """Gets the city of this Address.


        :return: The city of this Address.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this Address.


        :param city: The city of this Address.
        :type: str
        """

        self._city = city

    @property
    def state(self):
        """Gets the state of this Address.


        :return: The state of this Address.
        :rtype: State
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Address.


        :param state: The state of this Address.
        :type: State
        """

        self._state = state

    @property
    def zip_code(self):
        """Gets the zip_code of this Address.


        :return: The zip_code of this Address.
        :rtype: str
        """
        return self._zip_code

    @zip_code.setter
    def zip_code(self, zip_code):
        """Sets the zip_code of this Address.


        :param zip_code: The zip_code of this Address.
        :type: str
        """

        self._zip_code = zip_code

    @property
    def country(self):
        """Gets the country of this Address.


        :return: The country of this Address.
        :rtype: Country
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this Address.


        :param country: The country of this Address.
        :type: Country
        """

        self._country = country

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
        if issubclass(Address, dict):
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
        if not isinstance(other, Address):
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
        return cls.list_all_addresses(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_addresses(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_addresses(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_address_by_id(id)

    def create(self):
        new_instance = self.create_address(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_address_by_id(self.id, self)

    def delete(self):
        return self.delete_address_by_id(self.id)



    @classmethod
    def create_address(cls, address, **kwargs):
        """Create Address

        Create a new Address
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_address(address, async=True)
        >>> result = thread.get()

        :param async bool
        :param Address address: Attributes of address to create (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_address_with_http_info(address, **kwargs)
        else:
            (data) = cls._create_address_with_http_info(address, **kwargs)
            return data

    @classmethod
    def _create_address_with_http_info(cls, address, **kwargs):
        """Create Address

        Create a new Address
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_address_with_http_info(address, async=True)
        >>> result = thread.get()

        :param async bool
        :param Address address: Attributes of address to create (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address']
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
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `create_address`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'address' in params:
            body_params = params['address']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/addresses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Address',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_address_by_id(cls, address_id, **kwargs):
        """Delete Address

        Delete an instance of Address by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_address_by_id(address_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address_id: ID of address to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_address_by_id_with_http_info(address_id, **kwargs)
        else:
            (data) = cls._delete_address_by_id_with_http_info(address_id, **kwargs)
            return data

    @classmethod
    def _delete_address_by_id_with_http_info(cls, address_id, **kwargs):
        """Delete Address

        Delete an instance of Address by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_address_by_id_with_http_info(address_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address_id: ID of address to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id']
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
        # verify the required parameter 'address_id' is set
        if ('address_id' not in params or
                params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `delete_address_by_id`")

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']


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
            '/addresses/{addressId}', 'DELETE',
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
    def get_address_by_id(cls, address_id, **kwargs):
        """Find Address

        Return single instance of Address by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_address_by_id(address_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address_id: ID of address to return (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_address_by_id_with_http_info(address_id, **kwargs)
        else:
            (data) = cls._get_address_by_id_with_http_info(address_id, **kwargs)
            return data

    @classmethod
    def _get_address_by_id_with_http_info(cls, address_id, **kwargs):
        """Find Address

        Return single instance of Address by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_address_by_id_with_http_info(address_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address_id: ID of address to return (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id']
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
        # verify the required parameter 'address_id' is set
        if ('address_id' not in params or
                params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `get_address_by_id`")

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']


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
            '/addresses/{addressId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Address',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_addresses(cls, **kwargs):
        """List Addresses

        Return a list of Addresses
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_addresses(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Address]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_addresses_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_addresses_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_addresses_with_http_info(cls, **kwargs):
        """List Addresses

        Return a list of Addresses
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_addresses_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Address]
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
            '/addresses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Address]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_address_by_id(cls, address_id, address, **kwargs):
        """Replace Address

        Replace all attributes of Address
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_address_by_id(address_id, address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address_id: ID of address to replace (required)
        :param Address address: Attributes of address to replace (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_address_by_id_with_http_info(address_id, address, **kwargs)
        else:
            (data) = cls._replace_address_by_id_with_http_info(address_id, address, **kwargs)
            return data

    @classmethod
    def _replace_address_by_id_with_http_info(cls, address_id, address, **kwargs):
        """Replace Address

        Replace all attributes of Address
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_address_by_id_with_http_info(address_id, address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address_id: ID of address to replace (required)
        :param Address address: Attributes of address to replace (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id', 'address']
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
        # verify the required parameter 'address_id' is set
        if ('address_id' not in params or
                params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `replace_address_by_id`")
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `replace_address_by_id`")

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'address' in params:
            body_params = params['address']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/addresses/{addressId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Address',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_address_by_id(cls, address_id, address, **kwargs):
        """Update Address

        Update attributes of Address
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_address_by_id(address_id, address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address_id: ID of address to update. (required)
        :param Address address: Attributes of address to update. (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_address_by_id_with_http_info(address_id, address, **kwargs)
        else:
            (data) = cls._update_address_by_id_with_http_info(address_id, address, **kwargs)
            return data

    @classmethod
    def _update_address_by_id_with_http_info(cls, address_id, address, **kwargs):
        """Update Address

        Update attributes of Address
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_address_by_id_with_http_info(address_id, address, async=True)
        >>> result = thread.get()

        :param async bool
        :param str address_id: ID of address to update. (required)
        :param Address address: Attributes of address to update. (required)
        :return: Address
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['address_id', 'address']
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
        # verify the required parameter 'address_id' is set
        if ('address_id' not in params or
                params['address_id'] is None):
            raise ValueError("Missing the required parameter `address_id` when calling `update_address_by_id`")
        # verify the required parameter 'address' is set
        if ('address' not in params or
                params['address'] is None):
            raise ValueError("Missing the required parameter `address` when calling `update_address_by_id`")

        collection_formats = {}

        path_params = {}
        if 'address_id' in params:
            path_params['addressId'] = params['address_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'address' in params:
            body_params = params['address']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/addresses/{addressId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Address',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
