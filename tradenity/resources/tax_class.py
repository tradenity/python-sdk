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


class TaxClass(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'slug': 'str',
        'description': 'str',
        'status': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'slug': 'slug',
        'description': 'description',
        'status': 'status'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, slug=None, description=None, status=None):
        """TaxClass - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._slug = None
        self._description = None
        self._status = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        self.slug = slug
        if description is not None:
            self.description = description
        self.status = status

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
        """Gets the meta of this TaxClass.


        :return: The meta of this TaxClass.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this TaxClass.


        :param meta: The meta of this TaxClass.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this TaxClass.


        :return: The name of this TaxClass.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TaxClass.


        :param name: The name of this TaxClass.
        :type: str
        """

        self._name = name

    @property
    def slug(self):
        """Gets the slug of this TaxClass.


        :return: The slug of this TaxClass.
        :rtype: str
        """
        return self._slug

    @slug.setter
    def slug(self, slug):
        """Sets the slug of this TaxClass.


        :param slug: The slug of this TaxClass.
        :type: str
        """

        self._slug = slug

    @property
    def description(self):
        """Gets the description of this TaxClass.


        :return: The description of this TaxClass.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TaxClass.


        :param description: The description of this TaxClass.
        :type: str
        """

        self._description = description

    @property
    def status(self):
        """Gets the status of this TaxClass.


        :return: The status of this TaxClass.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this TaxClass.


        :param status: The status of this TaxClass.
        :type: str
        """
        allowed_values = ["enabled", "disabled"]
        if status is not None and status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(TaxClass, dict):
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
        if not isinstance(other, TaxClass):
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
        return cls.list_all_tax_classes()

    @classmethod
    def find_all_by(cls, **kwargs):
        return cls.list_all_tax_classes(**kwargs)

    @classmethod
    def find_one_by(cls, **kwargs):
        results = cls.list_all_tax_classes(**kwargs)
        if len(results) > 0:
            return results[0]

    @classmethod
    def find_by_id(cls, id):
        return cls.get_tax_class_by_id(id)

    def create(self):
        new_instance = self.create_tax_class(self)
        self.id = new_instance.id
        return self

    def update(self):
        return self.update_tax_class_by_id(self.id, self)

    def delete(self):
        return self.delete_tax_class_by_id(self.id)



    @classmethod
    def create_tax_class(cls, tax_class, **kwargs):
        """Create TaxClass

        Create a new TaxClass
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_tax_class(tax_class, async=True)
        >>> result = thread.get()

        :param async bool
        :param TaxClass tax_class: Attributes of taxClass to create (required)
        :return: TaxClass
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._create_tax_class_with_http_info(tax_class, **kwargs)
        else:
            (data) = cls._create_tax_class_with_http_info(tax_class, **kwargs)
            return data

    @classmethod
    def _create_tax_class_with_http_info(cls, tax_class, **kwargs):
        """Create TaxClass

        Create a new TaxClass
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.create_tax_class_with_http_info(tax_class, async=True)
        >>> result = thread.get()

        :param async bool
        :param TaxClass tax_class: Attributes of taxClass to create (required)
        :return: TaxClass
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_class']
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
        # verify the required parameter 'tax_class' is set
        if ('tax_class' not in params or
                params['tax_class'] is None):
            raise ValueError("Missing the required parameter `tax_class` when calling `create_tax_class`")

        collection_formats = {}

        path_params = {}


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tax_class' in params:
            body_params = params['tax_class']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/taxClasses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxClass',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def delete_tax_class_by_id(cls, tax_class_id, **kwargs):
        """Delete TaxClass

        Delete an instance of TaxClass by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_tax_class_by_id(tax_class_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_class_id: ID of taxClass to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._delete_tax_class_by_id_with_http_info(tax_class_id, **kwargs)
        else:
            (data) = cls._delete_tax_class_by_id_with_http_info(tax_class_id, **kwargs)
            return data

    @classmethod
    def _delete_tax_class_by_id_with_http_info(cls, tax_class_id, **kwargs):
        """Delete TaxClass

        Delete an instance of TaxClass by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.delete_tax_class_by_id_with_http_info(tax_class_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_class_id: ID of taxClass to delete. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_class_id']
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
        # verify the required parameter 'tax_class_id' is set
        if ('tax_class_id' not in params or
                params['tax_class_id'] is None):
            raise ValueError("Missing the required parameter `tax_class_id` when calling `delete_tax_class_by_id`")

        collection_formats = {}

        path_params = {}
        if 'tax_class_id' in params:
            path_params['taxClassId'] = params['tax_class_id']


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
            '/taxClasses/{taxClassId}', 'DELETE',
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
    def get_tax_class_by_id(cls, tax_class_id, **kwargs):
        """Find TaxClass

        Return single instance of TaxClass by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tax_class_by_id(tax_class_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_class_id: ID of taxClass to return (required)
        :return: TaxClass
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_tax_class_by_id_with_http_info(tax_class_id, **kwargs)
        else:
            (data) = cls._get_tax_class_by_id_with_http_info(tax_class_id, **kwargs)
            return data

    @classmethod
    def _get_tax_class_by_id_with_http_info(cls, tax_class_id, **kwargs):
        """Find TaxClass

        Return single instance of TaxClass by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_tax_class_by_id_with_http_info(tax_class_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_class_id: ID of taxClass to return (required)
        :return: TaxClass
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_class_id']
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
        # verify the required parameter 'tax_class_id' is set
        if ('tax_class_id' not in params or
                params['tax_class_id'] is None):
            raise ValueError("Missing the required parameter `tax_class_id` when calling `get_tax_class_by_id`")

        collection_formats = {}

        path_params = {}
        if 'tax_class_id' in params:
            path_params['taxClassId'] = params['tax_class_id']


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
            '/taxClasses/{taxClassId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxClass',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def list_all_tax_classes(cls, **kwargs):
        """List TaxClasses

        Return a list of TaxClasses
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_tax_classes(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[TaxClass]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._list_all_tax_classes_with_http_info(**kwargs)
        else:
            (data) = cls._list_all_tax_classes_with_http_info(**kwargs)
            return data

    @classmethod
    def _list_all_tax_classes_with_http_info(cls, **kwargs):
        """List TaxClasses

        Return a list of TaxClasses
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.list_all_tax_classes_with_http_info(async=True)
        >>> result = thread.get()

        :param async bool
        :param int page: page number
        :param int size: page size
        :param str sort: page order
        :return: page[TaxClass]
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
            '/taxClasses', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='page[TaxClass]',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_tax_class_by_id(cls, tax_class_id, tax_class, **kwargs):
        """Replace TaxClass

        Replace all attributes of TaxClass
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_tax_class_by_id(tax_class_id, tax_class, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_class_id: ID of taxClass to replace (required)
        :param TaxClass tax_class: Attributes of taxClass to replace (required)
        :return: TaxClass
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_tax_class_by_id_with_http_info(tax_class_id, tax_class, **kwargs)
        else:
            (data) = cls._replace_tax_class_by_id_with_http_info(tax_class_id, tax_class, **kwargs)
            return data

    @classmethod
    def _replace_tax_class_by_id_with_http_info(cls, tax_class_id, tax_class, **kwargs):
        """Replace TaxClass

        Replace all attributes of TaxClass
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_tax_class_by_id_with_http_info(tax_class_id, tax_class, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_class_id: ID of taxClass to replace (required)
        :param TaxClass tax_class: Attributes of taxClass to replace (required)
        :return: TaxClass
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_class_id', 'tax_class']
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
        # verify the required parameter 'tax_class_id' is set
        if ('tax_class_id' not in params or
                params['tax_class_id'] is None):
            raise ValueError("Missing the required parameter `tax_class_id` when calling `replace_tax_class_by_id`")
        # verify the required parameter 'tax_class' is set
        if ('tax_class' not in params or
                params['tax_class'] is None):
            raise ValueError("Missing the required parameter `tax_class` when calling `replace_tax_class_by_id`")

        collection_formats = {}

        path_params = {}
        if 'tax_class_id' in params:
            path_params['taxClassId'] = params['tax_class_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tax_class' in params:
            body_params = params['tax_class']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/taxClasses/{taxClassId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxClass',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_tax_class_by_id(cls, tax_class_id, tax_class, **kwargs):
        """Update TaxClass

        Update attributes of TaxClass
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_tax_class_by_id(tax_class_id, tax_class, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_class_id: ID of taxClass to update. (required)
        :param TaxClass tax_class: Attributes of taxClass to update. (required)
        :return: TaxClass
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_tax_class_by_id_with_http_info(tax_class_id, tax_class, **kwargs)
        else:
            (data) = cls._update_tax_class_by_id_with_http_info(tax_class_id, tax_class, **kwargs)
            return data

    @classmethod
    def _update_tax_class_by_id_with_http_info(cls, tax_class_id, tax_class, **kwargs):
        """Update TaxClass

        Update attributes of TaxClass
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_tax_class_by_id_with_http_info(tax_class_id, tax_class, async=True)
        >>> result = thread.get()

        :param async bool
        :param str tax_class_id: ID of taxClass to update. (required)
        :param TaxClass tax_class: Attributes of taxClass to update. (required)
        :return: TaxClass
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['tax_class_id', 'tax_class']
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
        # verify the required parameter 'tax_class_id' is set
        if ('tax_class_id' not in params or
                params['tax_class_id'] is None):
            raise ValueError("Missing the required parameter `tax_class_id` when calling `update_tax_class_by_id`")
        # verify the required parameter 'tax_class' is set
        if ('tax_class' not in params or
                params['tax_class'] is None):
            raise ValueError("Missing the required parameter `tax_class` when calling `update_tax_class_by_id`")

        collection_formats = {}

        path_params = {}
        if 'tax_class_id' in params:
            path_params['taxClassId'] = params['tax_class_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'tax_class' in params:
            body_params = params['tax_class']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/taxClasses/{taxClassId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TaxClass',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
