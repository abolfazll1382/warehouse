"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import { cn } from "@/lib/utils"
import type { ProductionLine } from "@/lib/data/production"

const columns: ColumnDef<ProductionLine>[] = [
  {
    accessorKey: "name",
    header: ({ column }) => <DataTableColumnHeader column={column} title="خط تولید" />,
    cell: ({ row }) => <span className="font-medium text-foreground">{row.original.name}</span>,
  },
  {
    accessorKey: "product",
    header: ({ column }) => <DataTableColumnHeader column={column} title="محصول تولیدی" />,
    cell: ({ row }) => <span className="text-muted-foreground">{row.original.product}</span>,
  },
  {
    accessorKey: "capacity",
    header: ({ column }) => <DataTableColumnHeader column={column} title="ظرفیت اسمی" />,
    cell: ({ row }) => <span className="tabular-nums text-muted-foreground">{row.original.capacity}</span>,
  },
  {
    accessorKey: "efficiency",
    header: ({ column }) => <DataTableColumnHeader column={column} title="بازدهی" />,
    cell: ({ row }) => (
      <div className="flex w-32 items-center gap-2">
        <div className="h-1.5 flex-1 overflow-hidden rounded-full bg-secondary">
          <div
            className={cn(
              "h-full rounded-full",
              row.original.efficiency >= 85
                ? "bg-success"
                : row.original.efficiency >= 60
                  ? "bg-warning"
                  : "bg-muted-foreground/40"
            )}
            style={{ width: `${row.original.efficiency}%` }}
          />
        </div>
        <span className="w-9 shrink-0 text-xs tabular-nums text-muted-foreground">
          {row.original.efficiency}٪
        </span>
      </div>
    ),
  },
  {
    accessorKey: "status",
    header: ({ column }) => <DataTableColumnHeader column={column} title="وضعیت" />,
    cell: ({ row }) => <StatusBadge status={row.original.status} />,
  },
]

export function ProductionLinesTable({ data }: { data: ProductionLine[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی خط تولید..." searchColumnId="name" />
}
