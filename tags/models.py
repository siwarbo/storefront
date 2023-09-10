from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here.
class TaggedItemManager(models.Manager):
    def get_taggs_for(self, object_type, object_id):
        content_type = ContentType.objects.get_for_model(object_type)
        return TaggedItem.objects.select_related("tag").filter(
            content_type=content_type, object_id=object_id
        )


class Tag(models.Model):
    label = models.CharField(max_length=255)


class TaggedItem(models.Model):
    objects = TaggedItemManager()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey()
