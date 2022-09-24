from app1.viewssets import Carviewsets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('car',Carviewsets)