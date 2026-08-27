from apps.production.models import ProductionLine, QualityCheck


def production_line_list():
    return ProductionLine.objects.all()


def quality_check_list(*, line_id: int | None = None, result: str | None = None):
    qs = QualityCheck.objects.select_related("line", "inspector")
    if line_id:
        qs = qs.filter(line_id=line_id)
    if result:
        qs = qs.filter(result=result)
    return qs
