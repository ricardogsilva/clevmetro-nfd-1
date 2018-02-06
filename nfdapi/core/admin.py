# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import *
from . import staticmodels

# Register your models here.
class SpeciesAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_common',
                     'name_sci',
                     'tsn',
                     'synonym',
                     'second_common',
                     'third_common'
    )
    search_fields = ['first_common',
                     'name_sci',
                     'tsn',
                     'synonym',
                     'second_common',
                     'third_common'
    ]
    
admin.site.register(Species, SpeciesAdmin)

admin.site.register(staticmodels.OccurrenceCategory)
admin.site.register(staticmodels.DayTime)
admin.site.register(staticmodels.Season)
admin.site.register(staticmodels.RecordOrigin)
admin.site.register(staticmodels.RecordingStation)
admin.site.register(staticmodels.CmStatus)
admin.site.register(staticmodels.SRank)
admin.site.register(staticmodels.NRank)
admin.site.register(staticmodels.GRank)
admin.site.register(staticmodels.RegionalStatus)
admin.site.register(staticmodels.UsfwsStatus)
admin.site.register(staticmodels.IucnRedListCategory)
admin.site.register(staticmodels.ElementType)
admin.site.register(staticmodels.MushroomGroup)
admin.site.register(staticmodels.Preservative)
admin.site.register(staticmodels.Storage)
admin.site.register(staticmodels.Repository)
admin.site.register(staticmodels.AquaticHabitatCategory)
admin.site.register(staticmodels.Gender)
admin.site.register(staticmodels.Marks)
admin.site.register(staticmodels.DiseasesAndAbnormalities)
admin.site.register(staticmodels.TerrestrialSampler)
admin.site.register(staticmodels.AquaticSampler)
admin.site.register(staticmodels.TerrestrialStratum)
admin.site.register(staticmodels.PondLakeType)
admin.site.register(staticmodels.PondLakeUse)
admin.site.register(staticmodels.ShorelineType)
admin.site.register(staticmodels.LakeMicrohabitat)
admin.site.register(staticmodels.StreamDesignatedUse)
admin.site.register(staticmodels.ChannelType)
admin.site.register(staticmodels.HmfeiLocalAbundance)
admin.site.register(staticmodels.LoticHabitatType)
admin.site.register(staticmodels.WaterFlowType)
admin.site.register(staticmodels.WetlandType)
admin.site.register(staticmodels.WetlandLocation)
admin.site.register(staticmodels.WetlandConnectivity)
admin.site.register(staticmodels.WaterSource)
admin.site.register(staticmodels.WetlandHabitatFeature)
admin.site.register(staticmodels.SlimeMoldClass)
admin.site.register(staticmodels.SlimeMoldMedia)
admin.site.register(staticmodels.PlantCount)
admin.site.register(staticmodels.MoistureRegime)
admin.site.register(staticmodels.GroundSurface)
admin.site.register(staticmodels.CanopyCover)
admin.site.register(staticmodels.GeneralHabitatCategory)
admin.site.register(staticmodels.LandscapePosition)
admin.site.register(staticmodels.Aspect)
admin.site.register(staticmodels.Slope)

admin.site.register(staticmodels.FernLifestages)
admin.site.register(staticmodels.FloweringPlantLifestages)
admin.site.register(staticmodels.MossLifestages)


