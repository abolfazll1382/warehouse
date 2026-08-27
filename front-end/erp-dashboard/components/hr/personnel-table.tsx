"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import { Avatar, AvatarFallback } from "@/components/ui/avatar"
import type { Personnel } from "@/lib/data/hr"

const columns: ColumnDef<Personnel>[] = [
  {
    accessorKey: "name",
    header: ({ column }) => <DataTableColumnHeader column={column} title="نام و نام خانوادگی" />,
    cell: ({ row }) => (
      <div className="flex items-center gap-2.5 font-medium text-foreground">
        <Avatar className="size-7">
          <AvatarFallback className="bg-secondary text-[11px]">
            {row.original.name.slice(0, 1)}
          </AvatarFallback>
        </Avatar>
        {row.original.name}
      </div>
    ),
  },
  {
    accessorKey: "position",
    header: ({ column }) => <DataTableColumnHeader column={column} title="سمت" />,
    cell: ({ row }) => <span className="text-muted-foreground">{row.original.position}</span>,
  },
  {
    accessorKey: "department",
    header: ({ column }) => <DataTableColumnHeader column={column} title="واحد سازمانی" />,
  },
  {
    accessorKey: "hireDate",
    header: ({ column }) => <DataTableColumnHeader column={column} title="تاریخ استخدام" />,
    cell: ({ row }) => <span className="tabular-nums">{row.original.hireDate}</span>,
  },
  {
    accessorKey: "status",
    header: ({ column }) => <DataTableColumnHeader column={column} title="وضعیت" />,
    cell: ({ row }) => <StatusBadge status={row.original.status} />,
  },
]

export function PersonnelTable({ data }: { data: Personnel[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی نام پرسنل..." searchColumnId="name" />
}
