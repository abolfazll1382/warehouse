"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { Star } from "lucide-react"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import type { Supplier } from "@/lib/data/purchasing"

const columns: ColumnDef<Supplier>[] = [
  {
    accessorKey: "name",
    header: ({ column }) => <DataTableColumnHeader column={column} title="نام تامین‌کننده" />,
    cell: ({ row }) => <span className="font-medium text-foreground">{row.original.name}</span>,
  },
  {
    accessorKey: "category",
    header: ({ column }) => <DataTableColumnHeader column={column} title="دسته‌بندی کالا" />,
    cell: ({ row }) => <span className="text-muted-foreground">{row.original.category}</span>,
  },
  {
    accessorKey: "contact",
    header: ({ column }) => <DataTableColumnHeader column={column} title="شماره تماس" />,
    cell: ({ row }) => (
      <span dir="ltr" className="block text-end tabular-nums text-muted-foreground">
        {row.original.contact}
      </span>
    ),
  },
  {
    accessorKey: "rating",
    header: ({ column }) => <DataTableColumnHeader column={column} title="رتبه‌بندی" />,
    cell: ({ row }) => (
      <div className="flex items-center gap-1 tabular-nums">
        <Star className="size-3.5 fill-warning text-warning" />
        {row.original.rating}
      </div>
    ),
  },
  {
    accessorKey: "status",
    header: ({ column }) => <DataTableColumnHeader column={column} title="وضعیت" />,
    cell: ({ row }) => <StatusBadge status={row.original.status} />,
  },
]

export function SuppliersTable({ data }: { data: Supplier[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی تامین‌کننده..." searchColumnId="name" />
}
