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


class Country(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'iso2': 'str',
        'iso3': 'str',
        'iso3166': 'str',
        'country_code': 'str',
        'sub_region': 'str',
        'region': 'str',
        'status': 'str',
        'states': 'list[State]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'iso2': 'iso2',
        'iso3': 'iso3',
        'iso3166': 'iso3166',
        'country_code': 'countryCode',
        'sub_region': 'subRegion',
        'region': 'region',
        'status': 'status',
        'states': 'states'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, iso2=None, iso3=None, iso3166=None, country_code=None, sub_region=None, region=None, status=None, states=None):
        """Country - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._iso2 = None
        self._iso3 = None
        self._iso3166 = None
        self._country_code = None
        self._sub_region = None
        self._region = None
        self._status = None
        self._states = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.iso2 = iso2
        self.iso3 = iso3
        self.iso3166 = iso3166
        self.country_code = country_code
        self.sub_region = sub_region
        self.region = region
        self.status = status
        if states is not None:
            self.states = states

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
        """Gets the meta of this Country.


        :return: The meta of this Country.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this Country.


        :param meta: The meta of this Country.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this Country.


        :return: The name of this Country.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Country.


        :param name: The name of this Country.
        :type: str
        """

        self._name = name

    @property
    def iso2(self):
        """Gets the iso2 of this Country.


        :return: The iso2 of this Country.
        :rtype: str
        """
        return self._iso2

    @iso2.setter
    def iso2(self, iso2):
        """Sets the iso2 of this Country.


        :param iso2: The iso2 of this Country.
        :type: str
        """

        self._iso2 = iso2

    @property
    def iso3(self):
        """Gets the iso3 of this Country.


        :return: The iso3 of this Country.
        :rtype: str
        """
        return self._iso3

    @iso3.setter
    def iso3(self, iso3):
        """Sets the iso3 of this Country.


        :param iso3: The iso3 of this Country.
        :type: str
        """

        self._iso3 = iso3

    @property
    def iso3166(self):
        """Gets the iso3166 of this Country.


        :return: The iso3166 of this Country.
        :rtype: str
        """
        return self._iso3166

    @iso3166.setter
    def iso3166(self, iso3166):
        """Sets the iso3166 of this Country.


        :param iso3166: The iso3166 of this Country.
        :type: str
        """

        self._iso3166 = iso3166

    @property
    def country_code(self):
        """Gets the country_code of this Country.


        :return: The country_code of this Country.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this Country.


        :param country_code: The country_code of this Country.
        :type: str
        """

        self._country_code = country_code

    @property
    def sub_region(self):
        """Gets the sub_region of this Country.


        :return: The sub_region of this Country.
        :rtype: str
        """
        return self._sub_region

    @sub_region.setter
    def sub_region(self, sub_region):
        """Sets the sub_region of this Country.


        :param sub_region: The sub_region of this Country.
        :type: str
        """

        self._sub_region = sub_region

    @property
    def region(self):
        """Gets the region of this Country.


        :return: The region of this Country.
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this Country.


        :param region: The region of this Country.
        :type: str
        """

        self._region = region

    @property
    def status(self):
        """Gets the status of this Country.


        :return: The status of this Country.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this Country.


        :param status: The status of this Country.
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
    def states(self):
        """Gets the states of this Country.


        :return: The states of this Country.
        :rtype: list[State]
        """
        return self._states

    @states.setter
    def states(self, states):
        """Sets the states of this Country.


        :param states: The states of this Country.
        :type: list[State]
        """

        self._states = states

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
        if issubclass(Country, dict):
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
        if not isinstance(other, Country):
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
        return cls.list_all_countries(**kwargs)

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_countries(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_countries(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_country_by_id(id)

    def create(self):
        new_instance = self.create_country(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_country_by_id(self.id, self)

    def delete(self):
        return self.delete_country_by_id(self.id)



    @classmethod
    def create_country(cls, country, **kwargs):
        """Create Country

        Create a new Country
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_country(country, async=True)
        >>> result = thread.get()

        :param async bool
        :param Country country: Attributes of country to create (required)
        :return: Country
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_country_with_http_info(country, **kwargs)
        else:
            (data) = cls._create_country_with_http_info(country, **kwargs)
            return data

    @classmethod
    def _create_country_with_http_info(cls, country, **kwargs):
        """Create Country

        Create a new Country
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_country_with_http_info(country, async=True)
        >>> result = thread.get()

        :param async bool
        :param Country country: Attributes of country to create (required)
        :return: Country
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country']
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
        # verify the required parameter 'country' is set
        if ('country' not in params or
                params['country'] is None):
            raise ValueError("Missing the required parameter `country` when calling `create_country`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'country' in params:
            body_params = params['country']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/countries', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Country',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_country_by_id(cls, country_id, **kwargs):
        """Delete Country

        Delete an instance of Country by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_country_by_id(country_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_id: ID of country to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_country_by_id_with_http_info(country_id, **kwargs)
        else:
            (data) = cls._delete_country_by_id_with_http_info(country_id, **kwargs)
            return data

    @classmethod
    def _delete_country_by_id_with_http_info(cls, country_id, **kwargs):
        """Delete Country

        Delete an instance of Country by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_country_by_id_with_http_info(country_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_id: ID of country to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_id']
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
        # verify the required parameter 'country_id' is set
        if ('country_id' not in params or
                params['country_id'] is None):
            raise ValueError("Missing the required parameter `country_id` when calling `delete_country_by_id`")

        collection_formats = {}

        path_params = {}
        if 'country_id' in params:
            path_params['countryId'] = params['country_id']


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
            '/countries/{countryId}', 'DELETE',
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
    def get_country_by_id(cls, country_id, **kwargs):
        """Find Country

        Return single instance of Country by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_country_by_id(country_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_id: ID of country to return (required)
        :return: Country
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_country_by_id_with_http_info(country_id, **kwargs)
        else:
            (data) = cls._get_country_by_id_with_http_info(country_id, **kwargs)
            return data

    @classmethod
    def _get_country_by_id_with_http_info(cls, country_id, **kwargs):
        """Find Country

        Return single instance of Country by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_country_by_id_with_http_info(country_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_id: ID of country to return (required)
        :return: Country
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_id']
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
        # verify the required parameter 'country_id' is set
        if ('country_id' not in params or
                params['country_id'] is None):
            raise ValueError("Missing the required parameter `country_id` when calling `get_country_by_id`")

        collection_formats = {}

        path_params = {}
        if 'country_id' in params:
            path_params['countryId'] = params['country_id']


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
            '/countries/{countryId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Country',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_countries(cls, **kwargs):
        """List Countries

        Return a list of Countries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_countries(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Country]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_countries_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_countries_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_countries_with_http_info(cls, **kwargs):
        """List Countries

        Return a list of Countries
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_countries_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[Country]
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
            '/countries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[Country]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_country_by_id(cls, country_id, country, **kwargs):
        """Replace Country

        Replace all attributes of Country
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_country_by_id(country_id, country, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_id: ID of country to replace (required)
        :param Country country: Attributes of country to replace (required)
        :return: Country
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_country_by_id_with_http_info(country_id, country, **kwargs)
        else:
            (data) = cls._replace_country_by_id_with_http_info(country_id, country, **kwargs)
            return data

    @classmethod
    def _replace_country_by_id_with_http_info(cls, country_id, country, **kwargs):
        """Replace Country

        Replace all attributes of Country
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_country_by_id_with_http_info(country_id, country, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_id: ID of country to replace (required)
        :param Country country: Attributes of country to replace (required)
        :return: Country
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_id', 'country']
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
        # verify the required parameter 'country_id' is set
        if ('country_id' not in params or
                params['country_id'] is None):
            raise ValueError("Missing the required parameter `country_id` when calling `replace_country_by_id`")
        # verify the required parameter 'country' is set
        if ('country' not in params or
                params['country'] is None):
            raise ValueError("Missing the required parameter `country` when calling `replace_country_by_id`")

        collection_formats = {}

        path_params = {}
        if 'country_id' in params:
            path_params['countryId'] = params['country_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'country' in params:
            body_params = params['country']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/countries/{countryId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Country',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_country_by_id(cls, country_id, country, **kwargs):
        """Update Country

        Update attributes of Country
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_country_by_id(country_id, country, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_id: ID of country to update. (required)
        :param Country country: Attributes of country to update. (required)
        :return: Country
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_country_by_id_with_http_info(country_id, country, **kwargs)
        else:
            (data) = cls._update_country_by_id_with_http_info(country_id, country, **kwargs)
            return data

    @classmethod
    def _update_country_by_id_with_http_info(cls, country_id, country, **kwargs):
        """Update Country

        Update attributes of Country
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_country_by_id_with_http_info(country_id, country, async=True)
        >>> result = thread.get()

        :param async bool
        :param str country_id: ID of country to update. (required)
        :param Country country: Attributes of country to update. (required)
        :return: Country
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['country_id', 'country']
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
        # verify the required parameter 'country_id' is set
        if ('country_id' not in params or
                params['country_id'] is None):
            raise ValueError("Missing the required parameter `country_id` when calling `update_country_by_id`")
        # verify the required parameter 'country' is set
        if ('country' not in params or
                params['country'] is None):
            raise ValueError("Missing the required parameter `country` when calling `update_country_by_id`")

        collection_formats = {}

        path_params = {}
        if 'country_id' in params:
            path_params['countryId'] = params['country_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'country' in params:
            body_params = params['country']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/countries/{countryId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Country',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
