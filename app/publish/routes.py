from flask_via.routers.default import Pluggable
from .views import PublishView, PublicationView

routes = [
    Pluggable('/publish/', PublishView, 'publish'),
    Pluggable('/publication/<vehicleId>', PublicationView, 'publication')
]
