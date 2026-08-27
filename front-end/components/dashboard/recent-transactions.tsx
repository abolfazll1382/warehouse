import { ArrowDownLeft, ArrowUpRight } from "lucide-react"
import {
  Card,
  CardAction,
  CardContent,
  CardDescription,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import {
  Table,
  TableBody,
  TableCell,
  TableHead,
  TableHeader,
  TableRow,
} from "@/components/ui/table"
import { Button } from "@/components/ui/button"
import { StatusBadge } from "@/components/shared/status-badge"
import { cn, formatToman } from "@/lib/utils"
import type { Transaction } from "@/types"

export function RecentTransactions({ transactions }: { transactions: Transaction[] }) {
  return (
    <Card>
      <CardHeader>
        <CardTitle>تراکنش‌های اخیر</CardTitle>
        <CardDescription>آخرین فعالیت‌های مالی ثبت‌شده در سامانه</CardDescription>
        <CardAction>
          <Button variant="ghost" size="sm" className="text-primary hover:text-primary">
            مشاهده همه
          </Button>
        </CardAction>
      </CardHeader>
      <CardContent className="px-0 sm:px-6">
        <Table>
          <TableHeader>
            <TableRow className="hover:bg-transparent">
              <TableHead className="ps-4 sm:ps-0">شرح تراکنش</TableHead>
              <TableHead>طرف حساب</TableHead>
              <TableHead>تاریخ</TableHead>
              <TableHead>وضعیت</TableHead>
              <TableHead className="pe-4 text-end sm:pe-0">مبلغ</TableHead>
            </TableRow>
          </TableHeader>
          <TableBody>
            {transactions.map((t) => (
              <TableRow key={t.id}>
                <TableCell className="ps-4 font-medium text-foreground sm:ps-0">
                  <div className="flex items-center gap-2.5">
                    <span
                      className={cn(
                        "flex size-7 shrink-0 items-center justify-center rounded-full",
                        t.direction === "in" ? "bg-success/12 text-success" : "bg-destructive/12 text-destructive"
                      )}
                    >
                      {t.direction === "in" ? (
                        <ArrowDownLeft className="size-3.5" />
                      ) : (
                        <ArrowUpRight className="size-3.5" />
                      )}
                    </span>
                    {t.description}
                  </div>
                </TableCell>
                <TableCell className="text-muted-foreground">{t.party}</TableCell>
                <TableCell className="text-muted-foreground tabular-nums">{t.date}</TableCell>
                <TableCell>
                  <StatusBadge status={t.status} />
                </TableCell>
                <TableCell
                  className={cn(
                    "pe-4 text-end font-medium tabular-nums sm:pe-0",
                    t.direction === "in" ? "text-success" : "text-foreground"
                  )}
                >
                  {t.direction === "in" ? "+" : "−"} {formatToman(t.amount)}
                </TableCell>
              </TableRow>
            ))}
          </TableBody>
        </Table>
      </CardContent>
    </Card>
  )
}
