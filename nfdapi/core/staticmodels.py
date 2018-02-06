from django.db import models
from django.utils.encoding import python_2_unicode_compatible


@python_2_unicode_compatible
class DictionaryTable(models.Model):
    code = models.TextField(unique=True)
    name = models.TextField()

    def __str__(self):
        return "{0}-{1}".format(self.code, self.name)

    class Meta:
        abstract = True


@python_2_unicode_compatible
class DictionaryTableExtended(models.Model):
    code = models.TextField(unique=True)
    name = models.TextField()
    description = models.TextField()

    def __str__(self):
        return "{0}-{1}".format(self.code, self.name)

    class Meta:
        abstract = True


class OccurrenceCategory(DictionaryTable):
    # natural_area, plant, animal, fungus, slimemold
    main_cat = models.TextField()

    def natural_key(self):
        return self.main_cat, self.code, self.name
    
    
class DayTime(DictionaryTable):
    pass


class Season(DictionaryTable):
    pass


class RecordOrigin(DictionaryTable):
    pass


class RecordingStation(DictionaryTable):
    pass


class Reservation(DictionaryTable):
    pass


class Watershed(DictionaryTable):
    pass


class CmStatus(DictionaryTableExtended):
    pass


class SRank(DictionaryTable):
    pass


class NRank(DictionaryTable):
    pass


class GRank(DictionaryTable):
    pass


class RegionalStatus(DictionaryTableExtended):
    pass


class UsfwsStatus(DictionaryTable):
    pass


class IucnRedListCategory(DictionaryTable):
    pass


class ElementType(DictionaryTable):
    # alga, arachnid, bird, conifer, etc
    pass


class MushroomGroup(DictionaryTable):
    pass


class Preservative(DictionaryTable):
    pass


class Storage(DictionaryTable):
    pass


class Repository(DictionaryTable):
    # FIXME: repository needs extra attributes (and maybe has to be managed as
    # a non-dictionary table)
    pass


class Gender(DictionaryTable):
    pass


class Marks(DictionaryTable):
    pass


class DiseasesAndAbnormalities(DictionaryTable):
    pass


class TerrestrialSampler(DictionaryTable):
    pass


class AquaticSampler(DictionaryTable):
    pass


class TerrestrialStratum(DictionaryTable):
    pass


class PondLakeType(DictionaryTable):
    pass


class PondLakeUse(DictionaryTable):
    pass


class ShorelineType(DictionaryTable):
    pass


class LakeMicrohabitat(DictionaryTable):
    pass


class StreamDesignatedUse(DictionaryTable):
    pass


class ChannelType(DictionaryTable):
    pass


class HmfeiLocalAbundance(DictionaryTable):
    pass


class LoticHabitatType(DictionaryTable):
    pass


class WaterFlowType(DictionaryTable):
    pass


class WetlandType(DictionaryTable):
    pass


class WetlandLocation(DictionaryTable):
    pass


class WetlandConnectivity(DictionaryTable):
    pass


class WaterSource(DictionaryTable):
    pass


class WetlandHabitatFeature(DictionaryTable):
    pass


class SlimeMoldClass(DictionaryTableExtended):
    pass


class SlimeMoldMedia(DictionaryTable):
    pass


class FernLifestages(DictionaryTable):  # FIXME: probably is not a dict table
    pass


# FIXME: probably is not a dict table
class FloweringPlantLifestages(DictionaryTable):
    pass


class MossLifestages(DictionaryTable):  # FIXME: probably is not a dict table
    pass


class PlantCount(DictionaryTable):
    pass


class MoistureRegime(DictionaryTable):
    pass


class GroundSurface(DictionaryTable):
    pass


class CanopyCover(DictionaryTable):
    pass


class GeneralHabitatCategory(DictionaryTable):
    pass


# class SoilType(DictionaryTable):
#     # FIXME: probably is not a dict table
#     pass
#
# class CommonTreesAndBushes(DictionaryTable):
#     # FIXME: probably is not a dict table
#     pass
#
# class CommonGroundVegetation(DictionaryTable):
#     # FIXME: probably is not a dict table
#     pass


class LandscapePosition(DictionaryTable):
    pass


class Aspect(DictionaryTable):
    pass


class Slope(DictionaryTable):
    pass


class FungusApparentSubstrate(DictionaryTable):
    pass


class MushroomVerticalLocation(DictionaryTable):
    pass


class MushroomGrowthForm(DictionaryTable):
    pass


class MushroomOdor(DictionaryTable):
    pass


class FungalAssociationType(DictionaryTable):
    pass


class CMSensitivity(DictionaryTable):
    pass


class NaturalAreaCondition(DictionaryTable):
    pass


class GlacialDepositPleistoceneAge(DictionaryTable):
    pass


class GlacialDeposit(DictionaryTable):
    pass


class NaturalAreaType(DictionaryTable):
    pass


class LeapLandCover(DictionaryTable):
    pass


class BedrockAndOutcrops(DictionaryTable):
    pass


class RegionalFrequency(DictionaryTable):
    pass


class AquaticHabitatCategory(DictionaryTable):
    pass


# class InvasivePlants(DictionaryTable):
#     # FIXME: probably is not a dict table
#     pass

