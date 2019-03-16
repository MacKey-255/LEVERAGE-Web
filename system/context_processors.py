from mine.settings import PAGE_NAME
from system.authenticate.models import Profile, Team


def dataStatic(request):
    return {
        "title_page": PAGE_NAME,
        "total_players": Profile.objects.count(),
        "total_teams": Team.objects.count(),
        "total_online": len(Profile.objects.filter(online=True)),
        "donwload_ftp": 'ftp://10.30.1.31/Cliente/Oficial/',
        "donwload_testing": 'ftp://10.30.1.31/Cliente/Testing/',
        "donwload_torrent": 'ftp://10.30.1.31/Cliente/'
    }