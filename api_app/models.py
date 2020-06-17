from django.db import models
# Create your models here.

class pokemon(models.Model):
    pokedex_id = models.IntegerField(default = 0, unique = True)
    pkmn_name = models.CharField(max_length=25, unique = True)
    is_legendary = models.BooleanField()
    
    def photo_upload_path(self,filename):
        path = f"api_app/uploads/photos/pokemon/{filename}"
        return path
    
    picture = models.ImageField(upload_to = photo_upload_path, null = True, blank = True)

    def __str__(self):
        return f"{self.pkmn_name} - {self.pokedex_id}"