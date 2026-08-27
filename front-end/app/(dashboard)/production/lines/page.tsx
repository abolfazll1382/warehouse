import { PageHeader } from "@/components/shared/page-header"
import { ProductionLinesTable } from "@/components/production/lines-table"
import { productionLines } from "@/lib/data/production"

export default function ProductionLinesPage() {
  return (
    <>
      <PageHeader
        title="خطوط تولید"
        description="وضعیت لحظه‌ای و بازدهی خطوط تولید کارخانه"
      />
      <ProductionLinesTable data={productionLines} />
    </>
  )
}
