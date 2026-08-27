import { PageHeader } from "@/components/shared/page-header"
import { InventoryTable } from "@/components/inventory/inventory-table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"
import Link from "next/link"
import { inventoryItems } from "@/lib/data/inventory"

export default function InventoryListPage() {
  return (
    <>
      <PageHeader
        title="لیست موجودی"
        description="موجودی لحظه‌ای کالاها در انبار مرکزی"
        actions={
          <Button size="sm" asChild>
            <Link href="/inventory/add">
              <Plus />
              افزودن کالا
            </Link>
          </Button>
        }
      />
      <InventoryTable data={inventoryItems} />
    </>
  )
}
