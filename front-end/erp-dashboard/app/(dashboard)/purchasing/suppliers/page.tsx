import { PageHeader } from "@/components/shared/page-header"
import { SuppliersTable } from "@/components/purchasing/suppliers-table"
import { Button } from "@/components/ui/button"
import { Plus } from "lucide-react"
import { suppliers } from "@/lib/data/purchasing"

export default function SuppliersPage() {
  return (
    <>
      <PageHeader
        title="تامین‌کنندگان"
        description="فهرست، دسته‌بندی و رتبه‌بندی تامین‌کنندگان"
        actions={
          <Button size="sm">
            <Plus />
            تامین‌کننده جدید
          </Button>
        }
      />
      <SuppliersTable data={suppliers} />
    </>
  )
}
