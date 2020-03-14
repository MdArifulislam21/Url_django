from django.db import models


from shortener.models import UssUrl

class ClickEventManager(models.Manager):
	def create_event(self, instance):
		if isinstance(instance, UssUrl):
			obj, created = self.get_or_create(uss_url=instance)
			obj.count += 1
			obj.save()
			return obj.count
		return None

class ClickEvent(models.Model):
	uss_url = models.OneToOneField(UssUrl, on_delete=models.CASCADE)
	count   = models.IntegerField(default = 0)
	updated = models.DateTimeField(auto_now=True)
	timestamp= models.DateTimeField(auto_now_add=True)
	
	objects = ClickEventManager()

	def __str__(self):
		return str(self.count)