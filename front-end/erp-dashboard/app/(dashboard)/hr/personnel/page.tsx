import { PageHeader } from "@/components/shared/page-header"
import { PersonnelTable } from "@/components/hr/personnel-table"
import { Button } from "@/components/ui/button"
import { UserPlus } from "lucide-react"
import { personnel } from "@/lib/data/hr"

export default function PersonnelPage() {
  return (
    <>
      <PageHeader
        title="لیست پرسنل"
        description="مدیریت اطلاعات، سمت و وضعیت کارکنان سازمان"
        actions={
          <Button size="sm">
            <UserPlus />
            افزودن پرسنل جدید
          </Button>
        }
      />
      <PersonnelTable data={personnel} />
    </>
  )
}
