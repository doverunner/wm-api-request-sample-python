from enum import Enum


class UrlInfo(Enum):
    PACK_JOB_REGISTER = ("https://api.pallycon.com/api/v2/pack/", "POST", None, "PACK_JOB_REGISTER")
    PACK_JOB_LIST = ("https://api.pallycon.com/api/v2/pack/", "GET", None, "PACK_JOB_LIST")

    SESSION_WATERMARK_URL_GENERATE = ("https://watermark.pallycon.com/api/v2/session/watermarkUrl/", "GET", None, "SESSION_WATERMARK_URL_GENERATE")
    SESSION_WATERMARK_TOKEN_GENERATE = ("https://watermark.pallycon.com/api/v2/session/watermarkData/", "GET", None, "SESSION_WATERMARK_TOKEN_GENERATE")
    SESSION_LIST = ("https://watermark.pallycon.com/api/v2/session/list/", "GET", None, "SESSION_LIST")

    STORAGE_REGISTER = ("https://api.pallycon.com/api/v2/storage/", "POST", None, "STORAGE_REGISTER")
    STORAGE_UPDATE = ("https://api.pallycon.com/api/v2/storage/", "PUT", None, "STORAGE_UPDATE")
    STORAGE_LIST = ("https://api.pallycon.com/api/v2/storage/", "GET", None, "STORAGE_LIST")

    DETECT_REGISTER = ("https://api.pallycon.com/api/v2/detect/", "POST", "url", "DETECT_REGISTER")
    DETECT_LIST = ("https://api.pallycon.com/api/v2/detect/", "GET", "list", "DETECT_LIST")
    DETECT_DETAIL = ("https://api.pallycon.com/api/v2/detect/", "GET", "detail", "DETECT_DETAIL")

    def __init__(self, url, method, sub_url, description):
        self.__url = url
        self.__method = method
        self.__subUrl = sub_url
        self.__description = description

    def request_url_method(self, api_data_str: str, site_id: str) -> str:
        return {
            'description': self.__description,
            'pallycon-apidata': api_data_str,
            'url': self.__make_request_url(api_data_str, site_id),
            'method': self.__method
        }

    def __make_request_url(self, api_data_str: str, site_id: str) -> str:
        url = []
        url.append(self.__generate_base_url(site_id))
        url.append(self.__generate_query_str(api_data_str))
        return ''.join(url)

    def __generate_base_url(self, site_id) -> str:
        base_url = []
        base_url.append(self.__url)
        base_url.append(site_id)

        if self.__subUrl is not None:
            base_url.append('/')
            base_url.append(self.__subUrl)

        return ''.join(base_url)

    def __generate_query_str(self, api_data_str) -> str:
        query_str = []
        query_str.append('?')
        query_str.append('pallycon-apidata')
        query_str.append('=')
        query_str.append(api_data_str)

        return ''.join(query_str)

# print(UrlInfo.DETECT_DETAIL)



