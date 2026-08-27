import { ArrowDownRight, ArrowUpRight } from "lucide-react"
import { Card, CardContent } from "@/components/ui/card"
import { cn } from "@/lib/utils"
import type { Kpi } from "@/types"

const accentClasses: Record<Kpi["accent"], string> = {
  primary: "bg-primary/12 text-primary",
  success: "bg-success/12 text-success",
  warning: "bg-warning/12 text-warning",
  sky: "bg-chart-5/12 text-chart-5",
}

export function KpiCard({ kpi }: { kpi: Kpi }) {
  const Icon = kpi.icon
  const TrendIcon = kpi.trend === "up" ? ArrowUpRight : ArrowDownRight

  return (
    <Card className="group relative overflow-hidden transition-colors hover:border-border">
      <CardContent className="flex items-start justify-between gap-4 px-5">
        <div className="flex flex-col gap-2.5">
          <p className="text-sm text-muted-foreground">{kpi.title}</p>
          <p className="text-2xl font-bold tabular-nums text-foreground">{kpi.value}</p>
          <div className="flex items-center gap-1 text-xs">
            <span
              className={cn(
                "flex items-center gap-0.5 rounded-md px-1.5 py-0.5 font-medium tabular-nums",
                accentClasses[kpi.accent]
              )}
            >
              <TrendIcon className="size-3.5 rtl:-scale-x-100" />
              {kpi.changeLabel}
            </span>
            <span className="text-muted-foreground">نسبت به ماه گذشته</span>
          </div>
        </div>
        <span
          className={cn(
            "flex size-11 shrink-0 items-center justify-center rounded-xl",
            accentClasses[kpi.accent]
          )}
        >
          <Icon className="size-[22px]" />
        </span>
      </CardContent>
    </Card>
  )
}
