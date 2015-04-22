#
# developed by Sergey Markelov (2013)
#

import random

BING_URL = 'http://www.bing.com'

# common headers for all requests
HEADERS = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "en-us,en;q=0.5",
    "Accept-Charset": "utf-8",
    "Accept-Encoding": "gzip, deflate",
    "Connection": "keep-alive",
}

class UserAgents:
    @staticmethod
    def generate():
        userAgents = UserAgents
        userAgents.pc     = USER_AGENTS_PC[ random.randint(0, len(USER_AGENTS_PC) - 1) ]
        userAgents.mobile = USER_AGENTS_MOBILE[ random.randint(0, len(USER_AGENTS_MOBILE) - 1) ]
        return userAgents

USER_AGENTS_PC = (
# Safari 7.0 MacOSX
# Chrome 31.0 Win7 64-bit
# Firefox 31.0 Win7 32-bit
    "Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0",
# Chrome 40.0 Win7 32-bit
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.111 Safari/537.36",
# Chrome 31.0 MacOSX
# Chrome 32.0 MacOSX
# Firefox 26.0 MacOSX
# Chrome 31.0 Win8.1 64-bit
)

USER_AGENTS_MOBILE = (
# Android 5.0.1
    "Mozilla/5.0 (Linux; Android 5.0.1; Nexus 4 Build/LRX22C) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.109 Mobile Safari/537.36",
# Android 2.3
# BlackBerry - BB10
# iPhone - iOS 7
# iPhone - iOS 6
)
