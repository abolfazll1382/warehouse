import { PageHeader } from "@/components/shared/page-header"
import { QualityControlTable } from "@/components/production/quality-table"
import { qualityChecks } from "@/lib/data/production"

export default function QualityControlPage() {
  return (
    <>
      <PageHeader
        title="کنترل کیفیت"
        description="نتایج بازرسی و کنترل کیفیت محصولات تولیدی"
      />
      <QualityControlTable data={qualityChecks} />
    </>
  )
}
