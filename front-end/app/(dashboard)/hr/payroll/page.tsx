import { PageHeader } from "@/components/shared/page-header"
import { PayrollTable } from "@/components/hr/payroll-table"
import { Button } from "@/components/ui/button"
import { FileDown } from "lucide-react"
import { payroll } from "@/lib/data/hr"

export default function PayrollPage() {
  return (
    <>
      <PageHeader
        title="حقوق و دستمزد"
        description="فیش‌های حقوقی و وضعیت پرداخت‌های ماه جاری"
        actions={
          <Button variant="outline" size="sm">
            <FileDown />
            خروجی اکسل
          </Button>
        }
      />
      <PayrollTable data={payroll} />
    </>
  )
}
