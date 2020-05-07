# Models -- objects that represent data
# These are all subclassed from the standard Django Model and
# use the ORM to handle persistence and retrieval.

from django.db import models

GENDER_CHOICES = [
    ('M', 'male'),
    ('F', 'female'),
]


class DataPage( models.Model ):
    #
    # free-form data page
    #
    title = models.CharField( max_length=100 )
    comment = models.TextField( blank=True, null=True )

    def __str__( self ):
        return self.title


class Name( models.Model ):
    #
    # name_display = "Johann Jakob Gehrig"
    # name_sort = "Gehrig, Johann Jakob"
    #
    name_display = models.CharField( max_length=100, primary_key=True )
    name_sort = models.CharField( max_length=100 )
    comment = models.TextField( blank=True, null=True )

    class Meta:
        ordering = ['name_sort', ]

    def __str__( self ):
        return self.name_sort


class Person( models.Model ):
    #
    # Basic data of a person
    #
    name = models.ManyToManyField( Name )
    birth = models.DateField( blank=True, null=True )
    birthplace = models.CharField( max_length=100, blank=True, null=True )
    death = models.DateField( blank=True, null=True )
    deathplace = models.CharField( max_length=100, blank=True, null=True )
    gender = models.CharField( max_length=1, blank=True, null=True, choices=GENDER_CHOICES )
    bio_mother = models.ForeignKey( 'Person', blank=True, null=True, on_delete=models.SET_NULL, related_name='mother' )
    bio_father = models.ForeignKey( 'Person', blank=True, null=True, on_delete=models.SET_NULL, related_name='father' )

    # todo: __str__ will need to handle case of multiple names


class DirectedRelation( models.Model ):
    #
    # Directed relationship -- first is the son, daughter, sister, of second
    #
    first_person = models.ForeignKey( Person, related_name='first', on_delete=models.CASCADE )
    second_person = models.ForeignKey( Person, related_name='second', on_delete=models.CASCADE )
    comment = models.TextField( blank=True, null=True )


class ImageMetadata( models.Model ):
    person = models.ManyToManyField( Person )
    comment = models.TextField( blank=True, null=True )

    # todo: remember media uploads etc.
