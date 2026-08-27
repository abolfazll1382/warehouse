import { PageHeader } from "@/components/shared/page-header"
import { CustomersTable } from "@/components/sales/customers-table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"
import { customers } from "@/lib/data/sales"

export default function CustomersPage() {
  return (
    <>
      <PageHeader
        title="لیست مشتریان"
        description="مدیریت اطلاعات و سوابق خرید مشتریان"
        actions={
          <Button size="sm">
            <Plus />
            مشتری جدید
          </Button>
        }
      />
      <CustomersTable data={customers} />
    </>
  )
}
