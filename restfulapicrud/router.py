from xmeme.viewsets import MemeViewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('meme',MemeViewsets)