"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import { formatNumber } from "@/lib/utils"
import type { InventoryItem } from "@/lib/data/inventory"

const columns: ColumnDef<InventoryItem>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => <DataTableColumnHeader column={column} title="کد کالا" />,
    cell: ({ row }) => <span className="font-medium tabular-nums text-muted-foreground">{row.original.id}</span>,
  },
  {
    accessorKey: "name",
    header: ({ column }) => <DataTableColumnHeader column={column} title="نام کالا" />,
    cell: ({ row }) => <span className="font-medium text-foreground">{row.original.name}</span>,
  },
  {
    accessorKey: "category",
    header: ({ column }) => <DataTableColumnHeader column={column} title="دسته‌بندی" />,
    cell: ({ row }) => <span className="text-muted-foreground">{row.original.category}</span>,
  },
  {
    accessorKey: "quantity",
    header: ({ column }) => <DataTableColumnHeader column={column} title="موجودی" />,
    cell: ({ row }) => (
      <span className="tabular-nums">
        {formatNumber(row.original.quantity)} <span className="text-muted-foreground">{row.original.unit}</span>
      </span>
    ),
  },
  {
    accessorKey: "status",
    header: ({ column }) => <DataTableColumnHeader column={column} title="وضعیت" />,
    cell: ({ row }) => <StatusBadge status={row.original.status} />,
  },
]

export function InventoryTable({ data }: { data: InventoryItem[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی کالا..." searchColumnId="name" />
}
