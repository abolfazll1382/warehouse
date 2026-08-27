"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import { formatToman } from "@/lib/utils"
import type { PurchaseOrder } from "@/lib/data/purchasing"

const columns: ColumnDef<PurchaseOrder>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => <DataTableColumnHeader column={column} title="شماره سفارش" />,
    cell: ({ row }) => <span className="font-medium tabular-nums">{row.original.id}</span>,
  },
  {
    accessorKey: "supplier",
    header: ({ column }) => <DataTableColumnHeader column={column} title="تامین‌کننده" />,
  },
  {
    accessorKey: "date",
    header: ({ column }) => <DataTableColumnHeader column={column} title="تاریخ ثبت" />,
    cell: ({ row }) => <span className="tabular-nums text-muted-foreground">{row.original.date}</span>,
  },
  {
    accessorKey: "amount",
    header: ({ column }) => <DataTableColumnHeader column={column} title="مبلغ سفارش" />,
    cell: ({ row }) => <span className="font-medium tabular-nums">{formatToman(row.original.amount)}</span>,
  },
  {
    accessorKey: "status",
    header: ({ column }) => <DataTableColumnHeader column={column} title="وضعیت" />,
    cell: ({ row }) => <StatusBadge status={row.original.status} />,
  },
]

export function PurchaseOrdersTable({ data }: { data: PurchaseOrder[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی سفارش..." searchColumnId="supplier" />
}
