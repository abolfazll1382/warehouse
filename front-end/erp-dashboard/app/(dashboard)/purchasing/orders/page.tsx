import { PageHeader } from "@/components/shared/page-header"
import { PurchaseOrdersTable } from "@/components/purchasing/orders-table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"
import { purchaseOrders } from "@/lib/data/purchasing"

export default function PurchaseOrdersPage() {
  return (
    <>
      <PageHeader
        title="سفارشات خرید"
        description="پیگیری وضعیت سفارشات خرید ثبت‌شده"
        actions={
          <Button size="sm">
            <Plus />
            سفارش خرید جدید
          </Button>
        }
      />
      <PurchaseOrdersTable data={purchaseOrders} />
    </>
  )
}
