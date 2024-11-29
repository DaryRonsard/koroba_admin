from django.db import models
from base.models.helpers.date_time_model import DateTimeModel




PAIEMENT =[

    ('Wave', 'Wave'),
    ('Orange money', 'Orange money'),
    ('Moov money', 'Moov money'),
    ('Djamo', 'Djamo'),
    ('Push', 'Push'),
    

]

class PaiementModel(DateTimeModel):
    paiement = models.CharField(max_length=255, choices=PAIEMENT)
    
   

    
    
