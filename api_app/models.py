from django.db import models

# Create your models here.

class pokemon(models.Model):
    pokedex_no = models.IntegerField(default = 0, unique = True)
    name = models.CharField(max_length=25, unique = True)
    is_legendary = models.BinaryField(unique = True)
    
    def photo_upload_path(self,filename):
        path = f"api_app/uploads/photos/pokemon/{filename}"
        return path
    
    picture = models.ImageField(upload_to = photo_upload_path, null = True, blank = True)