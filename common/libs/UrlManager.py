class UrlManager(object):
    @staticmethod
    def buildUrl(path):
        return path

    @staticmethod
    def buildStaticUrl(path):
        path = path + "?ver=" + "2019"
        return UrlManager.buildUrl(path)
