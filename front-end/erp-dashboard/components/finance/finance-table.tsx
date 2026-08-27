"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { ArrowDownLeft, ArrowUpRight } from "lucide-react"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { cn, formatToman } from "@/lib/utils"
import type { FinanceRecord } from "@/lib/data/finance"

const columns: ColumnDef<FinanceRecord>[] = [
  {
    accessorKey: "description",
    header: ({ column }) => <DataTableColumnHeader column={column} title="شرح تراکنش" />,
    cell: ({ row }) => (
      <div className="flex items-center gap-2.5 font-medium text-foreground">
        <span
          className={cn(
            "flex size-7 shrink-0 items-center justify-center rounded-full",
            row.original.type === "income" ? "bg-success/12 text-success" : "bg-destructive/12 text-destructive"
          )}
        >
          {row.original.type === "income" ? (
            <ArrowDownLeft className="size-3.5" />
          ) : (
            <ArrowUpRight className="size-3.5" />
          )}
        </span>
        {row.original.description}
      </div>
    ),
  },
  {
    accessorKey: "category",
    header: ({ column }) => <DataTableColumnHeader column={column} title="دسته‌بندی" />,
    cell: ({ row }) => <span className="text-muted-foreground">{row.original.category}</span>,
  },
  {
    accessorKey: "date",
    header: ({ column }) => <DataTableColumnHeader column={column} title="تاریخ" />,
    cell: ({ row }) => <span className="tabular-nums text-muted-foreground">{row.original.date}</span>,
  },
  {
    accessorKey: "amount",
    header: ({ column }) => <DataTableColumnHeader column={column} title="مبلغ" />,
    cell: ({ row }) => (
      <span className={cn("font-medium tabular-nums", row.original.type === "income" ? "text-success" : "text-foreground")}>
        {row.original.type === "income" ? "+" : "−"} {formatToman(row.original.amount)}
      </span>
    ),
  },
]

export function FinanceTable({ data }: { data: FinanceRecord[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی تراکنش..." searchColumnId="description" />
}
