"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import type { QualityCheck } from "@/lib/data/production"

const columns: ColumnDef<QualityCheck>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => <DataTableColumnHeader column={column} title="کد بازرسی" />,
    cell: ({ row }) => <span className="font-medium tabular-nums">{row.original.id}</span>,
  },
  {
    accessorKey: "product",
    header: ({ column }) => <DataTableColumnHeader column={column} title="محصول" />,
  },
  {
    accessorKey: "date",
    header: ({ column }) => <DataTableColumnHeader column={column} title="تاریخ بازرسی" />,
    cell: ({ row }) => <span className="tabular-nums text-muted-foreground">{row.original.date}</span>,
  },
  {
    accessorKey: "inspector",
    header: ({ column }) => <DataTableColumnHeader column={column} title="بازرس کیفیت" />,
    cell: ({ row }) => <span className="text-muted-foreground">{row.original.inspector}</span>,
  },
  {
    accessorKey: "result",
    header: ({ column }) => <DataTableColumnHeader column={column} title="نتیجه" />,
    cell: ({ row }) => <StatusBadge status={row.original.result} />,
  },
]

export function QualityControlTable({ data }: { data: QualityCheck[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی محصول..." searchColumnId="product" />
}
