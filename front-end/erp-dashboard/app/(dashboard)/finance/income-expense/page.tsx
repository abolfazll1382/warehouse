import { PageHeader } from "@/components/shared/page-header"
import { FinanceTable } from "@/components/finance/finance-table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"
import { financeRecords } from "@/lib/data/finance"

export default function IncomeExpensePage() {
  return (
    <>
      <PageHeader
        title="درآمد و هزینه‌ها"
        description="ثبت و مرور تراکنش‌های مالی درآمد و هزینه"
        actions={
          <Button size="sm">
            <Plus />
            تراکنش جدید
          </Button>
        }
      />
      <FinanceTable data={financeRecords} />
    </>
  )
}
