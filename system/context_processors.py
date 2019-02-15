from system.authenticate.models import Profile, Team
from system.info.models import News


def dataStatic(request):
    return {
        "total_players": Profile.objects.count(),
        "total_teams": Team.objects.count(),
        "total_online": len(Profile.objects.filter(online=True)),
        "donwload_ftp": 'ftp://10.30.1.31/Cliente/Oficial/',
        "donwload_testing": 'ftp://10.30.1.31/Cliente/Testing/',
        "donwload_torrent": 'ftp://10.30.1.31/Cliente/',
        "news": News.objects.all().order_by('-id')[:3]
    }