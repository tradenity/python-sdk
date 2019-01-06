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


class StoreProfile(object):
    

    swagger_types = { 
        'id': 'str',
        'meta': 'InstanceMeta',
        'name': 'str',
        'description': 'str',
        'contact_info': 'ContactInfo',
        'billing_info': 'ContactInfo',
        'facebook': 'str',
        'twitter': 'str',
        'youtube': 'str',
        'instagram': 'str',
        'pinterest': 'str',
        'linkedin': 'str'
    }

    attribute_map = { 
        'id': 'id',
        'meta': '__meta',
        'name': 'name',
        'description': 'description',
        'contact_info': 'contactInfo',
        'billing_info': 'billingInfo',
        'facebook': 'facebook',
        'twitter': 'twitter',
        'youtube': 'youtube',
        'instagram': 'instagram',
        'pinterest': 'pinterest',
        'linkedin': 'linkedin'
    }

    api_client = None

    def __init__(self, id=None, meta=None, name=None, description=None, contact_info=None, billing_info=None, facebook=None, twitter=None, youtube=None, instagram=None, pinterest=None, linkedin=None):
        """StoreProfile - a model defined in Swagger"""
        self._id = id

        self._meta = None
        self._name = None
        self._description = None
        self._contact_info = None
        self._billing_info = None
        self._facebook = None
        self._twitter = None
        self._youtube = None
        self._instagram = None
        self._pinterest = None
        self._linkedin = None
        self.discriminator = None

        if meta is not None:
            self.meta = meta
        self.name = name
        if description is not None:
            self.description = description
        if contact_info is not None:
            self.contact_info = contact_info
        if billing_info is not None:
            self.billing_info = billing_info
        if facebook is not None:
            self.facebook = facebook
        if twitter is not None:
            self.twitter = twitter
        if youtube is not None:
            self.youtube = youtube
        if instagram is not None:
            self.instagram = instagram
        if pinterest is not None:
            self.pinterest = pinterest
        if linkedin is not None:
            self.linkedin = linkedin

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
        """Gets the meta of this StoreProfile.


        :return: The meta of this StoreProfile.
        :rtype: InstanceMeta
        """
        return self._meta

    @meta.setter
    def meta(self, meta):
        """Sets the meta of this StoreProfile.


        :param meta: The meta of this StoreProfile.
        :type: InstanceMeta
        """

        self._meta = meta

    @property
    def name(self):
        """Gets the name of this StoreProfile.


        :return: The name of this StoreProfile.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this StoreProfile.


        :param name: The name of this StoreProfile.
        :type: str
        """

        self._name = name

    @property
    def description(self):
        """Gets the description of this StoreProfile.


        :return: The description of this StoreProfile.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this StoreProfile.


        :param description: The description of this StoreProfile.
        :type: str
        """

        self._description = description

    @property
    def contact_info(self):
        """Gets the contact_info of this StoreProfile.


        :return: The contact_info of this StoreProfile.
        :rtype: ContactInfo
        """
        return self._contact_info

    @contact_info.setter
    def contact_info(self, contact_info):
        """Sets the contact_info of this StoreProfile.


        :param contact_info: The contact_info of this StoreProfile.
        :type: ContactInfo
        """

        self._contact_info = contact_info

    @property
    def billing_info(self):
        """Gets the billing_info of this StoreProfile.


        :return: The billing_info of this StoreProfile.
        :rtype: ContactInfo
        """
        return self._billing_info

    @billing_info.setter
    def billing_info(self, billing_info):
        """Sets the billing_info of this StoreProfile.


        :param billing_info: The billing_info of this StoreProfile.
        :type: ContactInfo
        """

        self._billing_info = billing_info

    @property
    def facebook(self):
        """Gets the facebook of this StoreProfile.


        :return: The facebook of this StoreProfile.
        :rtype: str
        """
        return self._facebook

    @facebook.setter
    def facebook(self, facebook):
        """Sets the facebook of this StoreProfile.


        :param facebook: The facebook of this StoreProfile.
        :type: str
        """

        self._facebook = facebook

    @property
    def twitter(self):
        """Gets the twitter of this StoreProfile.


        :return: The twitter of this StoreProfile.
        :rtype: str
        """
        return self._twitter

    @twitter.setter
    def twitter(self, twitter):
        """Sets the twitter of this StoreProfile.


        :param twitter: The twitter of this StoreProfile.
        :type: str
        """

        self._twitter = twitter

    @property
    def youtube(self):
        """Gets the youtube of this StoreProfile.


        :return: The youtube of this StoreProfile.
        :rtype: str
        """
        return self._youtube

    @youtube.setter
    def youtube(self, youtube):
        """Sets the youtube of this StoreProfile.


        :param youtube: The youtube of this StoreProfile.
        :type: str
        """

        self._youtube = youtube

    @property
    def instagram(self):
        """Gets the instagram of this StoreProfile.


        :return: The instagram of this StoreProfile.
        :rtype: str
        """
        return self._instagram

    @instagram.setter
    def instagram(self, instagram):
        """Sets the instagram of this StoreProfile.


        :param instagram: The instagram of this StoreProfile.
        :type: str
        """

        self._instagram = instagram

    @property
    def pinterest(self):
        """Gets the pinterest of this StoreProfile.


        :return: The pinterest of this StoreProfile.
        :rtype: str
        """
        return self._pinterest

    @pinterest.setter
    def pinterest(self, pinterest):
        """Sets the pinterest of this StoreProfile.


        :param pinterest: The pinterest of this StoreProfile.
        :type: str
        """

        self._pinterest = pinterest

    @property
    def linkedin(self):
        """Gets the linkedin of this StoreProfile.


        :return: The linkedin of this StoreProfile.
        :rtype: str
        """
        return self._linkedin

    @linkedin.setter
    def linkedin(self, linkedin):
        """Sets the linkedin of this StoreProfile.


        :param linkedin: The linkedin of this StoreProfile.
        :type: str
        """

        self._linkedin = linkedin

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
        if issubclass(StoreProfile, dict):
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
        if not isinstance(other, StoreProfile):
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
    def find_by_id(cls, id):
        return cls.get_store_profile_by_id(id)

    def update(self):
        return self.update_store_profile_by_id(self.id, self)

    @classmethod
    def get_store_profile_by_id(cls, store_profile_id, **kwargs):
        """Find StoreProfile

        Return single instance of StoreProfile by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_store_profile_by_id(store_profile_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_profile_id: ID of storeProfile to return (required)
        :return: StoreProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._get_store_profile_by_id_with_http_info(store_profile_id, **kwargs)
        else:
            (data) = cls._get_store_profile_by_id_with_http_info(store_profile_id, **kwargs)
            return data

    @classmethod
    def _get_store_profile_by_id_with_http_info(cls, store_profile_id, **kwargs):
        """Find StoreProfile

        Return single instance of StoreProfile by its ID.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.get_store_profile_by_id_with_http_info(store_profile_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_profile_id: ID of storeProfile to return (required)
        :return: StoreProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_profile_id']
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
        # verify the required parameter 'store_profile_id' is set
        if ('store_profile_id' not in params or
                params['store_profile_id'] is None):
            raise ValueError("Missing the required parameter `store_profile_id` when calling `get_store_profile_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_profile_id' in params:
            path_params['storeProfileId'] = params['store_profile_id']


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
            '/storeProfiles/{storeProfileId}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreProfile',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def replace_store_profile_by_id(cls, store_profile_id, store_profile, **kwargs):
        """Replace StoreProfile

        Replace all attributes of StoreProfile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_store_profile_by_id(store_profile_id, store_profile, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_profile_id: ID of storeProfile to replace (required)
        :param StoreProfile store_profile: Attributes of storeProfile to replace (required)
        :return: StoreProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._replace_store_profile_by_id_with_http_info(store_profile_id, store_profile, **kwargs)
        else:
            (data) = cls._replace_store_profile_by_id_with_http_info(store_profile_id, store_profile, **kwargs)
            return data

    @classmethod
    def _replace_store_profile_by_id_with_http_info(cls, store_profile_id, store_profile, **kwargs):
        """Replace StoreProfile

        Replace all attributes of StoreProfile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.replace_store_profile_by_id_with_http_info(store_profile_id, store_profile, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_profile_id: ID of storeProfile to replace (required)
        :param StoreProfile store_profile: Attributes of storeProfile to replace (required)
        :return: StoreProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_profile_id', 'store_profile']
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
        # verify the required parameter 'store_profile_id' is set
        if ('store_profile_id' not in params or
                params['store_profile_id'] is None):
            raise ValueError("Missing the required parameter `store_profile_id` when calling `replace_store_profile_by_id`")
        # verify the required parameter 'store_profile' is set
        if ('store_profile' not in params or
                params['store_profile'] is None):
            raise ValueError("Missing the required parameter `store_profile` when calling `replace_store_profile_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_profile_id' in params:
            path_params['storeProfileId'] = params['store_profile_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'store_profile' in params:
            body_params = params['store_profile']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/storeProfiles/{storeProfileId}', 'PUT',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreProfile',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    @classmethod
    def update_store_profile_by_id(cls, store_profile_id, store_profile, **kwargs):
        """Update StoreProfile

        Update attributes of StoreProfile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_store_profile_by_id(store_profile_id, store_profile, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_profile_id: ID of storeProfile to update. (required)
        :param StoreProfile store_profile: Attributes of storeProfile to update. (required)
        :return: StoreProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return cls._update_store_profile_by_id_with_http_info(store_profile_id, store_profile, **kwargs)
        else:
            (data) = cls._update_store_profile_by_id_with_http_info(store_profile_id, store_profile, **kwargs)
            return data

    @classmethod
    def _update_store_profile_by_id_with_http_info(cls, store_profile_id, store_profile, **kwargs):
        """Update StoreProfile

        Update attributes of StoreProfile
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.update_store_profile_by_id_with_http_info(store_profile_id, store_profile, async=True)
        >>> result = thread.get()

        :param async bool
        :param str store_profile_id: ID of storeProfile to update. (required)
        :param StoreProfile store_profile: Attributes of storeProfile to update. (required)
        :return: StoreProfile
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['store_profile_id', 'store_profile']
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
        # verify the required parameter 'store_profile_id' is set
        if ('store_profile_id' not in params or
                params['store_profile_id'] is None):
            raise ValueError("Missing the required parameter `store_profile_id` when calling `update_store_profile_by_id`")
        # verify the required parameter 'store_profile' is set
        if ('store_profile' not in params or
                params['store_profile'] is None):
            raise ValueError("Missing the required parameter `store_profile` when calling `update_store_profile_by_id`")

        collection_formats = {}

        path_params = {}
        if 'store_profile_id' in params:
            path_params['storeProfileId'] = params['store_profile_id']


        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'store_profile' in params:
            body_params = params['store_profile']
        # HTTP header `Accept`
        header_params['Accept'] = cls.get_api_client().select_header_accept(
            ['application/json'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = cls.get_api_client().select_header_content_type(
            ['application/json'])

        # Authentication setting
        auth_settings = []

        return cls.get_api_client().call_api(
            '/storeProfiles/{storeProfileId}', 'PATCH',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='StoreProfile',
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
