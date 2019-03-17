from mine.settings import PAGE_NAME


def dataStatic(request):
    return {
        "title_page": PAGE_NAME,
        "donwload_ftp": 'ftp://10.30.1.31/Cliente/Oficial/',
        "donwload_testing": 'ftp://10.30.1.31/Cliente/Testing/',
        "donwload_torrent": 'ftp://10.30.1.31/Cliente/'
    }