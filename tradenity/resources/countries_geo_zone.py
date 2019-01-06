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


class CountriesGeoZone(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'status': 'str',
        'description': 'str',
        'countries': 'list[Country]'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'status': 'status',
        'description': 'description',
        'countries': 'countries'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, status=None, description=None, countries=None):
        """CountriesGeoZone - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._status = None
        self._description = None
        self._countries = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        self.status = status
        if description is not None:
            self.description = description
        self.countries = countries

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
        """Gets the meta of this CountriesGeoZone.


        :return: The meta of this CountriesGeoZone.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this CountriesGeoZone.


        :param meta: The meta of this CountriesGeoZone.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this CountriesGeoZone.


        :return: The name of this CountriesGeoZone.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this CountriesGeoZone.


        :param name: The name of this CountriesGeoZone.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this CountriesGeoZone.


        :return: The slug of this CountriesGeoZone.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this CountriesGeoZone.


        :param slug: The slug of this CountriesGeoZone.
        :type: str
        """

        self._slug = slug

    @property
    def status(self):
        """Gets the status of this CountriesGeoZone.


        :return: The status of this CountriesGeoZone.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this CountriesGeoZone.


        :param status: The status of this CountriesGeoZone.
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
        """Gets the description of this CountriesGeoZone.


        :return: The description of this CountriesGeoZone.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this CountriesGeoZone.


        :param description: The description of this CountriesGeoZone.
        :type: str
        """

        self._description = description

    @property
    def countries(self):
        """Gets the countries of this CountriesGeoZone.


        :return: The countries of this CountriesGeoZone.
        :rtype: list[Country]
        """
        return self._countries

    @countries.setter
    def countries(self, countries):
        """Sets the countries of this CountriesGeoZone.


        :param countries: The countries of this CountriesGeoZone.
        :type: list[Country]
        """

        self._countries = countries

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
        if issubclass(CountriesGeoZone, dict):
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
        if not isinstance(other, CountriesGeoZone):
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
        return cls.list_all_countries_geo_zones()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_countries_geo_zones(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_countries_geo_zones(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_countries_geo_zone_by_id(id)

    def create(self):
        new_instance = self.create_countries_geo_zone(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_countries_geo_zone_by_id(self.id, self)

    def delete(self):
        return self.delete_countries_geo_zone_by_id(self.id)



    @classmethod
    def create_countries_geo_zone(cls, countries_geo_zone, **kwargs):
        """Create CountriesGeoZone

        Create a new CountriesGeoZone
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_countries_geo_zone(countries_geo_zone, async=True)
        >>> result = thread.get()

        :param async bool
        :param CountriesGeoZone countries_geo_zone: Attributes of countriesGeoZone to create (required)
        :return: CountriesGeoZone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_countries_geo_zone_with_http_info(countries_geo_zone, **kwargs)
        else:
            (data) = cls._create_countries_geo_zone_with_http_info(countries_geo_zone, **kwargs)
            return data

    @classmethod
    def _create_countries_geo_zone_with_http_info(cls, countries_geo_zone, **kwargs):
        """Create CountriesGeoZone

        Create a new CountriesGeoZone
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_countries_geo_zone_with_http_info(countries_geo_zone, async=True)
        >>> result = thread.get()

        :param async bool
        :param CountriesGeoZone countries_geo_zone: Attributes of countriesGeoZone to create (required)
        :return: CountriesGeoZone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['countries_geo_zone']
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
        # verify the required parameter 'countries_geo_zone' is set
        if ('countries_geo_zone' not in params or
                params['countries_geo_zone'] is None):
            raise ValueError("Missing the required parameter `countries_geo_zone` when calling `create_countries_geo_zone`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'countries_geo_zone' in params:
            body_params = params['countries_geo_zone']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/countriesGeoZones', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountriesGeoZone',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_countries_geo_zone_by_id(cls, countries_geo_zone_id, **kwargs):
        """Delete CountriesGeoZone

        Delete an instance of CountriesGeoZone by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_countries_geo_zone_by_id(countries_geo_zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str countries_geo_zone_id: ID of countriesGeoZone to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, **kwargs)
        else:
            (data) = cls._delete_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, **kwargs)
            return data

    @classmethod
    def _delete_countries_geo_zone_by_id_with_http_info(cls, countries_geo_zone_id, **kwargs):
        """Delete CountriesGeoZone

        Delete an instance of CountriesGeoZone by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str countries_geo_zone_id: ID of countriesGeoZone to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['countries_geo_zone_id']
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
        # verify the required parameter 'countries_geo_zone_id' is set
        if ('countries_geo_zone_id' not in params or
                params['countries_geo_zone_id'] is None):
            raise ValueError("Missing the required parameter `countries_geo_zone_id` when calling `delete_countries_geo_zone_by_id`")

        collection_formats = {}

        path_params = {}
        if 'countries_geo_zone_id' in params:
            path_params['countriesGeoZoneId'] = params['countries_geo_zone_id']


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
            '/countriesGeoZones/{countriesGeoZoneId}', 'DELETE',
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
    def get_countries_geo_zone_by_id(cls, countries_geo_zone_id, **kwargs):
        """Find CountriesGeoZone

        Return single instance of CountriesGeoZone by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_countries_geo_zone_by_id(countries_geo_zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str countries_geo_zone_id: ID of countriesGeoZone to return (required)
        :return: CountriesGeoZone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, **kwargs)
        else:
            (data) = cls._get_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, **kwargs)
            return data

    @classmethod
    def _get_countries_geo_zone_by_id_with_http_info(cls, countries_geo_zone_id, **kwargs):
        """Find CountriesGeoZone

        Return single instance of CountriesGeoZone by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str countries_geo_zone_id: ID of countriesGeoZone to return (required)
        :return: CountriesGeoZone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['countries_geo_zone_id']
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
        # verify the required parameter 'countries_geo_zone_id' is set
        if ('countries_geo_zone_id' not in params or
                params['countries_geo_zone_id'] is None):
            raise ValueError("Missing the required parameter `countries_geo_zone_id` when calling `get_countries_geo_zone_by_id`")

        collection_formats = {}

        path_params = {}
        if 'countries_geo_zone_id' in params:
            path_params['countriesGeoZoneId'] = params['countries_geo_zone_id']


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
            '/countriesGeoZones/{countriesGeoZoneId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountriesGeoZone',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_countries_geo_zones(cls, **kwargs):
        """List CountriesGeoZones

        Return a list of CountriesGeoZones
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_countries_geo_zones(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[CountriesGeoZone]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_countries_geo_zones_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_countries_geo_zones_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_countries_geo_zones_with_http_info(cls, **kwargs):
        """List CountriesGeoZones

        Return a list of CountriesGeoZones
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_countries_geo_zones_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[CountriesGeoZone]
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
            '/countriesGeoZones', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[CountriesGeoZone]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_countries_geo_zone_by_id(cls, countries_geo_zone_id, countries_geo_zone, **kwargs):
        """Replace CountriesGeoZone

        Replace all attributes of CountriesGeoZone
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_countries_geo_zone_by_id(countries_geo_zone_id, countries_geo_zone, async=True)
        >>> result = thread.get()

        :param async bool
        :param str countries_geo_zone_id: ID of countriesGeoZone to replace (required)
        :param CountriesGeoZone countries_geo_zone: Attributes of countriesGeoZone to replace (required)
        :return: CountriesGeoZone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, countries_geo_zone, **kwargs)
        else:
            (data) = cls._replace_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, countries_geo_zone, **kwargs)
            return data

    @classmethod
    def _replace_countries_geo_zone_by_id_with_http_info(cls, countries_geo_zone_id, countries_geo_zone, **kwargs):
        """Replace CountriesGeoZone

        Replace all attributes of CountriesGeoZone
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, countries_geo_zone, async=True)
        >>> result = thread.get()

        :param async bool
        :param str countries_geo_zone_id: ID of countriesGeoZone to replace (required)
        :param CountriesGeoZone countries_geo_zone: Attributes of countriesGeoZone to replace (required)
        :return: CountriesGeoZone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['countries_geo_zone_id', 'countries_geo_zone']
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
        # verify the required parameter 'countries_geo_zone_id' is set
        if ('countries_geo_zone_id' not in params or
                params['countries_geo_zone_id'] is None):
            raise ValueError("Missing the required parameter `countries_geo_zone_id` when calling `replace_countries_geo_zone_by_id`")
        # verify the required parameter 'countries_geo_zone' is set
        if ('countries_geo_zone' not in params or
                params['countries_geo_zone'] is None):
            raise ValueError("Missing the required parameter `countries_geo_zone` when calling `replace_countries_geo_zone_by_id`")

        collection_formats = {}

        path_params = {}
        if 'countries_geo_zone_id' in params:
            path_params['countriesGeoZoneId'] = params['countries_geo_zone_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'countries_geo_zone' in params:
            body_params = params['countries_geo_zone']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/countriesGeoZones/{countriesGeoZoneId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountriesGeoZone',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_countries_geo_zone_by_id(cls, countries_geo_zone_id, countries_geo_zone, **kwargs):
        """Update CountriesGeoZone

        Update attributes of CountriesGeoZone
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_countries_geo_zone_by_id(countries_geo_zone_id, countries_geo_zone, async=True)
        >>> result = thread.get()

        :param async bool
        :param str countries_geo_zone_id: ID of countriesGeoZone to update. (required)
        :param CountriesGeoZone countries_geo_zone: Attributes of countriesGeoZone to update. (required)
        :return: CountriesGeoZone
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, countries_geo_zone, **kwargs)
        else:
            (data) = cls._update_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, countries_geo_zone, **kwargs)
            return data

    @classmethod
    def _update_countries_geo_zone_by_id_with_http_info(cls, countries_geo_zone_id, countries_geo_zone, **kwargs):
        """Update CountriesGeoZone

        Update attributes of CountriesGeoZone
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_countries_geo_zone_by_id_with_http_info(countries_geo_zone_id, countries_geo_zone, async=True)
        >>> result = thread.get()

        :param async bool
        :param str countries_geo_zone_id: ID of countriesGeoZone to update. (required)
        :param CountriesGeoZone countries_geo_zone: Attributes of countriesGeoZone to update. (required)
        :return: CountriesGeoZone
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['countries_geo_zone_id', 'countries_geo_zone']
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
        # verify the required parameter 'countries_geo_zone_id' is set
        if ('countries_geo_zone_id' not in params or
                params['countries_geo_zone_id'] is None):
            raise ValueError("Missing the required parameter `countries_geo_zone_id` when calling `update_countries_geo_zone_by_id`")
        # verify the required parameter 'countries_geo_zone' is set
        if ('countries_geo_zone' not in params or
                params['countries_geo_zone'] is None):
            raise ValueError("Missing the required parameter `countries_geo_zone` when calling `update_countries_geo_zone_by_id`")

        collection_formats = {}

        path_params = {}
        if 'countries_geo_zone_id' in params:
            path_params['countriesGeoZoneId'] = params['countries_geo_zone_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'countries_geo_zone' in params:
            body_params = params['countries_geo_zone']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/countriesGeoZones/{countriesGeoZoneId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CountriesGeoZone',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
