"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import { formatToman } from "@/lib/utils"
import type { Invoice } from "@/lib/data/sales"

const columns: ColumnDef<Invoice>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => <DataTableColumnHeader column={column} title="شماره فاکتور" />,
    cell: ({ row }) => <span className="font-medium tabular-nums">{row.original.id}</span>,
  },
  {
    accessorKey: "customer",
    header: ({ column }) => <DataTableColumnHeader column={column} title="مشتری" />,
  },
  {
    accessorKey: "date",
    header: ({ column }) => <DataTableColumnHeader column={column} title="تاریخ صدور" />,
    cell: ({ row }) => <span className="tabular-nums text-muted-foreground">{row.original.date}</span>,
  },
  {
    accessorKey: "amount",
    header: ({ column }) => <DataTableColumnHeader column={column} title="مبلغ فاکتور" />,
    cell: ({ row }) => <span className="font-medium tabular-nums">{formatToman(row.original.amount)}</span>,
  },
  {
    accessorKey: "status",
    header: ({ column }) => <DataTableColumnHeader column={column} title="وضعیت پرداخت" />,
    cell: ({ row }) => <StatusBadge status={row.original.status} />,
  },
]

export function InvoicesTable({ data }: { data: Invoice[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی فاکتور..." searchColumnId="customer" />
}
