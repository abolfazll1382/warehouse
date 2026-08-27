import { PageHeader } from "@/components/shared/page-header"
import { InvoicesTable } from "@/components/sales/invoices-table"
import { Button } from "@/components/ui/button"
import { FileDown } from "lucide-react"
import { invoices } from "@/lib/data/sales"

export default function InvoicesPage() {
  return (
    <>
      <PageHeader
        title="فاکتورها"
        description="فهرست فاکتورهای فروش صادر شده"
        actions={
          <Button variant="outline" size="sm">
            <FileDown />
            خروجی اکسل
          </Button>
        }
      />
      <InvoicesTable data={invoices} />
    </>
  )
}
