from user.api.routers import urlpatterns as user_urlpatterns
from true_layer.api.routers import urlpatterns as truelayer_urlpatterns

router_urlpatterns = []
router_urlpatterns += user_urlpatterns
router_urlpatterns += truelayer_urlpatterns
