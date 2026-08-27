"use client"

import type { ColumnDef } from "@tanstack/react-table"
import { DataTable } from "@/components/data-table/data-table"
import { DataTableColumnHeader } from "@/components/data-table/column-header"
import { StatusBadge } from "@/components/shared/status-badge"
import { formatToman } from "@/lib/utils"
import type { PayrollRecord } from "@/lib/data/hr"

const columns: ColumnDef<PayrollRecord>[] = [
  {
    accessorKey: "id",
    header: ({ column }) => <DataTableColumnHeader column={column} title="شماره فیش" />,
    cell: ({ row }) => <span className="font-medium tabular-nums">{row.original.id}</span>,
  },
  {
    accessorKey: "employee",
    header: ({ column }) => <DataTableColumnHeader column={column} title="نام کارمند" />,
  },
  {
    accessorKey: "baseSalary",
    header: ({ column }) => <DataTableColumnHeader column={column} title="حقوق پایه" />,
    cell: ({ row }) => <span className="tabular-nums text-muted-foreground">{formatToman(row.original.baseSalary)}</span>,
  },
  {
    accessorKey: "insurance",
    header: ({ column }) => <DataTableColumnHeader column={column} title="کسورات بیمه" />,
    cell: ({ row }) => <span className="tabular-nums text-muted-foreground">{formatToman(row.original.insurance)}</span>,
  },
  {
    accessorKey: "tax",
    header: ({ column }) => <DataTableColumnHeader column={column} title="مالیات" />,
    cell: ({ row }) => <span className="tabular-nums text-muted-foreground">{formatToman(row.original.tax)}</span>,
  },
  {
    accessorKey: "netPay",
    header: ({ column }) => <DataTableColumnHeader column={column} title="خالص پرداختی" />,
    cell: ({ row }) => <span className="font-medium tabular-nums text-foreground">{formatToman(row.original.netPay)}</span>,
  },
  {
    accessorKey: "status",
    header: ({ column }) => <DataTableColumnHeader column={column} title="وضعیت پرداخت" />,
    cell: ({ row }) => <StatusBadge status={row.original.status} />,
  },
]

export function PayrollTable({ data }: { data: PayrollRecord[] }) {
  return <DataTable columns={columns} data={data} searchPlaceholder="جستجوی نام کارمند..." searchColumnId="employee" />
}
