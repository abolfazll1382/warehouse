"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import { formatToman } from "@/lib/utils"
import type { Customer } from "@/lib/data/sales"

const columns: ColumnDef<Customer>[] = [
  {
    accessorKey: "name",
    header: ({ column }) => <DataTableColumnHeader column={column} title="نام مشتری" />,
    cell: ({ row }) => <span className="font-medium text-foreground">{row.original.name}</span>,
  },
  {
    accessorKey: "phone",
    header: ({ column }) => <DataTableColumnHeader column={column} title="شماره تماس" />,
    cell: ({ row }) => (
      <span dir="ltr" className="block text-end tabular-nums text-muted-foreground">
        {row.original.phone}
      </span>
    ),
  },
  {
    accessorKey: "city",
    header: ({ column }) => <DataTableColumnHeader column={column} title="شهر" />,
    cell: ({ row }) => <span className="text-muted-foreground">{row.original.city}</span>,
  },
  {
    accessorKey: "totalPurchases",
    header: ({ column }) => <DataTableColumnHeader column={column} title="مجموع خرید" />,
    cell: ({ row }) => <span className="font-medium tabular-nums">{formatToman(row.original.totalPurchases)}</span>,
  },
  {
    accessorKey: "status",
    header: ({ column }) => <DataTableColumnHeader column={column} title="وضعیت" />,
    cell: ({ row }) => <StatusBadge status={row.original.status} />,
  },
]

export function CustomersTable({ data }: { data: Customer[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی مشتری..." searchColumnId="name" />
}
