from django.contrib import admin

from compiapp.models import Socio_trivia_reg, SocioExhibition, HackathonRegistration,CaseStudy,PIL_DRAFT,union_budget_reg,mootcourt_reg,mock_parliament_reg,adhikar_reg
from import_export.admin import ImportExportModelAdmin
# Register your models here.
@admin.register(Socio_trivia_reg)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(SocioExhibition)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(HackathonRegistration)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(CaseStudy)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(PIL_DRAFT)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(union_budget_reg)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(mootcourt_reg)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(mock_parliament_reg)
class Acc (ImportExportModelAdmin):
  pass
@admin.register(adhikar_reg)
class Acc (ImportExportModelAdmin):
  pass